# Python program to find number of AP
# subsequences in the given array

''' Count of AP (Arithmetic Progression) Subsequences in an array
Difficulty Level : Hard
Last Updated : 21 May, 2021
Given an array of n positive integers. The task is to count the number of Arithmetic Progression 
subsequence in the array. Note: Empty sequence or single element sequence is Arithmetic Progression. 1 <= arr[i] <= 1000000.
Examples: 
 

Input : arr[] = { 1, 2, 3 }
Output : 8
Arithmetic Progression subsequence from the 
given array are: {}, { 1 }, { 2 }, { 3 }, { 1, 2 },
{ 2, 3 }, { 1, 3 }, { 1, 2, 3 }.

Input : arr[] = { 10, 20, 30, 45 }
Output : 12

Input : arr[] = { 1, 2, 3, 4, 5 }
Output : 23

'''

MAX = 1000001

def numofAP(a, n):

	# initializing the minimum value and
	# maximum value of the array.
	minarr = +2147483647
	maxarr = -2147483648

	# Finding the minimum and
	# maximum value of the array.
	for i in range(n):
		minarr = min(minarr, a[i])
		maxarr = max(maxarr, a[i])
	

	# dp[i] is going to store count of APs ending
	# with arr[i].
	# sum[j] is going to store sun of all dp[]'s
	# with j as an AP element.
	dp = [0 for i in range(n + 1)]
	

	# Initialize answer with n + 1 as single
	# elements and empty array are also DP.
	ans = n + 1

	# Traversing with all common difference.
	for d in range((minarr - maxarr), (maxarr - minarr) + 1):
		sum = [0 for i in range(MAX + 1)]
		
		# Traversing all the element of the array.
		for i in range(n):
		
			# Initialize dp[i] = 1.
			dp[i] = 1

			# Adding counts of APs with given differences
			# and a[i] is last element.
			# We consider all APs where an array element
			# is previous element of AP with a particular
			# difference
			if (a[i] - d >= 1 and a[i] - d <= 1000000):
				dp[i] += sum[a[i] - d]

			ans += dp[i] - 1
			sum[a[i]] += dp[i]

	return ans

# Driver code
arr = [ 1, 2, 3 ]
n = len(arr)

print(numofAP(arr, n))


