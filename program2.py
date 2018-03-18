i = int(input())
user_in = [input() for _ in range(i)]

for s in user_in:
	start = int(s.split(" ")[1])
	end   = int(s.split(" ")[2])
	new_s = s.split(" ")[0].replace(s.split(" ")[0][start:end], "")
	print(new_s)	
