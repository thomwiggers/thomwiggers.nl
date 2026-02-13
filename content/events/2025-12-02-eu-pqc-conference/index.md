---
# Documentation: https://docs.hugoblox.com/managing-content/

title: "Fully PQ TLS in the WWW"
event: "European Conference on PQC Migration 2025"
event_url: "https://pqc-conference.eu"
location: New Babylon Conference Centre
address:
  street: Anna van Buerenplein 29
  city: Den Haag
  region:
  postcode: 2595 DA
  country: The Netherlands
summary: |
  Key exchange in TLS is now mostly PQ! But what about authentication?
  In this talk, I discussed some of the ongoing work to make the costs
  of PQ certificates acceptable so that people will actually want to
  deploy them.

abstract:

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2025-12-03T14:35:00+01:00
date_end: 2025-12-03T15:00:00+01:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2025-12-03T17:18:46+01:00

authors: ['thom']
tags: []

# Is this a featured event? (true/false)
featured: true

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

# Optional filename of your slides within your event's folder or a URL.


# Markdown Slides (optional).
#   Associate this event with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

_AI-generated summary of my slides_

While the industry has successfully deployed Post-Quantum (PQ) Key Exchange,
the next step—PQ Authentication—presents significant infrastructure challenges
due to data size and latency. The presentation proposes **Merkle Tree
Certificates (MTC)** as a sustainable solution to enable full PQ security
without breaking the web.

### **1. Current Status: Key Exchange is Solved**
*   **Adoption:** Major players (Cloudflare, Chrome, Edge, Firefox) have already deployed PQ key exchange.
*   **Performance:** The current standard (X25519MLKEM768) adds only ~2kB to the handshake and causes a negligible ~4% slowdown.
*   **Motivation:** This is widely adopted because it solves the immediate "Harvest-Now-Decrypt-Later" threat.

### **2. The Challenge: PQ Authentication**
Implementing PQ authentication (signatures) is much harder than key exchange:
*   **The Bloat Problem:** Replacing current authentication chains (Server cert, Intermediate cert, Handshake signature, Certificate Transparency SCTs) with PQ standards like ML-DSA adds **18–36 kB** of data to the handshake.
*   **Operator Hesitance:** For website operators, this creates a massive performance hit for a threat that only exists in the future (the "Quantum Apocalypse"). Many are likely to "wait" rather than upgrade.
*   **Infrastructure Strain:** The current Certificate Transparency (CT) system is already fragile and expensive to maintain (consuming ~20TB of disk/year per log). Adding large PQ signatures would make running CT logs significantly harder and more expensive.

### **3. The Solution: Merkle Tree Certificates (MTC)**
To solve the data bloat issue, the IETF is standardizing Merkle Tree Certificates (MTC).
*   **How it Works:** Instead of a traditional chain of signatures, a Certificate Authority (CA) logs the certificate into a Merkle Tree. The "certificate" becomes a proof of inclusion in that tree.
*   **The Process:**
    1.  The CA logs the entry first, then signs a "tree head" (checkpoint).
    2.  Browsers/Clients fetch these tree heads out-of-band.
    3.  The server proves its certificate is valid via a short inclusion path (Merkle path).
*   **Short-lived Certificates:** MTCs allow for "signature-less" certificates if the client is up-to-date, or "full" certificates if not, utilizing short-lived proofs.

### **4. Key Benefits of MTC**
*   **Massive Size Reduction:** MTC log entries are **97x smaller** than the traditional CT approach combined with ML-DSA-44 signatures.
*   **Efficiency:** An inclusion proof is only ~736 bytes, compared to >7KB for multiple ML-DSA signatures.
*   **Sustainability:** It removes the need for intermediate certificates and makes running transparency mirrors cheaper and more reliable.

### **5. Timeline and Standardization**
*   **Standards Body:** The proposal is being developed in the IETF **PLANTS** (PKI, Logs, And Tree Signatures) working group.
*   **Backers:** The initiative is being pushed primarily by Google Chrome and Cloudflare.
*   **Deployment:** Cloudflare and Google have announced plans to begin experimenting with MTC on the web in **2026**.
