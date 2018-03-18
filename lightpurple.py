families = {}

famcount = 0
people = int(input())
connections = [input() for _ in range(people)]
people_c = int(input())
checks = [input() for _ in range(people_c)]

for c in connections:
	if c.split(" ")[2] in families and c.split(" ")[1] in ["mother", "mom", "father", "dad", "brother", "sister", "daughter", "son"]:
		family = families[c.split(" ")[2]]
	else:
		famcount += 1
		family = famcount
	families[c.split(" ")[0]] = family
	families[c.split(" ")[2]] = family
for c in checks:
	
	if c.split(" ")[0] in families and c.split(" ")[1] in families and families[c.split(" ")[0]] == families[c.split(" ")[1]]:
		print("Related")
	else:
		print("Not Related")
