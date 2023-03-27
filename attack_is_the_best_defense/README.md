# Concepts
For this project, we expect you to look at these concepts:

- Network basics
- Docker
#
![](https://www.alpinesecurity.com/wp-content/uploads/2020/02/offline-password-cracking.jpg)

## Resources
Read or watch:

- Network sniffing
- ARP spoofing
- Connect to SendGrid’s SMTP relay using telnet
- What is Docker and why is it popular?
- Dictionary attack
#
### man or help:

- tcpdump
- hydra
- telnet
- docker
#
Security is a vast topic, and network security is an important part of it. A lot of very sensitive information goes over networks that are used by many people, and some people might have bad intentions. Traffic going through a network can be intercepted by a malicious machine pretending to be another network device. Once the traffic is redirected to the malicious machine, the hacker can keep a copy of it and analyze it for potential interesting information. It is important to note that the traffic must then be forwarded to the actual device it was supposed to go (so that users and the system keep going as if nothing happened).

Any information that is not encrypted and sniffed by an attacker can be seen by the attacker - that could be your email password or credit card information. While today’s network security is much stronger than it used to be, there are still some legacy systems that are using unencrypted communication means. A popular one is telnet.

In this project, we will not go over ARP spoofing, but we’ll start by sniffing unencrypted traffic and getting information out of it.

Sendgrid offers is an emailing service that provides state of the art secure system to send emails, but also supports a legacy unsecured way: telnet. You can create an account for free, which is what I did, and send an email using telnet:
