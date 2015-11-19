# Python
from itertools import izip_longest
with open('old.txt', 'r') as old:
	rows = [line.split() for line in old]
	maxlen = max(len(x) for x in rows)
	for row in rows:
		print " ".join(row + ["0"] * (maxlen - len(row)))
