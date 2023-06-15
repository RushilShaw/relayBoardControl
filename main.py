import sys
import relayController


NUM_RELAY_PORTS = 4
function_dict = {
        "ON": relayController.relay_on,
        "OFF": relayController.relay_off,
        "TOGGLE": relayController.relay_toggle,
        "STATUS": relayController.get_relay_state,
    }


def validate_inputs(arguments: list[str]) -> (int, str):
    invalid_number_of_arguments_msg = "Must have two and only two arguments.\n"
    invalid_first_argument_msg = "The first argument must be the which port on the relay controller. " \
                                 "Starting at 1 thru NUM_RELAY_PORTS\n"
    invalid_second_argument_msg = "The second argument is the command on the port specified in the first argument. " \
                                  f"Valid commands include: [{' '.join(function_dict.keys())}]\n"

    error_msg = ""
    if len(arguments) != 3:
        error_msg = invalid_number_of_arguments_msg + invalid_first_argument_msg + invalid_second_argument_msg
    else:
        if not arguments[1].isnumeric() or not (0 < int(arguments[1]) <= relayController.NUM_RELAY_PORTS):
            error_msg += invalid_first_argument_msg
        if arguments[2] not in function_dict.keys():
            error_msg += invalid_second_argument_msg

    if error_msg:
        raise ValueError(error_msg)

    return int(arguments[1]), arguments[2]


def main():
    relay_number, command = validate_inputs(sys.argv)
    function = function_dict[command]
    response = function(relay_number)
    if response is False or response == -1:
        raise ConnectionRefusedError(f"{function.__name__} returned a response that was not okay")
    if command == "STATUS":
        print(response)






if __name__ == '__main__':
    main()
