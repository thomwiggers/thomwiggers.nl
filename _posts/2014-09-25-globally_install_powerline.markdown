---
layout: post
category: linux
title: Globally install powerline
date: 2014-09-25 23:50:18
---

Today I've tried to globally install [Powerline][1]. That was a bit of a pain
because it has no global config files.

Quick and dirty how-to:

1. Add `XDG_CONFIG_DIRS=/etc/xdg` to `/etc/environment` if it isn't already set,
2. Copy the config to `/etc/xdg/powerline`,
3. Customize config,
4. Load powerline from `/etc/bash.bashrc`, `~/.zshrc`, etc.

My config can be found at [on Github][2]

[1]: https://powerline.readthedocs.org
[2]: https://github.com/thomwiggers/powerline-config
