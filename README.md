# Minecraft SNAPSHOT .commands script v0.45

Written by YT_Veritas0923             

Twitter: @Veritas_83                  

Web: www.NigelTodman.com              

GitHub: Veritas83                     

BTC 18j2Env7QokhGG5MccS3LPBKnjsko6u4NQ

<img src="https://i.gyazo.com/495152aeeeeadccd2fb569767265b525.png">


Simply place beside your minecraft_server.jar and run.

<img src="https://i.gyazo.com/fd1652e942ea9edb4731459f3f35994b.png">

Config:
<pre>
Lines 30-37:

javacmd = 'java -Xms2G -Xmx2G -jar minecraft_server.jar nogui' # Java command line to start Minecraft Server jar, Must use nogui
spawn = "0 64 -3"  																						 # WorldSpawn Coordinates
rtpradius = 35000  																						 # Random Teleport radius (-35000,35000)
useautosave = True 																						 # Use Autosave?
useautoclear = True 																					 # Use Autoclear?
autosaveint = 1800																					   # Autosave Interval in seconds
autoclearint = 600																					   # Autoclear Interval in seconds
motd = "!##_##! MOTD Welcome to mc.nigeltodman.com, PLAYER_NAME! See our custom commands and their usage with '.help' !##_##! March Gamerules: keepInventory:Off mobGriefing:On Difficulty:Hard !##_##!"
																					   									 # Message of the Day notes:
																					   									 # PLAYER_NAME is replaced with connecting player.
</pre>

Commands:


.spawn

.sethome

.home

.rtp

.setwarp

.warp

.whois

.ping

.seen

.help

.about

.commands
