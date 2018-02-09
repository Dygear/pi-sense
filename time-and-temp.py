#!/usr/bin/python

from time import sleep, gmtime, strftime
from sense_hat import SenseHat
import subprocess

# Expects a floating point value in F.
def C(T):
    return (5.0 / 9.0) * (T - 32)

# Expects a floating point value in C.
def F(T):
    return (9.0 / 5.0) * T + 32

# Expects a floating point value in C.
def calibrated(temp_env):
    temp_cpu = float(subprocess.check_output("vcgencmd measure_temp", shell=True).split("=")[1].split("'")[0])
    return temp_env - ((temp_cpu - temp_env) / 5.466)

sense = SenseHat()
gammaProfile = [i for i in range(32)]
sense.gamma = gammaProfile
sense.set_rotation(180)
sense.low_light = True

while True:
    sense.show_message('%s'     %(strftime("%H:%M:%S")),        0.1, [8, 8, 8])
    sense.show_message('%dF'    %(F(calibrated(sense.temp))),   0.1, [8, 0, 0])
    sense.show_message('%dmbar' %(sense.pressure),              0.1, [0, 8, 0])
    sense.show_message('%d%%'   %(sense.humidity),              0.1, [0, 0, 8])
    sleep(1)
    sense.clear()
