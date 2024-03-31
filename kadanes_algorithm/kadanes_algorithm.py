# Here implementation Kadane's algorithm for finding max sum among subarrays

def get_max_sub_sum(arr: list[int]) -> int:
    max_sum = 0
    current_sum = 0
    
    for item in arr:
        current_sum += item
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:    # if current_sum is negative then it is equal to 0
            current_sum = 0
            
    return max_sum


# Some tests
# arr = [1, 2, -4, 4, 5, -2, 10] return 17
# arr = [-1, -2, -3, -4, -5] return 0
# arr = [1, -2, 3, 4, -5] return 7
# arr = [-1, -2, 3, 4, -5] return 7
# arr = [1, 2, -4, 4, 5] return 9