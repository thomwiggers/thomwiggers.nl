---
layout: post
category: code
title: Deprecating fields in MongoEngine Documents
date: 2015-07-26 17:01:45
---

I've had to rename some fields today with MongoEngine. Using the
following approach, I was able to raise ``DeprecationWarning``s
when old version were used.

Create the following function. It returns a property that will access
the new variable name.

{% highlight python %}
def deprecated_field(new_name):
    """Wrapper for deprecated fields"""
    def getter(self):
        warnings.warn('This field is deprecated, use {}'.format(new_name),
                      DeprecationWarning,
                      stacklevel=2)
        return getattr(self, new_name)

    def setter(self, value):
        warnings.warn('This field is deprecated, use {}'.format(new_name),
                      DeprecationWarning,
                      stacklevel=2)
        return setattr(self, new_name, value)

    return property(getter, setter)
{% endhighlight %}


Now use this function whenever you need to deprecate something

{% highlight python %}
class A:
    new_x = 'something'
    old_x = deprecated_field('new_x')
{% endhighlight %}

Trying to access ``A.old_x`` will now get the warning.

This will probably also work for regular Django Models, but I haven't tested that.
