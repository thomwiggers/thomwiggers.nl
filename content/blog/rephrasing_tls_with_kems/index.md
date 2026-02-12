+++
# vim: set ft=markdown ts=2 sw=2 tw=0 et :

title = "Rephrasing TLS key exchange in terms of KEMs"
date = 2018-11-21
lastmod = 2018-11-21
draft = false
math = true

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["thom"]

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["tls", "pqtls", "post-quantum", "cryptography"]
categories = ["research"]

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
[image]
  # Caption (optional)
  caption = ""

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = ""

projects= ["kemtls"]

+++

In the RFC for TLS 1.3 ([RFC8446][rfc8446]) especially, the key exchange is defined in terms of (EC)DH key shares being exchanged.
This limits us to algorithms which support non-interactive key exchanges, while this is not necessary for the security of TLS 1.3 as defined by RFC8446.[^NIKEs]
As we would like to implement (post-quantum) KEMs into TLS 1.3, we will now describe the changes to the spec that would be required.
As we can phrase (EC)DH key exchange as a key exchange with Key Encapsulation Mechanisms, this does not actually change TLS.
However, breaking the (EC)DH key exchange symmetries allows us to adopt other algorithms that don't have the same structure as (EC)DH.

We define a KEM as a set of three functions, as follows:

| Operation                                                                          | Description                                                                              |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| $(pk, sk) \leftarrow {\operatorname{KEM-KeyGen}}()$                                | Generates a public/private key pair.                                                      |
| $(K, ct) \leftarrow {\operatorname{KEM-Encaps}}(pk)$                               | Generates shared key $K$ and encapsulates it to public key pk as $ct$.                   |
| $K \leftarrow {\operatorname{KEM-Decaps}}(ct, sk)$                                 | Decapsulates $ct$ using $sk$ to obtain $K$                                               |

We can instantiate (EC)DH key exchange using a KEM as follows:


| Operation                                                                          | Description                                                                              |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| $(pk, sk) = (g^x, x) \leftarrow {\operatorname{DH-KEM-KeyGen}}()$                  | Generating secret value $x$, obtain public key as $g^x$                                  |
| $(K, ct) = ({(g^x)}^y, g^y) \leftarrow {\operatorname{DH-KEM-Encaps}}(pk)$         | Generate secret $y$, obtain $K$ as ${pk}^y = {(g^x)}^y$ and generate $ct$ as $g^y$       |
| $K = {(g^y)}^x \leftarrow {\operatorname{DH-KEM-Decaps}}(ct, sk)$                  | Obtain $K$ from $ct=g^y$ and the secret $x$                                              |

Here, $g$ is a shared generator for the (EC)DH group.

In TLS 1.3, we now change the following protocol messages[^keyshares]:

 1. In the `ClientHello`, the client sends over KEM public key(s) as key share(s).
 2. For the `ServerHello`, the server uses $\text{KEM-Encaps}(pk)$ and sends $ct$ as keyshare. 
       The subsequent messages are encrypted under the obtained $K$.

This would then for example allow us to plug in [Kyber 1024][kyber] instead of ECDH and do a post-quantum key exchange.
Unless we replace the signatures by a post-quantum signature scheme, the resulting protocol would only have post-quantum security against passive adversaries.
Those adversaries could otherwise record the messages and decrypt the key exchange by obtaining $x$ from $g^x$ using Shor's algorithm.

A quantum attacker could do active attacks by obtaining the private key from the RSA or Elliptic curve certificate and then forging signatures.
To preserve confidentiality when faced by these attackers, we would need a post-quantum signature scheme.
However, these signature schemes are often quite cumbersome, have large keys or are stateful.
OPTLS could be an alternative for these schemes, but we would need to change the handshake to get around OPTLS' requirement of having a non-interactive key exchange.
Current proposals for post-quantum NIKEs are just too slow to work in practice.

[^NIKEs]: If you want to do key exchanges where one of the key shares is a certified (EC)DH parameter, like in the OPTLS proposals, then RFC8446 DOES require non-interactive key exchang and KEMs don't work.
[^keyshares]: The TLS handhake defines the public keys sent over as "keyshares" and the algorithms supported as "supported groups". This naming is a bit unfortunate. There was a [pull request to change this to "supported key exchange methods"][kempr], but it never got adopted. It was recognised that this name may need to change at some point.

[rfc8446]: https://tools.ietf.org/html/rfc8446
[kyber]: https://pq-crystals.org/kyber/
[kempr]: https://mailarchive.ietf.org/arch/msg/tls/AnSksztK1vSaWB1Fzqdph0hryxw
