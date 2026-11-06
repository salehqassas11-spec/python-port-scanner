
import socket

# Common TCP ports and their associated services
services = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8000: "HTTP Alt",
    8080: "HTTP Proxy / Alt"
}

# Define the target IP address and port range
target = "127.0.0.1"  # Localhost (our computer)
start_port = 7998
end_port = 8002


# Function to check whether a TCP port is open
def scan_port(ip, port):

    # Create an IPv4 TCP socket
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set a 1-second connection timeout
    scanner.settimeout(1)

    try:
        # Attempt to connect to the target IP and port
        result = scanner.connect_ex((ip, port))

        # Identify the common service associated with the port
        service = services.get(port, "Unknown")

        # Check whether the TCP connection succeeded
        if result == 0:
            print(f"[OPEN] Port {port} - {service}")
        else:
            print(f"[NOT OPEN] Port {port} - {service}")

    except socket.error as error:
        # Display any socket-related errors
        print(f"[ERROR] Port {port}: {error}")

    finally:
        # Close the socket to release system resources
        scanner.close()


# Display scan information
print("===================================")
print("       PYTHON TCP PORT SCANNER     ")
print("===================================")

print(f"Target: {target}")
print(f"Scanning ports {start_port} to {end_port}...\n")

# Loop through the specified port range
for port in range(start_port, end_port + 1):
    scan_port(target, port)

# Display completion message
print("\nScan completed!")
