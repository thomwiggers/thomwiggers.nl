---
title: "Using (post-quantum) KEMs in TLS 1.3"
date: 2018-10-17
lastmod: 2018-10-22
draft: false
featured: true

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors: ["thom"]

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags: ["post-quantum", "TLS", "KEM", "research", "TLS 1.3"]
categories: ["research"]

math: true

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
# Use `caption` to display an image caption.
#   Markdown linking is allowed, e.g. `caption = "[Image credit](http://example.org)"`.
# Set `preview` to `false` to disable the thumbnail in listings.
header:
  image: ""
  caption: ""
  preview: true

projects: ['kemtls']
---

The new TLS 1.3 standard \[1\] does not yet provide any support for
post-quantum algorithms. In this blog post we'll be talking about how we
could negotiate a post-quantum key exchange using a (post-quantum) Key
Encapsulation Mechanism (KEM). In the NIST Standardisation effort \[2\],
many KEMs are currently under consideration.

<!--more-->

What is a KEM
-------------

A KEM is a set of functions that can be used to obtain a symmetric
encryption key from asymmetric keys. It should provide the following
functions:

-   *$\operatorname{KeyGen}$*: Generates a public key $pk$ and a private
    key $sk$
-   *$\operatorname{Encapsulate(pk)}$* Returns symmetric key $K$ and
    ciphertext $ct$.
-   *$\operatorname{Decapsulate}(sk, ct)$*: Returns $K$

This can be used, for example in the following protocol.

{{< figure src="images/kem.png" title="KEM key exchange" caption="KEM key exchange.  Erratum: Alice should be decapsulating using $sk_A$." >}}

After exchanging these messages, $A$ and $B$ will have derived the same
key, much like the classic Diffie-Hellman key exchange.

The TLS 1.3 handshake protocol
------------------------------

{{< figure src="images/tls_13.png" title="The typical TLS 1.3 handshake" caption="The typical TLS 1.3 handshake" >}}

The typical TLS 1.3 handshake has the client and the server include key
shares in the first messages. These key shares, typically ephemeral ECDH
public keys, are used to compute a shared secret key. The server can
already do that in the second message. This allows very early submission
of data.

However, if we want to use KEMs, we run in the problem that the client
can not send the encrypted ciphertext $ct$ as it does not have the
public key of the server. This prevents us from using KEMs in this
setting of TLS.

### Using an extra round trip

TLS allows us to let the server pick the key shares we're going to use,
at the cost of an extra round trip. We can do this by sending a
<tt>ClientHello</tt> that does not contain any key shares, but indicates
support for the KEM. The server will then send
<tt>HelloRetryRequest</tt>, indicating the server should try again. In
the <tt>HelloRetryRequest</tt>, it will include the public key we need.

This leads to the following protocol.

{{< figure src="images/tls_13_2rtt_kem.png" caption="Using the extra roundtrip to obtain the necessary public key." >}}

Of course, this extra round trip increases latency. In fact, one of the
main improvements of TLS 1.3 over TLS 1.2 was the getting rid of this
extra round trip. The client can't prepare their messages before the
server replied with the <tt>HelloRetryRequest</tt> either. This is why
we think it's worth it to look into how we can get KEMs into TLS while
preserving the single-round trip protocol.

## References

1. Rescorla, Eric: The Transport Layer Security (TLS) Protocol Version 1.3, <https://rfc-editor.org/rfc/rfc8446.txt>, (2018).

2. National Institute for Standardization of Technology: Round 1
submissions - post-quantum cryptography,
<https://csrc.nist.gov/Projects/Post-Quantum-Cryptography/Round-1-Submissions>,
(2017).

3. Langley, Adam: Post-quantum confidentiality for TLS, <https://www.imperialviolet.org/2018/04/11/pqconftls.html>, (2018).
