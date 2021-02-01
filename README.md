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
* https://acarril.github.io/posts/ssh-sripts-st3 - editing files remotlely with Sublime
* https://learn.adafruit.com/neopixels-on-raspberry-pi - covers wiring diagram and control of LED from Python
* https://www.instructables.com/Google-Home-Raspberry-Pi-Power-Strip/ - I used the Node/React portion as reference
* https://medium.com/swlh/run-python-script-from-node-js-and-send-data-to-browser-15677fcf199f - calling python from Node
* http://expressjs.com/en/starter - Express starter tutorial
* Google local reference
  * https://developers.google.com/assistant/smarthome/concepts/local
  * https://github.com/actions-on-google/smart-home-local - code sample for Google Local
* https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch - I'm new to Fetch, but it seems pretty straightforward

Commands
* sudo DEBUG=led:* npm start
  * Run as sudo so that the python script can run as root so it can control the GPIO board
* http://192.168.1.68

Notes
* Had to upgrade node on the raspberry pi, used n 