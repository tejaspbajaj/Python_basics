name1 = raw_input("Enter name 1: ")
name2 = raw_input("Enter name 2: ")
totallen = len(name1) + len(name2)

match_dir = {
	'a':[0,0],
	'b':[0,0],
	'c':[0,0],
	'd':[0,0],
	'e':[0,0],
	'f':[0,0],
	'g':[0,0],
	'h':[0,0],
	'i':[0,0],
	'j':[0,0],
	'k':[0,0],
	'l':[0,0],
	'm':[0,0],
	'n':[0,0],
	'o':[0,0],
	'p':[0,0],
	'q':[0,0],
	'r':[0,0],
	's':[0,0],
	't':[0,0],
	'u':[0,0],
	'v':[0,0],
	'w':[0,0],
	'x':[0,0],
	'y':[0,0],
	'z':[0,0]
}

for i in name1:
	match_dir[i][0] += 1
for i in name2:
	match_dir[i][1] += 1
for i in match_dir:
	if match_dir[i][0] > 0 and match_dir[i][1] > 0:
		totallen -= (match_dir[i][0] + match_dir[i][1])
flames = ["Friendship", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
print "You status is : %s" % flames[(totallen % len(flames)) - 1]



