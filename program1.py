fpd = input().split(" ")
spd = input().split(" ")
turn = []
for i in range(10):
	turn.append(input())

for i in range(0, 10, 2):
	if turn[i] in spd:
		fpd.remove(turn[i])
		print("HERE'S MY CARD")
	else:
		print("GO FISH")
	if turn[i + 1] in fpd:
		spd.remove(turn[i + 1])
		print("HERE'S MY CARD")
	else:
		print("GO FISH")
