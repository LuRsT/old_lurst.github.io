Title: How to fix problem with wireless mouse disconnecting after suspend
Date: 2012-10-13
Author: Gil Goncalves


I have had this problem for quite some time, where if I was using a wireless
mouse and I suspended my computer, afterwards, the mouse would disconnect
every 10 seconds and I had to shake it a bit to wake it up, so this got quite
annoying now that I'm using it more and more, to the point where I managed to
finally fix it.

Turns out, laptop-mode has an USB autosuspend feature, so the problem is that
by default, at least in my Linux distro (Manjaro) it is `auto`, so I just
setted it to `no`:

    sudo vim /etc/laptop-mode/conf.d/usb-autosuspend.conf

These are the line to change:

    # Enable USB autosuspend feature?
    # Set to 0 to disable
    CONTROL_USB_AUTOSUSPEND="no"

Hope this helps someone else.

