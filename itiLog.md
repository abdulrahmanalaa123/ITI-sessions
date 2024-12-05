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



