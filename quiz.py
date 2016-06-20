#!/usr/bin/python

import sys
import random

def load_qadb(fileName):
	db = []
	with open(fileName, 'r') as f:
		while True:
			q = f.readline().rstrip()
			if not q:
				break
			a = f.readline().rstrip()
			l = f.readline().rstrip()
			assert q.startswith('Q:')
			assert a.startswith('A:')
			assert l.startswith('L:')
			db.append((q[2:], a[2:], l[2:]))
	return db

def ask(q, a, l):
	print '%s?' % q,
	ans = raw_input()
	if ans == a:
		print 'OK\n'
		return True
	else:
		print 'NOPE: %s\n' % l
		return False

def main(fileName):
	db = load_qadb(fileName)
	hit = [0] * len(db)
	miss = [0] * len(db)
	while True:
		try:
			index = random.randint(0, len(db) - 1)
			if ask(*db[index]):
				hit[index] += 1
			else:
				miss[index] += 1
		except KeyboardInterrupt:
			bad = [(m, i) for i, m in enumerate(miss) if m > 0]
			bad.sort()
			print '\n\nHere are your worst results:'
			for m, i in reversed(bad):
				print '%s : %d' % (db[i][0], m)
			print 'Bye!'
			return

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'usage: quiz.py dbname.qadb'
	else:
		print "press Ctrl-C when you had enough.\n"
		main(sys.argv[1])
