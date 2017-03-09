import subprocess, string, csv, time, logging, threading, random
from subprocess import Popen, PIPE
from time import sleep
from nbstreamreader import NonBlockingStreamReader as NBSR
#nbstreamreader.py https://gist.github.com/EyalAr/7915597

ver = "Minecraft SNAPSHOT .commands script v0.48"
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

## Start Config ##
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
# 5m 300, 30m 1800, 1h 3600, 12h 43200, 1d 86400, 1w 604800, 1mo 2419200


cmdline = string.split(javacmd)
p = subprocess.Popen([cmdline[0],cmdline[1],cmdline[2],cmdline[3],cmdline[4],cmdline[5]], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
nbsr = NBSR(p.stdout)
print banner()

currtime = time.time()
lasttimesave = currtime
lasttimeclear = currtime
lasttimepoll = currtime
playerisonline = False
clearwarn10 = False
clearwarn60 = False
warplist = False
sethome = False
setwarp = False
logged = False
sbset = False
isop=False
tmparray=[]
cmdout = "[" + get24hrtime() + "] [Script thread/IDLE]: There was no output for awhile\n"
warpstr = ''
derp=''
seen=''
op=''
x=0
t=0
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
			elif tmp[3] == "The" and tmp[4] == "dataTag":
				derp=True
			elif tmp[3] == "Selector":
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
		autosave = "say World saved. Autosave by " + ver +  "\n"
		print "[" + get24hrtime() + "] [Script thread/EXEC]: " + autosave,
		p.stdin.write(autosave)
		print cmdout,
	if useautoclear == True and ((currtime - lasttimeclear) > (autoclearint-60)):
		if clearwarn60 == False:
			if ((currtime - lasttimeclear) > (autoclearint-60)):
				autoclear = "say Clearing items in 1 minute!\n"
				clearwarn60 = True
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + autoclear,
				p.stdin.write(autoclear)
				print cmdout,
		if clearwarn10 == False:
			if ((currtime - lasttimeclear) > (autoclearint-10)):
				autoclear = "say Clearing items in 10 seconds!\n"
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
		autoclear = "say Items cleared. Autoclear by " + ver +  "\n"
		p.stdin.write(autoclear)
		print cmdout,
		clearwarn60 = False
		clearwarn10 = False
	if sbset == False:
		setsb = "scoreboard objectives add inOverworld dummy\n"
		print "[" + get24hrtime() + "] [Script thread/INIT]: " + setsb,
		p.stdin.write(setsb)
		sbset = True
	if sbset == True and currtime - lasttimepoll > 15:
		lasttimepoll = time.time()
		setsb = "scoreboard players set @a inOverworld 0\n"
		#print "[" + get24hrtime() + "] [Script thread/CHKD]: " + setsb,
		p.stdin.write(setsb)
		setsb = "scoreboard players set @a inOverworld 1 {Dimension:0}\n"
		#print "[" + get24hrtime() + "] [Script thread/CHKD]: " + setsb,
		p.stdin.write(setsb)
	##
	#User .commands
	##
	if len(tmp) > 4:
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
			cmdin = "tell " + player + " Commands are: .spawn .sethome .home .rtp .setwarp .warp .whois .ping .seen .commands .about .help\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.about':
			player = getplayername(tmp[3])
			cmdin = "say " + ver + " -- Written by YT_Veritas0923 (GitHub: Veritas83 Twitter: @Veritas_83)\n"
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
						    ["ping", "-n", "1", "-l", "2", "-w", "2000", host],
						    stdout = subprocess.PIPE,
						    stderr = subprocess.PIPE
						)
						out, error = ping.communicate()
						pingreply = string.split(out,"\n")
						for t in xrange(0,len(pingreply)):
							if pingreply[t][0:5] == "Reply":
								tmparray4 = string.split(pingreply[t]," ")
								msreply = tmparray4[4][5:]
								cmdin = "say " + player + " Ping: " + msreply + "\n"
								print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
								p.stdin.write(cmdin)
		if tmp[4] == '.seen' and len(tmp) == 6:
			player = getplayername(tmp[3])
			seen = tmp[5]
			playerisonline=False
			#Open online list, Read it, Inform player is online
			with open('online.csv','rb') as csvfile:
				online = csv.reader(csvfile,delimiter=',',dialect='excel')
				for row in online:
					o = ','.join(row)
					ot = string.split(o,',')
					if ot[0] == seen:
						playerisonline = True
					else:
						derp=True
			if playerisonline == True:
				cmdin = "say Look harder! Player is online right now!\n"
				print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
				p.stdin.write(cmdin)
			else:
				with open('playerdb.csv','rb') as csvfile:
					playerdb = csv.reader(csvfile,delimiter=',',dialect='excel')
					for row in playerdb:
						db = ', '.join(row)
						dbt = string.split(db,', ')
						if dbt[0] == seen:
							if ((time.time() - float(dbt[4])) / 60.0) > 60:
								hours = str((((time.time() - float(dbt[4])) / 60.0) / 60.0))
								mintmp = string.split(hours,'.')
								hours = int(mintmp[0])
								minutes = round((60 * float('0.' + mintmp[1])))
								cmdin = "say Player: " + seen + " was last online " + str(int(hours)) + " hours " + str(int(minutes)) + " minutes ago.\n"
							else:
								cmdin = "say Player: " + seen + " was last online " + str(round(((time.time() - float(dbt[4])) / 60.0))) + " minutes ago.\n"
							print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
							p.stdin.write(cmdin)
		if tmp[4] == '.help':
			player = getplayername(tmp[3])
			cmdin = "say " + ver + " help\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = "say spawn - teleports you to spawn\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = "say sethome - sets .home to current coordinates\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = "say home - teleports you to your set home\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = "say rtp - teleports you to a random location\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = "say setwarp name - sets a public .warp as given name. name cannot contain spaces\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = "say warp name - teleports you to warp name. List warps with just .warp\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = "say whois player - checks if player has played on this server\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = "say ping - causes server to reply with ping response time in ms\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = "say seen player - displays when player was last seen online\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = "say commands - list available commands\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = "say about - display script version and author information\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
			cmdin = "say help - displays commands and their usage\n"
			print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
			p.stdin.write(cmdin)
		if tmp[4] == '.warp':
			player = getplayername(tmp[3])
			warpstr = ""
			if len(tmp) > 5:
				warpname = tmp[5]
			else:
				warplist = True
				cmdin = "tell " + player + " Warp List:\n"
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
				cmdin = "tell " + player + " " + warpstr[:-2] + "\n"
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
							cmdin = "say " + playername + " playing here since " + dbt[2] + "\n"
							print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
							p.stdin.write(cmdin)
			if oldplayer == False:		
						cmdin = "say " + playername + " not found.\n"
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
	##
	#Event functions
	##
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
					playerdb.writerow([newplayer,playerip,getdate(),getdate(),time.time()])	
					motd = string.replace(motd, "PLAYER_NAME", player)
					cmdin = "say " + motd + "'\n"
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					motd = string.replace(motd, player,"PLAYER_NAME")
					p.stdin.write(cmdin)
					if freeshulkerbox == True:
						cmdin = "give " + player + " purple_shulker_box 1\n"
						print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
						p.stdin.write(cmdin)
				with open('online.csv','ab') as csvfile:
					online = csv.writer(csvfile,delimiter=',',dialect='excel')
					online.writerow([player,playerip,time.time()])
			if oldplayer==True:
					motd = string.replace(motd, "PLAYER_NAME", player)
					motd = string.replace(motd, "Welcome to ", "Welcome back to ")
					cmdin = "say " + motd + "'\n"
					print "[" + get24hrtime() + "] [Script thread/EXEC]: " + cmdin,
					motd = string.replace(motd, player,"PLAYER_NAME")
					motd = string.replace(motd, "Welcome back to ", "Welcome to ")
					p.stdin.write(cmdin)
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