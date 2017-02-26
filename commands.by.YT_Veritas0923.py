import subprocess, string, csv
from subprocess import PIPE, Popen
ver = "0.2"
def banner():
	print "##########################################"
	print "# Minecraft SNAPSHOT .commands mod v" + ver + "  #"
	print "# Written by YT_Veritas0923              #"
	print "# Twitter: @Veritas_83                   #"
	print "# Web: www.NigelTodman.com               #"
	print "# GitHub: Veritas83                      #"
	print "# BTC 18j2Env7QokhGG5MccS3LPBKnjsko6u4NQ #"
	print "##########################################"
#Enter your Minecraft cmdline here, you must use nogui
a = 'java -Xms2G -Xmx2G -jar minecraft_server.jar nogui'
sethome = False
setwarp = False
warplist = False
warpstr = ""
print banner()
cmdline = string.split(a)
p = Popen([cmdline[0],cmdline[1],cmdline[2],cmdline[3],cmdline[4],cmdline[5]], stdin=PIPE, stdout=PIPE)
while Popen.poll(p) == None:
	cmdout = p.stdout.readline()
	print cmdout
	tmp = string.split(cmdout)
	#print len(tmp)
	if len(tmp) >= 4:
		if tmp[4] == '.spawn':
			player = string.strip(tmp[3],"<")
			player = string.strip(player,">")			
			#Enter your spawn coords on this line
			cmdin = "tp " + player + " 0 64 -3\n"
			p.stdin.write(cmdin)
		if tmp[4] == '.sethome':
			player = string.strip(tmp[3],"<")
			player = string.strip(player,">")			
			cmdin = "tp " + player + " ~ ~ ~\n"
			sethome = True			
			p.stdin.write(cmdin)
		if sethome == True and tmp[3] == "Teleported":
			sethome = False
			x = tmp[6]
			y = tmp[7]
			z = tmp[8]
			x = string.strip(x,",")
			y = string.strip(y,",")
			z = string.strip(z,",")
			with open('homes.csv','ab') as csvfile:
				homes = csv.writer(csvfile,delimiter=',',dialect='excel')
				homes.writerow([player,x,y,z])
				print "Home set to: " + x + " " + y + " " + z
		if tmp[4] == '.home':
			player = string.strip(tmp[3],"<")
			player = string.strip(player,">")			
			with open('homes.csv','rb') as csvfile:
				homes = csv.reader(csvfile,delimiter=',',dialect='excel')
				for row in homes:
					h = ', '.join(row)
					ht = string.split(h,', ')
					if ht[0] == player:
						cmdin = "tp " + player + " " + str(ht[1]) + " " + str(ht[2]) + " " + str(ht[3]) + "\n"
						p.stdin.write(cmdin)
		if tmp[4] == '.commands':
			player = string.strip(tmp[3],"<")
			player = string.strip(player,">")
			cmdin = "tell " + player + " Commands are: .spawn .sethome .home .setwarp .warp .commands .about .help\n"
			p.stdin.write(cmdin)
		if tmp[4] == '.about':
			player = string.strip(tmp[3],"<")
			player = string.strip(player,">")
			cmdin = "tell " + player + " Minecraft SNAPSHOT .commands mod v" + ver + " -- Written by YT_Veritas0923 (GitHub: Veritas83 Twitter: @Veritas_83)\n"
			p.stdin.write(cmdin)
		if tmp[4] == '.help':
			player = string.strip(tmp[3],"<")
			player = string.strip(player,">")
			cmdin = "say Minecraft SNAPSHOT .commands mod v" + ver + " help\n"
			p.stdin.write(cmdin)
			cmdin = "say spawn - teleports you to spawn\n"
			p.stdin.write(cmdin)
			cmdin = "say sethome - sets .home to current coords\n"
			p.stdin.write(cmdin)
			cmdin = "say home - teleports you to your set home\n"
			p.stdin.write(cmdin)
			cmdin = "say setwarp name - sets a public .warp as given name. name cannot contain spaces\n"
			p.stdin.write(cmdin)
			cmdin = "say warp name - teleports you to warp name. List warps with just .warp\n"
			p.stdin.write(cmdin)
			cmdin = "say commands - list available commands\n"
			p.stdin.write(cmdin)
			cmdin = "say about - display script version and author information\n"
			p.stdin.write(cmdin)
			cmdin = "say help - displays commands and their usage\n"
			p.stdin.write(cmdin)
		if tmp[4] == '.setwarp':
			player = string.strip(tmp[3],"<")
			player = string.strip(player,">")			
			cmdin = "tp " + player + " ~ ~ ~\n"
			setwarp = True			
			if len(tmp) >= 5:
				warpname = tmp[5]
			p.stdin.write(cmdin)
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
							p.stdin.write(cmdin)
			if setwarp == True:				
				with open('warps.csv','ab') as csvfile:
					warps = csv.writer(csvfile,delimiter=',',dialect='excel')
					warps.writerow([warpname,x,y,z])
					cmdin = "say " + warpname + " set to: " + x + " " + y + " " + z
					p.stdin.write(cmdin)
					setwarp = False
		if tmp[4] == '.warp':
			player = string.strip(tmp[3],"<")
			player = string.strip(player,">")			
			#print "Debug: " + str(len(tmp))
			warpstr = ""
			if len(tmp) > 5:
				warpname = tmp[5]
			else:
				warplist = True
				cmdin = "tell " + player + " Warp List:\n"
				p.stdin.write(cmdin)
			with open('warps.csv','rb') as csvfile:
				warps = csv.reader(csvfile,delimiter=',',dialect='excel')
				for row in warps:
					w = ','.join(row)
					wt = string.split(w,',')
					if warplist == False and wt[0] == warpname:
						cmdin = "tp " + player + " " + str(wt[1]) + " " + str(wt[2]) + " " + str(wt[3]) + "\n"
						p.stdin.write(cmdin)
					elif warplist == True:
						warpstr = warpstr + wt[0] + ", "
			if warplist == True:
				cmdin = "tell " + player + " " + warpstr + "\n"
				p.stdin.write(cmdin)
			warplist = False