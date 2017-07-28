def make_trie(args):
    trie = {}
    for word in args:
        temp_trie = trie
        for letter in word:
            temp_trie = temp_trie.setdefault(letter, {})
        #print "temp_trie",trie      pass by name in python
    return trie
 
 
def in_trie(trie, word):
	temp_trie = trie
	for i, letter in enumerate(list(word)):
		if letter not in temp_trie:
			return i+1
		temp_trie = temp_trie[letter]
	return -1
 
def f(n):
	pos = []
	neg = []
	ans = set()
	for _ in xrange(n):
		sy, s = raw_input().split()
		if sy == '+':
			pos.append(s)
		else:
			neg.append(s)
	trie = make_trie(pos)
	#print trie
	for i in xrange(len(neg)):
		j = in_trie(trie, neg[i])
		if j == -1:
			print -1
			return
		else:
			ans.add(neg[i][:j])
	ans = sorted(list(ans))
	print len(ans)
	for s in ans:
		print s
f(int(raw_input()))