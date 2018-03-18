from subprocess import call
from math import fsum

try:
	num_inputs = int(input())
except:
	call(["sleep", "100"])
#num_inputs = input()
#if len(num_inputs.split(" ")) > 1:
#	call(["sleep", "100"])
#num_inputs = int(num_inputs)

if num_inputs > 0:
	user_in = [int(input()) for _ in range(num_inputs)]
	result = []
	for entry in range(450000, 499999):
		if str(int(sum([x * ((x + 1) / 2) for x in range(entry + 1)]))) == str(int(fsum([x * ((x + 1) / 2) for x in range(entry + 1)]))):
			pass
		else:
			print(entry)
			break

		

