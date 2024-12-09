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
