import subprocess, string, csv, time, logging, threading, random, datetime
from subprocess import Popen, PIPE
from time import sleep
from nbstreamreader import NonBlockingStreamReader as NBSR
#nbstreamreader.py https://gist.github.com/EyalAr/7915597

ver = "Minecraft SNAPSHOT .commands script v0.56"
bannershown = False

def banner():
	banner = "##############################################\n# " + ver + "  #\n"
	banner += "# Written by YT_Veritas0923                  #\n# Twitter: @Veritas_83                       #\n"
	banner += "# Web: www.NigelTodman.com                   #\n# GitHub: Veritas83                          #\n"
	banner += "# BTC 18j2Env7QokhGG5MccS3LPBKnjsko6u4NQ     #\n##############################################\n"
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
	itemsdb="stone,cobblestone,dirt,arrow,wheat_seeds,cookie,torch,planks,potato,cobblestone,coal,wheat,glass,carrot,melon,chicken,fireworks,leather,cooked_fish,log2,log,bread,glowstone,bookshelf,emerald,hay_block,melon_block,ender_pearl,purple_shulker_box,lime_shulker_box,ender_chest,iron_ingot,gold_ingot,chainmail_leggings,chainmail_boots,chainmail_helmet,chainmail_chestplate,bow,leather_helmet,leather_chestplate,leather_leggings,leather_boots,iron_sword,iron_axe,iron_pickaxe,iron_hoe,iron_shovel,diamond,enchanting_table,iron_helmet,iron_chestplate,iron_leggings,iron_boots,golden_helmet,golden_chestplate,golden_leggings,golden_boots,diamond_helmet,diamond_chestplate,diamond_leggings,diamond_boots"
	return itemsdb
def LoadPrices():
	pricedb="1,15,1,2,4,5,5,5,8,10,10,10,15,15,15,25,25,25,25,25,25,25,50,50,100,125,135,1000,10000,12000,25000,250,500,100,100,100,100,100,125,200,175,100,500,750,750,500,250,2500,5000,500,800,700,400,2500,4000,3500,2000,12500,20000,17500,10000"
	return pricedb
def LoadRankItems():
	ritemsdb="0,1,2,3,4,5,6,7,8,9,10,11,12"
	return ritemsdb
def LoadRankPrices():
	rpricedb="0,1,100,500,1000,5000,10000,25000,40000,60000,120000,250000,500000"
	return rpricedb

def UpdateSB():
	setsb = "scoreboard players operation $ Character = @a money\n"
	#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
	p.stdin.write(setsb)
	setsb = "scoreboard players operation Kills Character = @a totalkills\n"
	#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
	p.stdin.write(setsb)
	setsb = "scoreboard players operation Rank Character = @a rank\n"
	#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
	p.stdin.write(setsb)
	setsb = "scoreboard objectives setdisplay list rank\n"
	#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
	p.stdin.write(setsb)
#spawn = "-82 64 264" Dev Server coords		(MC.NIGELTODMAN.COM:25599)
#spawn = "0 64 -3"    Snapshot srv coords (MC.NIGELTODMAN.COM:25565)
#spawn = "206 64 259" VNNLA Server coords (VNLLA.NIGELTODMAN.COM:25566)

## Start Config ##
javacmd = 'java -Xms128M -Xmx4G -jar minecraft_server.jar nogui' # Java command line to start Minecraft Server jar, Must use nogui
spawn = "206 64 259"   																					 # WorldSpawn Coordinates
rtpradius = 35000  																						 # Random Teleport radius (-35000,35000)
useautosave = True 																						 # Use Autosave?
useautoclear = True 																					 # Use Autoclear?
autosaveint = 1776																					   # Autosave Interval in seconds
autoclearint = 3625																					   # Autoclear Interval in seconds
freeshulkerbox = True																					 # Gives new players a shulker box on their first connect
motd = "!## MOTD ##! Welcome to mc.nigeltodman.com, PLAYER_NAME! See our custom commands and their usage with '.help' * April Gamerules: limitedCrafting:Off keepInventory:On mobGriefing:Off Difficulty:Hard"
votemsg = "Vote for this server! Vote #1 adf.ly/1kVCJK #2 adf.ly/1kVCLs #3 adf.ly/1g4VYV #4 adf.ly/1mCgLU #5 adf.ly/1mCgcL #6 adf.ly/1mCgoa"
admin="YT_Veritas0923"
																					   									 # Message of the Day notes:
																					   									 # PLAYER_NAME is replaced with connecting player.
