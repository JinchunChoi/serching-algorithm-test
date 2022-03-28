# print('Hello World!')
import matplotlib.pyplot as plt
import random
from datetime import datetime

# start = datetime.now()

# Parameters for the experiment
data_size = 1000
test_count = 100

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

# data.sort()

# end = datetime.now()
# print(str(end-start)[5:])
# print(data)
# print(target)

# Draw a histogram graph and present distribution of smaple data
# plt.hist(data, bins = 20)
# plt.show()

#  0 1 2 3 4 5 6 7 8
# [1,2,3,4,5,6,7,8,9]

binary_count = []

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



for i in range(test_count):
	data, target = init(data_size)
	result, count = binary_search(data, target)
	binary_count.append(count)

print(binary_count)
print(round(average(binary_count), 2))