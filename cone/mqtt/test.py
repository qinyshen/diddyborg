import iw_parse
networks = iw_parse.get_interfaces(interface='wlan0')
#print networks
for line in networks:
	print line
	print "------------------------------------------------------"
