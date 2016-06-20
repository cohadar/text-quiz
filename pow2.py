def tridec(n):
	r = []
	for i, d in enumerate(reversed(str(n))):
		if i % 3 == 0:
			r.append(',')
		r.append(d)
	s = "".join(r)
	s = s[::-1]
	if s[0] == ',':
		s = s[1:]
	if s[-1] == ',':
		s = s[:-1]
	return s

def shortexp(n):
	s = "%.2g" % n
	s = s.replace('+0', '')
	s = s.replace('+', '')
	return s

for x in xrange(0, 65):
	if x <= 16:
		print "Q:pow2(%s)" % x
		print "A:%s" % (str(1 << x))
		print "L:%s" % (str(1 << x))
	else:
		print "Q:pow2(%s)" % x
		print "A:%s" % shortexp(1 << x)
		print "L:%s (%s)" % (shortexp(1 << x), tridec(1 << x))
