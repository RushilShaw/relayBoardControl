import sys
import serial
import relayController

PORT = "COM4"
BAUD = 158200
NUM_RELAY_PORTS = 4
function_dict = {
        "ON": relayController.RelayController.turn_on_relay_by_index,
        "OFF": relayController.RelayController.turn_off_relay_by_index,
        "TOGGLE": relayController.RelayController.toggle_relay_by_index,
        "STATUS": relayController.RelayController.get_relay_status_by_index,
        "START_TIMER": relayController.RelayController.start_relay_timer
    }


def validate_inputs(arguments: list[str]) -> (int, str):
    invalid_number_of_arguments_msg = "Must have at least two arguments. \n"
    invalid_first_argument_msg = "The first argument is the command that is sent to the relay board. " \
                                 f"Valid commands include: [{' '.join(function_dict.keys())}]\n"
    invalid_second_argument_msg = "The second argument must be the which port on the relay controller. " \
                                  "This number must be between 1 and NUM_RELAY_PORTS\n"

    error_msg = ""
    if len(arguments) < 3:
        error_msg = invalid_number_of_arguments_msg + invalid_first_argument_msg + invalid_second_argument_msg
    else:
        if arguments[1] not in function_dict.keys():
            error_msg += invalid_second_argument_msg
        if not arguments[2].isnumeric() or not (0 < int(arguments[2]) <= NUM_RELAY_PORTS):
            error_msg += invalid_first_argument_msg

    if error_msg:
        raise ValueError(error_msg)

    return arguments[1], int(arguments[2]), arguments[3:]


def main():
    command, relay_number, args = validate_inputs(sys.argv)
    function = function_dict[command]
    with serial.Serial(port=PORT, baudrate=BAUD) as combus:
        relay_controller = relayController.RelayController(combus=combus)
        if command == "START_TIMER":
            response = function(relay_controller, relay_number, hours=0, minutes=0, seconds=35, relay=relay_number)
        else:
            response = function(relay_controller, relay_number, *args)


if __name__ == '__main__':
    main()
