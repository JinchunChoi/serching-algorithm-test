# print('Hello World!')
import matplotlib.pyplot as plt
import random

# rand = random.uniform(1,10000)
data = []
# data = random.randint(0,10000)

# i = 0
# while len(data) < 100:
# # while i < 100:
# 	rand = int(random.uniform(1,100000))

# 	if rand not in data:
# 		data.append(rand)
# 	i += 1

# 	# else:
# 	# 	i += 1

data.sort()

plt.hist(data, bins = 10)
plt.show()