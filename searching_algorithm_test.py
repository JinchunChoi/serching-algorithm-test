import matplotlib.pyplot as plt
import random
from datetime import datetime
import math
import statistics

# Parameters for the experiment
data_size = 1000
test_count = 100

binary_count = []
linear_count = []

# For target and data initialization
def init(data_size):
	data = []

	# Target setup
	target = random.randint(1, data_size)

	# Data setup
	try:
		data = random.sample(range(1,data_size), data_size-1)
	except:
		print('Sample size exceeded.')
		exit()
	return data, target

def average(nums):
	return sum(nums) / len(nums)


# Draw a histogram graph and present distribution of smaple data
# plt.hist(data, bins = 20)
# plt.show()

#  0 1 2 3 4 5 6 7 8
# [1,2,3,4,5,6,7,8,9]



def binary_search(nums, target):
	lo, hi = 0, len(nums) - 1	
	count_binary_search = 0
	while lo < hi:
		count_binary_search += 1
		mid = lo + (hi - lo) // 2
		# print(lo, hi, mid, target, nums[mid])
		if target > nums[mid]:
			lo = mid + 1
		else:
			hi = mid

	if nums[lo] == target:
		return lo, count_binary_search
	else:
		return -1, count_binary_search


def linear_search(nums, target):
	count_linear_search = 0
	for i in range(len(nums)):
		if nums[i] == target:
			return i, count_linear_search
		else:
			count_linear_search += 1
	return -1, count_linear_search


# start, end variables for time calculation
# start = datetime.now()
# end = datetime.now()
# print(str(end-start)[5:])


# run linear search and binary search
for i in range(test_count):
	# Initialize numbers in the list and target
	data, target = init(data_size)

	result_linear, count_linear = linear_search(data, target)
	linear_count.append(count_linear)

	result_binary, count_binary = binary_search(data, target)
	binary_count.append(count_binary)

print('The Number of Test: ', test_count)
print('The Size of list (n): ', data_size)
print('Log(n): ', round(math.log2(data_size), 2),'\n')

# Calculate count and average of binary search (close to logn) 
# print(linear_count)
print('Linear search average: ',round(average(linear_count), 2))
print('Linear search population variance: ', round(statistics.pvariance(linear_count), 2))
print('Linear search population standard deviation: ', round(statistics.pstdev(linear_count), 2),'\n')

# Calculate count and average of binary search (close to logn) 
# print(binary_count)
print('Binary search average: ', round(average(binary_count), 2))
print('Binary search population variance: ', round(statistics.pvariance(binary_count), 2))
print('Binary search population standard deviation: ', round(statistics.pstdev(binary_count), 2),'\n')

# Draw scatter plot for liner search and binary search
linear_color = 10
binary_color = 20
area =  20

x_axis = [x for x in range(test_count)]

# plt.scatter(x_axis, linear_count, s=area, alpha=1.0)
# plt.scatter(x_axis, binary_count, s=area, alpha=1.0)
# plt.show()

# Draw histogram for liner search and binary search
num_bins = 10
n, bins, patches = plt.hist(linear_count, num_bins, facecolor='blue', alpha=0.5)
plt.show()
n, bins, patches = plt.hist(binary_count, num_bins, facecolor='red', alpha=0.5)
plt.show()