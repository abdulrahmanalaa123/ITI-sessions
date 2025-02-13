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
- chmod u=#,g=#,o=# `file name` for the u is the owner of the file and g is the owner group of the file which usually if not changed is the primary group of the owner that created the file and others is anyone other than these 2 sets
- now for the rules application it goes in a heirarchy first it sees if youre a a user and applies its permissions if it occcurs it doesnt check for more then if youre a group and lastly the others permissions
- now defining the permissions in octals which is a binary set representation for the permissions which is a 3 bit set r-w-x 4-2-1 and the sum represents the combinations of these permissions r-x = 5 and combining them into 3 sets of permissions ugo 756 =` rwx,r-x,rw- 

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
- to substitute you will write :s/`word to replace`/`word you replace with` replaces the first occurence of that word in the lines to replace all occurences you use /g follwing the command to replace all occurences of the word in the line
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
- to access a variable you can use $`varname` to access the variable value inside the command line
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

***The main difference between either profile or .bashrc and their counterparts of /etc/profile /etc/bash.bashrc is that it is applied system-wide might look into the excution order but i presume is that the global settings are executed first then overridden by the local lets try but i presume /etc/profile -> /etc/bash.bashrc -` ~/.profile -` ~/.bashrc need to test it by appling several print debggin inside the files***

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

#### jobs
- are applications or processes that run inside the terminal and suspends the terminal process or the terminal main thread just as vim, gedit, etc.
- to stop the job you can stop it using ctrl+z to suspend the job 
- to show the current jobs running you can do so by typing jobs into the command line
- running the job as bg suspends the job process
- to run a job in the bg you can either type bg [job-id] or just add a suffix of the "&" sign for example vim [file] &
- to run a job in the fg you can type fg 1 which will start a stopped process in the bakcground
- you can stop and start services an infinite amount of time using bg or fg unless you kill the process

#### standard
- stdin is the terminal stdin in we're typing in usually
- stdout is the terminal default output which is inside the terminal itself
- stderrors are errors predefined inside bash such as permission denied or command not found etc you can check the latest return message using **echo $?** 0 means a successful return
- redirecting output from stdout to a file you can use "`" to write to a file and "``" to append the output to the file
- choosing which method would be the number followed by ` or `` as 1` 2`
- stdin,stderror,stdout are defined in the redirection with 0,1,2 respectively
- sdin,stderr,stdout are located in /dev/stderror, /dev/stdin, /dev/stdout /proc/self/fd/2 /proc/self/fd/0 /proc/self/fd/1
- errors are usually redirected to /dev/null , /dev/0  just as an error suppression method
- mail is used to send mails inside the server users locally 
- typing 0> redirects the stdin needed to anything

***combining redirections ls -R /etc >> file 2>&1 to redirect the error and the output into the same file***

#### wor character and grep
- wc -c gets the character count -l gets the line count
- grep just patern matches 

***can i copy using redirects contents of a file for example echo 0 > passwd >> newpasswdcpy or just echo passwd >> newpasswdcpy***

#### pipelining
- pipeling is just simply taking the output of a command as an input to another command if no input was found if 
- command | comand 
- ls | grep file ----
-  |--------------| (running search of the owrd file on the output of ls)

- ls | grep bash passwd
-  |--------------------X (here ls output wasnt used since grep used the passwd)

**how would pipelining affect a multi argument command where would it be or it ownt work because it will only work having multiple arguments like mv for example so its not pipelinable**

# 16-12-2024

## cut
- cut seperates the file as columns using the delimiter
- count of hte field using -d for the delimiter if the delimiter is ";" cut -d ";"
- to choose the field just  use -f (n1,...nk) for example cut -d: -f1,3,4 chooses the fields 1,3,4 after seperating using the delimiter
## sort
- using sort seperates tehe file into columns using a delimiter which is assigned using -t such as the cut
- and choose the field to sort on using -k(n1...nn) 
- n informs the sorting function that it should sort on numeric values and not on string values
## tr
- translate is a ocmmand used in translating characters in which the value to be replaced is placed first tr "-" " " exchanging - with " "
## inode
- indoe is the indexing method of linux on each file created to increase the retrieval and management speed of files where it contains the meta data about the file like file type, last edited, etc.
- all indoes are stored in an inode table on the kernel level
- each partition is assigned an inode range where mving a file preserves its inode number which is its identiying index assigned to it in the partition
- while copying creates a new inode number even if its the same or a different partition

***I assume that moving a file is faster than copying it because it removes the location of its pointer and moves it to another file but its location inside the storage device isnt changed at least thats what's implied from what he said or what i understood needs to be looked at***

- you can view the meta data about the file using "stat command" of the file or directory

## softlink
- soft links are shortcuts that points to the file applying permissions or operations to the soft link is directly assigned or performed on the original file 
- the symbolic link is just an access method located in a different place than the original file it has no control over the file 
- and removing the original file wouldnt  affect the soft link and would make it simply point to nothing
- you can assingn a soft link by using the command sl `filename`
## hardlink
- is simply a pointer pointing at the data inside the inode table which points to the address of the data in my storage devices each file's metadataa has the amount of links it has once the links goes to 0 the file gets deleted
- so 2 files which are essentially 2 pointers each having different inodes because they are different pointers which are different files so they have different inodes which point to the file which has an inode number in itself.
- so when the links goes down to 0 which is apparent in the file's meta data the file gets discarded
- f1 f2 points to the same fiel which is file1 stat on the f1 shows the links and meta data for f1 and removing f1 would remove the link

## find, locate
- locate uses a database of files which contains files and folders which doesnt require execute access on directories to add them to the db and its faster than find and its updated every 24 hrs
- find recursively search for all the files in the system which isnt as fast as locate but is more fine-grained you can use several critieias to find a file which will return the exact file you're looking for

## archiving and compression
- archiving is just bundling the files and folders for archiving or backup purposes and its just saved as a bundle and is used to backup the file
- tar -tf file.tar "f flag is put at the end because its the flag that takes the input of the file name"b
- -x debundles the file where -t can list the contents of the tar file and -c is responsible for creating a tar file
- compressing is reducing the size fo the file and bundling them as well where i presume it doesnt allow it to be read right away for example using cat it will be encrypted keywords yet zcat decompresses and views the compressed file
- you can use compress keep in mimnd ocmpress,gzip,bzip2 replaces the file specified  and doesnt create a new one while tar creates a new file and the file is appended with the extension .Z using compress and .gz with gzip and bzip2 with the extension of .bz
- compress is currently deprecated because of low compression ratios
- to view every compressed file in the each using their respective cat commands 
- keep in mind compress,gzip,bzip2 cna only compress files
- but zip creates an archivwe and compresses files as well as it can compress directories as well and its the most commonly used compressing 
- unzip -l views the contents of the zip file without actually extracting it

# 18-12-2024

## bash intro
- we're first taking a linux recap but most of what he said was said either in the linux 1 lectures or ive seen in the redhat course im taking
- split command splits the file into lines, bytes, etc.
### sed
- sed is the streamlined editor which manipulates text on files and doesnt edit the original file
- sed copies the file in the  buffer where each element is a line i presume he said he saves it into a buffer
#### Actions
- print p
- delete d
- replace s/old/new/g
- sed's default action for any line is print the line to suppress the default behaviour you can type -n
#### addressing
- you can address a line 1,2,$
- you can address a range of lines with n1,n2 from n1 to n2 from line n1 to last 2,$
- addressing using a pattern you can use /pattern/

- to type a sed command you need to type sed '{Addressing}{Action}' `filepath` 
- for example sed -n '1p' `file` which means print the first line of the file and suppress the default action
- you can mix and match addressing for example mmix ranges starting from a line to a pattern you can type '1,/pat/d' 
- you can delete a line or a range of lines or even a pattern with and keeping the default behaviour will print all the lines except the lines matching the addressing method 
- -e is extending the numbers of addressing and actions on the asme file
### awk
-  
# 19-12-2024

## Shell scripts
- bash script is an interpreted language and not a compiled language the interpreter exists inside the shell
- most user interactive scripts that needs choices are not recommended to be used in bash
- shell variables are dynamically alocated and can n=hold any type
- to print a varibale you can access its value using $`varName`
- export exports the variable to be visible to all the child shells but isnt persistent yet to be persistent you simply may add it to bashrc or the environmental variables however you want
- side note you can use ps -f to view the parent process id and the processes running and you can use which `command name` to find the location of the command
- to prompt the user for an input and use the stdin and store it in a variable you can use read `varName`
- when scripts are ran they run in a  bash child process and not the main bash shell you're using
- sourcing means to run the shell sciprt in the running shell process to do it you can type source "script absolute path or relative path"  or . "script absolute paht or relative path"
- to concatenate values to a variable you can reassign the varibale by typing "`varname`=`varname`"string to concat"" 
- you can typeset variables to define the static types and standardize expressions performed on it like an integer where a plus would sum and in a string it would concat so to do so you can type "typeset -i `varname`" to ensure its an integer specified by the option -i for a float you can type set with -f  
- let followed by let i=5+1 will also mean an arithmetic operation as well as you can type "5+1" between quotations to ensure its an arithmetic operation which is wierd you can also type ((`varname` = `varname` + 1))
- to access the arguments of a file you can use the # to get their number or use $ to get the actual list and $1,$2 etc. to access the arguments and the file name is the $0 argument list
- to print the return value of the previously ran scrip is with echo $? 
- to get the user's input and getting space seperated variables all at once for example prompting the full name "read first second third" will save the space seperated name into each one repsectively
- the read value of the user's input it will be saved in a varibale called $REPLY
- and to print the prompt as well as getting the input right away you can type read `varname`?"prompt needed"
- single quotes are a string which has no escapae unlinke duoble quotes where you can mention the variable inside it "hello $x" parses the $x and gets the variable value
- back ticks extract the command's output inside it as a formatted string but it can only work in a double quotations and no ta signle quotation string
- preceeding the variable inside double quotes discards the variable and prints it simply as a string 
- so if is followed by a command where if it ran then its true although it returns 0 which is weird i think
- writing in the if is followed by a command like test or running a command with exit status of 0 means it ran successfully 
- the square brackets in itself is a command and the expression is the arguments passed to that command which returns true or false evaluating the expression inside  
***now the question is how does square brackets command evaluate the 0 value into true which is insane to me***
- string evaluations are done by using string1 = string2  -nstring1 means the string isnt empty and -zstring means check if its an empty string
- using test to compare values which is in itself a command you can type test followed by a binary operation followed by options like -eq -gt -lt -gte -lte -o for or -a for and -n i think is for not
***these expressions of comparison arent a reference is just a reminder probably got it wrong and gotta look it up whenever i use it***
# 20-12-2024
- Apache is a software foundation that supports several projects and isnt just a company that provides http server only
## APACHE http server
- http servers are based on the client server model
- while mqtt is a protocol based on the pub-sub model 
- to perform the pub sub usage using http you can it using polling i think in which you keep requesting new info from the server if found
- status codes and optional return body are returned in the response of the server 
- post requests isnt best practice sending data using query params for the data you're trying to send and put in the request payload
- 
### URLS
- the url consists of a protcol://hostname/path?query

# 21-12-2024

## bash
### case
- case is the switch case inside bash shell where you can break the case command using ";;" breaking going into the next cases
- case var in val1) ;; val2) ;; or using star for the default condition
- to close the case you write it in reverse esac
- you must use ;; to specifically specify the end of a  given case using break only wouldnt compile because its not given a sign of finishing the given case
#### meta characters
- star is used for matching 0 or more characters
- ? is to match one char
- square brackets are used to match only one char in a given range of characters or a specific set of characters
- square brackets characters are implicitly or'd unlike regex where it is required to specify an or operation if needed
- adding brackets () means applying the the prefix to the given pattern unlike just adding it before will look for specific things before the pattern
- @(pat) means looking for only one occurence of the given pattern
- +(pat) means looking for the pattern's occurence one or more times similar to the star but the difference is the star applyies zero or more times
- !(pat) matches any string than that that contains the pattern
- "shopt -s extglob" to add the pattern matching using brackets, etc. to your bash shell if its not currently supported by your version

### while loops
- while command just like an if command takes in a command and checks the return value of the command
- while `command` do done

### until loops
- looping until is quite the opposite of while while is basically while true
- and until for an infinite loop you can type until false
- until just like if and just like while takes in a command for the conditions and not a boolean statement

### for 
- for in is to loop on space seperated values will be counted as an array i presume
- to substitute a command with a value as a list for you can type the command inside back ticks you can substitute it as well with $() with the command inside 
- keep in mind that this is for in and not just a for loop
- to loop over certain numbers you can use seq ***for i in $(seq 1 $END)***
or you can use
```
	END=5
	for ((i=1;i<=END;i++)); do
	    echo $i
	done
