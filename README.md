RPiMplayer
==========

Make your smart phone a remote controller for playing media files on RaspberryPi.

####Overview####
The [ReaspberryPi](http://www.raspberrypi.org/) has a local server running which is triggered by the script. It serves static html pages having buttons which on click sends the command back to the server.
To run server and receive commands, the app uses [Bottle.py](http://bottlepy.org/). Don't be deceived by the repo name, the app is compatible with CMUS Music player and not Mplayer. Slight modification shall allow the latter too.

####Getting Started####
1. [Turn your RaspberryPi into Wireless Access Point](http://raspberrypihq.com/how-to-turn-a-raspberry-pi-into-a-wifi-router/).
2. [Install Bottle](http://bottlepy.org/docs/dev/tutorial.html) on RPi OS, probably Raspbian.
3. [Install CMUS](https://cmus.github.io/) and set up playlist.
4. Run news.py script in terminal.
4. Make sure RPi's Hotspot is running. Connect your smart phone.
5. Open "<Your-Rpi-Ip>:5000" in a browser.
Enjoy Music! ...and control from anywhere in your home.

####Contribution####
Want to contribute to the still-naive project? First go throught the Getting Started section and start coding! Submit pull requests and I'll be happy to merge them.
