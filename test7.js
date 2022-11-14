// # 7) Write a JavaScript function to find the unique elements from two arrays. [2.5 marks]
// # Test Data: console.log(difference([1, 2, 3, 4, 5], [1, [2], [3, [[4]]],[5,6]]));
// # - Output: ["1", "2", "3", "4", "5", "6"]


const a = ([1, 2, 3, 4, 5], [1, [2], [3, [[4]]],[5,6]])
const unique = [...new Set(a)]
console.log(unique)