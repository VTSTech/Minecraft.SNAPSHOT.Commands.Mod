import subprocess, string, csv, time, logging, threading, random, datetime
from subprocess import Popen, PIPE
from time import sleep
from nbstreamreader import NonBlockingStreamReader as NBSR
#nbstreamreader.py https://gist.github.com/EyalAr/7915597

ver = "Minecraft SNAPSHOT .essentials script v0.6-r56"
bannershown = False

def banner():
	banner = "##################################################\n# " + ver + " #\n"
	banner += "# Written by YT_Veritas0923                      #\n# Twitter: @Veritas_83                           #\n"
	banner += "# Web: www.NigelTodman.com                       #\n# GitHub: Veritas83                              #\n"
	banner += "# BTC 18j2Env7QokhGG5MccS3LPBKnjsko6u4NQ         #\n##################################################\n"
	bannershown = True
	return banner

def get24hrtime():
	return time.strftime("%H",time.localtime()) + ":" + time.strftime("%M",time.localtime())+ ":" + time.strftime("%S",time.localtime())
def getdate():
	derp = string.split(time.strftime("%c",time.localtime()))
	return derp[0]

def getplayername(txt):
		player = string.strip(txt,"<")
		player = string.strip(player,">")	
		return player

#Give Looting III Enchantment Book:
#give @p minecraft:enchanted_book 1 0 {StoredEnchantments:[{id:21,lvl:3}]}
#Give Diamond Sword with Looting III Enchantment:
#give @p minecraft:diamond_sword 1 0 {ench:[{id:21,lvl:3}]}
#Give Night Vision Potion
#give @p potion 1 0 {Potion:night_vision}
#Give Regeneration Potion
#give @p potion 1 0 {Potion:regeneration}
#Give Swiftness Potion
#give @p potion 1 0 {Potion:swiftness}
#Give Healing Potion
#give @p potion 1 0 {Potion:healing}

#Enchantment IDs
#0=protection
#1=Fire protection
#2=feather falling
#3=blast protection
#4=projectile protection
#5=respiration
#6=aqua affinity
#7=thorns
#34=unbreaking
#16=sharpness
#17=smite
#18=bane of athropods
#19=knockback
#20=fire aspect
#21=looting
#34=unbreaking
#32=efficiency
#33=silk touch
#34=unbreaking
#35=fortune
#48=power
#49=punch
#50=flame
#51=infinity

#Potion IDs
#1-Speed
#2-Slowness
#3-Haste
#4-Mining Fatigue
#5-Strength
#6-Instant Health
#7-Instant Damage
#8-Jump Boost
#9-Nausea
#10-Regeneration
#11-Resistance
#12-Fire Resistance
#13-Water Breathing
#14-Invisibility
#15-Blindness
#16-Night Vision
#17-Hunger
#18-Weakness
#19-Poison
#20-Wither
#21-Health Boost
#22-Absorbsion
#23-Saturation
#24-Glowing
#25-Levitation

def LoadItems():
	itemsdb="stone,dirt,egg,arrow,wheat_seeds,cookie,torch,planks,potato,cobblestone,coal,wheat,reeds,cactus,cobblestone,glass,carrot,melon,string,chicken,fireworks,leather,cooked_fish,log2,log,bread,glowstone,bookshelf,bone,rotten_flesh,emerald,hay_block,experience_bottle,melon_block,bed,slime_ball,ender_pearl,purple_shulker_box,lime_shulker_box,ender_chest,iron_ingot,gold_ingot,chainmail_leggings,chainmail_boots,chainmail_helmet,chainmail_chestplate,bow,leather_helmet,leather_chestplate,leather_leggings,leather_boots,iron_sword,iron_axe,iron_pickaxe,iron_hoe,iron_shovel,diamond,enchanting_table,iron_helmet,iron_chestplate,iron_leggings,iron_boots,golden_helmet,golden_chestplate,golden_leggings,golden_boots,diamond_helmet,diamond_chestplate,diamond_leggings,diamond_boots"
	return itemsdb
def LoadPrices():
	pricedb="1,1,2,2,4,5,5,5,8,10,10,10,12,12,15,15,15,15,25,25,25,25,25,25,25,25,50,50,100,100,250,125,125,135,500,1000,1000,10000,12000,25000,500,1000,1750,1000,1250,2000,100,125,200,175,100,1000,1500,1500,1000,500,5000,5000,2500,4000,3500,2000,5000,8000,7000,4000,25000,40000,35000,20000"
	return pricedb
def LoadRankItems():
	ritemsdb="0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15"
	return ritemsdb
def LoadRankPrices():
	rpricedb="0,1,100,500,1000,5000,10000,25000,40000,60000,120000,250000,500000,1000000,2000000,4000000"
	return rpricedb

def UpdateSB():
	setsb = "scoreboard objectives setdisplay list rank\n"
	#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
	p.stdin.write(setsb)
	setsb = "scoreboard players set @a killcounter 0\n"
	#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
	p.stdin.write(setsb)
	setsb = "scoreboard players set @a woodcounter 0\n"
	#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
	p.stdin.write(setsb)
	setsb = "scoreboard players set @a stonecounter 0\n"
	#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
	p.stdin.write(setsb)
	setsb = "scoreboard players set @a coalcounter 0\n"
	#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
	p.stdin.write(setsb)
	setsb = "scoreboard players set @a ironcounter 0\n"
	#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
	p.stdin.write(setsb)
	setsb = "scoreboard players set @a goldcounter 0\n"
	#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
	p.stdin.write(setsb)
	setsb = "scoreboard players set @a redstonecounter 0\n"
	#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
	p.stdin.write(setsb)
	setsb = "scoreboard players set @a diamondcounter 0\n"
	#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
	p.stdin.write(setsb)

