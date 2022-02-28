import numpy as np
import argparse

def file2list(f):
	with open(f,'r') as file:
		l = [int(l.strip('\n')) for l in file.readlines()]
	
	return l


def compare_list_index(l):
	# given a list of ints, l, determine how many items are larger than the 
	# previous item in the list index. The first item doesn't count
	
	# assert list only contains ints
	assert all(isinstance(item, int) for item in l)

	l1 = l[1:]
	l2 = [l[n-1] for n in range(1,len(l))]

	return (np.array(l1) > np.array(l2)).sum()


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Advent of Code 2021 Day 1.')
	parser.add_argument('-f','--file-name', dest='file_name', help='input file name',required=True)

	args = vars(parser.parse_args())
	
	l = file2list(args.get('file_name'))
	print(compare_list_index(l))