```
### select
- to type the select statement is loopoing for selecting in an array of space seperated vlaues and wont sdave the value in x unless it is contained inside the array 
- the syntax for select is **select x in `space seperate values`do done** 
- seelct is oftenly used alongside case functionality and the break case is inside after performing my operation on my different valued array 
- breaking any loop can be done by using break; but to break cases specifically you must use ;; using break inside a case alongisde a loop will close hte loop

### shifting
- shifting shifts the arguments list from the left by 1 which gives you several interesting methods to loop over the arguments list using just **for ;** you can loop over the arguments lilst and by shifting them it will stop running when they're all done
- you can access the last element by using while and the length is $# === 1 after shifting all and breaking on the last element

### break
- break takes an argument which is the number of nesting given where for example if you have 3 nested loops you can leave all 3 by breaking using break 3;

### arrays
- arrays can hold a max of 1024 elements ranging from 1 mgb to 4 mgbs of data either chars or integers so arrays are defined by default with a size of 4mgb you dont define the size of an array or the length its always 4mgbs of data setting the defined size of an array is useless its size is determined by the amount of elements inside the array
- to define an array element you create an array and ***arr $arr[0]=val $arr[1]=val2***
- to access the array elements you can access it using ${} only i tested using different methods and didnt work
- looping over the array can be done using ***for i in ${!array[@]}*** 

### functions
- functions are declared by declaring function and function name 
- functions can accept any number of arguments and it isnt defined in the function declaration but cant be validated checking the arguments size
- to call a function with towo arguments you can do that using ```functionName var1 var2``` 
- you can call a script and it be defined as a function inside your current running script and the command will be defined i presume either set it inside a vraible or just call it inside the current running script dont know yet
### debugging
- to run the script in the debugging mode you can include -x after the shebang inside your current running script 
- after including the debugging you can suppress the debugging statements using set -x where it will supress the debugging messages for all of the commands located avobe the set -x line

# 27-12-2024

## version control
- all of what have been said is the benefits of version control systems like branches , versions, concurrency in working , merging, etc.

## ssh
- authorizing your machnine as an ssh available machine is by adding your pulbic key in the host machine youre trying to connect to by creating an ssh keygen pair


## basic commands and good to know 
- to reset staging items put into the staging area can be done by git restore --staged `fileName`
- to ammend a commit to another instead of creating a new commit you can type git commit ammend which will overwrite the last commit and change its commit id and use it as the last commit
- git reset --soft HEAD^ delete the commit and takes it back to the staging area
- git reset --soft HEAD^^ delete the last 2 commits and takes it back to the staging area of the commit before last and deletes the last commit completely 
- git reset --mixed (dont understand it)
- git reset --hard HEAD^ revert to the last commit and deltes its staging as well sth like that 

# 28-12-2024

## Version control the real thing
- branching out is copying the original branch which is the master or main depending on the original branch of the repo
- mainly branching is used for features adding new features, etc.
- to create a new branch you can type git checkout bracnch name
- `git branch `name`` new branch `git checkout `name`` move to branch `git checkout -b `name`` create and switch `git branch` list brnaches
- creating a branch copies the current branch youre standing in not always the main or master
- `git branch -r` lists remote branches and using -a lists all of them together
- you'll realize the remotes/origin/HEAD -> origin/main mean that the head of the repo is pointed at the origin which means that the repo by default is stuck on the latest main commit and isn't concerned by other branches
- to switch heads on local just simple by checking out using git log after switching the branch will show you all the head sharing branches which are standing on the latest commit of the branch you're standing on
- to delete a remote branch `git push origin :`name`` will delete the branch or using a more verbose --delete
- git branch -d `branch name`
- origin is an alias or a tldr for the link for the hub or repo you're using 
- for example you can use two repos one named origin and one named any other thing you can add onto your repo
- merging is the idea of merging all the changes in a feature branch for example into another branch all in one commit which is usually a hefty commit and needs a ton of mesages to understsand the changes merging 
- rebasing is replacing the original head to be the origin of my current branch constantly rebasing is to keep up with the master branch or the main branch for example master is ahead of me by 3 commits rebasing to the master will change my base to be the base of the latest master branch commits
- in real life situations merging simply adds all the commits you did on your branch merging them into the branhc youre merging into so imagine you have 50 commits and merging them into the master branch you will lose track of what to do soyou just simply squash your commits to one then merging will merge it infront of the master branch and adding all your changes into one commit which is much neater and simpler to handle
- git fetch gets the latest updates from the remote repository and you need to merge the hcanges to your local repository git pull typically shorthands these updates and does the fetching and merging in one step

***versioning needs to be revised because i slept through it a bit***

# 29-12-2024 / 30-12-2024

## MYSQL basics

# 31-12-2024

## Python 

***fetch decode execute interpreters takes longer because it does these three processes on each line***
***static code analysis tools are the blacokage of interpreting the language or running although she said that its built into the interpreter she said its called the parser***
***strings by default has the base size which can be found using sys.getsizeof() of 41 bytes which is why she said it was wrapping which might mean the header of the data type defining its a string but thats a fuck ton for no reason might need to check it out***
***she specified that python has no implicit type casting and using boolean operators i said it would implicitly type cast the values to booleans and she said i cannot explicityly say that***
- primtive data types ARE NONE, BOOL,STR,INT,FLOAT and non primitive has list,tuples,sets,dicts
- everything isn python is considered an object
- comparison in python comapres data types and values (python has no implicit casting unless typing if val)

### truthy and falsey values in python
- falsey values are empty collections and empty string and 0 and None (I presume that an empty list is truthy in javascript as i recall)
- truthy are any values other than falsey 

### sizes and primitive data types
- the size of an integer in python is 28 bytes while an empty list gave me a size of 56 bytes and adidng the first integer gave a size of 88 bytes which is 32 bytes
***how does python handle different types inside its list?***

#### strings
- strings are an immutable data type where to do most of hte operations on the string you have to treat it as a list and any changes that could happen should be done by creating a new string
- you can comprehend the string such as strname[::] to get each chracter of the string or str[::-1] to reverse, etc. 
- to loop over elements you cna loop by for x in strname:
- creating a formatted string (template string) is by typing the string normally and adding the placeholder inside curly braces and to format the string you can type string.format(keyword=val,keyword2=val...)
- rpelacing a character inside a string you can do it using replace
- string concatenation can only be doen on strings only and you must ensure casting each element into a string before concatenation

### lists
***lists mutability in python***
- lists are mutable (kind of questionable) if its mutable which means you can change the pointing easily well definition of mutable and immutable defined as just editing the value is kind of bad definition
- list slicing is done using [in1:in2] if in2 is not specified you will slice to the end of the list and the same as for the strings you can reverse the array by adding -1
- to insert an element at a specific index you can do so unsing .insert to add to the end you can list.append and list.remove from the end you can do pop()
- to sort the list you can say list.sort
- range retunrs an iterable of numbers and not a list you need to cast it into a list
***return type of range if its a generator or not do not remember it that well***

# 2-1-2025

## Python tuples
- tuples are an immutable data type and has basically the same list operations the only thing is that any element pointer reassigning couldnt be done
- casting an iterable which takes a sequence returning the iterable type for example a list taking a list to cast it as a list will take the elements and turn it simply into a list casting list and tuples both takes an iterable so they basically perform the same
```
list(["hello"]) => ["hello"]
tuple("hello") => ["h","e","l","l","o"]
```

***immutable dataTypes are hashed inside python which doesnt make sense kind of? or she says why are immutable immutable***
***you can use pythontutor to visualize python in memory to learn***

## Sets
- sets are a mutable datatype which doesnt care about ordering with no indexing done on the data
- sets arent used for iterations they're mainly used for set differencing and joining,et. and utilizing that the elements is non-repeating 

## dicts
- Dictionaries are a mutable unordered data type which has o(1) accessign time and ***it wasnt ordered before after py3.6 its an ordered datatype***

## for else
- the for else syntactic sugar means that if you reach the end of the loop then you should execute the block inside the else statement

## function defintion
- to define the function as a named variable parameter you can do so by specifying the input as a **inputargs 
```
def func(**args):
	print(args)
