month = ["jan", "feb", "mar", "apr", "maj", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

for i, v in enumerate(month):
	print "Q:%d" % (i + 1)
	print "A:%s" % v
	print "L:%s" % v
	
	print "Q:%s" % v
	print "A:%d" % (i + 1)
	print "L:%d" % (i + 1)
