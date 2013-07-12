import sys
import time
from datetime import datetime
import RPi.GPIO as GPIO

"""
Hour bits - Pin: 8, 10, 12, 16, 18
Minutes bits - Pin: 19, 21, 23, 22, 24, 26
Seconds bits - Pin: 3, 5, 7, 11, 13, 15
"""

pin_mapping = {"hour": [8, 10, 12, 16, 18],
               "minute": [19, 21, 23, 22, 24, 26],
               "second": [3, 5, 7, 11, 13, 15]}

def set_all_gpio_out():
    for k in pin_mapping:
        for pin in pin_mapping[k]:
            GPIO.setup(pin, GPIO.OUT)


def turn_off_all_pins():
    for k in pin_mapping:
        for pin in pin_mapping[k]:
            GPIO.output(pin, 0)


def sequential_test():
    for k in ['hour', 'minute', 'second']:
        for pin in pin_mapping[k]:
            GPIO.output(pin, 1)
            time.sleep(1)
            GPIO.output(pin, 0)


def display_time(hour, minute, second):
    binary_strs = dict(
        hour = bin(hour)[2:].rjust(5, '0'),
        minute = bin(minute)[2:].rjust(6, '0'),
        second = bin(second)[2:].rjust(6, '0')
    )

    #print("Time: %i:%i:%i  Binary: %s %s %s" % (hour, minute, second, binary_strs['hour'], binary_strs['minute'], binary_strs['second']))
    turn_off_all_pins()
    for mapping_name, mapping_list in pin_mapping.iteritems():
        for pin in mapping_list:
            idx = mapping_list.index(pin)
            sig = int(binary_strs[mapping_name][idx])
            GPIO.output(pin, sig)


if '__main__' == __name__:
    
    GPIO.setmode(GPIO.BOARD)
    set_all_gpio_out()
    turn_off_all_pins()
    
    if len(sys.argv) > 1 and 'test' == sys.argv[1]:
        sequential_test()
    else:
        try:
            while True:
                d = datetime.now()
                display_time(d.hour, d.minute, d.second)
                time.sleep(1)
        except (KeyboardInterrupt, SystemExit):
            turn_off_all_pins()
            print("Good bye!")