=> {each value is considered a key pair when inputted with a name}

# sepcifying arguments as a ** it defines it as a named parametered function then each input should be named while inputted
func(name="lsq",bla="wdq")
```
- and to define as a variable list input you can define it using *inputargs 
```
def func(*args):
	print(args)
func("bla",213,12312)

# its interpreted as a tuple because you cant edit the argument list after insertion
# although you can do so by casting it into a list and use it as one
=> ("bla",213,12312) 
```

# 15-1-2025
- The constructor in python isnt required for creation of an object its only required for initializing the object instance
## Testing
- Unit testing is usually less expensive and easier than end to end testing
### creating a virtual env
- to create a python environment you can create it using `python3 -m venv envname)`
- it would create your own interperter alongside your own pip verseion to run python independtly from your global python versions or environment
- to activate your venv you can source it in your current bash shell and run `source ./envname/bin/activate`
- to export your current package you can use pip freeze to your requirements.txt file
- and to install using your requirement.txt file you can use pip install -r requirements.txt
- note that you should add your venv directory to your .gitignore by typing the dir name followed by slash `envname/` adding thsi toy our gitignore you deny uploading the env dir and use only your requirements.tx file for managing your library dependencies
- python has no implicit casting which means strongly typed while loosely typed languages has implicit casting

## doctest
- using the doctest library you can run test cases using docstrings 
- to write a test case use >>> followed by the function followed in a new line wiht the expected output

```
"""
>>> sq(10)
100
>>> sq(2)
4
>>> sq(3)
9
"""
```

- decorator function (HOC) and @decorator annotation need to understand it

## unittest 
- to simulate function calls or asynchronous requests you can use with patch('file.func') simulating db requests or asynchronous requests where it detaches it from the external dependencies
- the point of unit testing is to not depending 
[read the docs](https://docs.python.org/3/library/unittest.html)
## coverage
- tests the coverage of your test cases for the code blocks located inside your function that you want to test
- it returns a report running all your test suite

# 18-11-2025

## Docker Introduction

- Explainin the vm tax where youre utilizing the hardware you have but deploying a whole vm with its licenses setting up and patching for a signle application to ensure isolation and increases the overhead
- This is the VM Tax where you need to pay money ensuring the utilization process which was solved by containerization
***you cant test on servers which is weird***
***why cant you use ansible for managing and intiializing virtual machines he implied that you can only do them one at a time***

### Containerization
- containerization is a virtualization technique whicch virtualizes the current operating system running on your host.
- it virtualizes the main operating system process currently running on your machine

***can you specify resources for any running container?***
***isolation of virtual machines vs isolation of containers?***
[Playground website](https://killercoda.com/)

### docker high-level architecture

- docker isnt the containerization application it only manages containers and running saving them into images
- it uses the client to which is the cli tool which is responsible for providing an interface for the user to interact with the docker CLI

#### container runtime

- It consists of containerD and runC these are what are used to set up the environment with its own vfs and network interface, etc and running the actual container isolated from the host operating system
- ContianerD is used for setting up the environment and runC is for actually running the container
- Docker Daemon is only responsible for managing and saving images and parsing the user input if the image isnt found loally the images is searched for on the docker registery which is dockerhub i presume

### docker command structure
- docker commands start with docker `object= container or image` `action= run stop restart etc.` `options` `argument[0]=most probably image` `argument[1]=the main command to execute the container on where if closed the container has no purpose to keep runnign thats what i remember`

- the exec acction enables the container to run the command as a different process which isnt related to the main process inside the docker container the container's life cycle is mainly dependant on that main process once it stops or fails the container dies or stops

- docker containers are by default ran as a background process to enable it and use its current shell process oyu add the otpion -it which runs the interactive terminal to reattach the container to your current stdin and stdout and stderroryou can run the container followed by the action attach 

- the commands are either overridden or added to be ran as a different process to when overridden it will be with the process id 1 and when the process exits the container seems it has no reason to keep running so it stops right away

- `inspect` is the command to view extra configurations and infor about the queried container

- `exec` exec should be ran on a running container 
- you can only remove a container only after stopping it and stopping a container mangaging it with the dependencies idk 


# 19-1-2025

## images

- images are a snapshot from the latest state containers
- containers are built upon images for example an nginx container needs an ubuntu image adding nginx and commiting that container will create an nginx image that has ubuntu image so commiting and using this image in creating your own web app would be read only and anything you can build open would be rw

- so basically an image is a base you can use as read only and bulding upon it would create another one to be reused by you or even different people by sharing it on the docker registry

- images cant be removed unless all containers running it or using it are removed completely
- images can be referenced by id and deleting them using it will delete every alias or the command and deleting by name:tag may delete an alias and leaves the actual image

### image commands
- `image pull` to pull the image from the registry
- `image push` to push the image to the registry
- `image rm` to remove
- `image inspect` to inspect the image
- `image tag` is changing name or version namae changing a tag for an image creates an alias for the same image with the same image id and doesnt change it or create a new version
- `container commit` to commit changes done by you on your working container exporting it into an image


### dockerFile

build vs runtime in docker
#### workdir
- specifying the workdir used inside the image by default its the root directory unless another is specified
#### add,copy
- add adds a file to the container from remote repos using http or git
- copy adds a file to the image or the ran container from local files 
#### env vs arg
- arg are arguments used or variables used inside the docker file can be used inside the build only and not used inside the runtime
- env are defined to be used in both the build time and run time and must be defined with a value and if it has the same name as the arg env has the higher priority and defined inside the env variables inside the running container
#### entrypoint, cmd
- cmd is the arguments provided to the entry point if no entry point is provided cmd is ran as its own 
- entrypoint is the default command ran on the start or as the main pid and can be overriden inside the run command using --entry-point sth like that
***look all of this shit is fuzzy needs to be revised***

#### exec versus shell
- exec and shell forms are forms are the forms of typing either the entry point or the cmd 
- each have its caveats and their ways of typing
#### multistage building
- its is used to optimize final image size required for running the final application
- in case of go you need an image a building for building the go application into a binary file and then no need for a go runtime to run it so you should only build a minimal ubuntu image and contains the binary file only

- using several froms enables multi stage building using the first from to get the image required for building
- the second from is used from scratch to run the binary which is super minimal just enough to run the binary file and to copy the built file from the first build you can use copy --from=image1 /bin/hello /bin/hello image1 is the alias given in the from keyword

```
FROM golang:1.23 as image1
WORKDIR /src
# copying the main.go in our current dir into /src
copy main.go ./main.go
RUN go build -o /bin/hello ./main.go

