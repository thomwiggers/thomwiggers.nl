+++
# Display name
title = "Thom Wiggers"

# Username (this should match the folder name)
authors = ["thom"]

# Is this the primary user of the site?
superuser = true

# Role/position
role = "Senior Cryptography Researcher"

# Organizations/Affiliations
#   Separate multiple entries with a comma, using the form: `[ {name="Org1", url=""}, {name="Org2", url=""} ]`.
organizations = [ { name = "PQShield", url = "https://pqshield.com/" } ]

# Short bio (displayed in user profile at end of posts)
bio = "My research interests include (post-quantum) cryptography and protocols"

# Enter email to display Gravatar (if Gravatar enabled in Config)
email = "thom@thomwiggers.nl"

# List (academic) interests or hobbies
interests = [
  "Cryptography",
  "Post-Quantum Cryptography",
  "Protocols",
  "Information Security",
]

# Organizational groups that you belong to (for People widget)
#   Set this to `[]` or comment out if you are not using People widget.
user_groups = []

highlight_name = true

# List qualifications (such as academic degrees)
[[education.courses]]
  course = "Ph.D. in Post-Quantum Cryptography"
  institution = "Radboud University Nijmegen"
  year = 2024

[[education.courses]]
  course = "MSc in Computing Science"
  institution = "Radboud University Nijmegen"
  year = 2018

# [[education.courses]]
#   course = "BScs in Computing Science and Information Sciences"
#   institution = "Radboud University Nijmegen"
#   year = 2015

# Social/Academic Networking
# For available icons, see: https://sourcethemes.com/academic/docs/widgets/#icons
#   For an email link, use "fas" icon pack, "envelope" icon, and a link in the
#   form "mailto:your-email@example.com" or "#contact" for contact widget.

[[social]]
  icon = "envelope"
  icon_pack = "fas"
  link = "#contact"  # For a direct email link, use "mailto:test@example.org".

[[social]]
  icon = "twitter"
  icon_pack = "fab"
  link = "https://twitter.com/thomwiggers"

[[social]]
  icon = "mastodon"
  icon_pack = "fab"
  link = "https://infosec.exchange/@thomw"

[[social]]
  icon = "google-scholar"
  icon_pack = "ai"
  link = "https://scholar.google.co.uk/citations?user=V0A4RMsAAAAJ"

[[social]]
  icon = "github"
  icon_pack = "fab"
  link = "https://github.com/thomwiggers"

[[social]]
  icon = "linkedin"
  icon_pack = "fab"
  link = "https://www.linkedin.com/in/thomwiggers/"

# Link to a PDF of your resume/CV from the About widget.
# To enable, copy your resume/CV to `static/files/cv.pdf` and uncomment the lines below.
# [[social]]
#   icon = "cv"
#   icon_pack = "ai"
#   link = "files/cv.pdf"


+++

Thom Wiggers is a cryptography researcher at [PQShield](https://pqshield.com).
His [PhD thesis][thesis] was on the interactions of post-quantum cryptography with protocols, under the supervision of [Peter Schwabe][cryptojedi], at the Institute of Computing and Information Sciences, Radboud University in The Netherlands.

[cryptojedi]: https://cryptojedi.org/peter/
[thesis]: {{< ref "/publication/thesis" >}}