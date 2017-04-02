# Minecraft SNAPSHOT .commands script v0.51

Written by YT_Veritas0923             

Twitter: @Veritas_83                  

Web: www.NigelTodman.com              

GitHub: Veritas83                     

BTC 18j2Env7QokhGG5MccS3LPBKnjsko6u4NQ

<img src="https://i.gyazo.com/17fad92894b25fb4aa149758894a5757.png">


Simply place beside your minecraft_server.jar and run.

<img src="https://i.gyazo.com/976bc0028d833cd6661a5cd659678177.png">

Config:
<pre>
Lines 29-42:

## Start Config ##
javacmd = 'java -Xms2G -Xmx2G -jar minecraft_server.jar nogui' # Java command line to start Minecraft Server jar, Must use nogui
spawn = "0 64 -3"  																						 # WorldSpawn Coordinates
rtpradius = 35000  																						 # Random Teleport radius (-35000,35000)
useautosave = True 																						 # Use Autosave?
useautoclear = True 																					 # Use Autoclear?
autosaveint = 1776																					   # Autosave Interval in seconds
autoclearint = 3625																					   # Autoclear Interval in seconds
freeshulkerbox = True																					 # Gives new players a shulker box on their first connect
motd = "!## MOTD ##! Welcome to mc.nigeltodman.com, PLAYER_NAME! See our custom commands and their usage with '.help' * April Gamerules: limitedCrafting:Off keepInventory:On mobGriefing:Off Difficulty:Hard"
votemsg = "Vote for this server! Vote #1 adf.ly/1kVCJK #2 adf.ly/1kVCLs #3 adf.ly/1g4VYV"
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

.stats

.vote

.uptime

.help

.about

.commands
