#!/usr/bin/python

import random
import argparse


def load_tsv(db, reverse, bidi, fileName):
    linenum = 0
    with open(fileName, 'r') as f:
        while True:
            linenum += 1
            line = f.readline().rstrip()
            if not line:
                break
            parts = line.split("\t")
            if len(parts) != 2:
                print "BAD LINE: %s[%d]: %s " % (fileName, linenum, line)
            if bidi:
                db.append((parts[0], parts[1]))
                db.append((parts[1], parts[0]))
            elif reverse:
                db.append((parts[1], parts[0]))
            else:
                db.append((parts[0], parts[1]))
    return db


def ask(q, a):
    print q,
    ans = raw_input()
    if ans == a:
        print 'OK'
        return True
    else:
        print 'NOPE: %s\n' % a
        return False


def main(reverse, bidi, cards):
    db = []
    for fileName in cards:
        load_tsv(db, reverse, bidi, fileName)
    miss = [0] * len(db)
    hit = [0] * len(db)
    while True:
        try:
            indices = list(xrange(len(db)))
            for i, m in enumerate(miss):
                if m - hit[i] > 0:
                    indices.extend([i] * (5 * (m - hit[i])))
            index = random.choice(indices)
            if ask(*db[index]):
                hit[index] += 1
            else:
                miss[index] += 1
        except KeyboardInterrupt:
            bad = [(m, i) for i, m in enumerate(miss) if m > 0]
            bad.sort()
            print '\n\nHere are your worst results:'
            for m, i in reversed(bad):
                print '%d: %s - %s' % (m, db[i][0], db[i][1])
            print 'Bye!'
            return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Learning Flashcards quiz.')
    parser.add_argument('-r', '--reverse', action='store_true', help='reverse side quiz')
    parser.add_argument('-b', '--bidi', action='store_true', help='both direct and reverse quiz')
    parser.add_argument('cards', metavar='CARD.tsv', type=str, nargs='+', help='flashcard tsv files')
    args = parser.parse_args()
    print '\t\tCtrl-C to exit.'
    main(args.reverse, args.bidi, args.cards)
