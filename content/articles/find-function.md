Title: Find Function
Date: 2012-10-13
Author: Gil Goncalves

I got this idea the other day, one command that I repeat often is the
`:g/<search>` to know which functions there are within the source file I'm
reading, since I mostly code perl and python, I had to use the autocmd to
distinguish between the two of them, so this is what I ended up with:

    autocmd FileType perl   nn <silent> _F :g/sub<CR>
    autocmd FileType python nn <silent> _F :g/def<CR>

Pretty simple and efective, just type \_F in normal mode to get the definition
of functions in a 'window' within vim.

