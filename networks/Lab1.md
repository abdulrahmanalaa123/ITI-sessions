Using Ubuntu 24.0.1 tls
4-12-2024

# Explain how to get the private IP
- by using ifconfig [interface name]
  tomato@tomato:~/CS/devops/ITI/networks$ ifconfig wlp60s0 

# difference between ifconfig and ifconfig [driver name]
- The difference is resulting in the list of interface cards where ifconfig would get all the adapters including their ip adresses and default gateway and dhcp server
- where only the driver name or in windows ipconfig would get the current tcp/ip configuration 

# find the public ip address
- you can find the public ip address either by visiting ifconfig.me or in the cli just type a curl request to the website
- curl ifconfig.me
  
# difference between public and private ip
- the difference between public and private ip is that the private is replicable in different networks while the public ip is unique for the device
- the idea of creating a private ip was to conserve the amount of ips given to devices since there is a scarce amount which is 4.2 Billion ip addresses so the private ip is given by the router and using nat is translated into public ip when communicating with eternal connections.

# how does the device gets its IP?

- The device gets its private IP either statically by writing it yourself in the allowed ranges
- or getting assigned an automatic IP using DHCP which resets after connecting or disconnecting
- and then there is the APIPA which is given a temporary IP assigned IP which isnt valid for establishing a connection but needs to be given so that the device cant be connected to a network without being assigned an ip and whenever trying to establish a connection an ip must be given either statically or with DHCP for it to work

# make your device get its private ip statically
***this question was the hardest to do in the cmd which i still need to figure out***
# Reset your device to get its private IP automatically
- it will be given automatically by enabling the DHCP
- after trying to set static IP it was a test run didnt change the actual ip so my current ip address and configuration is still the same as the first question

# What do you knwo about APIPA address
- APIPA which is a temporary IP assigned IP which isnt valid for establishing a connection but needs to be given so that the device cant be connected to a network without being assigned an ip and whenever trying to establish a connection an ip must be given either statically or with DHCP for it to work

# 2 ways to find out your device's mac address
- either by using ip addr command which will show the device's mac address
- you can use as well ifconfig which is found in the global section 

# differnce between getmac and getmac/v
- getmac /v is the same as getmac but in a more verbose output 

# How can you request a new IP from a dhcp server
- you can get a new IP address by restarting the device
- dhcp -k interface name to reset the configuration for the card
- dhpc -n interface name to flush the current configuration and request a new one from the dhcp server

# What do you know about the ARP protocol
- is a protocol that is present in the data link layer in the OSI and in the internet layer in TPC/IP responsible for finding the hardware address of (MAC) from a given IP address
# how to view the arp cache in the device
- by simply using the command arp
# how to delete the arp cache
- ip -s -s neigh flush all
# how to view the local routing table
- netstat -rn  where r shows the routing tables and n makes it show the numeric value of their addresses instead of trying to comprehend their symbolic names
# Command to check the connectivity between 2 devices
- its the ping command
## check the connectivity of your loopback address
- ping 127.0.0.1
## packets sent
- there were 7 packets sent to check the connectivity
## packets received
- packets received were 7 packets which means no packet loss happened and the connection is healthy
## pinging 10.10.0.10
- the current ip address which im trying to reach isnt up at the moment which proves that there is no connection happening at the moment between the specified ip address
# pinging 127.0.0.1 with packets of 5000 8 times
- ping 127.0.0.1 -s 5000 -c 8
- althought its 5000 -28 bytes to send an exact 5000 because of thte 28 bytes headers present in the icmp protocol
# ping 127.0.0.1 -t
means setting the number of hops to a specific endpoint limiting it to the number specified which is the number of routers the request hops through so it can reach the destination
# meaning of a DOS attack
it means bombarding the designated server with requests more than it can handle so it affects the connectivity and performance of the server in responding to other clients 
