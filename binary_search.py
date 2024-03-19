def binary_search(sorted_arr: list, to_search: int) -> int | None:
    
    # Set borders
    left = 0
    right = len(sorted_arr) - 1
    
    # Start the searching
    while left <= right:
        mid = (left + right) // 2
        guess = sorted_arr[mid]
        if guess == to_search:
            return mid
        if guess > to_search:
            right = mid - 1
        else:
            left = mid + 1

    return None

# Some tests
# lst = [1, 2, 2, 2, 3, 4, 5] x = 5
# lst = [i for i in range(1000001)] x = 999999
# lst = [5] x = 5
# lst = [1, 3, 5, 7, 9] x = 4
# lst = [1, 3, 5, 7, 9] x = 5


print(binary_search([1, 3, 5, 7, 9], 4))