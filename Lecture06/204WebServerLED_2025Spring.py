#----------------------------------------------------------------
#
#             LED Control from android app
#
#In this program, LED on Rpi5 will be connected through 
#GPIO2, below code work with android app,will turn the LED on/off 
#
#Program:204WebServerLED_2025Spring.py
#Date:04/26/2025
#Author: X.Tang
#Version: 1.0  Initial
#  1.1  Add ...
#-----------------------------------------------------------------

from flask import Flask, render_template
from gpiozero import LED

app = Flask(__name__)

led = LED(2)

#
#start the main program loop, read command from android app
#through local web server, decode the msg and control LED
#

@app.route("/<device>/<action>")

def action(device, action):
    actuator = LED
    if action == 'on':
        led.on()
    if action == 'off':
        led.off()
    return ""

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0', use_reloader=False)