def ProcessRewards(metric,reward):
	for i in range(1,6):
		setsb = "scoreboard players add @a[score_" + metric + "counter_min=" + str(i) + ",score_rank_min=0,score_rank=3] money " + str(int(round((int(i) * int(reward)) * 1.2))) + "\n"
		#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard players add @a[score_" + metric + "counter_min=" + str(i) + ",score_rank_min=4,score_rank=6] money " + str(int(round((int(i) * int(reward)) * 1.6))) + "\n"
		#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard players add @a[score_" + metric + "counter_min=" + str(i) + ",score_rank_min=7,score_rank=9] money " + str(int(round((int(i) * int(reward)) * 2))) + "\n"
		#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard players add @a[score_" + metric + "counter_min=" + str(i) + ",score_rank_min=10,score_rank=10] money " + str(int(round((int(i) * int(reward)) * 2.4))) + "\n"
		#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard players add @a[score_" + metric + "counter_min=" + str(i) + ",score_rank_min=11,score_rank=11] money " + str(int(round((int(i) * int(reward)) * 2.8))) + "\n"
		#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard players add @a[score_" + metric + "counter_min=" + str(i) + ",score_rank_min=12,score_rank=12] money " + str(int(round((int(i) * int(reward)) * 3.2))) + "\n"
		#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard players add @a[score_" + metric + "counter_min=" + str(i) + ",score_rank_min=13,score_rank=13] money " + str(int(round((int(i) * int(reward)) * 5))) + "\n"
		#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard players add @a[score_" + metric + "counter_min=" + str(i) + ",score_rank_min=14,score_rank=14] money " + str(int(round((int(i) * int(reward)) * 10))) + "\n"
		#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard players add @a[score_" + metric + "counter_min=" + str(i) + ",score_rank_min=15,score_rank=15] money " + str(int(round((int(i) * int(reward)) * 15))) + "\n"
		#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
		p.stdin.write(setsb)

def OverworldCheck():
	setsb = "scoreboard players set @a inOverworld 0\n"
	#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
	p.stdin.write(setsb)
	setsb = "scoreboard players set @a inOverworld 1 {Dimension:0}\n"
	#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
	p.stdin.write(setsb)

#spawn = "-82 64 264" Dev Server coords		(MC.NIGELTODMAN.COM:25599)
#spawn = "0 64 -3"    Snapshot srv coords (MC.NIGELTODMAN.COM:25565)
#spawn = "206 64 259" VNNLA Server coords (VNLLA.NIGELTODMAN.COM:25566)

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
motd = "!## MOTD ##! Welcome to mc.nigeltodman.com, PLAYER_NAME! See our custom commands and their usage with '.help' * May Gamerules: dolimitedCrafting:On keepInventory:Off mobGriefing:On Difficulty:Hard"
votemsg = "Vote for this server! Vote #1 adf.ly/1kVCJK #2 adf.ly/1kVCLs #3 adf.ly/1g4VYV #4 adf.ly/1mCgLU #5 adf.ly/1mCgcL #6 adf.ly/1mCgoa"
admin="YT_Veritas0923"
																						   									 # Message of the Day notes:
																						   									 # PLAYER_NAME is replaced with connecting player.
## End Config   ##												  	 									 # 'Welcome to' is replaced by 'Welcome back to' for returning players.
# 5m 300, 30m 1800, 1h 3600, 12h 43200, 1d 86400, 1w 604800, 1mo 2419200

itemsdb=LoadItems()
pricedb=LoadPrices()
rpricedb=LoadRankPrices()
ritemsdb=LoadRankItems()

