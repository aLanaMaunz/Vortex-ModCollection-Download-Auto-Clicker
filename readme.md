Fork of a Chat-GPD(?) script to automate the download process of vortex collections as a non-premium user. Added some QoL and improvements to the script. I know nothing about phyton, but it works pretty well? Downloaded 1200 mods without any major problems. (There are still "custom" popups which require manual interaction, but they are really rare.)

Usage:
- (Download and install Phython + dependencies. HINT: You can skip this if you use the precompiled exe release in case you don't want/have a Phyton installation.)
- Download and extract everything from the latest release (yes, the pictures too).
- Move everything into the same folder and start the .py script or the .exe.
- Open vortex and start installing a mod collection.
- Move the vortex window to your main screen.
- Wait until a browser window opens and move it to the main screen too.
- Go AFK and wait until everything is done.

Known problems:
- Looks like the script can't find windows on other monitors, make sure the browser always opens/stays on your main screen. Usage on multiple monitor setups can be a pain.
- Not working in background, only things like "light browsing" or watching a video on a 2nd screen is possible.
- No 100% afk solution, thanks to all the custom mod popups and configurations. (still saves A LOT of time and mentalhealth.)

Dependencies:

pip install pyautogui

pip install opencv-python

Note:

.exe packed with pyinstaller -F yourprogram.py on a Windows 11 Pro setup.
