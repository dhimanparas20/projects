import ping3

def ping(host="www.google.com"):
    return ping3.ping(host)

# Example usage
ping_time = ping("www.google.com")
if ping_time is not None:
    print(f"Ping time: {ping_time * 1000:.2f} ms")
else:
    print("Failed to ping the host.")
