
import socket
import argparse

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
    8080: "HTTP Proxy / Alt",
}


# Function to check whether a TCP port is open
def scan_port(ip, port):

    # Create an IPv4 TCP socket
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set the connection timeout to 1 second
    scanner.settimeout(1)

    try:
        # Attempt a TCP connection to the target
        result = scanner.connect_ex((ip, port))

        # Look up the common service for this port
        service = services.get(port, "Unknown")

        # Display the connection result
        if result == 0:
            print(f"[OPEN] Port {port} - {service}")
        else:
            print(f"[NOT OPEN] Port {port} - {service}")

    except socket.error as error:
        print(f"[ERROR] Port {port}: {error}")

    finally:
        # Always release the socket
        scanner.close()


# Main function to control the program
def main():

    # Create the command-line argument parser
    parser = argparse.ArgumentParser(
        description="Python TCP Port Scanner"
    )

    # Target IPv4 address
    parser.add_argument(
        "--target",
        default="127.0.0.1",
        help="Target IPv4 address (default: 127.0.0.1)",
    )

    # Starting TCP port
    parser.add_argument(
        "--start",
        type=int,
        default=7998,
        help="Starting TCP port (default: 7998)",
    )

    # Ending TCP port
    parser.add_argument(
        "--end",
        type=int,
        default=8002,
        help="Ending TCP port (default: 8002)",
    )

    # Read the arguments supplied by the user
    args = parser.parse_args()

    # Validate the port range
    if not (1 <= args.start <= args.end <= 65535):
        parser.error(
            "Ports must be between 1 and 65535, "
            "and --start must not exceed --end."
        )

    # Validate the target as an IPv4 address
    try:
        socket.inet_aton(args.target)
        if args.target.count(".") != 3:
            raise ValueError("Invalid IPv4 address")
    except (OSError, ValueError):
        parser.error("Please provide a valid IPv4 address.")

    # Display scan information
    print("===================================")
    print("       PYTHON TCP PORT SCANNER     ")
    print("===================================")

    print(f"Target: {args.target}")
    print(f"Scanning ports {args.start} to {args.end}...\n")

    # Scan each port in the requested range
    for port in range(args.start, args.end + 1):
        scan_port(args.target, port)

    print("\nScan completed!")


# Run main() only when this file is executed directly
if __name__ == "__main__":
    main()
