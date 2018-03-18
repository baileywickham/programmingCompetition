user_in = [input() for _ in range(10)]

small = 0
med = 0
large = 0

for line in user_in:
	temp_large = len(line.split("oxoxxooo")) - 1
	temp_med = len(line.split("oxo")) - 1 - temp_large
	temp_small = len(line.split("oo")) - temp_large - 1
	small += temp_small
	med += temp_med
	large += temp_large
print("{0} small\n{1} medium\n{2} large".format(small, med, large))
