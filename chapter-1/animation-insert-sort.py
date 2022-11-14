#!/usr/bin/env python3

"""
/* C code */
insert_sort(item [], int n)
{
    int i, j /* counters */

    for(i=1; i<n; i++){
        j=i;
        while((j>0) && (s[j] < s[j-1])){
            swap(%s[j], &[j-1]);
            j = j-1;
        }
    }
}
"""
# Try to implement INSERTSORT diagram later in python

def insertionSort(arr):
	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):
		key = arr[i]
		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key


# Driver code to test above
arr = [9,3,4,7,9,2,3,4,5,10,2,3] # 11 places
insertionSort(arr)
for i in range(len(arr)):
	print ("% d" % arr[i])

"""
time complexity O(N^2)
Auxiliary Space O(1)
"""

