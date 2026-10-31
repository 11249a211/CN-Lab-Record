import socket

# Get the hostname
hostname = socket.gethostname()

# Get the IP address
ip_address = socket.gethostbyname(hostname)

print("Host Name:", hostname)
print("IP Address:", ip_address)

output
Host Name: DESKTOP-CNLAB01
IP Address: 192.168.1.100
