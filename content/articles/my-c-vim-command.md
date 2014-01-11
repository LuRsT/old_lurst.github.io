Title: My ç vim command
Date: 2012-10-06
Author: Gil Goncalves

When I saw this [video](https://www.youtube.com/watch?v=iwVvqwLDsJo) about
iPython, I liked the idea of running commands within the editor we're using,
and showing the output inside it after running it. Since my editor of choice
is vim, I started working on something like that for me. First I've got this
one:

    map ç :read !

I used ç since vim isn't using it for anything, what this does is simply upon
pressing ç in normal mode, waits for my input into :! and inserts the output in
the line bellow the one that I'm editing. But this wasn't what I wanted, I
wanted to run the line where my cursor was. For that, I did this:

    map ç :cexpr system(getline("."))<cr>:cope<cr><cr>

This executes the line where the cursor is, opening a :cope window inside vim
with the output from the command, not really what I wanted but a lot closer.

I'm going to try and mix the both of them to copy the iPython behaviour.

Update: Since I don't have that letter in my keyboard layout anymore, I'm now
using upper case 'c' for this purpose.

