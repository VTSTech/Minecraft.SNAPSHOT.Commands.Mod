# Minecraft SNAPSHOT .essentials script v0.6-r55

Written by YT_Veritas0923             

Twitter: @Veritas_83                  

Web: www.NigelTodman.com              

GitHub: Veritas83                     

BTC 18j2Env7QokhGG5MccS3LPBKnjsko6u4NQ

<img src="https://i.gyazo.com/a1168fecc97d4be34bd900c006a0e2e3.png">


Simply place beside your minecraft_server.jar and run.

<img src="https://i.gyazo.com/19fce9abb82b282af71de902124d3868.png">

Config:

specify admin player name in config. add mods to mods.csv, 1 player name per line.

<pre>
Lines 179-204:

## Start Config ##
javacmd = 'java -Xms128M -Xmx4G -jar minecraft_server.jar nogui' # Java command line to start Minecraft Server jar, Must use nogui
spawn = "0 64 -3"   																						 # WorldSpawn Coordinates
rtpradius = 35000	  																						 # Random Teleport radius (-35000,35000)
useautosave = True	 																						 # Use Autosave?
useautoclear = True 																						 # Use Autoclear?
usemoney = True																									 # Use Money?
usewarp = True			 																						 # Allow .warp?
usehome = True			 																						 # Allow .home/.sethome?
usertp = True				 																						 # Allow .rtp?
useshop = True			 																						 # Allow .shop/.buy/.sell?
usespawn = True			 																						 # Allow .spawn?
autosaveint = 1776																						   # Autosave Interval in seconds
autoclearint = 3625																						   # Autoclear Interval in seconds
basicincomeint = 3600																						 # Basic Income Payout Interval in seconds
basicincomeamt = 1500																						 # Basic Income Payout Amount in Money
freeshulkerbox = True																						 # Gives new players a shulker box on their first connect
giveubi = True																									 # Gives world a Universal Basic Income
givehead = True																									 # Gives new players a likeness of their head on their first connect
motd = "!## MOTD ##! Welcome to mc.nigeltodman.com, PLAYER_NAME! See our custom commands and their usage with '.help' * May Gamerules: limitedCrafting:On keepInventory:Off mobGriefing:On Difficulty:Hard"
votemsg = "Vote for this server! Vote #1 adf.ly/1kVCJK #2 adf.ly/1kVCLs #3 adf.ly/1g4VYV #4 adf.ly/1mCgLU #5 adf.ly/1mCgcL #6 adf.ly/1mCgoa"
admin="YT_Veritas0923"
																						   									 # Message of the Day notes:
																						   									 # PLAYER_NAME is replaced with connecting player.
## End Config   ##												  	 									 # 'Welcome to' is replaced by 'Welcome back to' for returning players.
# 5m 300, 30m 1800, 1h 3600, 12h 43200, 1d 86400, 1w 604800, 1mo 2419200

Shop Config, Lines 96,99

itemsdb=""stone,cobblestone,dirt,arrow,wheat_seeds,cookie,torch,planks,potato,cobblestone,coal,wheat,glass,carrot,melon,chicken,fireworks,leather,cooked_fish,log2,log,bread,glowstone,bookshelf,emerald,hay_block,melon_block,ender_pearl,purple_shulker_box,lime_shulker_box,ender_chest,iron_ingot,gold_ingot,chainmail_leggings,chainmail_boots,chainmail_helmet,chainmail_chestplate,bow,leather_helmet,leather_chestplate,leather_leggings,leather_boots,iron_sword,iron_axe,iron_pickaxe,iron_hoe,iron_shovel,diamond,enchanting_table,iron_helmet,iron_chestplate,iron_leggings,iron_boots,golden_helmet,golden_chestplate,golden_leggings,golden_boots,diamond_helmet,diamond_chestplate,diamond_leggings,diamond_boots"
pricedb="1,15,1,2,4,5,5,5,8,10,10,10,15,15,15,25,25,25,25,25,25,25,50,50,100,125,135,1000,10000,12000,25000,250,500,100,100,100,100,100,125,200,175,100,500,750,750,500,250,2500,5000,500,800,700,400,2500,4000,3500,2000,12500,20000,17500,10000"

</pre>

User Commands:

.about - display script version and author information

.bal - displays your balance

.balance - alias of .bal

.buy item_name 64 - buys 64 items from the .shop, increase or decrease 64 as needed

.commands - list available commands

.essentials - alias of .about

.help - displays commands and their usage

.home - teleports you to your set home

.version - alias of .about

.motd - displays server Message Of The Day

.ping - causes server to reply with ping response time in ms

.ranks - Displays Ranks, Their cost and their money drop multiplier.

.rankup - Increases your rank by 1. See cost use .rank

.report player reason - reports player for specified reason

.reset - resets your money to 100

.rtp - teleports you to a random location

.seen player - displays when player was last seen online

.sell item_name 1 - sells 1 item to the .shop, increase or decrease 1 as needed

.sethome - sets .home to current coordinates

.shop - lists items for sale, use .buy to purchase

.spawn - teleports you to spawn

.staff - list server staff

.stats - displays total players in PlayerDB and server uptime

.tdf - Toggles downfall

.tpa player - sends .tpa request to specified player

.tpaccept - Accepts .tpa request. Teleports player to you.

.tpdeny - Denies .tpa request.

.tpyes - alias of .tpaccept

.tpno - alias of .tpdeny

.uptime - displays server uptime

.vote - displays server vote links

.warp name - teleports you to warp name. List warps with just .warp

.whois player - checks if player has played on this server

Mod Commands:

.console command - runs /command on the server as console

.kick player reason - kicks a player, reason is optional. reason cannot contain spaces (use . instead of space)

.setwarp name - sets a public .warp as given name. name cannot contain spaces

.stop - issues /stop command as console.
