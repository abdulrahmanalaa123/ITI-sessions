Using Ubuntu 24.0.1 tls
# Explain how to get the private IP
- by using ifconfig [interface name]
- since there is a difficulty of attaching screenshots

- i will attach the result from ifconfig of my wlan interface card
tomato@tomato:~/CS/devops/ITI/networks$ ifconfig wlp60s0 
wlp60s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet ***192.168.1.38***  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::dbce:4752:4bb2:9dee  prefixlen 64  scopeid 0x20<link>
        inet6 fd64:6d6c:e922:d500:be7d:7aac:d67f:60d4  prefixlen 64  scopeid 0x0<global>
        inet6 fd64:6d6c:e922:d500:8bf2:15c6:4b0f:e7d1  prefixlen 64  scopeid 0x0<global>
        ether 82:22:a5:14:92:4c  txqueuelen 1000  (Ethernet)
        RX packets 3797083  bytes 3728995147 (3.7 GB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1247285  bytes 302666307 (302.6 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

# difference between ifconfig and ifconfig [driver name]
- The difference is resulting in the list of interface cards where ifconfig would get all the adapters including their ip adresses and default gateway and dhcp server
-
- where only the driver name or in windows ipconfig would get the current tcp/ip configuration  

# find the public ip address
- you can find the public ip address either by visiting ifconfig.me or in the cli just type a curl request to the website
- curl ifconfig.me
- which would result in 41.239.11.226  

# difference between public and private ip
- the difference between public and private ip is that the private is replicable in different networks while the public ip is unique for the device
- the idea of creating a private ip was to conserve the amount of ips given to devices since there is a scarce amount which is 4.2 Billion ip addresses so the private ip is given by the router and using nat is translated into public ip when communicating with eternal connections.

# how does the device gets its IP?

- The device gets its private IP either statically by writing it yourself in the allowed ranges
- or getting assigned an automatic IP using DHCP which resets after connecting or disconnecting
- and then there is the APIPA which is given a temporary IP assigned IP which isnt valid for establishing a connection but needs to be given so that the device cant be connected to a network without being assigned an ip and whenever trying to establish a connection an ip must be given either statically or with DHCP for it to work

# make your device get its private ip statically

- by using ifconfig and root user access to set the ip address into for example
- sudo ifconfig wlp60s0 192.168.1.7 netmask 255.255.255.0
- sudo route add default gw 192.168.1.1 wlp60s0 

# Reset your device to get its private IP automatically
- it will be given automatically by enabling the DNS 
- after trying to set static IP it was a test run didnt change the actual ip so my current ip address and configuration is still the same as the first question

# What do you knwo about APIPA address
 APIPA which is a temporary IP assigned IP which isnt valid for establishing a connection but needs to be given so that the device cant be connected to a network without being assigned an ip and whenever trying to establish a connection an ip must be given either statically or with DHCP for it to work

# 2 ways to find out your device's mac address
- either by using ip addr command which will show the device's mac address 
- you can use as well ifconfig which is found in the global section which is
- 82:22:a5:14:92:4c
  
# differnce between getmac and getmac/v
- getmac /v is the same as getmac but in a more verbose output give

# How can you request a new IP from a dhcp server
- you can get a new IP address by restarting the device

# What do you know about the ARP protocol
- is a protocol in the data link layer that is present in the data link layer in the OSI and in the internet layer in TPC/IP responsible for finding the hardware address of (MAC) from a given IP address

# how to delete the arp cache
- ip -s -s neigh flush all 
