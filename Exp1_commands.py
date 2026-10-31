ipconfig

ping google.com

tracert google.com

nslookup google.com

netstat

hostname

getmac

arp -a

tasklist

ipconfig
hostname
nslookup google.com

output:
C:\Users\User>ipconfig

Windows IP Configuration


Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . : localdomain
   IPv6 Address. . . . . . . . . . . : 2607:f8b0:4004:809::200e
   Link-local IPv6 Address . . . . . : fe80::1a2b:3c4d:5e6f:7g8h%12
   IPv4 Address. . . . . . . . . . . : 192.168.1.100
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.1.1

C:\Users\User>ping google.com

Pinging google.com [142.250.190.46] with 32 bytes of data:
Reply from 142.250.190.46: bytes=32 time=14ms TTL=117
Reply from 142.250.190.46: bytes=32 time=15ms TTL=117
Reply from 142.250.190.46: bytes=32 time=13ms TTL=117
Reply from 142.250.190.46: bytes=32 time=14ms TTL=117

Ping statistics for 142.250.190.46:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 13ms, Maximum = 15ms, Average = 14ms

C:\Users\User>tracert google.com

Tracing route to google.com [142.250.190.46]
over a maximum of 30 hops:

  1     1 ms     1 ms     1 ms  192.168.1.1
  2    10 ms     9 ms     9 ms  10.0.0.1
  3    12 ms    11 ms    12 ms  172.16.0.1
  4    14 ms    13 ms    14 ms  142.250.190.46

Trace complete.

C:\Users\User>nslookup google.com
Server:  UnKnown
Address:  192.168.1.1

Non-authoritative answer:
Name:    google.com
Addresses:  2607:f8b0:4004:809::200e
          142.250.190.46

C:\Users\User>netstat

Active Connections

  Proto  Local Address          Foreign Address        State
  TCP    192.168.1.100:49672    142.250.190.46:https   ESTABLISHED
  TCP    192.168.1.100:49673    142.250.190.188:https  ESTABLISHED
  TCP    192.168.1.100:49674    20.198.118.22:https    ESTABLISHED

C:\Users\User>hostname
DESKTOP-CNLAB01

C:\Users\User>getmac

Physical Address    Transport Name
=================== ==========================================================
00-1A-2B-3C-4D-5E   \Device\Tcpip_{A1B2C3D4-E5F6-7A8B-9C0D-1E2F3A4B5C6D}

C:\Users\User>arp -a

Interface: 192.168.1.100 --- 0x0b
  Internet Address      Physical Address      Type
  192.168.1.1           00-11-22-33-44-55     dynamic
  192.168.1.255         ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static

C:\Users\User>tasklist

Image Name                     PID Session Name        Session#    Mem Usage
========================= ======== ================ =========== ============
System Idle Process              0 Services                   0          8 K
System                           4 Services                   0      1,024 K
smss.exe                       352 Services                   0      1,120 K
csrss.exe                      512 Services                   0      4,200 K
wininit.exe                    600 Services                   0      5,120 K
explorer.exe                  1240 Console                    1     85,400 K
cmd.exe                       3412 Console                    1      4,800 K
tasklist.exe                  4108 Console                    1      7,200 K

C:\Users\User>ipconfig

Windows IP Configuration


Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . : localdomain
   IPv6 Address. . . . . . . . . . . : 2607:f8b0:4004:809::200e
   Link-local IPv6 Address . . . . . : fe80::1a2b:3c4d:5e6f:7g8h%12
   IPv4 Address. . . . . . . . . . . : 192.168.1.100
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.1.1

C:\Users\User>hostname
DESKTOP-CNLAB01

C:\Users\User>nslookup google.com
Server:  UnKnown
Address:  192.168.1.1

Non-authoritative answer:
Name:    google.com
Addresses:  2607:f8b0:4004:809::200e
          142.250.190.46
