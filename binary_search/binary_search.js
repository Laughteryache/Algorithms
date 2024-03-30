const binarySearch = (sorted_arr, target) => {

    // Set borders
    let left = 0;
    let right = sorted_arr.length - 1;

    // Start searching
    while (left <= right) {

        let mid = Math.floor((left + right) / 2);
        let guess = sorted_arr[mid];

        if (guess === target) return mid;

        if (guess > target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return null;
}

// Some tests
// lst = [1, 2, 2, 2, 3, 4, 5] x = 5
// lst = [i for i in range(1000001)] x = 999999
// lst = [5] x = 5
// lst = [1, 3, 5, 7, 9] x = 4
// lst = [1, 3, 5, 7, 9] x = 5
// lst = [5] x = 4