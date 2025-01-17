---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Post-Quantum TLS without handshake signatures at RWC 2021"
event: IACR Real World Crypto 2021
event_url: https://rwc.iacr.org/2021/
location: Virtual
address:
  street:
  city:
  region:
  postcode:
  country:
summary: Talk about Post-Quantum TLS without Handshake Signatures at RWC 2021 (virtual).
abstract: |
  It's possible to make TLS 1.3 post-quantum secure by just plugging in post-quantum key exchange and a post-quantum signature scheme. But PQ signatures tend to be quite big and slow. KEMTLS is our proposal for a post-quantum secure variant of TLS that authenticates by using KEMs instead of the handshake signature. With a trick to preserve the ability to allow the client to send the request after the server sends its certificate: using KEMs instead of signatures doesn't take more round trips for this first message.
  We compare a few instantiations of KEMTLS. Optimised for communication size, KEMTLS, with SIKE for KEX and handshake authentication, GeMSS for the CA certificate and a custom XMSS for optional intermediate certificates, requires less than half the bandwidth of a post-quantum TLS 1.3 using Falcon for the handshake signature. When picking primitives for speed, KEMTLS reduces the amount of server CPU cycles by up to 90% compared to an equivalent post-quantum instantiation of TLS 1.3, as well as reducing the time before the client can send its first application data.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2021-01-11T18:00:00+01:00
date: 2021-01-11T18:15:00+01:00
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: 2021-01-11

authors: ['thom', 'sofiaceli']
tags:
  - KEMTLS
  - PQTLS
  - Post-Quantum
  - research

# Is this a featured talk? (true/false)
featured: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

# Optional filename of your slides within your talk's folder or a URL.
url_slides: "presentation.pdf"

url_code:
url_pdf:
url_video: https://youtu.be/TZMgRnSV3pk?t=3175

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects:
  - 'kemtls'

highlight: true
highlight_languages:
 - go
---

# Post-Quantum TLS with KEMs instead of signatures

