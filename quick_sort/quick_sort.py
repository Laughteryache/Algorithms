# All elements have to be non-eqivalent

def quick_sort(lst: list[int]) -> list[int]:

    # Base Case
    if len(lst) < 2:
        return lst
    
    # Recursion Case
    else:
        pivot = len(lst) // 2
        less = [i for i in lst[:pivot] + lst[pivot:] if i < lst[pivot]]
        greater = [i for i in lst[:pivot] + lst[pivot:] if i > lst[pivot]]

        return quick_sort(less) + [lst[pivot]] + quick_sort(greater)

# Some tests
# lst = [5, 4, 3, 2, 1] lst = [1, 2, 3, 4, 5]
# lst = [-3, -1, -4, -1, -5, -9, -2, -6, -5 ] lst = [-9, -6, -5, -4, -3, -2, -1]
# lst = [5] lst = [5]
# lst = [1, 71, 92392, 191, -1111111, 192421] lst = [-1111111, 1, 71, 191, 92392, 192421]