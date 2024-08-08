import os
import requests
import time

# Telegram bot settings but your token and chat id here
TOKEN = ''
CHAT_ID = ''

def send_telegram_message(message):
    # Send a message to the specified Telegram chat
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage' 
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f'Failed to send message: {e}')

def check_computer(ip):
    # Set the ping command based on the operating system
    param = '-n' if os.name == 'nt' else '-c'
    response = os.system(f"ping {param} 1 {ip}")
    
    if response != 0:
        send_telegram_message(f"Computer with IP {ip} is down.")

def load_active_ips(filename='active_ips.txt'):
    # Load the active IP addresses from a file
    with open(filename, 'r') as f:
        active_ips = f.read().splitlines()
    return active_ips

while True:
    # Load the saved IP addresses and check their status
    computers = load_active_ips()
    for ip in computers:
        check_computer(ip)
    time.sleep(60)  # Check every 60 seconds
