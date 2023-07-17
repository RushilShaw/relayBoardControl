import sys
import serial
import socket
import relayController


USE_ETHERNET_INSTEAD_OF_USB = True
COM_PORT = "COM14"
IP_ADDRESS = "192.168.11.1"
PORT = 2101
BAUD = 115200
NUM_RELAY_PORTS = 16
command_to_function = {
        "ON": relayController.RelayController.turn_on_relay_by_index,
        "OFF": relayController.RelayController.turn_off_relay_by_index,
        "TOGGLE": relayController.RelayController.toggle_relay_by_index,
        "STATUS": relayController.RelayController.get_relay_status_by_index,
        "KEEP_LED_ON": relayController.RelayController.keep_led_on
    }


def validate_inputs(argv: list[str]) -> (str, int):
    invalid_number_of_arguments_msg = "This program must be run with two command line arguments. \n"
    invalid_first_argument_msg = "The first argument is the command that is sent to the relay board. " \
                                 f"Valid commands include: [{' '.join(command_to_function.keys())}]\n"
    invalid_second_argument_msg = "The second argument must be the which port on the relay controller. " \
                                  "This number must be between 1 and NUM_RELAY_PORTS\n"

    error_msg = ""
    if len(argv) != 3:
        error_msg = invalid_number_of_arguments_msg + invalid_first_argument_msg + invalid_second_argument_msg
    else:
        if argv[1] not in command_to_function.keys():
            error_msg += invalid_first_argument_msg
        if not argv[2].isnumeric() or not (1 <= int(argv[2]) <= NUM_RELAY_PORTS):
            error_msg += invalid_second_argument_msg

    if error_msg:
        raise ValueError(error_msg)

    return argv[1], int(argv[2])


def main():
    command, relay_number = validate_inputs(sys.argv)
    function = command_to_function[command]

    if USE_ETHERNET_INSTEAD_OF_USB:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((IP_ADDRESS, PORT))
        sock.settimeout(0.5)
        communication_method = sock
    else:
        communication_method = serial.Serial(port=COM_PORT, baudrate=BAUD)

    with communication_method as combus:
        relay_controller = relayController.RelayController(combus=combus)
        response = function(relay_controller, relay_number)
    print(response)


if __name__ == '__main__':
    main()
