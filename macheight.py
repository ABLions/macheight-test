# function in Python that takes a list of integers and a target sum as inputs, 
# and returns a list of tuples containing pairs of integers from the input list 
# that add up to the target sum:

def find_pairs(array_numbers, target_sum):
    # Create an empty dictionary to store the difference between
    # the target sum and each number in the input list as a key
    # and the number itself as a value
    diff_dict = {}
    # Create an empty list to store the pairs of integers
    pairs = []
    for num in array_numbers:
        # Calculate the difference between the target sum and the current number
        diff = target_sum - num
        # If the difference is in the dictionary, add the current number and the
        # number associated with the difference to the pairs list
        if diff in diff_dict:
            pairs.append((diff, num))
        else:
            # Otherwise, add the current number and its difference to the dictionary
            diff_dict[num] = diff
    print(pairs)

# call the function with the arguments
array_numbers = [1,9,5,0,20,-4,12,16,7,12]
target_sum = 12
find_pairs(array_numbers, target_sum)

# The function first creates an empty dictionary to store the difference between the target sum and 
# each number in the input list as a key and the number itself as a value. It then creates an empty 
# list to store the pairs of integers. The function then iterates through the input list of numbers. 
# For each number, it calculates the difference between the target sum and the current number. 
# If the difference is already in the dictionary, it adds the current number and the number associated 
# with the difference to the pairs list. Otherwise, it adds the current number and its difference to the 
# dictionary.

# This solution has a time complexity of O(n) because it loops through the input list once and performs 
# a constant time lookup in the dictionary.

# You can run this fuction from terminal with the following command py .\macheight.py, 
# feel free to change the array_numbers and target_sum arguments
