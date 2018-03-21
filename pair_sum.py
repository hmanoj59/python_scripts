def pair_sum(array, res):
	if len(array)<2:
		return

	#example value is([1,3,2,2],4)

	seen = set()
	output = set()

	for number in array:
		target  = res - number
		if target not in seen:
			seen.add(number)
		else:
			output.add( (min(target, number), max(target, number)) )
	return len(output)

pair_sum([1,3,2,2],4)
