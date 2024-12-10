# 9-12-2024

## Setting up a vm as an ftp server and I would be the client using ftpd

### 1- first install vsftpd on centos using yum 

```
sudo yum install vsftpd
```

### 2- and configure the firewall public zone for enabling the ports on passive mode

```
 sudo firewall-cmd --zone=public --permanent --add-port=20/tcp 
 sudo firewall-cmd --zone=public --permanent --add-port=21/tcp
 sudo firewall-cmd --zone=public --permanent --add-port=5000-6000/tcp
 sudo firewall-cmd --zone=public --permanent --add-service=ftp
 
 // protocol 6 is the number for the tcp protocol defined in /etc/protocols 
 sudo firewall-cmd --zone=public --permanent --add-protocol=6
```

### 3- disable seLinux for testing purposes on a real life situation you would need to configure to enable access for ftp which i dont know how and didnt bother which is in /etc/selinux/config

### 4- and finally config the ftp to chroot any non-admin user but this link does the ftp config really well and i see that i have no input over it unless you want to customize which you need to man the conf as mentioned below thats what i did at least 
 
- https://www.geeksforgeeks.org/how-to-setup-and-configure-an-ftp-server-in-linux-2/

### 5-setup a host domain in the /etc/hosts on the client side to not specifically call it by the ip address (not necessary just a convenience)

```
xxx.xxx.xxx.xxx www.myftp.com
```

### 6- in your ftp directory create a large txt file of 1gb for testing transfer 
```
dd if=/dev/zero of=large_file.txt bs=100M count=10
```

### finally you can connect and test your own ftp server
```
ftp www.myftp.com
```
## learned along the way

### Vsftpd
- Well I cant and wont explain the whole service since its not preferrable all you need to know is written in their man just read it but what you need to know is that its an ftp daemonn that if specified listen it will run as a background service and would be handled with systemctl and if not you need to run the binary for the service to start
- a sfor another helpful tip for the cocnfigs is just open man vsftpd.conf.5 and it contains everything you need as well from chroot options to local access.
### FTP

- https://www.cosmos.esa.int/documents/772136/977578/psa_activeVsPassiveFtp.pdf/5e36a7b8-8732-4e65-ab6b-6cf94a742ea6

- this is a real concise and a neat explanation for ftp and ftp protcols 
- ftp is a unique protocol which uses 2 ports to perform a transfer 20,21 one is called a command port which is done to send the identification and establish the connection and one is the data port which is established to transfer data through it 
- ftp is divided into two connection methods active and passive connections
- ascii mode is the conversion method of line terminators in windows to linux or vice versa where it standardizes both in the connection and transforms it at the host platform for whomever initiated the request or requesting the file
- disabling it just transfers the file as is without modification
- there is some info about binary file transferring which i dont fully understand but fuck it it aint that useful

#### Active Connection
- well the active connection handles the connection server side which means the client connects to the command port from a random port(n) and the server responds from its command port (21) to the client's command port(n) 
- then the server connects to the client's random port 2 (n+1) through its data port (20) and then the client responds back to the data port (20) 
- and finally the client sends acknowledgment to the server establishing the tcp connection on which they can transfer data 
- this compromises the client since its ports are random it must enable a range of ports in its firewall so it weakens the security a bit (not fully understood tho)

#### Passive connection
- The passive connection handles the connection on the client side.
- The client sends from a random port (n) to the server's command port (21) wanting to connect then the server responds from the command port(21) to (n) opening a random port specified in a range outside the reserved ports(k)
- The client then connects to the said port(k) from its data port(n+1) sending the sync request and the server responds back with the ack to the port(n+1)
- Now how this comprimises the server by exposing a range of allowed inbound ports which comprimises the server in this case 

### chroot
-  well chroot is a virtual root folder change for the current process and all of its children which is useful in the ftp server where you can set the ftp directory as the root directory for the anon user for example cant access but it
-  and if you use ldd to see the required shared libraries or binaries needed for the chroot to take a copy of the directory you're trying to make the root to work
-  creates an isolated environment which is perfect for ftp


### sda1
- is mass storage driver , a = 1st registered device on the system, 1 = 1st partition on that device
- is just a block storage inside your hard drive
### fstab , df 
- fstab is the mounting map for the linux which implies where and what to boot from which partition but wont look into that since its not of that much use rn 
- df prints the current available storage space on the device with all its partitions and drives, etc.
### friewalld
- firewalld is a zone based firewall which puts poilicies and services with rules against different zones
- so what does zone based mean? a zone is typically a network whihc is connected by a router zone based firewalls work on zone to zone communication which unlike past where each device has his context based firewall (not delving into this rabbit hole)
- zone based configurations are usually split into 3 main types 
#### Main Types of Zones
- public zones which accesses the internet which is configured for outbound requests coming into my server 
- private zones are firewall rules applied to internal zone to zone communication for example i have a netowrk of pcs that wants to communicate to another inside my facility we mark these with private zones and assigning the proper interface
- DMZ (dematerialized zones) its a neutral zone (keep in mind i dont understand it that well its a bit out of my scope rn) its said to be the zones which are in between public and private zones they dont access the internet but can be accessed publicly sth like that dont really know for sure but yet its one type i guess
- It is encouraged to put ftp servers on dmz because if it does get compromised people dont get access to the private network or your sensitive info thats logical but yet i cant configure that atm so fuck it

### Policies
- requests in firewalls in general go through a policy chain with each having its own priority in firewalld policies have a default priority of -1 which means it goes through the zone policy second
- policy priority numbers range from -3786 to 3786 (as i remember) and each policy have its own ports, targets, rules, etc 
- negative being applied before the zone rules and positive being applied after the zone rules

### Zone Targets in firewalld

- The zone targets are actions required to do when not following the defined rules
- They are for zones default , Accept, Reject, Drop and for the default is just like the reject but it will pass ICMP messages trying to reach the network
- Accept is letting the packet go through and its in cases that the zone is trusted and 
- And for drop is drop the incoming packet coming into the zone not following any of the policies
- and finally for reject is simply block the packet that doesnt match the rules

### Policy Targets in firewalld
- They are the same as the zone policies but instead of default it has a continue target which i believe makes it continue on the policy chain

- ***need to look in ingress and egress-zones for policies but later i dont need it rn to create the server***


- ***note that to the default for policies to apply on any traffic going from the host to any other zone is ingress-zone:HOST egress-zone:ANY***
