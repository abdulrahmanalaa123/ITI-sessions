# 9-12-2024

## Setting up a vm as an ftp server and I would be the client using ftpd

- first install vsftpd on centos using yum 

## learned along the way

### Vsftpd

### chroot
- well chroot is a virtual root folder change for the current process and all of its children which is useful in the ftp server where you can set the ftp directory as the root directory for the anon user for example cant access but it
- and if you use ldd to see the required shared libraries or binaries needed for the chroot to take a copy of the directory you're trying to make the root to work
- creates an isolated environment which is perfect for ftp


### sda1
- is mass storage driver , a = 1st registered device on the system, 1 = 1st partition on that device
- is just a block storage inside your hard drive
### fstab , df 
- fstab is the mounting map for the linux which implies where and what to boot from which partition but wont look into that since its not of that much use rn 
- df prints the current available storage space on the device with all its partitions and drives, etc.
### apropos
- the manuals library
### friewalld
- firewalld is a zone based firewall which puts poilicies and services with rules against different zones
- so what does zone based mean? a zone is typically a network whihc is connected by a router zone based firewalls work on zone to zone communication which unlike past where each device has his context based firewall (not delving into this rabbit hole)
- zone based configurations are usually split into 3 main types 
#### Main Types of Zones
- public zones which accesses the internet which is configured for outbound requests coming into my server 
- private zones are firewall rules applied to internal zone to zone communication for example i have a netowrk of pcs that wants to communicate to another inside my facility we mark these with private zones and assigning the proper interface
- DMZ (dematerialized zones) its a neutral zone (keep in mind i dont understand it that well its a bit out of my scope rn) its said to be the zones which are in between public and private zones they dont access the internet but can be accessed publicly sth like that dont really know for sure but yet its one type i guess
- It is encouraged to put ftp servers on dmz because if it does get compromised people dont get access to the private network or your sensitive info thats logical but yet i cant configure that atm so fuck it
