# 1-12-2024

## Computer Netowrks Fundementals

### basics
#### software components

- Protocols are there to standardize the communication between devices
- These are considered one of the software components of networking
- messages are considered a software component for some reason.

#### hardware components
- NIC with the mac adress burned on the NIC and unique for each chip
- ***mac address cant be changed although there is spoofing dont know if it changes the underlying chip mac address or just exposing a differenet mac address to the network although it can be changed and needs to be checked***
- the hub is the broadcasting device which sends the message to all devices till it finds the reciever which comprimises security and efficiency 
- switches creates lan networks for devices to communicate each other effectively rather than the hub
- routers connects networks together
- Access points are a network extender extending a wired network into a wireless network and thats it 
- repeaters are used for increasing the signal strenght


### networks according to covered areas 

- PAN this defines that the definition of a network is kind of vague it doesnt specify including these specified hardware components its just a group of devices transmitting data or resources across each other
- LAN this is the typical representation of a network which requires one of the predefined hardware components such as a switch where a group of devices or computers per se connected together through a switch 
- ***for switches to be connected to each other they must be connected to each other using a router but the reason why is because of the address ranges would be unidentified*** 
- MAN connecting accross several 
- WAN is the connection of networks across each other connecting multiple LANS together
- The Internet is just a huge wan which is a network of networks or I presume is considered a WAN of WANS mbe 

### The Internet
- ICANN is the corporation that handles the naming and numbers which allows translating names into ip addresses such as google.com

### Topologies
- Star Topology from its cons are its single point of failure and congestion issues without management for communication pros are adding devices and failure of a device wouldnt affect the network as a whole as well as troubleshooting is easy
- Star topology using a siwtch is called a switch star and a hub is a hub star topology
- Ring topology his pros are only that he's fast and can handle congestion well since it only flows in one direction using a token that carries the data needed to be transferred  and his cons that if one node fails the network fails and that it loses the speed if connected devices exceeds 60 
- dual ring topology fixes the one direction transfer issue
- mesh topology is the connection directly of devices to each other doesnt scale well with issues including complexity of cables together as well as durable and secure since no connection out of the network can access it and its divided into full and partial mesh topology regarding the connection links 

- hybrid topology is just utilizing several topologies together regualrly connect by a switch or a router i presume 

### Network Models
- PtP Network specifies that they all are the same authority inside the netowrk not necessarily giving any privelage to the other. 
- Server-Client Model
- Servers are just a powerful computer taht hosts services that could serve several clients which doesnt necessarily specified as a powerful computer but thats a requirement to serve several customers

# 2-12-2024

## Basics

### Protocols

- OSI model was a standardized refernce model made by the ISO copropration to aid in generalizing the connection methods between devices manufactured by different companies

- Application
- Presentation
- session
- transport 
- network
- data link
- physical

ip addresses define the location and network info while mac addresses are unique and can be utilized in communication between device but it wouldnt be an efficient way because routing to it would be extremely exhaustive and impossible since it has no info about how to reach but only has info about what to reach which is the device being sent to.

### MAC Addresses

- mac addresses 
- physical addresses can be either unicast, multicast , broadcast
- and these are the physical addresses depending on the type of connection and restrictions on communications

### Netowrk layer inside the TCP/IP

- ip addresses and subnet masking 
- ip addresses can be assigned automatically by the router using dhcp
- dhcp dynamic hsot configuration protocol
- you can set ip addresses manually
- ***ip address classes need to look it up as well as dhcp***
- ip addresses in the 172.16.x.x (B) or 196.168.x.x (C) or 10.x.x.x (A) are reserved for private ip addresses and public resides in anywhere outside these ranges
- apipa is a temp ip address that is assigned to the device while the dhcp is down and is given the ip address 168.124.x.x and cant acces the internet while using the apipa address
- pinging the loopback ip address is used for checking that the NIC is working correctly or not 

# 3-12-2024

## TCP/IP protocols

### Trasnport layer

- transport layer is where the data is segmented and checksum on checking the packet's validity
- its where the protocol used to send the message is determined
- its where the connection check is performed when using the tcp protocol

#### TCP protocol
- connection oriented where it denies sending unless a connection is established
- it works using three way handshakes sends sync and waits from an ack and then starts sending
- and the handshake is performed on each window size which is determined by the ctl which is tcp's method of flow control and the number of fragments or segments of the data are determined with the sync request at the beginning.
- each packet is assigned a sequence no. so that the reciever can reorganize the packets after receivin them given that it was sent out of order.

