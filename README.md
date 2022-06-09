# Dank Memer Auto Farmer
Dank Memer Auto-farmer is a simple python script that automatically runs the following commands for you:

* Pls beg
* Pls hunt
* Pls fish
* Pls dig
* Pls postmemes
* Pls search

## Prereqisities

* Have Python 3.8.x or higher installed.
* Have the pynput python module installed (install it with `pip install pynput`).
* Have some fishing rods, shovels, laptops in your Dank memer inventory.

## How to run the script
 
 1. Clone the repo: 
 `git clone https://github.com/Smartich0ke/dank-memer-automator.git`
 2. To use the `pls search` command, we first need to get the mouse coordinates so the script can press one of the buttons for the options of where to search. To do this, run the `pls search` command in Discord and hover your mouse over the left-most button in the message from the dank memer bot. You can capture the mouse coordinates by either taking a screenshot on a Mac with CMD+SHIFT+4 which shows the mouse's position next to the cursor or by running `xdotool getmouselocation --shell` on Linux and using ALT+TAB to get over to your terminal without moving the mouse.
 3. Open `main.py` and set the buttonCoords and focusCoords to their appropriate values from step 2.
 4. Open discord and get your channel ready wherer you want to do the farming.
 5. Run the script with `python3 main.py` or hit `F5` in the IDLE
 6. Enjoy! To avoid getting banned, regularly switch between 2-3 alt accounts (about 12 hour intervals)

 If you have any problems, please open an issue in the `issues` tab or email me: nikolaipatricknp@gmail.com

 Pull Requests are welcome.


 

