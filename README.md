# Minecraft SNAPSHOT .commands script v0.47

Written by YT_Veritas0923             

Twitter: @Veritas_83                  

Web: www.NigelTodman.com              

GitHub: Veritas83                     

BTC 18j2Env7QokhGG5MccS3LPBKnjsko6u4NQ

<img src="https://i.gyazo.com/4c71c3bbc11758a3ff00181d4b43dc8b.png">


Simply place beside your minecraft_server.jar and run.

<img src="https://i.gyazo.com/541e4b9594d87a0c81d3b13ba33103ce.png">

Config:
<pre>
Lines 30-38:

javacmd = 'java -Xms2G -Xmx2G -jar minecraft_server.jar nogui' # Java command line to start Minecraft Server jar, Must use nogui
spawn = "0 64 -3"  																						 # WorldSpawn Coordinates
rtpradius = 35000  																						 # Random Teleport radius (-35000,35000)
useautosave = True 																						 # Use Autosave?
useautoclear = True 																					 # Use Autoclear?
autosaveint = 1776																					   # Autosave Interval in seconds
autoclearint = 3625																					   # Autoclear Interval in seconds
freeshulkerbox = True																					 # Gives new players a shulker box on their first connect
motd = "!## MOTD ##! Welcome to mc.nigeltodman.com, PLAYER_NAME! See our custom commands and their usage with '.help' * March Gamerules: keepInventory:Off mobGriefing:On Difficulty:Hard"
																					   									 # Message of the Day notes:
																					   									 # PLAYER_NAME is replaced with connecting player.
## End Config   ##												   									 # 'Welcome to' is replaced by 'Welcome back to' for returning players.
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