#### UDP protocol
- connectionles unreliable and a faster unsecure channel of sending data without sequencing

#### ports
- port mapping is used to differentiate differnt services using the same connection protocol whihc is defined wiht the reserved ports
- ports are used to define which connection methods are we using
- socket address is combining the ip address alongisde its port number or the service its using

### Application Layer
- includes the protocols that are used to transmit messages using different methods
#### DNS
- THE DNS job is to translate the URL from protocol://socket-address.host
- into a name only which is given the domain name
- top level domains are .com .edu .gov , etc.
- the browser resolves the ip to which youre going to by looking into the browser cache to find the ip address if not found looks into the /etc/hosts file isnidei your device and next is finally asking the dns servie to translate teh given name into an ip address
***nslookup doesnt show several ip addresses on yahoo.com while google.com shows only 1 ip address***
#### FTP
- file transferring protocol most of waht was explained is how to use it not on how does it exactly work neither its headers, form, etc.
#### Mail server
***needs to be studied again as well as what protocol does google uses for gmail***
- smtp protocol is one of the protocol
- pop3
- the question is the difference between smtp and pop3
- she discussed the mail server quota and how pop3 saves up the mail server quota
#### telnet and ssh
- remote access to a machine telnet sends the data between the two devices using plain text
- while ssh is the standard right now and offers a much more secure connection

# 5-12-2024

## CyberSecurity

- Security is as secure as its weakest link
- the three links for security are The client (End user)
- Network resources (Routers, Switches, or even Mobile Networks)
- Server Resources (Blade Servers, Rack Mounts)

### CIA 

#### confidentiality
- The data allocated or process performed needs to be condifential with no access for any one
#### integrity
- The data allocated or process performed determines its integrity by minimalizing or proofing tampering using such methods as hashing and checksums, etc.
#### Availability
- The data is available only to the owner and the chosen members with access to it and cant be changed unauthorized 

### Security is as important as what you are protecting
- No security system can awork with the system of 9s like 3 9s 99.9% because there's always a vulnerability inside the system which can be managed to be cracked

### Hat types
- Black (Malicious)
- White (Security analysis)
- Grey (A bit of both)

- Social engineering is the art of manipulating people and identifying several key info enough to access their account or credentials, etc.
- Phising attack 
- spoofing is modifying the source of packets so that they appear to be coming from someone else
- man in the middle attack is someone that cna intercept the packets sent between two devices usually due to wifi as well as he can only intercept and understand non encrypted data sent between those 2 nodes 
### Malwares
- Independent Malicious software means that once its on the device it doesnt need interaction to be activated like worms or zombies
- Dependent are systems that need a host system to spread cant replicate on its own like viruses, trojans 
- Worms are of the family of trojans, and they are the transfer medium or the program to replicate and transfer itself onto several devices where it doesnt require user access or host initiation for it to start replicating as well as run their onboarded viruses which can be replicated throughout the network or through storage systems, etc.
- Zombies are a malware which can replicate itself but it hijacks the computer and uses its resources for malicious activities could be mining or using them as a node for ddosing, etc.
- man in the middle is the attack responsible for intercepting the incoming packets and utilizing it in malicious activities but normally intercepting the packets he cant identify anything due to encryption standards in https and several connection methods 

### IPS
- IPS is an intrusion prevention system which can be divided into two categories host based which on an end client and a network based one installed on the network device how can it detect the intrusion is based on three types a combination of them also keep in mind that IPS isnt deployed and cant protect on its own it is deployed usually within a protection suite of programs like an advanced firewall, etc.
- History of attacks: detects network activity for registered malicious attacks that has historically been done
- Anomaly detection: detect anomalies inside the network by analyzing a random sample of requests made by the host or network
- Policy based: where it detects intrusions based on policies or requests defined by the adminstrator such as for example any ftp reuqest is denied, etc.

***the question is how can a vpn protect which sounds like bs to me since it doesnt provide any encryption over outcoming requests he still can intercept it using his router and or the pinapple, etc. vpn wouldnt protect shit from that needs to be looked upon*** 
***on my knowledge vpn is shit well here is what backs it but the concensus of people on stackoverflow and its a useless topic atm needs no further searching but yet im confident im right https://stackoverflow.com/questions/50033054/can-a-man-in-the-middle-attack-on-an-https-read-all-the-communication***

# 7-12-2024
## Security

