def constructList(max, increment):
	i = 0
	numbers = []
	#while i < max:
	for i in range(0, max):
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	return numbers

numbers = constructList(6, 2)
		
print "The numbers: "

for num in numbers:
	print num