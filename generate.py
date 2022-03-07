import sys
import random as rd
import time

def read_file(ifiles):
	out = []
	for i in ifiles:
		with open(i, 'r') as f:
			out.extend([j.strip('\n') for j in f.readlines()])
		
	return out



def main():
	lst = read_file(sys.argv[1:len(sys.argv)-1])

	generated = list(range(len(lst)))
	# randomly generate from the lst of words
	while len(generated) != 0:
		num = rd.choice(generated)

		generated.remove(num)

		print(lst[num])

		time.sleep(int(sys.argv[-1]))

main()