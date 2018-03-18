num_inputs = int(input())
result = []
for i in range(num_inputs):
	max_weight = input().split(" ")[0]
	values = [int(x) for x in input().split(" ")]
	weights = [int(x) for x in input().split(" ")]

	all_values= []
	ratio_values = []
	for i in range(len(values)):
		for _ in range(weights[i]):
			all_values.append(values[i])
			ratio_values.append([values[i] / weights[i]])
	all_values.sort()
	summ = 0
	index = 0
	while summ <= max_weight:
		summ += all_values(index)
		index += 1
	summ -= all_values(index)
	print(summ)
