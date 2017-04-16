# Minecraft SNAPSHOT .commands script v0.55

Written by YT_Veritas0923             

Twitter: @Veritas_83                  

Web: www.NigelTodman.com              

GitHub: Veritas83                     

BTC 18j2Env7QokhGG5MccS3LPBKnjsko6u4NQ

<img src="https://i.gyazo.com/a61907ee29455e53eee6b08f386dc7f0.png">


Simply place beside your minecraft_server.jar and run.

<img src="https://i.gyazo.com/fa6774c428f7a276047616098109a04d.png">

Config:

specify admin player name in config. add mods to mods.csv, 1 player name per line.

<pre>
Lines 48-58:

## Start Config ##
javacmd = 'java -Xms2G -Xmx2G -jar minecraft_server.jar nogui' # Java command line to start Minecraft Server jar, Must use nogui
spawn = "0 64 -3"   																					 # WorldSpawn Coordinates
rtpradius = 35000  																						 # Random Teleport radius (-35000,35000)
useautosave = True 																						 # Use Autosave?
useautoclear = True 																					 # Use Autoclear?
autosaveint = 1776																					   # Autosave Interval in seconds
autoclearint = 3625																					   # Autoclear Interval in seconds
freeshulkerbox = True																					 # Gives new players a shulker box on their first connect
motd = "!## MOTD ##! Welcome to mc.nigeltodman.com, PLAYER_NAME! See our custom commands and their usage with '.help' * April Gamerules: limitedCrafting:Off keepInventory:On mobGriefing:Off Difficulty:Hard"
votemsg = "Vote for this server! Vote #1 adf.ly/1kVCJK #2 adf.ly/1kVCLs #3 adf.ly/1g4VYV"
admin="YT_Veritas0923"
																					   									 # Message of the Day notes:
																					   									 # PLAYER_NAME is replaced with connecting player.
## End Config   ##												   									 # 'Welcome to' is replaced by 'Welcome back to' for returning players.

Shop Config, Lines 30,33

itemsdb="arrow,torch,coal,iron_ingot,gold_ingot,chainmail_leggings,chainmail_boots,chainmail_helmet,chainmail_chestplate,bow,iron_sword,iron_shovel,iron_pickaxe,iron_hoe,diamond,enchanting_table"
pricedb="2,5,10,25,50,100,100,100,100,100,250,250,250,250,5000,2000"
</pre>

User Commands:

.spawn

.sethome

.home

.rtp

.warp

.whois

.ping

.report

.shop

.buy

.sell

.seen

.stats

.staff

.tpa

.tpaccept

.tpdeny

.vote

.uptime

.help

.about

.commands

Mod Commands:

.setwarp

.kick