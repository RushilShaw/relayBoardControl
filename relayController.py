import requests


relay_board_ip = "192.168.0.100"
relay_board_port = 80


def relay_on(relay_number):
    state = "on"
    url = f"http://{relay_board_ip}:{relay_board_port}/{relay_number}/{state}"
    response = requests.get(url)
    return response.ok


def relay_off(relay_number):
    state = "off"
    url = f"http://{relay_board_ip}:{relay_board_port}/{relay_number}/{state}"
    response = requests.get(url)
    return response.ok


def relay_toggle(relay_number):
    state = get_relay_state(relay_number)
    if state == "on":
        return relay_off(relay_number)
    else:
        return relay_on(relay_number)


def get_relay_state(relay_number):
    url = f"http://{relay_board_ip}:{relay_board_port}/state/{relay_number}"
    response = requests.get(url)
    if response.ok:
        if response.text == "off":
            return 0
        elif response.text == "on":
            return 1
    return -1
