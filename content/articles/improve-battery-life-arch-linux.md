Title: How to improve battery life on Arch linux
Date: 2014-03-02
Author: Gil Goncalves

Today I decided to make my laptop's battery last a bit more, so I looked for a
way to do it, since I had to fiddle a bit a look multiple sources, I decided to
create a blog post to rule them all.

So, this will be the instructions on how to improve the battery life on an Arch
or Manjaro Linux with `systemd` installed.

### What needs tuning?

First, you need to install powertop:

    sudo pacman -S powertop
    sudo pacman -S ethtool # This may be required for the optimization process

Next, use it to create a report with it, like so:

    sudo powertop -html

You will end up with a file called `tml.html` in your $HOME directory.

Now, open it and go to the "Tuning" tab, in there you will find a description
of what to tune and to the right, a command to do it, you should use your
common sense and google abilities to pick the things that you want to improve.

Move the ones you want to a file somewhere in the system, I picked
`/usr/local/bin/powertop_tuning.sh` but as long as root can control it, you can put it,
whatever you want.

Your file now may look like this:

    #!/bin/bash

    # NMI watchdog should be turned off
    echo '0' > '/proc/sys/kernel/nmi_watchdog';

    # Other stuff

I know mine does, we need to make it executable:

    sudo chmod +x /usr/local/bin/powertop_tuning.sh

Bam! Done! No, not really, to test it, you should execute it and then do the
report again to check if the tuning tab doesnt have the issues anymore.

#### Optional

    sudo /usr/local/bin/powertop_tuning.sh
    sudo powertop -html

    (Check the tab)

### Create the service

Now, to make this script executable everytime you turn your pc on, we need to
create a service, calm down, it's not that hard. Reminder: This is for `systemd`

Now open/create this file (you can pick a different name if you like):

    sudo $EDITOR /lib/systemd/system/powertop_tuning.service

And put this inside:

    [Unit]
    Description="PowerTop Tuning config"
    ConditionPathExists=/usr/local/bin/powertop_tuning.sh

    [Service]
    Type=oneshot
    RemainAfterExit=yes
    KillMode=none
    ExecStart=/usr/local/bin/powertop_tuning.sh
    ExecStop=exit

    [Install]
    WantedBy=multi-user.target

Wow, now you created your own service, congratulate yourself! Now for the
boring part, testing it:

#### Optional

    sudo systemctl start powertop_tuning.service
    sudo powertop -html

    (Check the tab)

If everything looks ok, you just need one more last step...

### Start it automatically

Finally run this:

    sudo systemctl enable powertop_tuning.service

You are now the proud (hopefully) owner of a laptop with improved battery life :)

