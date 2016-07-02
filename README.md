![GitHub Logo](/lm.png)
#Installation Instructions

Use QGIS official python plugin manager, or...

Use files from _Master_ or Stable Release (https://github.com/klakar/lmOpenData/releases/latest)

Download and unzip in your QGIS plugins folder...

Change the folder name from "LmOpenData-master" to just "LmOpenData".

#####IMPORTANT: 
You will need a personal Swedish National Land Survey Token to use the plugin.

Register at: https://opendata.lantmateriet.se/#apis

Activate the plug-in and add layer from "Web" menu.

####Change log:
Version|Change
-------|------
0.3|Remade Plugin to require personal token and registration.
0.2.2|Changed to new token based API (My own token for now)
0.2.1|Added some links to this repository
0.2|Minor update
0.1|First version (local)

###Problem solving
If you get a "Broken Plug-In" message you probably did not remove the "-master" part from the folder name. (Python sometimes don't like "-" )