from scratch
copy --from=image1 /bin/hello /bin/hello
CMD ["/bin/hello"]
```

***port binding happens in runtime and just exposing just adds the port to the exposed ports which are able to be bound***

#### docker push
- to push an image to your remote registry you need to first specify it first by your account username/image name 
- to be logged through the cmd using credentials you can log in using login -u username
- after that you can successfully push your image on to your docker hub account

#### docker container inspect
- you can get the private ip of a docker container using docker container inspect to check its ip in runtime
- without port forwarding or exposing ports in any kind

# 20-1-2025

## docker storage
- docker has 3 options of storage 2 persistent options like volumes or bind mounds
- and one in memory option called tmpfs which stores the container's data inside the host's memory
### bind mounts
- linking locations on the container's file system to actual dirs on my host file system which writes to the file with any new file created
### volumes
- volumes is a persistent storage solution managed by docker where it simply saves the data to a docker managed location on my host called volume to be able to persist its state

#### volume management commands
- `docker volume create vol_1`
- `docker volume ls`
- `docker volume inspect vol_1`
- `docker volume rm vol_1`
- to mount the volume to the container on runtime using `--mount type=volume, src=vol_1, target=/usr/share/nginx/html` the target can be any location on the docker container
- to mount using any different types just specify the type `--mount type=bind, src` `--mount type=tmpfs`
- you need to specify the src in both volume and bind types

## docker networks
- docker networks types Bridge,host,null
- `Bridge` all containers included are by default able to connect to each other and containers from outside arent able to connect to containers inside the bridge
- the type is specified by the driver option `--driver=bridge` you can as well specify the subnet when creating the network
- `network` type null makes the container inaccessible by either the host or other contianers in the same network
- `host` removes isolation between the docker container network and the host network so it act as the host machine in the sense of the network and can access different containers using their ip addresses if they're using bridge and if they're using host using localhost
- `network create/inspect/ls/rm/connect/add` just like volumes they have network lifecycle commands and treated as a docker managed objet

# 26-1-2025

## Boot sequence
1. BIOS/UEFI are stored in the ROM and loaded into the RAM on boot
2. POST checking the hardware if its running properly is done after loading the bios/UEFI to the RAM  
3. detect and hand off control to the MBR( master boot record)
### MBR
- booting from mbr boots up on two stages using BIOS and not the UEFI while using UEFI boots up directly 
- The boot loader GRUB2 checks for the current available operating systems and grub `/etc/grub2.cfg` loads the system kernel into memory 

4. systemd is then laoded or running the inti process from `/sbin/init` `/etc/init` `/bin/init`  which is included in `/etc/systemd`
5. if systemd fails executing a certain service it will go into emergency mode or change the default.target which is the cli or the gui.target and then it goes through the multi-user.target then through each of the targets
6. it passes the default.target after successfully loading necessary service then multi-user.target
***note that enabling a serviceaadds the service file to the multi-user.target.wants to the -> /service to run the scrip on load*** 
## targets
- mounts are called upon any file system or dev that interacts with the fs 
- sockets are any file that interacts with the netowrk device ( which donesnt make sens to be called like that)
- and services are what interacts with applications (also a vague definition doesnt make sense)
- all of these combined are called targets whcih means they are whats required to be ran inside the target
## systemd
- service mask enforces that the service couldnt be manually started whcih creates a symlink between the service file and /dev/null
- static services are services which are dependent on another which can be enabled to be auto started and can only be started by the service itself or probably forked or sth
- maybe it is used in the display managers just like he said for example you need audio to build up video
- sudo journalctl gets the logs of a service in systemd
### things i dont understand
- look for systemd isolate and isolation logs out of gnome from graphical.target and goes to multi-user.target
- recovery.target happens when one fails for example multi-user.target
- service reload and service restart
- daemon reload when editing a service using `systemctl daemon-reload`
### creating your own service
- `/etc/systemd/system` creating a system file with the extension `.service`
- creating service files manually is by creating the service files inside the `/etc/systemd/system`
- structure of a service file
- to view the configuration service file of the service by doin `systemctl cat service_name`
- to view the syntax of the configuration file of the service you can do so by `man systemd.service`
- the user must be specified because the wanted target is multi-user.target specifying its service user

***thats why service users are created without logins because file creations and access needs to be done by said user thats why service users are used which is nice***

```
# Unit describes the service and dependencies but nothing related ot the actual service runtime
[Unit]
#these describe the service runtime specifications
[Service]
key=val
Type=
User=
Group=
EnvironmentFile
#specifies when is the service needed
[Install]
WantedBy=multi-user.target
```
## grub menu and config
- the default config file could be found in `/etc/sysconfig/grub` or `/etc/default/grub`
- sudo grub2-mkconfig -o /boot/grub2/grub.cfg

# 27-1-2025

## scheduling 
- `at` using it to schedule a service its a servivce that uses minutes at least to schedule a job and no secs
- viewing your current jobs can be done by `atq` 
- to send mail to your user after running the task by using `at -m`
- you can escape spaces using backslash `touch file1\ super` will create a file called `"file1 super"`
- you can allow or deny users to use at by adding the user in `/etc/at.deny` you can use blacklisting in deny and white listing in `/etc/at.allow`
## crontab
- crontab syntax hyphens (range) , commas (set), slashes (incrementing)
- minute hour day Month week  day (1-31) week (0-6) (Sun to Sat)
- * * * * * means run it by feault every 1 min
- 1/5 means run from 1 every 5 and for \*/5 means run it every 5 in each unit from now 
- star specifies now 
- 1,5 means run on number 1 and number 5
- and for 1-5 means run from 1 to 5 
- specifying week day implies that the days and months should meet the day specified to run
- `L` used in day of the week and day of the month used to specify n to last day to the week
- `#` used in day of the week for the nth day in teh month

