# Church-Carillon-Bells
Automatic church bells program, created to replace archaic Maas-Rowe Carillon Bells machine. Runs in Python, and plays Westminster Chimes &amp; Hymns as defined by the user.

#Requirements
Requires Python 3. I run Python 3.11.3 currently.
Requires `argparse`, `datetime`, and `pathlib`, `schedule` and `playsound`.

#Setup
`carillonbells.py` is the application prgram. It will be looking for __uppercase__ .WAV files in the "Tolls" and "Hymns" folder. I have not created every Westminster Chime, as I only need it to run a few times per day, but the Tolls folder contains Westminster Chimes. The Hymns folder contains short Weslyan hymns on bells, which the program is currently set to play every day at noon, after the 12 Westminster chimes. There is also a folder for Christmas Hymns, but the program must be modified to look for __lowercase__ .wav files if you use that folder, as I exported them differently.

# Usage
To use, simply launch the Python script in Command Prompt or Terminal.

> python3 carillonbells.py

It will print that the program is launched and that the chimes are scheduled. Each time it plays a chime, it will print that it completed the chime at the current time, on the current date. This way you can keep a log of when the chimes played and if they worked or didn't work.

To change the times that the chimes play, you will need to edit the Python script. It's decently straight-forward.

__Currently, the script is set to skip the 9:00 AM chime on Sunday mornings, so be aware of that.__

# License
This was made for my church and all the hymn songs were recorded by the church's organist. I am releasing all this as GPL 3.0 License. If you fork this or edit it, please credit me. However, it is __Free to use__ forever! I hope this will help you in your ministry.

# Why?
Real bells in bell towers are often a thing of the past for many churches. Mine included. The church installed loud-speakers on the top of the bell-tower in the 1980s, and purchased a ~ $50,000 music machine to play bell sounds. It broke, however, and it's prohibitably expensive to repair. Thus it sat, playing no bells for about 20 years. That's where I come in. I hook a 100W Amplifier to the cable that runs to the loudspeakers, I hook a Mac Mini to the amp, I write this program (with help from @le717), and wham, we have free carillon bells (sans the cost of the computer, but I found all this equipment at church just lying around, so technically for me this progject was completely free!). And now I want to share this with YOU. :) 


![vlcsnap-2023-03-06-14h13m14s570](https://github.com/rioforce/Church-Carillon-Bells/assets/3674297/de4ec473-d5c9-4474-a675-ce3bd96437a5)

![DSC03929](https://github.com/rioforce/Church-Carillon-Bells/assets/3674297/4ec86e70-ad04-40dc-9cb9-8079d295c9b0)

Video of Carillon in action:

https://github.com/rioforce/Church-Carillon-Bells/assets/3674297/0f58ad12-75a1-48ce-b904-e67dd31eb2d8



