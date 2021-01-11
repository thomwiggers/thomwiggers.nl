+++
title = "Solving LPN Using Large Covering Codes"

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date = 2019-04-08T10:45:00+01:00
#date_end = 2019-04-08T15:45:00+01:00
all_day = false

# Schedule page publish date (NOT talk date).
publishDate = 2019-04-08

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["Thom Wiggers"]

# Location of event.
location = "Utrecht, The Netherlands"

# Name of event and optional event URL.
event = "Crypto Working Group 2019-04-12"
event_url = "https://www.win.tue.nl/eipsi/seminars_cwg.html"

# Abstract. What's your talk about?
abstract = """
Since quantum computers are expected to break most of the cryptographic schemes we rely on today, we need to look at alternatives. Learning
Parity with Noise (LPN) is mathematical problem that we can base cryptographic schemes on, and it is supposed to be hard for both
classical and quantum computers. We will be looking at how hard this problem actually is, by studying existing attacks on the LPN problem.
Most attacks on LPN use enormous amounts of memory. We aim to improve that situation."

More concretely, we study composing a reduction based on covering codes with a solving algorithm called Gauss. Both the reduction and the Gauss
algorithm use little memory, but by itself Gauss is slower than attacks that use more memory.

Unfortunately, we determine that this combination will not work. We also look at improving the codes used by the reduction by applying StGen
codes, which was proposed by Simona Samardjiska at a DS lunch talk in March 2017. While this improves run-time performance in theory, the
real-world performance is much less positive.

Finally, we developed software that we hope allows people to easily work with the LPN problem and the algorithms that aim to solve it.
"""

# Summary. An optional shortened abstract.
summary = ""

# Is this a featured talk? (true/false)
featured = false

# Tags (optional).
#   Set `tags = []` for no tags, or use the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["lpn", "post-quantum cryptography", "cryptography", "academic"]

# Markdown Slides (optional).
#   Associate this page with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references 
#   `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides = ""

# Optional filename of your slides within your talk folder or a URL.
url_slides = "presentation.pdf"

# Projects (optional).
#   Associate this talk with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["deep-learning"]` references 
#   `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects = []

# Links (optional).
url_pdf = ""
url_video = ""
url_code = ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
[image]
  # Caption (optional)
  caption = ""

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = ""
+++
