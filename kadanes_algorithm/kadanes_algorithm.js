// Here implementation Kadane's algorithm for finding max sum among subarrays

const getMaxSubSum = arr => {
    let maxSum = 0;
    let currentSum = 0;

    for (let item of arr) {
        currentSum += item;
        maxSum = Math.max(maxSum, currentSum);
        if (currentSum < 0) currentSum = 0;    // if currentSum is negative then it is equal to 0
    }

    return maxSum;
}


// Some tests
// arr = [1, 2, -4, 4, 5, -2, 10] return 17
// arr = [-1, -2, -3, -4, -5] return 0
// arr = [1, -2, 3, 4, -5] return 7
// arr = [-1, -2, 3, 4, -5] return 7
// arr = [1, 2, -4, 4, 5] return 9