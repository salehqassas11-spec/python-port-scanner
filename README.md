# Python TCP Port Scanner

A lightweight, command-line TCP port scanner developed in Python to explore network security fundamentals, TCP connections, service identification, and automated security reporting.

Built as a hands-on cybersecurity learning project using Python's standard library.

## Features

- **TCP Port Scanning:** Check whether TCP ports accept connections.
- **Multi-Port Scanning:** Scan a configurable range of TCP ports.
- **Service Identification:** Display common services associated with port numbers.
- **Command-Line Interface:** Specify target IPv4 addresses and port ranges.
- **Input Validation:** Reject invalid IP addresses and port ranges.
- **JSON Reporting:** Export scan results with UTC timestamps.
- **Scan Statistics:** Display total scanned ports and open ports.
- **Automated Testing:** Unit tests using Python's `unittest` framework.

## Technologies Used

- Python 3
- Socket Programming (`socket`)
- Command-Line Parsing (`argparse`)
- JSON
- Python `unittest`
- Git & GitHub

No third-party Python dependencies are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/salehqassas11-spec/python-port-scanner.git
```

Navigate to the project directory:

```bash
cd python-port-scanner
```

## Usage

### Basic Scan

```bash
python scanner.py
```

By default, the scanner targets `127.0.0.1` and scans TCP ports 7998–8002.

### Custom Target and Port Range

```bash
python scanner.py --target 127.0.0.1 --start 7999 --end 8001
```

### Export Results to JSON

```bash
python scanner.py --target 127.0.0.1 --start 7999 --end 8001 --output results.json
```

### View Available Options

```bash
python scanner.py --help
```

## Example Output

The following example assumes a local HTTP server is listening on TCP port 8000.

```text
===================================
       PYTHON TCP PORT SCANNER
===================================
Target: 127.0.0.1
Scanning ports 7999 to 8001...

[NOT_OPEN] Port 7999 - Unknown
[OPEN] Port 8000 - HTTP Alt
[NOT_OPEN] Port 8001 - Unknown

========== SCAN SUMMARY ==========
Total ports scanned: 3
Open ports: 1
Other results: 2
==================================

Scan completed!
```

## JSON Reporting

The scanner generates structured reports containing:

- Target IPv4 address
- UTC timestamp
- Starting and ending port numbers
- Total ports scanned
- Number of open ports
- Individual port results and common service labels

Generated reports can be used for further analysis or integrated into other Python projects.

## Automated Testing

Run the unit tests:

```bash
python -m unittest -v test_scanner.py
```

The tests check:

1. Detection of an open TCP port.
2. Structure of returned scan results.
3. Detection of a TCP port without a listener.

## Limitations

- Supports IPv4 TCP connect scanning only.
- Scans ports sequentially.
- Service names are based on common port associations, not application fingerprinting.
- A failed TCP connection does not necessarily indicate that a port is closed; filtering, timeouts, and network errors may produce similar results.
- Does not perform vulnerability scanning or exploitation.

## Ethical Usage

This tool is intended for educational purposes and authorized security testing only.

Only scan systems that you own or have explicit permission to assess.

## Future Improvements

- Concurrent scanning for improved performance
- More detailed connection error classification
- CSV report exporting
- Service banner detection
- Improved logging and exception handling

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
