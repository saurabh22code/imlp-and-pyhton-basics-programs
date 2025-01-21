"""
Q.6. Create the python programme That validates IPV 4 Addresses using regular expression module

Here’s a Python program that validates IPv4 addresses using the re (regular expression) module"""
import re

# Function to validate an IPv4 address
def is_valid_ipv4(ip):
    # Regular expression pattern for a valid IPv4 address
    pattern = r'^([0-9]{1,3}\.){3}[0-9]{1,3}$'
    
    # Check if the IP matches the basic pattern
    if not re.match(pattern, ip):
        return False
    
    # Further validate each octet to ensure it is within the range 0-255
    octets = ip.split('.')
    for octet in octets:
        if not 0 <= int(octet) <= 255:
            return False
    
    return True

# Example usage
ip_addresses = [
    "192.168.0.1",  # Valid
    "255.255.255.255",  # Valid
    "0.0.0.0",  # Valid
    "256.100.50.25",  # Invalid
    "192.168.1",  # Invalid
    "192.168.0.256",  # Invalid
    "abc.def.ghi.jkl"  # Invalid
]

print("IPv4 Address Validation Results:")
for ip in ip_addresses:
    result = "Valid" if is_valid_ipv4(ip) else "Invalid"
    print(f"{ip}: {result}")
