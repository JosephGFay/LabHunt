
import random

mac_addresses = []

# Generate 24 MAC addresses and append them to the list
for i in range(24):
    mac_hex = [random.randint(0x00, 0xff) for _ in range(6)]  # Generate 6 random bytes
    mac_str = ':'.join(f'{b:02x}' for b in mac_hex)  # Convert bytes to a formatted string
    mac_addresses.append(mac_str)


names = [
    'Chris',
    'Joseph',
    'Brittany',
    'Jose',
    'Damion',
    'Devon',
    'David',
    'Josh',
    'Lauren',
    'Cinthya',
    'Nancy',
    'Jaia',
    'Glenn',
    'Stephanie',
    'Ali',
    'Andy',
    'Victor',
    'Marcus',
    'Justin',
    'Pearce',
    'Macie',
    'Brennen',
    'Rodrigo',
    'John',
]
ips = ['99.106.62.1', '99.106.62.2', '99.106.62.3', '99.106.62.4', '99.106.62.5', '99.106.62.6', '99.106.62.7', '99.106.62.8', '99.106.62.9', '99.106.62.10', '99.106.62.11', '99.106.62.12', '99.106.62.13', '99.106.62.14', '99.106.62.15', '99.106.62.16', '99.106.62.17', '99.106.62.18', '99.106.62.19', '99.106.62.20', '99.106.62.21', '99.106.62.22', '99.106.62.23', '99.106.62.24', '99.106.62.25']


npc_data = {
    'names': names,
    'ips': ips,
    'macs': mac_addresses
}
