def sort_ascending(arr: list[int]) -> list[int]:
    
    # Create function which find index pf the smallest number
    def find_smallest(arr: list[int]) -> int:
        smallest = arr[0]
        smallest_index = 0
        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        return smallest_index
    
    # Sorting process
    sorted_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr


# Some tests
# arr = [5, 5, 5, 5, 5]
# arr = [5, 4, 3, 2, 1]
# arr = [-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]
# arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# arr = [5]

print(sort_ascending([-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]))

