def getNthUglyNo(n): 

	ugly = [0] * n

	ugly[0] = 1

	i2 = i3 =i5 = 0

	next_multiple_of_2 = 2
	next_multiple_of_3 = 3
	next_multiple_of_5 = 5

	for l in range(1, n):

		ugly[l] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)

		if ugly[l] == next_multiple_of_2:
			i2 += 1
			next_multiple_of_2 = ugly[i2] * 2

		if ugly[l] == next_multiple_of_3:
			i3 += 1
			next_multiple_of_3 = ugly[i3] * 3

		if ugly[l] == next_multiple_of_5:
			i5 += 1
			next_multiple_of_5 = ugly[i5] * 5

	return ugly[-1]

def main():

	n = 150

	print(getNthUglyNo(n))


if __name__ == '__main__':
	main()
