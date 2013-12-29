Title: How to lock the screen and suspend on i3 (or xmonad, openbox etc...)
Date: 2013-12-28
Author: Gil Goncalves

If you don't use a fancy graphical Desktop Manager like Xfce4/Gnome/KDE or the
other forks, sometimes it's hard to do some things, since you have to fiddle
with files and scripts to do the fancy stuff they do by default.

One of those things is suspend on power button press/lid closed/etc..., to do
this without using a DE, you can use the script located in
`/etc/acpi/handler.sh/` to do that for you.

Depending on your distro you may alredy have some contents there, here is a
snippet from mine:


    button/power)
        case "$2" in
            PBTN|PWRF)
                logger 'PowerButton pressed'
                ;;
            *)
                logger "ACPI action undefined: $2"
                ;;
        esac
        ;;


So in here you can add some commands to do anything you want whenever the power
button is pressed, here's what I did in mine:


    button/power)
        case "$2" in
            PBTN|PWRF)
                logger 'PowerButton pressed'
                DISPLAY=:0.0 su $USER -c /usr/bin/i3lock
                pm-suspend;
                ;;
            *)
                logger "ACPI action undefined: $2"
                ;;
        esac
        ;;


Now whenever I press the power button, the screen gets locked by i3 and then the
laptop is suspended.

This of course, as the name of the article shows, can be done when the computer
suspends, so this will do the trick:

    button/lid)
        case "$3" in
            close)
                logger 'LID closed'
                DISPLAY=:0.0 su $USER -c /usr/bin/i3lock
                pm-suspend
                ;;
            open)
                logger 'LID opened'
                ;;
            *)
                logger "ACPI action undefined: $3"
                ;;
        esac
        ;;


If you're using xscreensaver, you just need to change `/usr/bin/i3lock` to
 `/usr/bin/xscreensaver-command -l`.

Pages where I took this from:

[https://bbs.archlinux.org/viewtopic.php?id=70364](https://bbs.archlinux.org/viewtopic.php?id=70364)

[https://bbs.archlinux.org/viewtopic.php?id=140932](https://bbs.archlinux.org/viewtopic.php?id=140932)

