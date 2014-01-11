Title: Set AltGr key using xmodmap
Date: 2013-10-02
Author: Gil Goncalves

Get the complete layout:

    xmodmap -pke > ~/.Xmodmap

Find the correct keycode that you want to change (e.g. the Left Windows key):

    keycode 134 = Super_L NoSymbol Syper_L

Update it with this:

    keycode 134 = ISO_Level3_Shift Multi_key ISO_Level3_Shift Multi_key

Test it by doing:

    xmodmap ~/.Xmodmap

If you just need to change that key, you can simply create a file with only that
line and be sure to automaticaly run `xmodmap ~/.Xmodmap` every time you login.

