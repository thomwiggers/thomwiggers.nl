---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: '6rem'

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: me
      text: ''
      # Show a call-to-action button under your biography? (optional)
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      # Use the new Gradient Mesh which automatically adapts to the selected theme colors
      background:
        gradient_mesh:
          enable: true

      # Name heading sizing to accommodate long or short names
      name:
        size: md # Options: xs, sm, md, lg (default), xl

      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
  - block: markdown
    content:
      title: '📚 My Research'
      subtitle: ''
      text: |-
        Thom Wiggers is a cryptography researcher at [PQShield](https://pqshield.com).
        His research focuses on the design, formal analysis, and standardization of post-quantum cryptographic protocols.

        Building on his [PhD research]({{< ref "/publications/thesis" >}}) into KEM-based authentication (KEMTLS), he has recently worked on redesigning [Post-Quantum WireGuard]({{< ref "/publications/pq-wireguard" >}}) using reinforced KEMs and providing a comprehensive deniability analysis of the [Signal handshake protocol]({{< ref "/publications/bake" >}}).

        In the IETF, Thom is active in the PQUIP, PLANTS, and TLS working groups. In the TLS working group, he is a member of its formal analysis triage team (FATT). He is currently working on standardizing [state and backup management for stateful hash-based signatures]({{< ref "/events/2025-03-17-pquip-stateful-hbs" >}}) and has co-authored the [AuthKEM proposal]({{< ref "/docs/authkem-abridged" >}}) for TLS.
    design:
      columns: '1'
  - block: collection
    id: papers
    content:
      title: Featured Publications
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: 2
  - block: collection
    content:
      title: Recent Publications
      text: ''
      filters:
        folders:
          - publications
        exclude_featured: false
    design:
      view: citation
  - block: collection
    id: talks
    content:
      title: Recent & Upcoming Talks
      filters:
        folders:
          - events
    design:
      view: card
  - block: collection
    id: news
    content:
      title: Recent News
      subtitle: ''
      text: ''
      # Page type to display. E.g. post, talk, publication...
      page_type: blog
      # Choose how many pages you would like to display (0 = all pages)
      count: 10
      # Filter on criteria
      filters:
        author: ''
        category: ''
        tag: ''
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ''
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      view: card
      # Reduce spacing
      spacing:
        padding: [0, 0, 0, 0]
  - block: markdown
    id: contact
    content:
      title: Contact
      subtitle:
      text: |-
        You can reach me via email at [thom@thomwiggers.nl](mailto:thom@thomwiggers.nl).
    design:
      columns: '1'
---
