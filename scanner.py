
import socket
import argparse
import json
from datetime import datetime, timezone

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


# Function to scan a single TCP port
def scan_port(ip, port):

    service = services.get(port, "Unknown")

    # Create an IPv4 TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:

        # Set a one-second connection timeout
        scanner.settimeout(1)

        try:
            result = scanner.connect_ex((ip, port))

            if result == 0:
                status = "open"
            else:
                status = "not_open"

        except socket.error as error:
            status = "error"
            print(f"[ERROR] Port {port}: {error}")

    # Return structured data instead of only printing
    return {
        "port": port,
        "status": status,
        "service": service,
    }


def main():

    # Configure command-line arguments
    parser = argparse.ArgumentParser(
        description="Python TCP Port Scanner"
    )

    parser.add_argument(
        "--target",
        default="127.0.0.1",
        help="Target IPv4 address",
    )

    parser.add_argument(
        "--start",
        type=int,
        default=7998,
        help="Starting TCP port",
    )

    parser.add_argument(
        "--end",
        type=int,
        default=8002,
        help="Ending TCP port",
    )

    # Optional JSON output filename
    parser.add_argument(
        "--output",
        help="Save scan results to a JSON file",
    )

    args = parser.parse_args()

    # Validate the port range
    if not (1 <= args.start <= args.end <= 65535):
        parser.error("Invalid port range.")

    # Validate the IPv4 address
    try:
        socket.inet_pton(socket.AF_INET, args.target)
    except OSError:
        parser.error("Invalid IPv4 address.")

    # Display scanner information
    print("===================================")
    print("       PYTHON TCP PORT SCANNER     ")
    print("===================================")

    print(f"Target: {args.target}")
    print(f"Scanning ports {args.start} to {args.end}...\n")

    results = []

    # Scan every port in the selected range
    for port in range(args.start, args.end + 1):

        scan_result = scan_port(args.target, port)
        results.append(scan_result)

        print(
            f"[{scan_result['status'].upper()}] "
            f"Port {port} - {scan_result['service']}"
        )

    # Calculate scan statistics
    open_ports = sum(
        1 for result in results
        if result["status"] == "open"
    )

    total_ports = len(results)

    # Create a structured scan report
    report = {
        "target": args.target,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "start_port": args.start,
        "end_port": args.end,
        "total_ports_scanned": total_ports,
        "open_ports": open_ports,
        "results": results,
    }

    # Export the report if an output filename was provided
    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as file:
                json.dump(report, file, indent=4)

            print(f"\n[+] Report saved to {args.output}")

        except OSError as error:
            print(f"\n[ERROR] Could not save report: {error}")

    # Display the scan summary
    print("\n========== SCAN SUMMARY ==========")
    print(f"Total ports scanned: {total_ports}")
    print(f"Open ports: {open_ports}")
    print(f"Other results: {total_ports - open_ports}")
    print("==================================")

    print("\nScan completed!")


if __name__ == "__main__":
    main()