_This article has also been posted to [Sofía Celi's blog](https://claucece.github.io/2021/01/10/cf-kemtls.html) and the [Cloudflare blog](https://blog.cloudflare.com/kemtls-post-quantum-tls-without-signatures/)._

Fundamentally, the Transport Layer Security protocol (TLS), which
secures most of the Internet connections, has mainly been a key exchange
authenticated by digital signatures.[^1] Even though it has undergone
major changes since 1994, when SSL 1.0 was introduced by Netscape, it's
main mechanism has remained the same. The key exchange that is used was
first based on RSA and later on (elliptic curve) Diffie-Hellman. The
signatures used for authentication have almost always been RSA-based,
though in recent years other kinds of signatures have been adopted,
mainly ECDSA and Ed25519. This recent change to elliptic curve
cryptography at both at a key exchange and signature level has resulted
in considerable speed and bandwidth benefits in comparison to classic
Diffie-Hellman and RSA.

TLS is the main protocol that protects the connections we use everyday.
It is everywhere: it is used when we buy products online, when we
register for a newsletter or when we access any kind of website. But,
with the imminent threat of the arrival of
[quantum computers](https://blog.cloudflare.com/securing-the-post-quantum-world/)
(a threat that seems to be getting closer and closer), we need to
reconsider again the future of TLS. [A wide-scale post-quantum
experiment](https://blog.cloudflare.com/the-tls-post-quantum-experiment/)
was carried out by Cloudflare and Google: two post-quantum key exchanges
were integrated into their TLS stack and deployed at their edge servers
and in Chrome Canary clients. The goal of that experiment was to
evaluate the performance and feasibility of deployment of two
post-quantum key exchanges in TLS.

Similar experiments have been proposed for introducing post-quantum
algorithms into the TLS handshake itself. But, they all seem infeasible
to be introduced at authentication by signature and key exchange levels
as, unfortunately, post-quantum cryptographic primitives are bigger, or
slower (or both) than their predecessors. The proposed algorithms under
consideration in the [NIST post-quantum standardization
process](https://csrc.nist.gov/Projects/post-quantum-cryptography/round-3-submissions)
use larger mathematical objects than what is used for elliptic curves,
traditional Diffie-Hellman or RSA. As a result, the size of public keys,
signatures and key exchange material is much bigger than those from
elliptic curves, Diffie-Hellman or RSA.

How can we solve this problem? How can we use post-quantum algorithms as
part of the TLS handshake without making the material too big to be
transmitted? In this blogpost, we will introduce a new mechanism for
making this happen, explain how it can be integrated into the handshake
and talk about implementation details. The key observation in this
mechanism is that, while post-quantum algorithms have bigger
communication size than their predecessors, post-quantum *key exchanges*
have somewhat smaller sizes than post-quantum *signatures*, so we can
try to replace key exchanges with signatures in some places to save
space. We will only focus on the TLS 1.3 handshake as it is the TLS
version that should be currently used.

## The past experiments: making the traditional TLS 1.3 handshake post-quantum

[TLS 1.3](https://tools.ietf.org/html/rfc8446) was introduced in
August 2018 with many security and performance improvements (notably,
having only one round-trip to complete the handshake). But TLS 1.3 is
designed for a world with classical computers, and some of its
functionalities will be broken by quantum computers when they arrive.

The primary goals of TLS 1.3 are to provide authentication (the server
side of the channel is always authenticated, the client side is
optionally authenticated), confidentiality and integrity by using a
handshake protocol and a record protocol. The handshake protocol, the
one of interest for us today, establishes the cryptographic parameters
for securing and authenticating a connection. It can be thought of as of
having three main phases, as defined in
[RFC8446](https://tools.ietf.org/html/rfc8446):

* The Parameter Negotiation phase (referred to as 'Server Parameters'
in RFC8446), which establishes other handshake parameters (whether the
client is authenticated, application-layer protocol support, etc).

* The Key Exchange phase, which establishes shared keying material and
selects the cryptographic parameters to be used. Everything after this
phase will be encrypted.

* The Authentication phase, which authenticates the server (and,
optionally, the client) and provides key confirmation and handshake
integrity.

The main idea of past experiments that introduced post-quantum
algorithms into the handshake of TLS 1.3 was to use them in place of
classical algorithms by advertising them as part of the [supported
groups](https://tools.ietf.org/html/rfc8446#section-4.2.7) (an
extension used by the client to indicate which named groups -Elliptic
Curve Groups, Finite Field Groups- it supports for key exchange) and
[key share](https://tools.ietf.org/html/rfc8446#section-4.2.8) (an
extension which contains the endpoint's cryptographic parameters)
extensions, and, therefore, establishing with them the negotiated
connection parameters. Key encapsulation mechanisms (KEMs) are an
abstraction of the basic key exchange primitive and were used to
generate the shared secrets. In the case of using a [pre-shared
key](https://tools.ietf.org/html/rfc8446#section-4.2.11), its symmetric
algorithms can be easily replaced by post-quantum KEMs, as well; and, in
the case of password-authenticated TLS, there has been some
[proposed ideas](https://eprint.iacr.org/2017/1192.pdf) on how to use
post-quantum algorithms with them.

Most of the above ideas only provide what is often defined as
'transitional security', as its main focus is providing
quantum-resistant confidentiality, but do not take into account
quantum-resistant authentication. The idea of using post-quantum
signatures for TLS authentication is possible, but the sizes of
post-quantum signatures are larger than traditional ones. Furthermore,
it is [worth noting](https://csrc.nist.gov/Presentations/2019/the-2nd-round-of-the-nist-pqc-standardization-proc)
that using post-quantum signatures is much heavier than using
post-quantum KEMs.

We can estimate the impact of such a replacement on network traffic by
simply looking at the sum of the cryptographic objects that are
transmitted during the handshake. In a typical TLS 1.3 handshake using
elliptic curve X25519 and RSA-2048, such a handshake would transmit 1376
bytes corresponding to: the public keys for key exchange, the
certificate, the signature of the handshake, and the certificate chain.
If we were to replace X25519 by the post-quantum KEM
[Kyber512](https://pq-crystals.org/kyber/) and RSA by the post-quantum
signature [Dilithium II](https://pq-crystals.org/dilithium/), two of
the more efficient proposals, the size transmitted data would increase
to 10036 bytes.[^2] The increase is mostly due to the size of the
post-quantum signature algorithm.

The question then is: how can we achieve full post-quantum security and
give a handshake that is efficient to be used?

## A more efficient proposal: KEMTLS

There is a long history of other mechanisms, besides signatures, being
used for authentication. Modern protocols, such as the Signal protocol,
the Noise framework or WireGuard, rely on key exchange mechanisms for
authentication; but are somewhat unsuitable for the TLS 1.3 case as they
expect the long-term key material to be known in advance by the
interested parties.

The [OPTLS proposal](https://eprint.iacr.org/2015/978.pdf) by Krawczyk
and Wee gives authentication for the TLS handshake without signatures by
using a non-interactive key exchange (NIKE). However, the only somewhat
efficient construction for a post-quantum NIKE is CSIDH, the security of
which is the subject of ongoing debate. But, we can build on this idea
by using KEMs for authentication. KEMTLS, the current proposed
experiment, replaces the handshake signature by a post-quantum KEM key
exchange. It was designed and introduced by Peter Schwabe, Douglas
Stebila and Thom Wiggers on the
[publication 'Post-Quantum TLS Without Handshake Signatures'](https://thomwiggers.nl/publication/kemtls/kemtls.pdf).

KEMTLS, therefore, gives the same goals as TLS 1.3 (authentication,
confidentiality and integrity) in the face of quantum computers for both
clients and servers. One small difference compared to TLS 1.3 is that
KEMTLS only allows to send application data since the second
client-to-server TLS message flow (TLS 1.3 allows the server to send
encrypted and authentication application data in its first response
message).

Intuitively, the handshake signature in TLS 1.3 proves possession of the
private key corresponding to the public key certified in the TLS 1.3
server certificate. For these signature schemes, this is the
straightforward way to prove possession; but it's also possible to make
such proof through key exchanges. By carefully considering the key
derivation sequence, only the server holding the private key that
corresponds to the certified public key can decrypt any messages sent by
the client to the server. Therefore, implicit authentication is
fulfilled. It is worth noting that KEMTLS still relies on signatures by
certificate authorities to authenticate the long-term KEM keys.

As said, KEMTLS' application data transmitted during the handshake is
implicitly, rather than explicitly authenticated (as in TLS 1.3), and
has slightly weaker downgrade resilience and forward secrecy; but full
downgrade resilience and forward secrecy is achieved once the KEMTLS
handshake completes.

![TLS vs KEMTLS state diagram](statediagrams.jpg)

By replacing the handshake signature by a KEM key exchange, we reduce
the size of the data transmitted in the example handshake using Kyber512
and Dilithium II to 8344 bytes, a significant reduction. Even for
algorithms, such the NTRU-assumption based KEM NTRU and signature
algorithm Falcon, that have a less-pronounced size gap, we still reduce
bytes. KEM operations are typically computationally much lighter than
signing operations as well, which makes the reduction even more
significant.

KEMTLS was presented at ACM CCS 2020. You can read more about its
details in [the paper](https://thomwiggers.nl/publication/kemtls/kemtls.pdf). It was
initially [implemented in the RustTLS library](https://github.com/thomwiggers/kemtls-experiment)
by Thom Wiggers using optimized C and assembly implementations of the post-quantum
algorithms provided by the [PQClean](https://github.com/PQClean/PQClean) and
[Open Quantum Safe](https://openquantumsafe.org/) projects.

## Cloudflare and KEMTLS: the implementation

As part of our effort to show that TLS can be completely post-quantum
safe, we implemented the full KEM TLS handshake over the Golang's TLS
1.3 suite. The implementation was done in several steps:

* We first needed to clone our own version of Golang, so we could add
  different post-quantum algorithms to it. You can find our own version
  [here](https://github.com/cloudflare/go/). This code gets constantly updated
  with every release of Golang, following
  [these steps](https://github.com/cloudflare/go/wiki/Starting-out).

* We needed to implement post-quantum algorithms in Golang, which we
  did on our own cryptographic library
  [CIRCL](https://github.com/cloudflare/circl/tree/master/kem).

* As we cannot force certificate authorities to use certificates with
  long-term key post-quantum KEM keys, we decided to use [Delegated
  Credentials](https://blog.cloudflare.com/keyless-delegation/). A
  delegated credential is a short-lasting key that the certificate's
  owner has delegated for use in TLS. Therefore, they can be used for
  having post-quantum KEM keys. See its implementation in our Golang
  code
  [here](https://github.com/cloudflare/go/tree/cf-delegated-credentials).

* We implemented mutual auth KEMTLS by using Delegated Credentials for
  the authentication process. See its implementation in our Golang
  code [here](https://github.com/cloudflare/go/tree/cf-pq-kemtls).
  You can also check its
  [test](https://github.com/cloudflare/go/blob/cf-pq-kemtls/src/crypto/tls/delegated_credentials_test.go#L774)
  for an overview of how it works.

Implementing KEMTLS was a straightforward process, although it did require
changes to the way Golang handles a TLS 1.3 handshake and how the key schedule
works.

A "regular" TLS 1.3 handshake in Golang (from the server perspective) looks like
this:

```go
func (hs *serverHandshakeStateTLS13) handshake() error {
	c := hs.c

	// For an overview of the TLS 1.3 handshake, see RFC 8446, Section 2.
	if err := hs.processClientHello(); err != nil {
		return err
	}
	if err := hs.checkForResumption(); err != nil {
		return err
	}
	if err := hs.pickCertificate(); err != nil {
		return err
	}
	c.buffering = true
	if err := hs.sendServerParameters(); err != nil {
		return err
	}
	if err := hs.sendServerCertificate(); err != nil {
		return err
	}
	if err := hs.sendServerFinished(); err != nil {
		return err
	}
	// Note that at this point we could start sending application data without
	// waiting for the client's second flight, but the application might not
	// expect the lack of replay protection of the ClientHello parameters.
	if _, err := c.flush(); err != nil {
		return err
	}
	if err := hs.readClientCertificate(); err != nil {
		return err
	}
	if err := hs.readClientFinished(); err != nil {
		return err
	}

	atomic.StoreUint32(&c.handshakeStatus, 1)

	return nil
}
```

We had to interrupt at the point that the server sends the Certificate
(`sendServerCertificate()`) in order to send the KEMTLS specific messages. In
the same way, we had to add the appropriate KEM TLS messages to the client's
handshake. And, as we didn't want to change so much the way Golang handles TLS
1.3, we only added one new constant to the configuration that can be used by
a server in order to ask for the Client's Certificate (the constant is
`serverConfig.ClientAuth = RequestClientKEMCert`).

The implementation is easy to work with: if a delegated credential or
a certificate has a public key of a supported post-quantum KEM algorithm, the
handshake will proceed with KEMTLS. If the server requests for a Client KEMTLS
Certificate, the handshake will invoke client KEMTLS authentication.

Many thanks to everyone involved in the project: Chris Wood, Armando
Faz-Hernandez, Thom Wiggers, Bas Westerbaan, Peter Wu, Peter Schwabe, Goutam
Tamvada, Douglas Stebila, Thibault Meunier, and the whole Cloudflare
cryptography team.

[^1]:  It is worth noting that the RSA key transport in TLS ≤1.2 authenticates
  the server by RSA public key encryption, although the server's RSA public key
  is certified using RSA signatures by Certificate Authorities.

[^2]: These numbers, as we do in the paper, are based on the round-2 submissions.
