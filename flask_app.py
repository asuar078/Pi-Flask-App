'''
FILE NAME
app.py
Version 1
1. WHAT IT DOES
Implements the first version of the project's Flask application.
This version contains a single page that reports current temperature and humidity.
2. REQUIRES
* Any Raspberry Pi
3. ORIGINAL WORK
Raspberry Full Stack 2015, Peter Dalmaris
4. HARDWARE
* Any Raspberry Pi
* DHT11 or 22
* 10KOhm resistor
* Breadboard
* Wires
5. SOFTWARE
Command line terminal
Simple text editor
Libraries:
from flask import Flask, request, render_template
6. WARNING!
None
7. CREATED 
8. TYPICAL OUTPUT
A simple web page served by this flask application in the user's browser.
The page contains the current temperature and humidity.
 // 9. COMMENTS
 i have dht11 on pin27
--
 // 10. END
'''

from flask import Flask, request, render_template
app = Flask(__name__)
app.debug = True # Make this False if you are no longer debugging

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/temp")
def temp():
        import sys
        import Adafruit_DHT
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 27)
        if humidity is not None and temperature is not None:
                return render_template("temp.html",temp=temperature,hum=humidity)
        else:
                return render_template("no_sensor.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
