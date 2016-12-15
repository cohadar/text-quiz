import math

for p in xrange(1, 21):
	print "Q:log2(%d)" % p
	l = math.log(p) / math.log(2)
	print "A:%.3f" % l
	print "L:%f ~ %.3f" % (l, l)