### Firewalls
- FireWall can control inbound and outbound requests where it resides in the network and transport layer
- IPS/IDS
- nextgengfirewall (includes IPS/IDS/Firewall all in one system)
### Proxy servers
- A rerouting agent responsible for obsucring the source ip address and changing its origin location which acts as a middleman between us
- A vpn
### VPN
- The Vpn includes a tunneled connection which is directed between the device and destination network to be such as a device inside the network and can only be configured inside that network 
### Wireless Access security
- close the SSID which is what broadcasts the network or wifi to everyone which means it is hidden
- wpa2 strong securit uses AES
- ACL mac address access control list

## Distributed Systems
- is a state that divides traffic over multiple pcs 
- More robust
### scalability types
- Vertical
- Horizontal 

### Distributed Systems Architecture
- peer to peer 
- 3 Tier
- n tier architecture

### Distributed Systems characteristics

***I dont like throwing terms and what are the cons of distributed systems alot was left out while explaining distributed systems which isnt that good but alot of research needs to be done naturally although these characteristics im sure that most of them are lose and arent a defined terms***

- scalability
- heterogeneity
- security
- openness
- failure handling (in other terms availability)
- concurrency 
- transparency

***keep in mind I will explain this later as i didnt write much because it seems that the discussion on this day wasnt enough for explaining these charachteristics or distributed systems in general maybe in another repo not here neither the security as well***

# 9-12-2024

https://dev.to/sardarmudassaralikhan/layered-architecture-used-in-software-development-8jd

## Choosing between Relational and non-relational databases
- it was specified by the amount of joins needed to be performed to retrieve on unit of data or the deepest length
- and using relational in the ocnsistency of the input data like for exmaple im making an email storing database with attachments i dont know what types of attachments are we adding then we might choose no sql while you can give arguments for relational but just bear with me 

ptp database cant be a relational database
database sharding doesnt provide several endpoints and neither a simulated one she says that when using relational databases it must be on one endpoint even if its sharded which is bs i think gotta check
(reasoinings are fucked up)

columnar data storage vs column oriented databases

keys and weak entities candidate vs primary vs surrogate key vs partial key

how would a string column be indexed and would integer be easier in indexing than strings
 check on anomalies as well insertion , deletion , updating anomaly and its relation to not choosing a primary key for the ssn of the child

shopping cart best practises she says its a big nono fro saving a shopping cart inside the database ffs that's fucking dumb

reason for nroomalizing your database schema?? when to not as well

Concurrent data access behaviour on sql server with transactions commits, etc.


# 11-12-2024


## Operating Systems

- OS is simply just a sfotware
- Cpu's Components are:
### ALU
- is the arithmetci logic unit responsible for arithmetic operations and logical operations probably
### Registers
- MAR is the register required to store the address of the memory needs to be accessed
- MDR is the data registry which stroes data being transferred to and from memory so not only the address for fast calculations if it stays in the disk it will halt the process of calculation needs to be very fast
- AC (Where itermediate  arithmetic and logic results are stored) (dont understand that fully)
- PC program counter contains the address of the next instruction to be executed
- CIR current instruction register address of the current instruction needed to be executed
### Address Bus
- carries the addresses between the memory and the registers or processor 
- carries a maximum of a word size
### Data Bus
- carries the data between the memory and the registers and ( processor)
- while this i believe can handle multiple bytes of data
### porcces bus
- its the bus which carries the instructions performed by the cpu between it and the memory i believe (not fully understood as well)
### ROM
- Read only memory used in the boot sequence and boot oeprations done on os startup boot sequence is called boot strapping
### drivers
- its a usage manual for the os to interact with the hw device
### kernel
- its the base level process that needs to be running it relies on kernel modules which are base processes running on the kernel like graphics modules network module, etc.
### Control unit
### multiprocessor systems
- serving and loading processes comes in different algorithms and its called a schedhuling algorithm
- Their whole goal is to optimize throughput (amount of rpocesses done), utilization (decrease down time), a 
- Round robin random processes selection
- shortest job serve first
- Firtst in first serve
***paging ???***
### IPC (Inter process communication)
- Its the procols used to communicate between applications depending on the os
### Responsibilities of an OS
- Scheduliing
- Memory management
- Io and resource management
- Security (Access and protection)
- File Systems
- User interfacing (ease of access) (GUI/Shell)
## Scheduling
- A process (job) any program running
### Program execution 
- process conents:
- text section Program instructions
- program counter: next instruction address
- Stack section: ordered data? ( at least he said that) 
- heap section: static and global variables , Dynamic allocation of variables 

