n = [input() for _ in range(int(input()))]
for s in n:
	print(s)
	for idex, char in enumerate(s[1:-1]):
		print(char + (" " * (len(s) - 2)) + s[len(s) - idex - 2])
	if len(s) > 1:
		print(s[::-1])
	
