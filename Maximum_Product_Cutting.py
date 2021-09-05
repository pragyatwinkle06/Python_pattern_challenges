# The main function that returns maximum
# product obtainable from a rope of length n

''' Maximum Product Cutting | DP-36
Difficulty Level : Medium
Last Updated : 14 May, 2021
Given a rope of length n meters, cut the rope in different parts of integer lengths in a way that maximizes product of
lengths of all parts. You must make at least one cut. Assume that the length of rope is more than 2 meters. 
Examples: 

Input: n = 2
Output: 1 (Maximum obtainable product is 1*1)

Input: n = 3
Output: 2 (Maximum obtainable product is 1*2)

Input: n = 4
Output: 4 (Maximum obtainable product is 2*2)

Input: n = 5
Output: 6 (Maximum obtainable product is 2*3)

Input: n = 10
Output: 36 (Maximum obtainable product is 3*3*4)  '''

def maxProd(n):
	
	# Base cases
	if (n == 0 or n == 1):
		return 0

	# Make a cut at different places
	# and take the maximum of all
	max_val = 0
	for i in range(1, n - 1):
		max_val = max(max_val, max(i * (n - i), maxProd(n - i) * i))

	#Return the maximum of all values
	return max_val;


# Driver program to test above functions
print("Maximum Product is ", maxProd(10));
	

