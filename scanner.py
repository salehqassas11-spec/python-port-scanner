
import socket  # Python's built-in networking module

# Define the target and the range of TCP ports
target = "127.0.0.1"
start_port = 7998
end_port = 8002


# Function to check whether a TCP port is open
def scan_port(ip, port):

    # Create an IPv4 TCP socket
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wait a maximum of 1 second for a connection
    scanner.settimeout(1)

    try:
        # Attempt a TCP connection to the target
        result = scanner.connect_ex((ip, port))

        # A return value of 0 means the connection succeeded
        if result == 0:
            print(f"[OPEN] Port {port}")
        else:
            print(f"[NOT OPEN] Port {port}")

    except socket.error as error:
        print(f"[ERROR] Port {port}: {error}")

    finally:
        # Always close the socket after scanning
        scanner.close()


# Display information about the scan
print("=== Python TCP Port Scanner ===")
print(f"Target: {target}")
print(f"Scanning ports {start_port} to {end_port}...\n")

# Loop through every port in the specified range
for port in range(start_port, end_port + 1):
    scan_port(target, port)

print("\nScan completed!")
