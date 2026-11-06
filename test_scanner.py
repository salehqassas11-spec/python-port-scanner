
import socket
import threading
import unittest

# Import the scanning function from our project
from scanner import scan_port


class TestPortScanner(unittest.TestCase):

    # Test 1: Check whether the scanner detects an open port
    def test_open_port(self):

        # Create a temporary local TCP server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind(("127.0.0.1", 0))
            server.listen(1)

            # Get the automatically assigned port
            port = server.getsockname()[1]

            # Scan the temporary server
            result = scan_port("127.0.0.1", port)

            # Verify the port is detected as open
            self.assertEqual(result["status"], "open")
            self.assertEqual(result["port"], port)

    # Test 2: Check the structure of the scan result
    def test_result_structure(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind(("127.0.0.1", 0))
            server.listen(1)

            port = server.getsockname()[1]
            result = scan_port("127.0.0.1", port)

            # Verify the required JSON fields exist
            self.assertIn("port", result)
            self.assertIn("status", result)
            self.assertIn("service", result)

    # Test 3: Check detection of a port with no listener
    def test_not_open_port(self):

        # Reserve an available local port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind(("127.0.0.1", 0))
            port = server.getsockname()[1]

        # After closing the socket, nothing should be listening
        result = scan_port("127.0.0.1", port)

        self.assertEqual(result["status"], "not_open")


if __name__ == "__main__":
    unittest.main()
