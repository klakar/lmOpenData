![GitHub Logo](/lm.png)
#Installation Instructions

Use QGIS official python plugin manager, or...

Use files from _Master_ or Stable Release (https://github.com/klakar/lmOpenData/releases/latest)

Download and unzip in your QGIS plugins folder...

Change the folder name from "LmOpenData-xxxx" to just "LmOpenData".

#####IMPORTANT: 
You will need a personal Swedish National Land Survey Token to use the plugin.

Register (free) at: https://opendata.lantmateriet.se/#register

Activate the plug-in and add layer from "Web" menu.

#####License
Layers are licensed with CC-BY "Lantmäteriet".
Plugin is published under GPL2 license (same as QGIS).

####Change log:
Version|Change
-------|------
0.4|Update for QGIS 2.99/3.0
0.3.3|Bug fix for initial python error about "incompatible types"
0.3.2|Bug fix and added CC-BY Lantmäteriet license text.
0.3.1|Translation Fix.
0.3|Remade Plugin to require personal token and registration.
0.2.2|Changed to new token based API (My own token for now)
0.2.1|Added some links to this repository
0.2|Minor update
0.1|First version (local)

###Problem solving
If you get a "Broken Plug-In" message you probably did not remove the "-master" part from the folder name. (Python sometimes don't like "-" )

Sometimes you need to add the token more than once. To avoid this you can add a second map layer the first time after you add the token.
