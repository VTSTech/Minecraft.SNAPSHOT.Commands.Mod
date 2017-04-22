# Minecraft SNAPSHOT .essentials script v0.6-r49

Written by YT_Veritas0923             

Twitter: @Veritas_83                  

Web: www.NigelTodman.com              

GitHub: Veritas83                     

BTC 18j2Env7QokhGG5MccS3LPBKnjsko6u4NQ

<img src="https://i.gyazo.com/7c1f3994dcaa10fc1bd68fe458afa8dc.png">


Simply place beside your minecraft_server.jar and run.

<img src="https://i.gyazo.com/2305feb592e1b2a4237f40e65e2442a1.png">

Config:

specify admin player name in config. add mods to mods.csv, 1 player name per line.

<pre>
Lines 122-142:

## Start Config ##
javacmd = 'java -Xms128M -Xmx4G -jar minecraft_server.jar nogui' # Java command line to start Minecraft Server jar, Must use nogui
spawn = "-82 64 264"   																					 # WorldSpawn Coordinates
rtpradius = 35000	  																						 # Random Teleport radius (-35000,35000)
useautosave = True	 																						 # Use Autosave?
useautoclear = True 																						 # Use Autoclear?
usemoney = False																								 # Use Money?
usewarp = True			 																						 # Allow .warp?
usehome = True			 																						 # Allow .home/.sethome?
usertp = True				 																						 # Allow .rtp?
useshop = False			 																						 # Allow .shop/.buy/.sell?
usespawn = True			 																						 # Allow .spawn?
autosaveint = 1776																						   # Autosave Interval in seconds
autoclearint = 3625																						   # Autoclear Interval in seconds
freeshulkerbox = False																					 # Gives new players a shulker box on their first connect
motd = "!## MOTD ##! Welcome to mc.nigeltodman.com, PLAYER_NAME! See our custom commands and their usage with '.help' * April Gamerules: limitedCrafting:Off keepInventory:On mobGriefing:Off Difficulty:Hard"
votemsg = "Vote for this server! Vote #1 adf.ly/1kVCJK #2 adf.ly/1kVCLs #3 adf.ly/1g4VYV #4 adf.ly/1mCgLU #5 adf.ly/1mCgcL #6 adf.ly/1mCgoa"
admin="YT_Veritas0923"
																						   									 # Message of the Day notes:
																						   									 # PLAYER_NAME is replaced with connecting player.
## End Config   ##												  	 									 # 'Welcome to' is replaced by 'Welcome back to' for returning players.

Shop Config, Lines 96,99

itemsdb=""stone,cobblestone,dirt,arrow,wheat_seeds,cookie,torch,planks,potato,cobblestone,coal,wheat,glass,carrot,melon,chicken,fireworks,leather,cooked_fish,log2,log,bread,glowstone,bookshelf,emerald,hay_block,melon_block,ender_pearl,purple_shulker_box,lime_shulker_box,ender_chest,iron_ingot,gold_ingot,chainmail_leggings,chainmail_boots,chainmail_helmet,chainmail_chestplate,bow,leather_helmet,leather_chestplate,leather_leggings,leather_boots,iron_sword,iron_axe,iron_pickaxe,iron_hoe,iron_shovel,diamond,enchanting_table,iron_helmet,iron_chestplate,iron_leggings,iron_boots,golden_helmet,golden_chestplate,golden_leggings,golden_boots,diamond_helmet,diamond_chestplate,diamond_leggings,diamond_boots"
pricedb="1,15,1,2,4,5,5,5,8,10,10,10,15,15,15,25,25,25,25,25,25,25,50,50,100,125,135,1000,10000,12000,25000,250,500,100,100,100,100,100,125,200,175,100,500,750,750,500,250,2500,5000,500,800,700,400,2500,4000,3500,2000,12500,20000,17500,10000"

</pre>

User Commands:

.about
.buy
.commands
.essentials
.help
.home
.motd
.ping
.ranks
.rankup
.report
.rtp
.seen
.sell
.sethome
.shop
.spawn
.staff
.stats
.tpa
.tpaccept
.tpdeny
.uptime
.version
.vote
.warp
.whois

Mod Commands:

.console
.kick
.setwarp