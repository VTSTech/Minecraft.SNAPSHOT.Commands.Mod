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

itemsdb="stone,cobblestone,dirt,arrow,torch,planks,cobblestone,coal,wheat,leather,carrot,melon,log,bread,iron_ingot,gold_ingot,chainmail_leggings,chainmail_boots,chainmail_helmet,chainmail_chestplate,bow,leather_helmet,leather_chestplate,leather_leggings,leather_boots,iron_sword,iron_axe,iron_pickaxe,iron_hoe,iron_shovel,diamond,enchanting_table,iron_helmet,iron_chestplate,iron_leggings,iron_boots,golden_helmet,golden_chestplate,golden_leggings,golden_boots,diamond_helmet,diamond_chestplate,diamond_leggings,diamond_boots"
pricedb="1,10,1,2,5,5,10,10,10,15,15,15,20,25,100,250,100,100,100,100,100,75,120,105,60,200,750,750,200,100,2500,2000,500,800,700,400,1250,2000,1750,1000,12500,20000,17500,10000"

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