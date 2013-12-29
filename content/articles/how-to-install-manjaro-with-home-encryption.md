Title: How to install Manjaro Linux with /home encrypted
Date: 2013-12-28
Author: Gil Goncalves

So, this weekend I decided to upgrade my little Asus Vivobook with my old SSD
since I want to only use one laptop, and having one laptop that I don't intend
to use for programming with an SDD and another which I do use for programming
without doesn't make sense.

Having moved all the data around is time consuming enough, but I still had to
deal with the fact that the laptop uses a slim hard drive and my SSD wasn't very
slim at all, so I had to remove the SSD casing and plug it it, and it worked
right away!

But I was far from finishing the setup of my machine, I had to install Linux on
it, and this shouldn't be difficult but I wanted my /home partition to be
encrypted and that complicated everything...

I won't bother you with the details of my many installations until I got it
right, so here are the instructions:

* Create the partitions you'll need with Gparted;
* Use the testing installation (cli) and setup everything that you need, just
don't partition anything since you already did it in Gparted.
* After that create the LUKS partition in the /home partition
* Configure your system by putting these HOOKS in `mkinitcpio.conf` BEFORE
`filesystem`:
    * `encrypt`
    * `lvm2`
* Add this line to `/etc/crypttab`:


    home /dev/sda3 none luks


If you could not do the last step during the installation it's ok, you can do
it from the live cd, just change the file in the correct partition that should
be mounted by manjaro.

If you failed to put the HOOKS in `mkinitcpio.conf` (which I did), you'll have
to do a little `chroot` magic, which I'll explain in another article...
