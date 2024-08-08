import os
import platform

def get_arp_table():
    # Determine the correct ARP command based on the operating system
    if platform.system().lower() == 'windows':
        arp_command = 'arp -a'
    else:
        arp_command = 'arp -n'
    
    # Execute the ARP command and retrieve the result
    arp_result = os.popen(arp_command).read()
    return arp_result

def parse_arp_table(arp_table):
    # Split the ARP table into lines and parse each line
    lines = arp_table.split('\n')
    active_ips = []
    for line in lines:
        # For Windows, check for 'dynamic'. For Linux/Unix, check for 'ether' and '0x2'
        if 'dynamic' in line or ('ether' in line and '0x2' in line):
            parts = line.split()
            if len(parts) > 1:
                active_ips.append(parts[0])
    return active_ips

def save_active_ips(active_ips, filename='active_ips.txt'):
    # Save the active IP addresses to a file
    with open(filename, 'w') as f:
        for ip in active_ips:
            f.write(f"{ip}\n")

# Get the ARP table and save the active IP addresses
arp_table = get_arp_table()
active_ips = parse_arp_table(arp_table)
save_active_ips(active_ips)
