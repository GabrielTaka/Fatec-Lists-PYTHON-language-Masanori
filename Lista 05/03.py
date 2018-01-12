count = 0


for i in range(1067, 3628):
	if not i%2 and not i%7:
		count += 1

print (count)
