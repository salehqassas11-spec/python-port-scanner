import socket # Import Python's built-in networking module

# Define the target IP address and TCP port to scan
target = "127.0.0.1" # Localhost (our own computer)
port = 8000 # TCP port we want to check

# Create a TCP socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

scanner.settimeout(1) # Set a 1-second timeout to prevent waiting indefinitely

# Attempt to establish a TCP connection to the target IP and port
# connect_ex() returns 0 if the connection succeeds
result = scanner.connect_ex((target, port))

# Check whether the TCP connection was successful
if result == 0:
    print(f"[OPEN] Port {port}")
else:
    # A failed connection may indicate a closed or filtered port
    print(f"[NOT OPEN] Port {port}")

    # Close the socket to release system resources
    scanner.close()