## End Config   ##												   									 # 'Welcome to' is replaced by 'Welcome back to' for returning players.
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
tmparray=[]
cmdout = "[" + get24hrtime() + "] [Script thread/IDLE]: There was no output for awhile\n"
strtime= time.clock()
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
			if tmp[3] == "Set" and tmp[4] == "score":
				derp=True
			elif tmp[3] == "Set" and tmp[6] == "objective":
				derp=True
			elif tmp[3] == "The" and tmp[4] == "dataTag":
				derp=True
			elif tmp[3] == "Selector":
				derp=True
			elif tmp[3] == "Operation":
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
		print cmdout,
		autosave = 'tellraw @a {"text":"World saved. Autosave by ' + ver + '","color":"yellow"}\n'
		print "[" + get24hrtime() + "] [Script thread/EXEC]: " + autosave,
		p.stdin.write(autosave)
		print cmdout,
	if useautoclear == True and ((currtime - lasttimeclear) > (autoclearint-60)):
		if clearwarn60 == False:
			if ((currtime - lasttimeclear) > (autoclearint-60)):
				autoclear = 'tellraw @a {"text":"Clearing Items in 1 minute!","color":"aqua"}\n'
				clearwarn60 = True
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + autoclear,
				p.stdin.write(autoclear)
				print cmdout,
		if clearwarn10 == False:
			if ((currtime - lasttimeclear) > (autoclearint-10)):
				autoclear = 'tellraw @a {"text":"Clearing items in 10 seconds!","color":"aqua"}\n'
				clearwarn10 = True
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + autoclear,
				p.stdin.write(autoclear)
				print cmdout,
	if useautoclear == True and ((currtime - lasttimeclear) > autoclearint):
		lasttimeclear = time.time()
		autoclear = "kill @e[type=Item]\n"
		print "[" + get24hrtime() + "] [Script thread/EXEC]: " + autoclear,
		p.stdin.write(autoclear)
		print cmdout,
		autoclear = 'tellraw @a {"text":"Items cleared. Autoclear by ' + ver +  '","color":"aqua"}\n'
		p.stdin.write(autoclear)
		print cmdout,
		clearwarn60 = False
		clearwarn10 = False
	#Setup Scoreboard
	if sbset == False:
		setsb = "scoreboard objectives add inOverworld dummy\n"
		print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
		p.stdin.write(setsb)
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
		setsb = "scoreboard objectives add rank dummy Rank\n"
		print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard objectives add money dummy Money\n"
		print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard objectives setdisplay sidebar Character\n"
		print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard players operation $ Character = @a money\n"
		print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard players operation Kills Character = @a totalkills\n"
		print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard players operation Rank Character = @a rank\n"
		print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard players operation Kills Info = @a totalkills\n"
		print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard objectives setdisplay list rank\n"
		print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
		p.stdin.write(setsb)
		sbset = True
	#12s Poll time
	if sbset == True and currtime - lasttimepoll > 12:
		lasttimepoll = time.time()
		for i in range(1,16):
			setsb = "scoreboard players add @a[score_killcounter_min=" + str(i) + ",score_rank_min=0,score_rank=3] money " + str(int(i) * 5) + "\n"
			#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
			#p.stdin.write(setsb)
			setsb = "scoreboard players add @a[score_killcounter_min=" + str(i) + ",score_rank_min=4,score_rank=5] money " + str(int(round((int(i) * 5) * 1.2))) + "\n"
			#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
			#p.stdin.write(setsb)
			setsb = "scoreboard players add @a[score_killcounter_min=" + str(i) + ",score_rank_min=6,score_rank=7] money " + str(int(round((int(i) * 5) * 1.4))) + "\n"
			#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard players add @a[score_killcounter_min=" + str(i) + ",score_rank_min=8,score_rank=9] money " + str(int(round((int(i) * 5) * 1.6))) + "\n"
			#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard players add @a[score_killcounter_min=" + str(i) + ",score_rank_min=10,score_rank=10] money " + str(int(round((int(i) * 5) * 1.8))) + "\n"
			#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard players add @a[score_killcounter_min=" + str(i) + ",score_rank_min=11,score_rank=11] money " + str(int(round((int(i) * 5) * 2))) + "\n"
			#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
			p.stdin.write(setsb)
			setsb = "scoreboard players add @a[score_killcounter_min=" + str(i) + ",score_rank_min=12] money " + str(int(round((int(i) * 5) * 2.5))) + "\n"
			#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
			p.stdin.write(setsb)
		setsb = "scoreboard players operation $ Character = @a money\n"
		#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard players operation Kills Character = @a totalkills\n"
		#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard objectives setdisplay list Info\n"
		#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard objectives setdisplay sidebar Character\n"
		#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard players set @a killcounter 0\n"
		#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard players set @a inOverworld 0\n"
		#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard players set @a inOverworld 1 {Dimension:0}\n"
		#print "[" + get24hrtime() + "] [Script thread/POLL]: " + setsb,
		p.stdin.write(setsb)
	##
	#User .commands
	##
	if len(tmp) > 4:
		player = getplayername(tmp[3])
		if tmp[4] == '.spawn':
			player = getplayername(tmp[3])
			cmdin = "tp @a[name=" + player + ",score_inOverworld_min=1] " + spawn + "\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.sethome':
			player = getplayername(tmp[3])
			cmdin = "tp " + player + " ~ ~ ~\n"
			sethome = True			
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.home':
			player = getplayername(tmp[3])
			with open('homes.csv','rb') as csvfile:
				homes = csv.reader(csvfile,delimiter=',',dialect='excel')
				for row in homes:
					h = ','.join(row)
					ht = string.split(h,',')
					if ht[0] == player:
						cmdin = "tp @a[name=" + player + ",score_inOverworld_min=1] " + str(ht[1]) + " " + str(ht[2]) + " " + str(ht[3]) + "\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
		if tmp[4] == '.commands':
			player = getplayername(tmp[3])
			cmdin = 'tellraw ' + player + ' {"text":"User Commands are: .spawn .sethome .home .rtp .warp .whois .ping .report .seen .uptime .shop .buy .sell .stats .staff .tpa .tpaccept .tpdeny .vote .ranks .rankup .report .commands .about .help Mod Commands are: .setwarp .kick","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.about':
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
			cmdin = 'tellraw ' + player + ' {"text":"' + ver + ' help","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"spawn - teleports you to spawn","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"sethome - sets .home to current coordinates","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"home - teleports you to your set home","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"rtp - teleports you to a random location","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"warp name - teleports you to warp name. List warps with just .warp","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"whois player - checks if player has played on this server","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"ping - causes server to reply with ping response time in ms","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"ranks - Displays Ranks, Their cost and their money drop multiplier.","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"rankup - Increases your rank by 1. See cost use .rank","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"report player reason - reports player for specified reason","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"shop - lists items for sale, use .buy to purchase","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"buy item_name 64 - buys 64 items from the .shop, increase or decrease 64 as needed","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"sell item_name 1 - sells 1 item to the .shop, increase or decrease 1 as needed","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"seen player - displays when player was last seen online","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"stats - displays total players in PlayerDB and server uptime","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"tpa player - sends .tpa request to specified player","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"tpaccept - Accepts .tpa request. Teleports player to you.","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"tpdeny - Denies .tpa request.","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"uptime - displays server uptime","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"vote - displays server vote links","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"commands - list available commands","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"staff - list server staff","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"about - display script version and author information","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"help - displays commands and their usage","color":"aqua"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"setwarp name - sets a public .warp as given name. name cannot contain spaces","color":"red"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = 'tellraw ' + player + ' {"text":"kick player reason - kicks a player, reason is optional. reason cannot contain spaces (use . instead of space)","color":"red"}\n'
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.warp':
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
						cmdin = "tp @a[name=" + player + ",score_inOverworld_min=1] " + str(wt[1]) + " " + str(wt[2]) + " " + str(wt[3]) + "\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
					elif warplist == True:
						warpstr = warpstr + wt[0] + ", "
			if warplist == True:
				cmdin = 'tellraw ' + player + ' {"text":"' + warpstr[:-2] + '","color":"aqua"}\n'
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
				p.stdin.write(cmdin)
			warplist = False
		if tmp[4] == '.rtp':
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
			if oldplayer == False:		
						cmdin = 'tellraw @a {"text":"' + playername + ' not found.","color":"aqua"}\n'
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
		if tmp[4] == '.ranks':
			ranks = open('ranks.csv','rb')
			rankstr = ''
			for line in ranks:
				if len(line) > 3:
					rankstr = string.split(string.strip(line,"\r\n"),",")
					cmdin = 'tellraw @a {"text":"Rank: ' + str(rankstr[0]) + ' Cost: ' + str(rankstr[1]) + ' Bonus: ' + str(rankstr[2]) + '","color":"red"}\n'
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					p.stdin.write(cmdin)
		if tmp[4] == '.rankup':
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
		if tmp[4] == '.tpaccept' and player == tpatarget and tpareq == True:
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
		if tmp[4] == '.tpdeny' and player == tpatarget and tpareq == True:
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
		if tmp[4] == '.buy':
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
						cmdin = "give @a[name=" + player + ",score_money_min=" + pricedb[i]+ "] " + itemsdb[i] + " 1\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
						cmdin = "scoreboard players remove @a[name=" + player + "] money " + pricedb[i]+ "\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
						setsb = "scoreboard players operation $ Character = @a money\n"
						p.stdin.write(setsb)
						setsb = "scoreboard players operation Kills Character = @a totalkills\n"
						p.stdin.write(setsb)
						cmdin = 'tellraw @a {"text":"' + player + ' has just bought ' + str(buyqty) + ' '+ itemsdb[i] + ' for $' + str(totalprice) + '","color":"yellow"}\n'
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
					if tmp[5] == itemsdb[i] and tmp[6] > 1:
						buyqty = tmp[6]
						totalprice = int(pricedb[i]) * int(buyqty)
						cmdin = "give @a[name=" + player + ",score_money_min=" + str(int(totalprice)) + "] " + itemsdb[i] + " " + str(tmp[6]) + "\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
						cmdin = "scoreboard players remove @a[name=" + player + "] money " + str(int(totalprice)) + "\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
						setsb = "scoreboard players operation $ Character = @a money\n"
						p.stdin.write(setsb)
						setsb = "scoreboard players operation Kills Character = @a totalkills\n"
						p.stdin.write(setsb)
						cmdin = 'tellraw @a {"text":"' + player + ' has just bought ' + str(buyqty) + ' '+ itemsdb[i] + ' for $' + str(totalprice) + '","color":"yellow"}\n'
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
			if len(tmp) < 6:
				cmdin = "tell " + player + " .buy requires a quantity! (ie: .buy log 64 or .buy log 1)\n"
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
				p.stdin.write(cmdin)
		if tmp[4] == '.sell':
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
					if tmp[5] == itemsdb[i] and tmp[6] == 1:
						sellprice = str(int(round((int(pricedb[i]) * 0.5))))
						sellqty = 1
						cmdin = "clear @a[name=" + player + "] " + itemsdb[i] + " -1 0\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)					
						a=UpdateSB()
					if tmp[5] == itemsdb[i] and tmp[6] > 1:
						sellprice = str(int(round((int(pricedb[i]) * 0.5))) * int(tmp[6]))
						sellqty = int(tmp[6])
						cmdin = "clear @a[name=" + player + "] " + itemsdb[i] + " -1 0\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)					
						a=UpdateSB()
			if len(tmp) > 5:
				sellqty = int(tmp[6])
			else:
				sellqty = 1
		#Selling Event
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
				cmdin = "scoreboard players add @a[name=" + tmp[5] + "] money " + str(int(tmp[6])) + "\n"
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
		#Selling Event
		if selling == True:
			if tmp[3] == sellplayer:
				selling=False
				soldqty = tmp[5]
				soldprice = int(sellprice)
				print "[" + get24hrtime() + "] [Script thread/DBUG]: " + sellplayer + " " + str(soldqty) + " " + str(sellqty) + " " + str(soldprice) + " " + str(sellprice) + "\n",
				if int(soldqty) < int(sellqty):
					cmdin = "tell " + sellplayer + " You do not hold enough " + sellitem + " to sell!\n"
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					p.stdin.write(cmdin)
				if int(soldqty) >= int(sellqty):
					cmdin = "clear @a[name=" + sellplayer + "] " + sellitem + " -1 " + str(sellqty) + "\n"
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					p.stdin.write(cmdin)	
					cmdin = "scoreboard players add @a[name=" + sellplayer + "] money " + str(int(soldprice)) + "\n"
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					p.stdin.write(cmdin)
					cmdin = 'tellraw @a {"text":"' + sellplayer + ' has just sold ' + str(sellqty) + ' '+ sellitem + ' for $' + str(soldprice) + '","color":"green"}\n'
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					p.stdin.write(cmdin)
			if tmp[3] == "Could" and tmp[4] == "not" and tmp[5] == "clear":
				selling=False
				cmdin = "tell " + sellplayer + " You do not hold any " + sellitem + " to sell!\n"
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
				p.stdin.write(cmdin)
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
						setsb = "scoreboard players add " + player + " money 25\n"
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
					setsb = "scoreboard players add " + player + " money 2\n"
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