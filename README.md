# Bluetooth Client-Server Communication

These scripts demonstrate a simple client-server communication setup using Bluetooth technology. The client and server scripts allow you to exchange messages over Bluetooth using the RFCOMM protocol.

## Prerequisites

Before using these scripts, make sure you have the following:

- Python 3.x installed on both the client and server machines.
- The `socket` module, which is usually included with Python by default.

## Setup

1. Clone or download the repository containing these scripts to your local machine.

2. Ensure that your Bluetooth devices are discoverable and can establish a Bluetooth connection.

## Usage

### Server Script

1. Run the server script (`server.py`) on the machine that will act as the server.

2. The server script will wait for a connection from the client. Once the connection is established, it will receive messages from the client and display them on the console.

### Client Script

1. Run the client script (`client.py`) on the machine that will act as the client.

2. The client script will attempt to connect to the server using the server's Bluetooth address and port number. You can modify the address and port in the script as needed.

3. After the connection is established, the client can send messages to the server, which will be displayed on the server's console.

## Communication

- Both the client and server scripts use the RFCOMM protocol for Bluetooth communication.

- Messages sent between the client and server are encoded in UTF-8 format.

## Important Notes

- These scripts are intended for educational and experimental purposes. They provide a basic foundation for Bluetooth communication and can be extended for more complex applications.

- Ensure that your devices have Bluetooth capabilities and are paired or discoverable.

- Make sure to adjust Bluetooth device addresses and port numbers in the scripts to match your setup.
