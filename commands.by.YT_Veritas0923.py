import subprocess, string, csv
from subprocess import PIPE, Popen
def banner():
	print "##########################################"
	print "# Minecraft SNAPSHOT .commands mod v0.1  #"
	print "# Written by YT_Veritas0923              #"
	print "# Twitter: @Veritas_83                   #"
	print "# Web: www.NigelTodman.com               #"
	print "# GitHub: Veritas83                      #"
	print "# BTC 18j2Env7QokhGG5MccS3LPBKnjsko6u4NQ #"
	print "##########################################"
#Enter your Minecraft cmdline here, you must use nogui
a = 'java -Xms2G -Xmx2G -jar minecraft_server.jar nogui'
sethome = False
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
			cmdin = "tell " + player + " Commands are: .spawn .sethome .home .commands -- Written by YT_Veritas0923 (GitHub: Veritas83 Twitter: @Veritas_83)\n"
			p.stdin.write(cmdin)