cmdline = string.split(javacmd)
p = subprocess.Popen([cmdline[0],cmdline[1],cmdline[2],cmdline[3],cmdline[4],cmdline[5]], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
nbsr = NBSR(p.stdout)
print banner()

currtime = time.time()
starttime = currtime
tpastart = currtime
lasttimesave = currtime
lasttimeclear = currtime
lasttimepoll = currtime
lasttimetpa = currtime
lasttimeubi = currtime
playerisonline = False
playerisseen = False
clearwarn10 = False
clearwarn60 = False
buying=False
selling=False
auction=False
tpasent = False
warplist = False
sethome = False
setwarp = False
tpareq = False
tpyes = False
tpno = True
logged = False
sbset = False
ismod=False
isop=False
getbal=False
tmparray=[]
cmdout = "[" + get24hrtime() + "] [Script thread/IDLE]: There was no output for awhile\n"
strtime= time.clock()
playername=''
warpstr = ''
modstr = ''
reportstr = ''
writestr = ''
reported = ''
tpasource = ''
tpatarget = ''
sellitem=''
sellplayer=''
solditem=''
sellprice=''
soldprice=''
ranknew=''
rankcost=''
derp=''
seen=''
op=''
playercnt = 0
x=0
t=0
i=0
itemsdb=LoadItems()
pricedb=LoadPrices()
while True:
	output = nbsr.readline(0.1)
	# 0.1 secs to let the shell output the result
	if not output:
	    #print '[No more data]'
			derp=True
	    #break
	currtime = time.time()
	line = output
	cmdout = output
	if not cmdout or output == 'None':
		cmdout = "[" + get24hrtime() + "] [Script thread/IDLE]: There was no output for awhile\n"
		tmp = string.split(cmdout)
	else:
		tmp = string.split(cmdout)
		#Filter some output here...
		if len(tmp) > 4:
			if len(tmp) > 7:
				if tmp[6] == "quickly!":
					derp=True
			if tmp[3] == "Set" and tmp[4] == "score":
				derp=True
			elif tmp[3] == "No" and tmp[5] == "score":
				derp=True
			elif tmp[3] == "Set" and tmp[6] == "objective":
				derp=True
			elif tmp[3] == "The" and tmp[4] == "dataTag":
				derp=True
			elif tmp[3] == "Selector":
				derp=True
			elif tmp[3] == "Operation":
				derp=True
			elif tmp[3] == "Horse":
				derp=True
			#if not matching a filter, send output to console (display, not stdin)
			else:
				print line,
	##
	#Timed Functions
	##
	if useautosave == True and ((currtime - lasttimesave) > autosaveint):
		lasttimesave = time.time()
		autosave = "save-all\n"
		print "[" + get24hrtime() + "] [Script thread/EXEC]: " + autosave,
		p.stdin.write(autosave)
		autosave = 'tellraw @a {"text":"World saved. Autosave by ' + ver + '","color":"yellow"}\n'
		print "[" + get24hrtime() + "] [Script thread/EXEC]: " + autosave,
		p.stdin.write(autosave)
	if useautoclear == True and ((currtime - lasttimeclear) > (autoclearint-60)):
		if clearwarn60 == False:
			if ((currtime - lasttimeclear) > (autoclearint-60)):
				autoclear = 'tellraw @a {"text":"Clearing Items in 1 minute!","color":"aqua"}\n'
				clearwarn60 = True
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + autoclear,
				p.stdin.write(autoclear)
		if clearwarn10 == False:
			if ((currtime - lasttimeclear) > (autoclearint-10)):
				autoclear = 'tellraw @a {"text":"Clearing items in 10 seconds!","color":"aqua"}\n'
				clearwarn10 = True
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + autoclear,
				p.stdin.write(autoclear)
	if useautoclear == True and ((currtime - lasttimeclear) > autoclearint):
		lasttimeclear = time.time()
		autoclear = "kill @e[type=Item]\n"
		print "[" + get24hrtime() + "] [Script thread/EXEC]: " + autoclear,
		p.stdin.write(autoclear)
		autoclear = 'tellraw @a {"text":"Items cleared. Autoclear by ' + ver +  '","color":"aqua"}\nlist\n'
		p.stdin.write(autoclear)
		clearwarn60 = False
		clearwarn10 = False
	if giveubi == True and ((currtime - lasttimeubi) > basicincomeint):
		lasttimeubi = time.time()
		basicincome = "scoreboard players add @a[m=0] money " + str(int(basicincomeamt)) + "\n"
		print "[" + get24hrtime() + "] [Script thread/EXEC]: " + basicincome,
		p.stdin.write(basicincome)
		basicincome = 'tellraw @a {"text":"Basic Income Payments issued. Thanks for playing!","color":"green"}\nlist\n'
		print "[" + get24hrtime() + "] [Script thread/EXEC]: " + basicincome,
		p.stdin.write(basicincome)
	#Setup Scoreboard
	if sbset == False:
		setsb = "scoreboard objectives add inOverworld dummy\n"
		print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
		p.stdin.write(setsb)
		if usemoney == True:
			setsb = "scoreboard objectives add Character dummy\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add Info dummy\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add totalkills stat.mobKills Kills\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add killcounter stat.mobKills\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add woodcounter stat.mineBlock.minecraft.log\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add stonecounter stat.mineBlock.minecraft.stone\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add coalcounter stat.mineBlock.minecraft.coal_ore\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add ironcounter stat.mineBlock.minecraft.iron_ore\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add goldcounter stat.mineBlock.minecraft.gold_ore\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add redstonecounter stat.mineBlock.minecraft.redstone_ore\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add diamondcounter stat.mineBlock.minecraft.diamond_ore\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add wood stat.mineBlock.minecraft.log Wood\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add stone stat.mineBlock.minecraft.stone\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add coal stat.mineBlock.minecraft.coal_ore\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add iron stat.mineBlock.minecraft.iron_ore\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add gold stat.mineBlock.minecraft.gold_ore\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add redstone stat.mineBlock.minecraft.redstone_ore\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add diamond stat.mineBlock.minecraft.diamond_ore\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add woodcounter stat.mineBlock.minecraft.log\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add rank dummy Rank\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives add money dummy Money\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard objectives setdisplay list rank\n"
			print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard players set @a killcounter 0\n"
			#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard players set @a woodcounter 0\n"
			#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard players set @a stonecounter 0\n"
			#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard players set @a coalcounter 0\n"
			#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard players set @a ironcounter 0\n"
			#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard players set @a goldcounter 0\n"
			#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard players set @a redstonecounter 0\n"
			#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard players set @a diamondcounter 0\n"
			#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
		sbset = True
	#6s Poll time
	if sbset == True and currtime - lasttimepoll > 6:
		lasttimepoll = time.time()
		if usemoney == True:
			tasks = ['kill','wood','stone','coal','iron','gold','redstone','diamond']
			reward = [10,5,1,8,16,32,10,64]
			for t in range(0,len(tasks)):
				a=ProcessRewards(tasks[t],reward[t])
		a=UpdateSB()
		a=OverworldCheck()
	##
	#User .commands
	##
	if len(tmp) > 4:
		player = getplayername(tmp[3])
		if tmp[4] == '.spawn' and usespawn == True:
			player = getplayername(tmp[3])
			cmdin = "tp @p[name=" + player + ",score_inOverworld_min=1] " + spawn + "\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.sethome' and usehome == True:
			player = getplayername(tmp[3])
			cmdin = "tp " + player + " ~ ~ ~\n"
			sethome = True			
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.home' and usehome == True:
			player = getplayername(tmp[3])
			with open('homes.csv','rb') as csvfile:
				homes = csv.reader(csvfile,delimiter=',',dialect='excel')
				for row in homes:
					h = ','.join(row)
					ht = string.split(h,',')
					if ht[0] == player:
						cmdin = "tp @p[name=" + player + ",score_inOverworld_min=1] " + str(ht[1]) + " " + str(ht[2]) + " " + str(ht[3]) + "\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
		if tmp[4] == '.commands':
			player = getplayername(tmp[3])
			cmdin = 'tellraw ' + player + ' {"text":"User Commands are: .about .bal .balance .buy .commands .essentials .help .home .motd .pay .ping .ranks .rankup .report .reset .rtp .seen .sell .sethome .shop .spawn .staff .stats .tdf .tpa .tpaccept .tpdeny .tpyes .tpno .uptime .version .vote .warp .whois Mod Commands are: .console .kick .setwarp .stop","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.about' or tmp[4] == '.version' or tmp[4] == '.essentials':
			player = getplayername(tmp[3])
			cmdin = 'tellraw @a {"text":"' + ver + ' -- Written by YT_Veritas0923 (GitHub: Veritas83 Twitter: @Veritas_83)","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.vote':
			player = getplayername(tmp[3])
			cmdin = 'tellraw @a {"text":"' + votemsg + '","color":"yellow"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.uptime':
			player = getplayername(tmp[3])
			minutes, seconds = divmod(time.clock(), 60)
			hours, minutes = divmod(minutes, 60)
			days, hours = divmod(hours, 24)
			months, days = divmod(days, 30)
			strtime = str(round(days)) + " days " + str(round(hours)) + " hours " + str(round(minutes)) + " minutes " + str(round(seconds)) + " seconds"
			cmdin = 'tellraw @a {"text":"Server Uptime: ' + strtime + '","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.ping':
			player = getplayername(tmp[3])
			pingreply = []
			tmparray4 = []
			msreply = ''
			with open('online.csv','rb') as csvfile:
				online = csv.reader(csvfile,delimiter=',',dialect='excel')
				for row in online:
					db = ','.join(row)
					dbt = string.split(db,',')
					if dbt[0] == player:
						host = dbt[1]
						ping = subprocess.Popen(
						    ["ping", "-n", "1", "-l", "2", "-w", "4000", host],
						    stdout = subprocess.PIPE,
						    stderr = subprocess.PIPE
						)
						out, error = ping.communicate()
						pingreply = string.split(out,"\n")
						for t in xrange(0,len(pingreply)):
							if pingreply[t][0:5] == "Reply":
								tmparray4 = string.split(pingreply[t]," ")
								msreply = tmparray4[4][5:]
								cmdin = 'tellraw @a {"text":"' + player + ' Ping: ' + msreply + '","color":"aqua"}\n'
								print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
								p.stdin.write(cmdin)
							elif pingreply[t][0:7] == "Request":
								cmdin = 'tellraw @a {"text":"' + player + ' Ping: Timeout or ping blocked. Make sure your network does not discard ping!","color":"aqua"}\n'
								print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
								p.stdin.write(cmdin)
		if tmp[4] == '.seen' and len(tmp) == 6:
			player = getplayername(tmp[3])
			seen = tmp[5]
			playerisonline=False
			playerisseen=False
			#Open online list, Read it, Inform if player is online
			with open('online.csv','rb') as csvfile:
				online = csv.reader(csvfile,delimiter=',',dialect='excel')
				for row in online:
					o = ','.join(row)
					ot = string.split(o,',')
					if ot[0] == seen:
						playerisonline = True
						playerisseen = True
					else:
						derp=True
			if playerisonline == True:
				cmdin = 'tellraw @a {"text":"Look harder! Player is online right now!","color":"aqua"}\n'
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
				p.stdin.write(cmdin)
			else:
				with open('playerdb.csv','rb') as csvfile:
					playerdb = csv.reader(csvfile,delimiter=',',dialect='excel')
					for row in playerdb:
						db = ', '.join(row)
						dbt = string.split(db,', ')
						if dbt[0] == seen:
							playerisseen = True
							minutes, seconds = divmod(round((time.time() - float(dbt[4]))), 60)
							hours, minutes = divmod(minutes, 60)
							days, hours = divmod(hours, 24)
							months, days = divmod(days, 30)
							strtime = str(round(days)) + " days " + str(round(hours)) + " hours " + str(round(minutes)) + " minutes " + str(round(seconds)) + " seconds"
							cmdin = 'tellraw @a {"text":"Player: ' + seen + ' was last online ' + strtime + ' ago","color":"aqua"}\n'
							print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
							p.stdin.write(cmdin)
					if playerisseen == False:
							cmdin = 'tellraw @a {"text":"Player: ' + seen + ' has not been seen","color":"aqua"}\n'
							print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
							p.stdin.write(cmdin)
		if tmp[4] == '.help':
			player = getplayername(tmp[3])
			cmdin = 'tellraw ' + player + ' {"text":"' + ver + ' help\\nspawn - teleports you to spawn\\nsethome - sets .home to current coordinates\\nhome - teleports you to your set home\\nreset - resets your money to 100\\nrtp - teleports you to a random location\\nwarp name - teleports you to warp name. List warps with just .warp\\nwhois player - checks if player has played on this server\\nmotd - displays server Message Of The Day\\nping - causes server to reply with ping response time in ms\\nranks - Displays Ranks, Their cost and their money drop multiplier.\\nrankup - Increases your rank by 1. See cost use .ranks\\nreport player reason - reports player for specified reason\\nreset - resets your money to 100\\nshop - lists items for sale, use .buy to purchase\\nbal - displays your balance\\nbalance - alias of .bal\\nbuy item_name 64 - buys 64 items from the .shop, increase or decrease 64 as needed\\nsell item_name 1 - sells 1 item to the .shop, increase or decrease 1 as needed\\nseen player - displays when player was last seen online\\nstats - displays total players in PlayerDB and server uptime\\ntpa player - sends .tpa request to specified player\\ntpaccept - Accepts .tpa request. Teleports player to you.\\ntpdeny - Denies .tpa request.\\ntpyes - alias of .tpaccept\\ntpno - alias of .tpdeny\\nuptime - displays server uptime\\nvote - displays server vote links\\ncommands - list available commands\\nstaff - list server staff\\nabout - display script version and author information\\nversion - alias of .about\\nessentials - alias of .about\\nhelp - displays commands and their usage","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"setwarp name - sets a public .warp as given name. name cannot contain spaces\\nkick player reason - kicks a player, reason is optional. reason cannot contain spaces (use . instead of space)","color":"red"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.warp' and usewarp == True:
			player = getplayername(tmp[3])
			warpstr = ""
			if len(tmp) > 5:
				warpname = tmp[5]
			else:
				warplist = True
				cmdin = 'tellraw ' + player + ' {"text":"Warp List:","color":"aqua"}\n'
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
				p.stdin.write(cmdin)
			with open('warps.csv','rb') as csvfile:
				warps = csv.reader(csvfile,delimiter=',',dialect='excel')
				for row in warps:
					w = ','.join(row)
					wt = string.split(w,',')
					if warplist == False and wt[0] == warpname:
						cmdin = "tp @p[name=" + player + ",score_inOverworld_min=1] " + str(wt[1]) + " " + str(wt[2]) + " " + str(wt[3]) + "\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
					elif warplist == True:
						warpstr = warpstr + wt[0] + ", "
			if warplist == True:
				cmdin = 'tellraw ' + player + ' {"text":"' + warpstr[:-2] + '","color":"aqua"}\n'
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
				p.stdin.write(cmdin)
			warplist = False
		if tmp[4] == '.rtp' and usertp == True:
			player = getplayername(tmp[3])
			rtpneg = "-" + str(rtpradius)
			rtpneg = int(rtpneg)
			rtppos = int(rtpradius)
			cmdin = "spreadplayers " + str(random.randint(rtpneg,rtppos)) + " " + str(random.randint(rtpneg,rtppos)) + " 1 100 false " + player + "\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.whois':
			with open('playerdb.csv','rb') as csvfile:
				playerdb = csv.reader(csvfile,delimiter=',',dialect='excel')
				oldplayer = False
				for row in playerdb:
					db = ', '.join(row)
					dbt = string.split(db,', ')
					if len(tmp) > 5:
						playername = tmp[5]
						if dbt[0] == playername:
							oldplayer = True
							cmdin = 'tellraw @a {"text":"' + playername + ' playing here since ' + dbt[2] + '","color":"aqua"}\n'
							print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
							p.stdin.write(cmdin)
			if oldplayer == False and len(playername) > 1:		
						cmdin = 'tellraw @a {"text":"' + playername + ' not found.","color":"aqua"}\n'
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
			if len(playername) <=1:
						cmdin = 'tellraw @a {"text":"Proper syntax is .whois player","color":"aqua"}\n'
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
		if tmp[4] == '.stats':
			playercnt = 0
			minutes, seconds = divmod(time.clock(), 60)
			hours, minutes = divmod(minutes, 60)
			days, hours = divmod(hours, 24)
			months, days = divmod(days, 30)
			strtime = str(round(days)) + " days " + str(round(hours)) + " hours " + str(round(minutes)) + " minutes " + str(round(seconds)) + " seconds"
			with open('playerdb.csv','rb') as csvfile:
				playerdb = csv.reader(csvfile,delimiter=',',dialect='excel')
				for row in playerdb:
					playercnt = playercnt + 1
			if playercnt >= 1:		
				cmdin = 'tellraw @a {"text":"Total Players: ' + str(playercnt) + ' Uptime: ' + strtime + '","color":"aqua"}\n'
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
				p.stdin.write(cmdin)
		if tmp[4] == '.staff':
			mods = open('mods.csv','rb')
			modstr = ''
			for line in mods:
				if len(line) > 3:
					modstr = modstr + line[:-2] + " "
			cmdin = 'tellraw @a {"text":"Server Admin: ' + str(admin) + ' Mods: ' + modstr + '","color":"red"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.ranks' and usemoney == True:
			ranks = open('ranks.csv','rb')
			rankstr = ''
			rankstr2 = ''
			for line in ranks:
				if len(line) > 3:
					rankstr = string.split(string.strip(line,"\r\n"),",")
					rankstr2 = rankstr2 + "Rank: " + str(rankstr[0]) + " Cost: " + str(rankstr[1]) + " Bonus: " + str(rankstr[2]) + "\\n"
					#cmdin = 'tellraw @a {"text":"Rank: ' + str(rankstr[0]) + ' Cost: ' + str(rankstr[1]) + ' Bonus: ' + str(rankstr[2]) + '","color":"red"}\n'
			cmdin = 'tellraw @a {"text":"' + rankstr2 + '","color":"red"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.rankup' and usemoney == True:
			player = getplayername(tmp[3])	
			rankcost = LoadRankPrices()
			rankcost = string.split(rankcost,",")
			for i in range(12,0,-1):
				setrank = "scoreboard players add @a[name=" + str(player) + ",score_money_min=" + rankcost[i] + ",score_rank_min=" + str(i-1) +",score_rank=" + str(i-1) + "] rank 1\n"
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + setrank,
				p.stdin.write(setrank)
				setrank = "scoreboard players remove @a[name=" + str(player) + ",score_money_min=" + rankcost[i] + ",score_rank_min=" + str(i) +",score_rank=" + str(i) + "] money " + str(rankcost[i]) + "\n"
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + setrank,
				p.stdin.write(setrank)
			a=UpdateSB()
		if tmp[4] == '.report':
			player = getplayername(tmp[3])
			if len(tmp) > 5:
				reported = tmp[5]
				for i in range(6,len(tmp)):
					reportstr = reportstr + tmp[i] + "."
					i=i+1
				with open('reports.csv','wb') as csvfile:
					tmparray3 = []
					reports = csv.writer(csvfile,delimiter='\n',dialect='excel')
					writestr = player + "," + reported + "," + reportstr + "," + getdate() + "," + get24hrtime()
					reports.writerow([writestr])
				cmdin = 'tellraw @a {"text":"Reporting: ' + str(reported) + ' Reason: ' + reportstr + '","color":"red"}\n'
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
				p.stdin.write(cmdin)
		if tmp[4] == '.tpa':
			player = getplayername(tmp[3])
			tpastart = time.time()
			tpareq = True
			tpyes = False
			tpasent = False
			if len(tmp) > 5:
				tpasource = player
				tpatarget = tmp[5]
				cmdin = 'tellraw @a {"text":"Sending .tpa request to ' + tpatarget + ' from ' + tpasource + ' Type .tpaccept to accept. .tpdeny to deny","color":"red"}\n'
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
				p.stdin.write(cmdin)
		if tmp[4] == '.tpaccept' and player == tpatarget and tpareq == True or tmp[4] == '.tpyes' and player == tpatarget and tpareq == True:
			tpyes = True
			tpno = False
			tpareq = False
			cmdin = 'tellraw @a {"text":"Accepting .tpa request to ' + tpatarget + ' from ' + tpasource + '!","color":"red"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			lasttimetpa = time.time()
			cmdin = "tp " + tpasource + " " + tpatarget + "\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)			
			tpareq = False		
			tpyes = False
			tpasent = False
		if tmp[4] == '.tpdeny' and player == tpatarget and tpareq == True or tmp[4] == '.tpno' and player == tpatarget and tpareq == True:
			tpyes = False
			tpno = True
			tpareq = False
			cmdin = 'tellraw @a {"text":"Denying .tpa request to ' + tpatarget + ' from ' + tpasource + '!","color":"red"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.shop':
			itemsdb=LoadItems()
			pricedb=LoadPrices()
			itemsdb=string.split(itemsdb,",")
			pricedb=string.split(pricedb,",")
			shopstr = ''
			for i in range(0,len(itemsdb)):
				shopstr = "Item: " + itemsdb[i] + " Price: " + pricedb[i]
				cmdin = 'tellraw ' + player + ' {"text":"' + shopstr + '","color":"green"}\n'
				p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"Buy with .buy item_name","color":"green"}\n'
			p.stdin.write(cmdin)
		if tmp[4] == '.buy' and useshop == True:
			buying=True
			itemsdb=LoadItems()
			pricedb=LoadPrices()
			itemsdb=string.split(itemsdb,",")
			pricedb=string.split(pricedb,",")
			player = getplayername(tmp[3])
			for i in range(0,len(itemsdb)):
				if len(tmp) > 6:
					if tmp[5] == itemsdb[i] and tmp[6] == 1:
						buyqty = 1
						totalprice = int(pricedb[i]) * int(buyqty)
						cmdin = "give @p[name=" + player + ",score_money_min=" + pricedb[i]+ "] " + itemsdb[i] + " 1\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
						cmdin = "scoreboard players remove @a[name=" + player + "] money " + pricedb[i]+ "\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
						a=UpdateSB()
						cmdin = 'tellraw @a {"text":"' + player + ' has just bought ' + str(buyqty) + ' '+ itemsdb[i] + ' for $' + str(totalprice) + '","color":"yellow"}\n'
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
					if tmp[5] == itemsdb[i] and tmp[6] > 1:
						buyqty = tmp[6]
						if int(buyqty) > int(1024):
							buyqty = int(1024)
						totalprice = int(pricedb[i]) * int(buyqty)
						cmdin = "give @p[name=" + player + ",score_money_min=" + str(int(totalprice)) + "] " + itemsdb[i] + " " + str(buyqty) + "\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
						cmdin = "scoreboard players remove @a[name=" + player + "] money " + str(int(totalprice)) + "\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
						a=UpdateSB()
						cmdin = 'tellraw @a {"text":"' + player + ' has just bought ' + str(buyqty) + ' '+ itemsdb[i] + ' for $' + str(totalprice) + '","color":"yellow"}\n'
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
			if len(tmp) < 6:
				cmdin = "tell " + player + " .buy requires a quantity! (ie: .buy log 64 or .buy log 1)\n"
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
				p.stdin.write(cmdin)
		if tmp[4] == '.sell' and useshop == True:
			selling=True
			itemsdb=LoadItems()
			pricedb=LoadPrices()
			itemsdb=string.split(itemsdb,",")
			pricedb=string.split(pricedb,",")
			player = getplayername(tmp[3])
			selltime = currtime
			sellplayer = player
			if len(tmp) > 5:
				sellitem = tmp[5]
			for i in range(0,len(itemsdb)):
				if len(tmp) > 6:
					if tmp[5] == itemsdb[i] and int(tmp[6]) == int(1):
						sellprice = str(int(round((int(pricedb[i]) * 0.5))))
						sellqty = 1
						cmdin = "clear @p[name=" + player + "] " + itemsdb[i] + " -1 0\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)					
						a=UpdateSB()
					elif tmp[5] == itemsdb[i] and int(tmp[6]) > int(1):
						sellqty = int(tmp[6])
						if int(sellqty) > int(1024):
							sellqty = int(1024)
						sellprice = str(int(round((int(pricedb[i]) * 0.5))) * int(sellqty))
						cmdin = "clear @p[name=" + player + "] " + itemsdb[i] + " -1 0\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)					
						a=UpdateSB()
			#-> Selling Event
		if tmp[4] == '.motd':
			player = getplayername(tmp[3])
			motd = string.replace(motd, "PLAYER_NAME", player)
			motd = string.replace(motd, "Welcome to ", "Welcome back to ")
			cmdin = 'tellraw @a {"text":"' + motd + '","color":"yellow"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			motd = string.replace(motd, player,"PLAYER_NAME")
			motd = string.replace(motd, "Welcome back to ", "Welcome to ")
			p.stdin.write(cmdin)
		if tmp[4] == '.pay':
			player = getplayername(tmp[3])
			if tmp[6] > 1:
				target = str(tmp[5])
				amount = int(tmp[6])
				cmdin = "scoreboard players remove @a[name=" + player + ",score_money_min=" + str(amount) + "] money " + str(amount) + "\n"
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
				p.stdin.write(cmdin)
				cmdin = "scoreboard players add @a[name=" + target + "] money " + str(amount) + "\n"
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
				p.stdin.write(cmdin)
		if tmp[4] == '.tdf':
			cmdin = "toggledownfall\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw @a {"text":"Toggled Downfall.","color":"blue"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.reset':
			cmdin = "scoreboard players reset " + player + " money\nscoreboard players set " + player + " money 100\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.bal' or tmp[4] == '.balance':
			balplayer = player
			getbal=True
			cmdin = "scoreboard players test @p[name=" + player + "] money -1\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
	##			
	#Mod .commands
	##
		if tmp[4] == '.setwarp':
				isop=False
				ops = open('ops.json','rb')
				player = getplayername(tmp[3])
				for line in ops:
					if line[:13] =='    "name": "':
						#print "Debug: Op Detected as: " + line[13:-3]
						op = line[13:-3]
					if op == player:
						isop=True
				if isop == True:
					player = getplayername(tmp[3])
					cmdin = "tp " + player + " ~ ~ ~\n"
					setwarp = True			
					if len(tmp) >= 5:
						warpname = tmp[5]
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					p.stdin.write(cmdin)
				else:
					cmdin = "say Only ops may .setwarp\n"
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					p.stdin.write(cmdin)
		if tmp[4] == '.console':
				isop=False
				ops = open('ops.json','rb')
				player = getplayername(tmp[3])
				for line in ops:
					if line[:13] =='    "name": "':
						#print "Debug: Op Detected as: " + line[13:-3]
						op = line[13:-3]
					if op == player:
						isop=True
				if isop == True:
					player = getplayername(tmp[3])
					cmdin = ''
					if len(tmp) >= 5:
						for i in range(5,len(tmp)):
							cmdin = cmdin + " " + tmp[i]
					cmdin = cmdin + "\n"					
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					p.stdin.write(cmdin)
				else:
					cmdin = "say Only ops may .console\n"
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					p.stdin.write(cmdin)
		if tmp[4] == '.stop':
				isop=False
				ops = open('ops.json','rb')
				player = getplayername(tmp[3])
				for line in ops:
					if line[:13] =='    "name": "':
						#print "Debug: Op Detected as: " + line[13:-3]
						op = line[13:-3]
					if op == player:
						isop=True
				if isop == True:
					player = getplayername(tmp[3])
					cmdin = "stop\n"					
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					p.stdin.write(cmdin)
				else:
					cmdin = "say Only ops may .stop\n"
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					p.stdin.write(cmdin)
		if tmp[4] == '.kick':
			ismod=False
			mods = open('mods.csv','rb')
			player = getplayername(tmp[3])
			for line in mods:
				if line[:-2] == player:
					ismod=True
			if ismod == True or str(player) == str(admin):
				if len(tmp) > 5:
					pkick = tmp[5]
					cmdin = "kick " + pkick + "\n"
				if len(tmp) > 6:
					pkick = tmp[5]
					kreason = tmp[6]
					cmdin = "kick " + pkick + " " + kreason + "\n"
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
				p.stdin.write(cmdin)
	##
	#Event functions
	##
		#GetBalance Event
		if getbal == True:
			#[16:58:27] [Script thread/EXEC]:  scoreboard players test @p[name=YT_Veritas0923] money -1
			#[16:58:27] [Server thread/INFO]: Score 70500 is in range -1 to 2147483647
			#cmdin = "tell @a DEBUG: Len " + str(len(tmp)) + " tmp3 " + tmp[3] + "\n"
			#p.stdin.write(cmdin)
			if len(tmp) > 10:
				if tmp[3] == "Score" and tmp[6] != "NOT" and int(tmp[10]) == 2147483647:
					playerbal = tmp[4]
					cmdin = 'tellraw ' + balplayer + ' {"text":"Your balance is: $' + str(playerbal) + '","color":"green"}\n'
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					p.stdin.write(cmdin)
				elif tmp[3] == "Score" and tmp[6] == "NOT":
					playerbal = tmp[4]
					cmdin = 'tellraw ' + balplayer + ' {"text":"Your balance is: $' + str(playerbal) + '.Use .reset to go back to +100","color":"green"}\n'
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					p.stdin.write(cmdin)
				getbal = False
		#Selling Event
		if selling == True:
			if tmp[3] == sellplayer and tmp[4] == "has" and tmp[7] != "advancement":
				soldqty = tmp[5]
				soldprice = int(sellprice)
				#print "[" + get24hrtime() + "] [Script thread/DBUG]: " + sellplayer + " " + str(soldqty) + " " + str(sellqty) + " " + str(soldprice) + " " + str(sellprice) + "\n",
				if int(soldqty) < int(sellqty):
					cmdin = "tell " + sellplayer + " You do not hold enough " + sellitem + " to sell!\n"
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					p.stdin.write(cmdin)
					selling=False
					sellplayer=''
					a=UpdateSB()
				if int(soldqty) >= int(sellqty):
					cmdin = "clear @p[name=" + sellplayer + "] " + sellitem + " -1 " + str(sellqty) + "\n"
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					p.stdin.write(cmdin)	
					cmdin = "scoreboard players add @a[name=" + sellplayer + "] money " + str(int(soldprice)) + "\n"
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					p.stdin.write(cmdin)
					cmdin = 'tellraw @a {"text":"' + sellplayer + ' has just sold ' + str(sellqty) + ' '+ sellitem + ' for $' + str(soldprice) + '","color":"green"}\n'
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					p.stdin.write(cmdin)
					selling=False
					sellplayer=''
					a=UpdateSB()
			if tmp[3] == "Could" and tmp[4] == "not" and tmp[5] == "clear":
				selling=False
				cmdin = "tell " + sellplayer + " You do not hold any " + sellitem + " to sell!\n"
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
				p.stdin.write(cmdin)
				selling=False
				sellplayer=''
				a=UpdateSB()
		#.setwarp
		if setwarp == True and tmp[3] == "Teleported":
			x = tmp[6]
			y = tmp[7]
			z = tmp[8]
			x = string.strip(x,",")
			y = string.strip(y,",")
			z = string.strip(z,",")
			with open('warps.csv','rb') as csvfile:
				warps = csv.reader(csvfile,delimiter=',',dialect='excel')
				for row in warps:
					w = ','.join(row)
					wt = string.split(w,',')
					if setwarp == True:
						if wt[0] == warpname:
							setwarp = False
							cmdin = "say A warp with that name already exists!\n"
							print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
							p.stdin.write(cmdin)
			if setwarp == True:				
				with open('warps.csv','ab') as csvfile:
					warps = csv.writer(csvfile,delimiter=',',dialect='excel')
					warps.writerow([warpname,x,y,z])
					cmdin = "say " + warpname + " set to: " + x + " " + y + " " + z + "\n"
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					p.stdin.write(cmdin)
			setwarp = False
		#.sethome
		if sethome == True and tmp[3] == "Teleported":
			sethome = False
			oldhome = False
			x = tmp[6]
			y = tmp[7]
			z = tmp[8]
			x = string.strip(x,",")
			y = string.strip(y,",")
			z = string.strip(z,",")
			player = tmp[4]
			with open('homes.csv','rb') as csvfile:
				homes = csv.reader(csvfile,delimiter=',',dialect='excel')
				tmparray3 = []
				for row in homes:
					h = ','.join(row)
					ht = string.split(h,',')
					if ht[0] == player:
						oldhome = True
						cmdin = "say home already set! replacing with current coordinates.\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
					else:
						tmparray3.append(h)
			with open('homes.csv','wb') as csvfile:
				homes = csv.writer(csvfile,delimiter='\n',dialect='excel')
				for t in xrange(0,len(tmparray3)):
					tmparray3[t] = string.replace(tmparray3[t],', ',',')
					homes.writerow([tmparray3[t]])
				if oldhome == True:
					homestr = player + "," + x + "," + y + "," + z
					homes.writerow([homestr])
				if oldhome == False:
					homestr = player + "," + x + "," + y + "," + z
					homes.writerow([homestr])
				print "Home set to: " + x + " " + y + " " + z
		#0          1       2             3                              4      5  6    7      8  9     10 11
		#[00:16:23] [Server thread/INFO]: Player_Name[/ip.ip.ip.ip:port] logged in with entity id 31337 at (0.0, 0.0, 0.0)
		#Player connecting...
		if tmp[4] == 'logged':
			newconn = tmp[3]
			newconn = string.split(newconn,"/")
			newplayer = newconn[0][:-1]
			playerip = newconn[1][:string.find(newconn[1],":")]
			logged = True
			oldplayer = False
		if logged == True:
			logged = False
			player = newplayer
			with open('playerdb.csv','rb') as csvfile:
				playerdb = csv.reader(csvfile,delimiter=',',dialect='excel')
				for row in playerdb:
					db = ', '.join(row)
					dbt = string.split(db,', ')
					if dbt[0] == player:
						oldplayer=True
			if oldplayer==False:
				with open('playerdb.csv','ab') as csvfile:
					playerdb = csv.writer(csvfile,delimiter=',',dialect='excel')
					playerdb.writerow([newplayer,playerip,getdate(),getdate(),time.time(),0])	
					motd = string.replace(motd, "PLAYER_NAME", player)
					cmdin = 'tellraw @a {"text":"' + motd + '","color":"yellow"}\n'
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					motd = string.replace(motd, player,"PLAYER_NAME")
					p.stdin.write(cmdin)
					if freeshulkerbox == True:
						cmdin = "give " + player + " purple_shulker_box 1\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
					if givehead == True:
						cmdin = "give " + player + " minecraft:skull 1 3 {SkullOwner:" + player + "}\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
					setsb = "scoreboard players add " + player + " money 250\n"
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + setsb,
					p.stdin.write(setsb)
					setsb = "scoreboard players add " + player + " rank 0\n"
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + setsb,
					p.stdin.write(setsb)
				with open('online.csv','ab') as csvfile:
					online = csv.writer(csvfile,delimiter=',',dialect='excel')
					online.writerow([player,playerip,time.time()])
			if oldplayer==True:
					motd = string.replace(motd, "PLAYER_NAME", player)
					motd = string.replace(motd, "Welcome to ", "Welcome back to ")
					cmdin = 'tellraw @a {"text":"' + motd + '","color":"yellow"}\n'
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					motd = string.replace(motd, player,"PLAYER_NAME")
					motd = string.replace(motd, "Welcome back to ", "Welcome to ")
					p.stdin.write(cmdin)
					setsb = "scoreboard players add " + player + " money 100\n"
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + setsb,
					p.stdin.write(setsb)
					with open('online.csv','ab') as csvfile:
						online = csv.writer(csvfile,delimiter=',',dialect='excel')
						online.writerow([player,playerip,time.time()])					
		#Player disconnecting...
		if tmp[4] == 'left':
			player = tmp[3]
			#Open online list, Read it, Write it back without the leaving player
			tmparray=[]
			with open('online.csv','rb') as csvfile:
				online = csv.reader(csvfile,delimiter=',',dialect='excel')
				for row in online:
					o = ','.join(row)
					ot = string.split(o,',')
					if ot[0] == player:
						lastonline = ot[0] + ',' + ot[1] + ',' + str(time.time())
					else:
						tmparray.append(o)			
			with open('online.csv','wb') as csvfile:
				online = csv.writer(csvfile,delimiter='\n',dialect='excel')
				for y in xrange(0,len(tmparray)):
					online.writerow([tmparray[y]])
			#Open playerdb, Write new last online time
			tmparray2=[]
			with open('playerdb.csv','rb') as csvfile:
				playerdb = csv.reader(csvfile,delimiter=',',dialect='excel')
				for row in playerdb:
					db = ','.join(row)
					dbt = string.split(db,',')
					if dbt[0] == player:
						t = dbt[0] + ',' + dbt[1] + ',' + dbt[2] + ',' + dbt[3] + ',' + str(time.time())
						tmparray2.append(t)
					else:
						tmparray2.append(db)
			with open('playerdb.csv','wb') as csvfile:
				playerdb = csv.writer(csvfile,delimiter='\n',dialect='excel')
				for y in xrange(0,len(tmparray2)):
					playerdb.writerow([tmparray2[y]])
print "[" + get24hrtime() + "] [Script thread/DONE]: Script completed (this shouldn't happen!)\n"