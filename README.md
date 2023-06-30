# Relay Controller

For this project there are 5 functions:



ON - this turns the relay onto its on state

OFF - this turns the relay onto its off state

TOGGLE - this changes the state of a relay to on if its off and off if its on

STATUS - this returns that state of the relay. 1 if on and 0 if off

KEEP_LED_ON - sets the timer and the relay on for 31 seconds



### Usage

main.py [function_name] [relay_number]

Example: 

main.py TOGGLE 1

returns the output of the function including a success/fail indicator 