### Process States
- create (new)
- admitted (ready)
- the running and waiting process or interrupting is the job of the scheduler
- running back to ready only happens on interrupting signals and timeouting of the process
- terminated 
### Process control block ( i dont actually understand what this is at least)
- pointer (only occurs in child processes and not parent processes)
- because the child process has the pointer of its parent to know which process it will return their outcome 
- priority
- pc
- Cpu registers (MAR, MDR,AC)
- Memory managemnt info
- IO information
- Accounting information

### context switching
- its a factor that should be taken in account as an overhead for the process for example process A and B switching from A to B you need to save the state of A and load the state of B and run B then stop and load the state of A  

### Schedhuling criteria 
- Cput utilization and Execution runtime the processes utilizing the cpu excluding idle cycles
- Volume/Excution throughput is the ratio between the amount of processes you have into you and the amoutn you serve
- 
- 
### Memory management
- Memory management is encessary in 3 parts
- Exchtable is loaded into memory
- loading data required by the process before hand
- loading data required by the process in runtime (stack/heap)
### Address binding
- didnt understand it at all
### IPC methods
#### Shared Memory method
- using memory as a shared resource for communcating between processes which could be a hassle in synchronization
#### IPC
- using system calls to share data between processes in the kernels
- we can also use tcp ip to communcate between cpus called the internet 
### I/O
- 
### File Systems 
- File systems is composed of two services 
- Directory Service , Storage Service

# 12-12-2024
what i dont understand since most are basic commands and listing file directories which i already know
- more vs less
- find vs locate

- you can use wild cards inside the command in itself no need to use grep to use them
- col command in linux dont understand
# 13-12-2024

# user management 
- any service running on my machine needs to have a user to control its permissions on files and directories it owns

```
- tomato:x:1000:1000:tomato,,,:/home/tomato:/bin/bash
- tomato is my username
- x is supposedly the passwd but it is no longer saved there
- and 1000 is my user id
- and 1000 is my group id
- tomato ,,, comment about the user oftenly is the full name of the user
- /home/tomato home dir
- /bin/bash is the user login shell
```

- terminal is the front interface for the shellwhich is the link between you and the kernel

```
- tomato:$y$j9T$6HNUejiY3qUTCGrMFyCnq0$w3NfAjeMbYeFB3ocUji74e9hMpII0/6Q8VSmSXlo348:20065:0:99999:7:::
```

- 20065 the last time the user changed his passwd and time is calculate since he last changed it
- 0 is the amount of days he needs to wait so he could change his passwd again
- 99999 is the maximum amount of days needed for the passwd change which is infinity meaning you dont need to change it basically
- 7 is th warning days happens before expiring of the passwd 
- : is the amount of days where the passwd is inactive
- : after passing the inactive days the account expires 
- the last is for future use

```
- lxd:x:135:tomato
- tomato:x:1000:
```

- tomato group name
- x is a discarded position
- 1000 is the group ids

# contorlling users
- useradd modifies /etc/passwd
- -md means we're defining his home dir 
- -s defines his shell location /bin/bash
- -c comment ",,," which was shown above
- /etc/skel is the folder whihc is needed to initialize the home dir for the user
- su - omar swtiching the user specifying "-" meaning we're changing the user and going into his home directory

- id shows the current id and the groups you're in

