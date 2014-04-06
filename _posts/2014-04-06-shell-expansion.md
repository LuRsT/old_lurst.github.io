---
title: Shell Expansion
layout: post
---

I learned about this nifty trick about two years ago from a colleague at work and ever since
I tried to use it because this can really spare your hands some typing, and it's also a fun
trick to show to your peers.

Basically this trick enables you to "expand" a string into multiple strings, I'll show you an
example because this is quite a wierd concept to get your head around:

    $ echo a
    a
    $ echo {a,b}
    a b
    $ echo {a,b,c}
    a b c

See? So basically whatever you put within `{}` gets printed, and for each `,` you get another
string. This is was a simple example to understand (hopefully), but not very useful, the power
of shell expansion comes when we join it with pre-existing strings, now for a more advanced
example:

    $ echo a{b,c}
    ab ac

So, what happened here? The initial `a` was repeated for each string inside `{}` together with
each charater, so if you can't see the power of this now, you will see in the next example:

    $ echo file.{txt,md}
    file.txt file.md

Hmmm, this looks familiar, it looks like the input to the `mv` command:

    $ mv file.txt file.md
    $ mv file.{txt,md}

And yes, you don't need to try it out, they both work the same way, but guess which one needs
fewer keystrokes (Yeah yeah, you can <Tab> but it's not as fun and you may not have completion).

Another useful examples where you can use this:

    # Create multiple files
    $ touch {a,b,c,d,e,f,g,h,i}
    # Rename part of a file
    $ mv _posts/2014-0{4,5}-06-shell-expansion.md

You can use Shell expansion for a lot of things, you just need a little creativity.

I'll leave you with a word of caution, if you want to add two different `{}`, the
behavior may be different from what you're thinking:

    # Want to rename a file in two different parts?
    $ mv _posts/2014-0{4,5}-0{6,7}-shell-expansion.md

You will end up with 3 files:

    _posts/2014-04-07-shell-expansion.md _posts/2014-05-06-shell-expansion.md _posts/2014-05-07-shell-expansion.md

Why, you ask? Because it is expanding twice, see what happens with the `echo` command:

    $ echo _posts/2014-0{4,5}-0{6,7}-shell-expansion.md
    _posts/2014-04-06-shell-expansion.md _posts/2014-04-07-shell-expansion.md _posts/2014-05-06-shell-expansion.md _posts/2014-05-07-shell-expansion.md

So be careful. If you are unsure of an expansion, I recommend you run it first through `echo`.

Read more [here](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_04.html)