# 29-1-2025

## rsyslog
- the syslog config file you determine the log output and prioristy of services using selectors
- the selectors has a syntax of 
-syslog is a protocol for loggin the messages on unix based systems and rsyslogd uses said protocol to save logs on the machine
## journald 
- its the upgrade of the rsyslogd service which is essentially a protocl so its built  upon the syslog protocol enable log rotating and saving log files in binary json formats which is stored in memory and its probably commited using the syslog service
- memory processes are saved insiide the run file and saved with a temp id and can be found using `sudo journalctl -u <service>` `run/log/journal/journalctl`
## SELINUX (MAC)
- service context you can view it using -Z in `ls -z dir/file` 
- you can assign the selinux to a running script ensuring it runs in the specific process you can use `semanage` and attach the context to the script or file and assign the rules on the directory using `setenforce or semanage` as well dont remember specifically
- to set the permissive rules of selinux you can change the selinux config file and and changing the enforcing mode of selinux of enforcing and primitive and disabled  if you want to set the current enforcing mod eis done by `setenforcei 0|1|2`
- the config file could be found in `/etc/selinux/config`and you can find the current ecforce using `getenforce`
- you can view all your rules with `sebool` although im not convinced
[LINK SHOWING moving and copying files with selinux contexts attached](https://superuser.com/questions/1347564/mv-vs-cp-what-is-different-about-the-resulting-file)
[SHOWING THE FACILITIES PRIORITY](https://extreme-networks.my.site.com/ExtrArticleDetail?an=000090331)

# 30-1-2025

- curly braces in wildcard creates an array of multiple options for examlpe wanting {1,2,3}.bla will look for 1.bla 2.bla 3.bla
- users by default should have a primary group which defines the file creation ownership  
- saving in vim without read permissions wouldnt be able to load the file into the buffer unless it has read access and if you only have write access saving would overwrite the file you viewed

## special permissions
- set user id if put on the file and that file is runnable and you have execute privelage in your group or other when ran your user privilages when running the script would be the same as the owner specifying a script with root as its owner then if the script is ran then the user id would be root. 
- permissions of setuid and setgid are specified are S capital and s depedning if the owner or group permission had execute permissions in the beginning 
- if set gid is assigned then the file group permission while running it is the same as the group permissions assigned to it and for directories any file or directory created inside the directory take sthe owner group would be the owner group of said files no matter who created them
- sticky bits are only put on directories and are ignored on files they are used to prevent different users with teh same write permissions in the same directory from deleting files of a different user
- using special permissions you can assign by adding a bit to the numeric permissions 7777 if its a file the max numeric value is 6 and if its a directory the max numeric value is 3 

## sudoers
- the wheel group is the default group assigned by the os and adds to it the base user that has sudo privelages and does all assigning all the commands for it


# 2-2-2025

## Ansible 
- ansible prvides automation for the process of configuring servers and setting them up
- you can for eample use ansible to create 3 docker read environments and installing each of your servers replicated across multiple devices
- idempotency Ansible is specialized with idempotency each configuration operation will no tbe repeated although how it is done is not known yet
***The question is if it runs the command and linux provides the idempotency layer or ansible saves state knowing which configurations are added or changed,etc.***
- Agentless tools like puppet and chef needs to install a client agent on the target servers you need to configure
- while ansible needs only to be ssh enabled and no agent or other services required (while oyu still need to configure the public key of the ansible host to be a part of the known hosts and python installed on the target machine) with no dependencies needed
- daemons are basically said to be the process accepting requests on the server or the recieving side while the client is the tool or interface used to interact or call the request for the ssh daemon.
***when connecting to an ssh client it is said that you the client wont use the daemon and only use client part and the recieving side will use the daemon (which needs to be understood what is the difference between both)***

***SSH was said to be from user to user and not a machine to machine connection the term is well defined but needs to be further researched yet it explains that fingerprints and know public key hosts for ssh is sunique and installed on each user on its own***

- ansible host is called control node , servers needed to be configured are called targets, or nodes, etc.
- its not necessary for ansible to connect using fingerprint it can connect using the user name and password
- chpasswd is used to batch update the users passwords you casn create a onleline password change writing `echo "user:pass" | chpasswd`
***difference between known_hosts (people who can connect) and authroized_keys***
- you can securely copy files which most probably the public key you need form the machine to the target machine using `ssh-copy-id -i /.ssh/key.pub target_ip` so which adds it to the authroized keys file using ssh 

## ansible commands

- adhoc commands running a command once and discard it on several machines all at once using ansible

- `ansible` `[pattern]` `-i` `[inventory]`(available list of ips or file of inventory machines (their hostnames)) `--private-key path` `-u username` `-m module`
 
- inventory file you create your inventory file writing by the group name writing the ip each in one new line

```
[group_name]
 ip_addr  default_user=ubuntu
 ip_addr args=vals
 hostname
```  
- the group name can be used in place of the pattern or writing a patternf ro the groups you want to be selected and applying -u wont override the default_user variable and you can assign variables to each group or individual host

- you can type a group with children group names to specify that running the parten group will select all the children in the pattern part `[parent_name:children]` followed by the group names

- youcan view the ungrouped ips using the pattern ungroup instead of a group name

## configuration file

- search order of ansible_coinfig search starts by the `ANSIBLE_CONFIG` environmnental variable followed by the `ansible.cfg` file available in the current working dir then the `~/.ansible.cfg` then `/etc/ansible/ansible.cfg`

```
[defaults]
# to set the default variables for your default command
inventory=path
user=username
[privilege_escalation]
# set the privilege esceelation method
# you can attach the --become flag after your command to escalate the privilege
become = true
#ask the users for passwords if trying to access the privilege escalation
become_ask_pass = true
#define the privilege escalation ocmmand used when adding privilege escalation
become_method = [sudo|wheel....]

```

## playbook
- is a play or list of plays (tasks or commands) to setup your environmentst
- but its redundant to use one command for a whole playbook
```
# written in YML
# syntax
## to start a play in the playbook you should prefix with "-"
-name:your paly name
	
	hosts:all #define group or the pattern you need to select to whom you apply
	gather_facts: false #disable the fact gathering in your current play
	#now write the tasks you need to apply to your hosts
	tasks:
		-name:task name #task
			# oyu can type any module name
			module_name:

```
***lookup strategy in ansible***
- running a playbook uses `ansible-playbook playbook_name` it runs first `gathertargets play` to find out several info about the servers youre trying to connectwhich is used to define info to base conditions on while creating your own playbook
- configuration files are used on both the playbooks and the commands if not then you must specify when running the playbook each of the configurations you need

# 3-2-2025

**templating**
## variables
- to write variables in the playbook syntax you can type `{{varName}}`
- to write variables adding them to your play you can type
```
vars:
  myvar: bla
  var2: blabla
  bar3: [1,2,3]
```
## Tags in ansible
- you can assign a tag to a task and either run the playbook with a tag  
- to specify a tag of tasks to be ran while running a playbook you can add the option `--tag` i think alongside the tag name to only excute said tags

## loops
- you can type a loop either using a list or a dictionary `- elem1 - elem2...]`, `- {prop1:"val",prop2:"val2"} - {bla}` and they are accesssed in the given task by using `{{item}}` or `{{item.prop}}` for dictionaries 

```
loop:
- elem1
- elem2
- elem3
```
## when
- when is used with getfacts to get info about the server to connect to
- when is an if statemnt given to run a task when a condition happens and skip the task when the condition fails and adds it to the skipped values

## register
- you can add a register property to save the output of the latest command `register: varname`
- you can either use it as a dictionary to access values or either just viewing it first by using the debug module and passing the register variable name all i guess must be in the same play


# 9-2-2025

## Kubern8s intro
- Nodes are deifned as a signel machine,server virutal machine 
- you have one control plane and several worker nodes as many as you like control plane might be replicated to achieve high availability for precaution of failure
- master and workers are controlled y the service or daemon installed to be used as a master node or a worker node

### kubern8es architecture
- etcd is a highly available keyvalue storage database that stores the cluster's state
- kube apiserver is the endpoint you use for using kubrn8es pods nodes, containers and initilaizing given specific endpoints 
- kubectl is the client used to interact wiht the kube apiserver to control the cluster or maybe using the control plane directly but its not feasible to do so 
- the schedules is the unit responsile for specifying which pod is deployed to which node specified by a set of rules given or by the default set of rules givenby the scheduler 
- controller manager checks for the node state matching the current node state if any mismatch like assigning a 4 cpu for a pod of a 6 cpu node and checks the vitality of the node and 0 cpus are taken the pods are reinitiated
- controllers have many types (node controllers, )
- worker nodes have the kubelet client side agent application used to talk to the kube apiserver to allow it for health checks and status requests as well as management to initiate containers from the requests of the controllers,etc. 
- mainly the kubelet is the main interaction method between the master and worker
- it also sends heartbeats alive check for the control plane to the kube api server
- the kube proxy initializes a network between the pods and each other it can also be installed on the control plane but they are all virtualized to be on the same network so its a virtual network assigned to expose the pods with each other

- does changing of state send a notification request to the kubeapiserver and changes all without writing to the etcd first or just always checking the latest state how doe sit exactly work?

- kubeDNS provides clusters wide dns services

### creating your k8s
- minikube
- kubeadm (project)
### kubernetes order of execution (needs to be further researched)
- first request is to authenticate the user taken while talking to the api server
- validate request that its correctly set up 
#### commands
- kubectl is the main command line tool to interact with your api server
- `kubectl get pods` to view your current running pods info about them
- YAML file for creating the file declaratively (was specified to be idempotent but its not usually necessary but its mostly idempotent)
- running with the commands for creating adhoc creation or fixes

## YAML structure
```
apiVersion: --> apiversion of the object created ?????
kind: ---> Type of the object Pod,ReplicaSet (workloads)
metadata: --> metadata of the kind of point created
 name:  --> name of the object created
spec: ---> the resource required configuration depends on the type of object
 containers:
 -name: ---> name of the container
  image: --> name of the image 
```
### workloads
- Pod is the smallest unit used inside kubernetes it contains containers but the containers used in the sense of running a container contains several processes sharing the same namespace cgroup, etc. whiere the processes arent provided isolation for the need of each other but the pod can now  manage the process and replicate, etc. which igves higher control yet provides less isolation between processes and each other which isnt exactly needed in that sense

#### Replicaset
- Is a controller object that creates a desired number of pods managaing lifetime in case of failure syntax
```
apiVersion:
kind: Replicaset
metadata: --> metadata of the replica set
spec:
replicas: --> number of replicas
selector: --> selecting pods on a specific labels
	matchLabels --> match the pods according to their label
		tier: --> tier specifying the label
template: --> every replica set must have a template to create a replicaset on (you can create a replica set on running pods matching the same template spec)
 metadata: --> metadata for the each pod created inside the replica set
  label:
  tier:
 spec: --> the spec for the template of the pod needed to be replicated
```

#### Deployement
```
kind: Deployment
metadata:
 name: --> name of the deployment
spec:
 replicas: --> number of replicas of pods created
 strategy: 
  type: --> the type of startegies used in reacreating when updating or rolling back the updates (Reacreate remove the old replicasets and create new ones, Rolling update )
  rollingUpdate: --> a property used when using the rollingupdate strategy
   maxSurge:  --> the max number of pods created when rolling a new update 
   maxUnavailable: --> the max number of pods you can destroy while rolling a new update to surge a new pod
```
- when rolling back pods are scaled down to 0 and then scaled up to an n number in the previous replicasets because deleting the replica set when recreating wouldnt enable the rollback method

# 10-2-2025

## DaemonSet
- ensures that the template pod is exisstent on some or all nodes where the limiting of nodes are the scheduler rules and not specified inside the configuration yml file of the daemonSet.
- most common use case of a daemonset is the logging pod used to log the pods sttae

## StatefulSet
- managing pods and replicas and in a stateful manner and assigning sticky identities to each pod and unique netowrk identifiers and unique storage attachments and
- failures and updates are rolled for each unique pod using the same attachments and each pod or each replicaset is assigned a unique name for example or a pod idk which is which yet 
- yet its used to replicate and manage stateful apps

## Set based selectors
- labels are simply a set and its matched in a selector when the 
## Services
- exposing a group of Pods over a network using a selector 
- which acts as a load balancer for my pods and a unified single endpoint
- it has several types (Cluster IP,Headless, Node port,LoadBalancer)

### Cluster IP 
- exposing the traffic of several pods on a single hostname which is the service or the service ip instead of accessing each pod with its own ip address
- you need to specify in the pod or replicaset port routing exposing pods on a specific port needed 
- the routing of traffic between each pod and which will take the next request would be the function of the service and not the pods
- keep in mind that contianer network assignemnt and port forwarding is done by default in the pods and talking to the pod is done instead fo talking to the container directly and its exposed to the pod to the same network interface becuase all the containers are sharing the same netowkr interface isolated by the pod on the node

### Headless Service
- Headless service is the same as the 
### NodePort
- routes ports from external traffic to internal nodes configuring the ports to listen on the specified Nodeport property
### LoadBalancer
- ingress manages routing names and paths which redirects traffic to a specific service which is then configured ????
- would initializing the service with the loadbalancer type negate the need of a loadbalancer or not

### External Name
- needs to be understood it only has the property external domain name
- which i dont understand
### Syntax

```
apiVersion: --> a version string v1
kind: Service
metadata: --> metadata about the service
 name: --> name of the service used as a hostname when rerouting traffic using the service name exposition
spec:
 type: --> type of the service (Cluster IP,Headless, Node port,LoadBalancer)
 clusterIP: None --> specified with none to specify a headless service
 selector: --> the selector to apply the service to how to expose it
  selector_name: --> it could be name,tier,label,etc. smoething to match pod, certain pods
ports: --> specifying ports that will be routed but doesnt expose ports or forward any of them it acts as a guide and speifies where traffic would go from and where would it go to 
 - port:80 --> port accessed with the hostname of the service
   protocol: --> is defined in the LoadBalancer
   nodePort: 31333 --> port exposed to the public traffic to access a specified port on the service layer wrapping the pods with the target port
   targetPort:8080 --> rerouted port for the pods initiated or replicasets unified by the service (you must specify the target port as the exposed port for the pod or replicaset template when creating)

```

**how can i deteremine the limits for a current running system or process?**

**if i specify in the resource quota number of delpoyments and pods what if a pod with 3 and 2 and 2 fails and 3 sees that it has an empty slot so it can start the pod**

**what exactly does the throttling mean does it mean halting the process or simply stop incoming requests or what eaxctly**

**why specify that its ignored during execution on node affinity**

**pod affinity is going close to pods i think maybe look it up more**

# 13-2-2025

## MultiContainers
- is just the idea of having several containers in one pod several containers are given names for example attach a proxy container or attach a sidecar container each of these are conceptual container types and not actually specified inside the yml file

## InitContainers

- these are containers specified in the yml file by `initContainers:` and these are a type of containers that are ran on pod initialization and after successfully exiting the containers list is started running and used as the core functionality of the pod for example a running process such as ssh or nginx

## Probes
- the probes check certain checks at different stages of the container lifecycle
- probes are container specific they are applied to containers and not pods
- k8s have three tyeps of checks (exec,httpGet,tcpSocket)

### Probe checks
- `exec` runs a command when an exit status of 0 then it succeeds
- `httpGet` runs a http request at a specified path and port number and with a status code of 200+ <400 then it succeeds
- `tcpConnection` listens at a socket and suceeds if the connection is open at that specific port

### Pobe configurations 
- `successThreshold` applies the rules of the probe type after success counts minimum is 1 for sucess and liveness
- `terminationGrace` applies a minimum amount of seconds for the container to fail and stop not to stop it abruptly
- `failure threshhold` start restarting after the number of failures of the specified probe
- `initialDelay` delay of executing the check on the first time 
- `PeriodSeconds` used in periodic checks such as liveness and readiness the amount of seconds between each check and the next

### StartupProbe
- Runs on the start of the contianer to let it be live and ready to recieve requests
### LivenessProbe
- Runs on periodically during the lifetime of the container and when it fails it restarts the container and keeps checking
### ReadinessProbe 
- Runs periodically and checks the container is ready for accepting requests it means it isnt ready to accept requests but yet it doenst need to be restarted and needs to be solved for example stopping traffic because sending a requests has a huge delay so stop the incoming requests yet dont restart the container

## Commands and args

- commands are overriding the entrypoint for the image of the container created
- args are the arguments passed to the command written inside the container
- if args are passed it doesnt overwrrite i presume the entry point yet it passes theses arguments to the entry point of the container and if sepcified a cmd it will probably override it (these are all assumptions and needs further teesting)
```
# shell form and exec form
command:
 - sh
 - -c
# or
command: ["/bin/sh","-c"]
# shell form and exec form
args: ["echo hello"]
# or
args:
 - echo hello
```

**you can view the output of the pod you're targeting by kubectl logs pod-name**


## Environment variables

- you can pass environment variables to your container just like passing your environment variables to the container in teh dockerfile
```
env:
 - name: name
   value: value
```

## ConfigMap 
- ConfigMap is a non-encrypted environment variables sharing entity that is shared across the namespace as well and can be created as an entity on its own
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-configmap
# probably its treated as a json object when parsing from yml to json
data:
  key: value
```
- calling the configMap is done in the same namespace and cant be done across namespaces
- syntax for calling the configMap is

```
envFrom:
   configMapRef:
	name: configMap-name
# or 

env:
  - name: bla
    valueFrom:
      configMapKeyRef:
	name: configMap-name
	key: country

# where from the first you call country by its key name and value
# in the second option you can call the value of country and set it into bla environmental variable
```

## Secrets
- secrets are the same as configmaps yet its content must be encoded to base64 and not encrypted for anyone to see the file must decode the values ifrst to view it
- secrets are used with tokens and certificates becuase they contian mainly special characters and you need to encode it to not break the yml file
- `kubectl create secret` 

```
evFrom:
  - secretRef:
	name: secret-name
env:
 valueFrom:
  secretKeyRef:
    name:
    key:
```
