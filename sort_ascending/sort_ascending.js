const sortAscending = arr => {

    // Create function which find index of the smallest number
    const findSmallest = arr => {
        let smallest = arr[0];
        let smallestIndex = 0;
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] < smallest) {
                smallest = arr[i];
                smallestIndex = i;
            }
        }
        return [smallest, smallestIndex];
    }

    // Sorting process
    let sortedArr = [];
    let arrayLength = arr.length;
    for (let i = 0; i < arrayLength; i++) {
        let [smallest, smallestIndex] = findSmallest(arr);
        arr.splice(smallestIndex, 1);
        sortedArr.push(smallest);
    }
    return sortedArr;
}

// Some tests
// arr = [5, 5, 5, 5, 5]
// arr = [5, 4, 3, 2, 1]
// arr = [-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]
// arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
// arr = [5]