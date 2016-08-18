import subprocess
import time
import argparse


def signal_check():
	parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
	parser.add_argument(dest='interface', nargs='?', default='wlan0',
			    help='wlan interface (default: wlan0)')
	args = parser.parse_args()


	
	cmd = subprocess.Popen('iwconfig %s' % args.interface, shell=True,
			   stdout=subprocess.PIPE)

	for line in cmd.stdout:
		if  'wlan0'  in line:	
			words = line.split()  
			IEEE = words[2]
			ESSID = words[3].split('"')[1]
			print IEEE
			print ESSID


		if  'Mode:Managed'  in line:	
			words = line.split()  
			Frequency = words[1].split(":")[1]+"GHz"
			Access_Point = words[5]
			print Frequency
			print Access_Point



		if  'Bit Rate'  in line:	
			words = line.split()  
			Bit_Rate = words[1].split("=")[1]+"Mb/s"
			Tx_Power = words[3].split("=")[1]+"dBm"
			print Bit_Rate
			print Tx_Power

	return IEEE, ESSID, Frequency, Access_Point, Bit_Rate, Tx_Power


	#    lines = []
	#    words = [[]]
	#	
	#    for line in cmd.stdout:
	#	woed = line.split()
	#	words.append(woed)
	#	lines.append(line)
	##	if  'Not-Associated'  in line:
	##    	    print "no wifi"
	##	    print "--------------------------------------------"
	##	    continue

	#    for line in lines:
	#	print line

	#    print "--------------------------------------------"

	#    print words




	#    for line in cmd.stdout:
	#        if 'Link Quality' in line:
	#            print line
	#        elif 'Not-Associated' in line:
	#            print 'No signal'
#	    time.sleep(1)





