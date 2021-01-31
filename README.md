# led
Weekend project to use a raspberry pi I've had sitting around.  

Goal: create a DIY LED light strip similar to nanoleaf.

Parts:
* Raspberry pi
* LED strip
* LED grid
* jumper cables
* power source for LED lights
* Google Home

Software:
* Python scripts to control the LED lights
* Nodejs server to receive POST requests and trigger Python scripts
* Google home developer toolkit 

Resources
* https://learn.adafruit.com/neopixels-on-raspberry-pi - covers wiring diagram and control of LED from Python
* https://www.instructables.com/Google-Home-Raspberry-Pi-Power-Strip/ - I used the Node/React portion as reference
* Google local reference
  * https://developers.google.com/assistant/smarthome/concepts/local
  * https://github.com/actions-on-google/smart-home-local - code sample for Google Local