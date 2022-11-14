// # 6) Write a JavaScript program to compute the union of two arrays. [5 marks]
// # Sample Data : console.log(union([1, 2, 3], [100, 2, 1, 10]));
// # Output: [1, 2, 3, 10, 100]


const arr1 = [1, 2, 3]
const arr2 = [100, 2, 1, 10]

const union = Array.from(new Set([...arr1, ...arr2]));

console.log(union)