```
 -> id
- gid=1000(tomato) groups=1000(tomato),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),122(lpadmin),135(lxd),136(sambashare)
```
- where the primary group is 1000(tomato) and all the others are supplementary groups for us (don't really know why specify them as supplementary)

- usermod changes anything about the user if you're the sudo user -s changing his shell and -g changing his primary group keep in mind options come before the user name
- sudo usermod -s /bin/bash -g hamada omar
- meaning we swtich the shell to bash and his primary group is hamada
- primary group's use is that anything created by the user by default the file's group owner is the primary group
- supplementary groups are groups where you have their same permissions as well you can change file's group owner into one of the supplementary groups you belong to 
- usermod -G overrides all the supplementary groups of the user to the specifiedgroup of -G  in usermod to append you need to specify the option -a which is append user mod changes the data which can be changed in chage but for another user i think
- keep in mind in the etc/groups shows the supplementary members and no thte primary members and each primary isnt shown in the file after the line explaining the groups
- sudo chage -l [user name] lists the current settings for the user which is apparent in the shadow file whihc we explained before 
- to change each in an interactive form dont write any options and to set 
- just check the man for each condition the only important thing is just how to list them

```
Last password change					: ديس 08, 2024
Password expires					: never
Password inactive					: never
Account expires						: never
Minimum number of days between password change		: 0
Maximum number of days between password change		: 99999
Number of days of warning before password expires	: 7
```

- this is the output for you to remember 
- userdel deletes the user also chekc the man but keep in mind basically -r removes any data assigned to the group and the -R capital command deletes chroot user with all his chroot data
- groupadd adds groups and adds user to the group
- as well as modifying groups you can modify the id of the groups
- who and w and whoami to 
- who is for who is logged in on the system
- w shows it in the long form
- whoami shows the user youre logged in as
- newgrp changes your current primary group to the group specified but the group must be on of the supplementary groups you belong to 
- ctrl D exits the current group resetting to your primary group
- gpasswd such as passwd command changes the passwd for the user gpasswd changes the passwd for the group
- chown changes the file owners and groups owners you can use chown owner:ownergroup and tochange user just write chown owner and for changing a group :ownerg

# 14-12-2024

## permissions
- first defining chmod and the symoblic permission setting as in chmod
- dir read is the capability of lsing the folder and for the file its lsing as well as cat on the file
- and for writing for the file is editing it and for the dir is deleting the dir or creating a new file or deleting a file inside
- and for the execute on the dir enables you to navigate to the dir by cd and on the file enables you to run it

- the symbolic permissions for the files and directories as explained above
- chmod u=#,g=#,o=# <file name> for the u is the owner of the file and g is the owner group of the file which usually if not changed is the primary group of the owner that created the file and others is anyone other than these 2 sets
- now for the rules application it goes in a heirarchy first it sees if youre a a user and applies its permissions if it occcurs it doesnt check for more then if youre a group and lastly the others permissions
- now defining the permissions in octals which is a binary set representation for the permissions which is a 3 bit set r-w-x 4-2-1 and the sum represents the combinations of these permissions r-x = 5 and combining them into 3 sets of permissions ugo 756 => rwx,r-x,rw- 

***there is a fourth member in the set which is defined by the ACL will be explained later in the course or i would just look it up later today***

- now to apply a deafult permission rules on a files and dirs when creating it is by using umask which is applied to the current terminal session and goes away as soon as you terminate it
- the umask can be assigned in different ways first is the symbolic as well which replaces the permissions by assigned symbolic rules in the mask for example
- umask u=rw,g=rwx,o=r this means that any file or dir will be created with the specified rules upon any file creation
- the numerical is subtracting the specified mask form 777 for example umask 555will result in permissions of 222 which would be w,w,w 
- you can add the umask to the bashrc so it will be the main parent to all processes that wil be created which will include the said umask add the line umask 0002 to the bashrc
- keep in mind by default any file creation either by a umask or with the default umask it will never be applied an execute permission (file not dir) its for security reasons which i dont understand why fully ngl

## VI
- a text editor available on all unix machines and is the only editor available in emergency mode which is the state in which the machine kind of breaks and you have sudo permissions to fix the problems youve encountered using vi
### modes
- insert mode
- command mode
- last line mode (:) accessible by typing colon in the command mode and pressing enter
### going into insert mode
- using i goes into insert mode on the cursor
- using a goes into isnert mode on the position right next to the cursos
- using o goes into insert mode on a new line
- using I goes into insert mode into the beginning of the line
- using A goes into insert mode into the start of the line
- using O goes into insert mode into the line above

### command mode
- using w goes with the cursor forward one word
- using b is the opposite which is backward one word
- using 0 moves the cursor to the beginning of the line
- h is moving left l is moving right j is moving down k is moving up
- G is responsible for moving to the last line
- nG is responsible for moving to the nth line 
- u is responsible for undoing the last operation since the last save
- ctrl+R is responsible redoing what you have undoed
- x deletes the current letter on the cursor
- dd deletes a line
- dw deletes a word
- D deletes the rest of the line from the position of the cursor
- yy or Y copies a line
- yw copies a word
- p pastes a line below
- P pastes the line above the current cursor line
- s goes into insert and removes the current cursor position and replacing it with the input
- r replaces the cursor with another without going into the insert mode 
- to search for a word use /word and press enter for searching for the word pressing n goes to the next word below and for the word above you can use N
- to substitute you will write :s/<word to replace>/<word you replace with> replaces the first occurence of that word in the lines to replace all occurences you use /g follwing the command to replace all occurences of the word in the line
- deleted items are put inside the clipboard and you can paste them
- :w saves file 
- :q quits file :q! to discard changes
- ZZ saves and exits the file or :wq or :x
### last line mode
- :l1,l2 co l3  which means copy for line 1 to line 2 and paste them after line 3
### other text editors
- gedit is a normal notepad
- and vim is an improved version of vi which includes a visual mode which is just like the command mode but can select words, multiple lines, etc.

## variables in bash

- assigning a variable is just like the normal variable assignment but space senstiive x=10 is the correct way while x = 10 wont assign anything to it
- to access a variable you can use $<varname> to access the variable value inside the command line
- variables assigned inside the terminal sesison are only temporary for the session only
- exporting a variable saves the variable locally and it will be accessed i presume by all child processes
-  opening a new bash which is i think is considered a child terminal process which has its own session
- global variables as always are conventioned to UPPERCASE SNAKE_CASE as for enviromental varibales
- global variables predefined in linux $HOME, $PWD,$SHELL (shell location),$USER,$USERNAME 
- environment variables could be listed by using the env command
- the $PATH environment is the variable responsible for the paths of all the binaries which could be used inside the terminal reassigning path would make it not possible to run the binaries youre used to running
- I as well presume that insatlling a package or an app that isnt saved in the common bin directory it needs to be added to the PATH variable 

***how it is loaded and how it is persistent is related to the bashrc file which is the source for all child bash processes spun up which is a loosely defined by me needs to be looked into***
- aliases are just a shortcut or a shorthand command  
- environmental variables .profile bashrc 
- to find the enviromental variables of the bash which defines certain standards if the bash shll initiated can be found under shell variables inside the man bash page

# 15-12-2024

## initialization files

#### profile
- the profile file contains the initialization file for the system wide scripts on the login command
- it has the variable PS1 which is responsible for the terminal's cursor look or the prefix of the terminal
- the profile intiializes the bashrc on login and is by default set to the home dir bashrc 
- so whatever you want to be a permenant change needs to be put in the bashrc and not the profile because if profile runs bashrc and applies the setting after bashrc would overwrite just after after resetting the shell 
- # /etc/profile: system-wide .profile file for the Bourne shell (sh(1))
#### bashrc
- is the source file that runs whenever a new non-login shell unlike profile which is ran specifically for login shells
- bashrc contains a ton of configurations
- for example applying a permenant configurationby adding it to the bashrc for example a permenant default umask and default aliases
- the bashrc isnide the /etc/bash.bashrc is applied system-wide onn any new user but .bashrc in the home dir is user specific

***The main difference between either profile or .bashrc and their counterparts of /etc/profile /etc/bash.bashrc is that it is applied system-wide might look into the excution order but i presume is that the global settings are executed first then overridden by the local lets try but i presume /etc/profile -> /etc/bash.bashrc -> ~/.profile -> ~/.bashrc need to test it by appling several print debggin inside the files***

#### process
- the scheduling algorithm of the cpu is ttime share
- PR priorities means increasing the privelage of the task to consume more resources than average processes
- priority number is 20 which is the normal vlaue ranging from 0 to 40 the higher it goes the  least priority it gets 
- NI is the suffix of the priorty number which ranges from -20 to 20 where -20 NI is higher priority than 20 NI 
- you can change the priority but using the command **nice -n processname**
- to apply nice on running processes you need to specify the process id using **renice -n 5 -p [pid]"**

 **why cant we edit the priority right away?**
- killing a process uses the command **kill** to find the all the signals responsible for killing a terminal you can type kill -l
- the main tyeps of termination signals are quit (3) kill (9) terminate(15)
- kill is a force kill process while terminate is the default and it closes processes gracefully unlike kill
- ps is a command to show a snapshot of the current porcesses running on the shell adding the option -e shows the processes on the system
- pkill uses the process name to kill a process and it uses that name to kill all instances of that process
***kernel process has the process id of 0***
***need to look up the boot process of linux and which services does it neeed in bootstrapping***

#### pattern matching
- using pgrep is to search and grep processes and -l is to show the name of the processes apeparing alongside the process id where using -x only returns the eact match
- grep and pgrep are one of the only commands that understand regexp while wildcards are understood system-wide 

https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/x11655.htm
