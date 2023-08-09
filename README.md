# Relay Controller

This code allows you to control a relay board either through USB or Ethernet communication. The relay board is used to control switches or devices connected to its relay ports.

## Prerequisites

- Python 3.x
- `serial` library 

## Setup

1. Make sure the relay board is connected.
2. Install the required libraries by running the following command:
   ```bash
   pip install pyserial
   ```
   (Only required if using USB communication)

## Usage

To use the relay controller, run the following command:

```bash
python relay_controller.py <command> <relay_number>
```

Replace `<command>` with one of the following valid commands:

- `ON`: Turns on the specified relay.
- `OFF`: Turns off the specified relay.
- `TOGGLE`: Toggles the state of the specified relay.
- `STATUS`: Retrieves the status of the specified relay.
- `KEEP_LED_ON`: Keeps the specified relay on for 35 seconds.

Replace `<relay_number>` with the port number of the relay you want to control. The relay number must be between 1 and the total number of relay ports defined in the code.

## Configuration

The behavior of the relay controller can be configured by modifying the following variables in the code:

- `USE_ETHERNET_INSTEAD_OF_USB`: Set this variable to `True` if you want to use Ethernet communication, or `False` to use USB communication.
- `IP_ADDRESS` (Ethernet): Specify the IP address of the relay board if using Ethernet communication. Example: `"192.168.11.1"`.
- `PORT` (Ethernet): Specify the port number to establish the socket connection. Example: `2101`.
- `COM_PORT` (USB): Specify the COM port to which the relay board is connected. Example: `"COM14"`.
- `BAUD` (USB): Specify the baud rate for USB communication. Example: `115200`.
- `NUM_RELAY_PORTS`: Specify the total number of relay ports on the relay board.

## Examples

- To turn on relay number 3 using USB communication:

  ```bash
  python relay_controller.py ON 3
  ```

- To toggle the state of relay number 2 using Ethernet communication:

  ```bash
  python relay_controller.py TOGGLE 2
  ```

- To get the status of relay number 1 using USB communication:

  ```bash
  python relay_controller.py STATUS 1
  ```