# Network Controller

This project consists of two scripts for monitoring devices on a network:

1. `arp_scanner.py`: Scans the network for active IP addresses and saves them to a file.
2. `network_controller.py`: Reads the saved IP addresses from the file and checks their status, sending a Telegram notification if any device is down.

## Features

- Retrieves the list of active IP addresses from the ARP table.
- Saves the list of active IP addresses to a file.
- Periodically checks the status of devices using ping.
- Sends a notification to a Telegram bot if a device is down.

## Requirements

- Python 3.x
- `requests` library
- A Telegram bot token and chat ID

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/GoktugGulcan/network-controller.git
    cd network-controller
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install requests
    ```

## Configuration

1. Replace `TOKEN` and `CHAT_ID` in `network_controller.py` with your Telegram bot token and chat ID.

## Usage

1. First, run the ARP scanner script to get the list of active IP addresses:
    ```bash
    python arp_scanner.py
    ```

2. Then, run the network controller script to monitor the devices:
    ```bash
    python network_controller.py
    ```

The ARP scanner script will save the active IP addresses to `active_ips.txt`, and the network controller script will read from this file and monitor the status of these IP addresses, sending a notification to the specified Telegram chat if any device is down.


