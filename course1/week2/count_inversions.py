import random
#naive way
DEBUG = False

def dev_log(*a):
	if DEBUG:
		print(a)

#desc: counts number of inversions in O(n^2) number of comparisons
#params: a, array in arbitrary order 
#return: number of inversions
def naive_count_inv(a):
	c = 0
	for i in range(len(a)-1):
		for j in range(i+1,len(a)):
			dev_log('idx',a[i],a[j])
			dev_log('values',a[i],a[j])
			if a[i] > a[j]:
				dev_log('adding')
				c += 1
	return c

#desc: counts number of inversions between two ordered halves in linear time
#params: left, right: left and right ordered halves of bigger array
#returns: ordered array and number of split inversions (amount of times that
#		  element in the right is less than an element in the left)
def count_split(left,right):
	j,k = 0,0
	c = 0
	ordered = []
	for i in range(len(left)+len(right)):
		if right[k]<left[j]:
			c += len(left) - j
			ordered.append(right[k])
			k += 1
			if k>= len(right):
				ordered = ordered + left[j:]
				return ordered, c
		else:
			ordered.append(left[j])
			j += 1
			if j >= len(left):
				ordered = ordered + right[k:]
				return ordered, c
	return ordered, c

#desc: counts number of inversions and orders an input array in O(n lon_n) number of comparisons
# params: left, right: a, array in arbitrary order
#returns: ordered array and number of splits in it
def fast_count_inv(a):
	#base case
	if len(a)==1:
		return a, 0#I'm gonna have trouble with this not being a fucking list
	if len(a)==2:
		if a[1] < a[0]:
			return [a[1],a[0]], 1
		return a, 0
	#recursive part
	split = len(a)//2
	right = a[split:]
	left = a[:split]
	left, left_invs = fast_count_inv(left)
	right, right_invs = fast_count_inv(right)
	ordered, split_invs = count_split(left,right)
	return ordered, left_invs + right_invs + split_invs

#ok let's test
MAX_LEN = 100
MAX_VAL = 100
while True:
	arr_len = random.randint(1,MAX_LEN)
	arr = random.choices(range(MAX_VAL+1),k=arr_len)
	ordered, fast = fast_count_inv(arr)
	if fast != naive_count_inv(arr):
		print(arr,ordered)
		break

_, invs = fast_count_inv(test)