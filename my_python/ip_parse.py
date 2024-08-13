from collections import defaultdict

# Choose the number of octets to use (2 or 3)
octet_count = 2  # Change to 2 for first two octets

def read_ips_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Path to the file containing the list of IP addresses
file_path = 'ip_addresses.txt'  # Replace with your file path

# Read IP addresses from the file
ip_addresses = read_ips_from_file(file_path)

# Count occurrences
counts = defaultdict(int)
for ip in ip_addresses:
    octets = ip.split('.')
    if len(octets) == 4:
        key = tuple(octets[:octet_count])
        counts[key] += 1
    else:
        print(f"Invalid IP address format: {ip}")

# Print results
for key, count in counts.items():
    print(f"{'.'.join(key)} found {count} times")

