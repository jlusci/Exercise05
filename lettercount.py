from sys import argv

script, filename = argv

def main():
	my_file = open(filename)
	print "Opening the file %r" % filename
	indata = my_file.read()
	lowered = indata.lower()
	my_list = list(lowered)

	# print ord(my_list[23567])
	# lowered = indata.lower()
	# print lowered
	# print ord('a')
	ascii_nums = range(97,123)

	file_ascii_values = list()
	
	for index in range(len(my_list)):
		# print ord(my_list[index])
		if ord(my_list[index]) in ascii_nums:
			file_ascii_values.append(ord(my_list[index]))
		index += 1

	returned_counts = list()

	for new_index in ascii_nums:
		returned_counts.append(file_ascii_values.count(new_index))

	for j in range(len(returned_counts)):
		print returned_counts[j]

	# print returned_counts
	# print ord(my_list[676417])	

if __name__ == '__main__':
	main()