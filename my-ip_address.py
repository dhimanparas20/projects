import socket 

hostname = socket.gethostname()
ipadd = socket.gethostbyname(hostname)

print(f"Compuer name: {hostname}")
print(f"Compuer IP-Address: {ipadd}")
