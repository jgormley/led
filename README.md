# led
Weekend project to use a raspberry pi I've had sitting around.  

Goal: create a DIY LED light strip similar to nanoleaf.

Status:
* Basic python script (led_utils.py) created for running a few different visuals on the LEDs (flag, spiral, diagonal, and clear)
* Node/Express server running locally with a basic UI for activating the Python script
  * POST to / with body of {command:'COMMAND_HERE'}
* DuckDNS dynamic DNS configured
* Port forwarding on router

TODO:
* Connect smart home to the Express/Node server -- either via IFTTT or Google local or some other method (maybe Zapier)
* Clean up JS code, I hacked in a global variable to track whether a script was running.  I could either switch to sync calls, or be more elegant about handling state.  I did this because calling the python script multiple times puts it in a bad state and requires me to kill the processes
* Add ability to pass in params to the python script
* Add more visuals
* build a case
* Add better error handling and start/stop scripts for the raspberry pi
* Add a password for triggering commands via the Express/Node POST endpoint

Parts:
* Raspberry pi
* LED strip
* LED grid
* jumper cables
* power source for LED lights
* Google Home
* Python scripts to control the LED lights
* Express/Nodejs server to receive POST requests to trigger Python scripts (and provide a simple UI)
  * PUG template engine
* Google home developer toolkit 
* DuckDNS for Dynamic DNS

Resources
* https://acarril.github.io/posts/ssh-sripts-st3 - editing files remotlely with Sublime
* https://learn.adafruit.com/neopixels-on-raspberry-pi - covers wiring diagram and control of LED from Python
* https://www.instructables.com/Google-Home-Raspberry-Pi-Power-Strip/ - I used the Node/React portion as reference
* https://medium.com/swlh/run-python-script-from-node-js-and-send-data-to-browser-15677fcf199f - calling python from Node
* http://expressjs.com/en/starter - Express starter tutorial
  * https://pugjs.org/api/getting-started.html - Pug for template engine
* Google local reference
  * https://developers.google.com/assistant/smarthome/concepts/local
  * https://github.com/actions-on-google/smart-home-local - code sample for Google Local
* https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch - I'm new to Fetch, but it seems pretty straightforward
  * https://www.freecodecamp.org/news/a-practical-es6-guide-on-how-to-perform-http-requests-using-the-fetch-api-594c3d91a547/
* https://www.duckdns.org/domains - dynamic DNS
* https://zapier.com/apps/amazon-alexa/integrations/webhook -- alternative to IFTTT
* https://ifttt.com -- if this then that -- now requires paid membership when you have more than 3 applets

Commands
* sudo DEBUG=led:* npm start
  * Run as sudo so that the python script can run as root so it can control the GPIO board
* http://192.168.1.68

Notes
* Had to upgrade node on the raspberry pi, used n 
* IFTTT is free for only 3 scriptlets and I'm struggling to get the first one to work.  It's not passing the json body correctly
