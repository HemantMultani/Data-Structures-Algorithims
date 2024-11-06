// Problem link -
// https://leetcode.com/problems/shuffle-the-array/

impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> {
        let mut ans: Vec<i32> = Vec::new();
        for i in 0..n as usize {
            ans.push(nums[i]);
            ans.push(nums[i+n as usize]);
        }
        ans
    }
}

"USIZE"
"In Rust, the usize type is a platform-specific integer type used for indexing and sizes. The size of usize depends on the computer's architecture:

On a 64-bit machine, usize is 64 bits.
On a 32-bit machine, usize is 32 bits."

"In Rust, array indexing or slicing is expected to be in usize not integer"

//-------------------------
"Extending a Vector with Multiple Elements"

let other_nums = vec![1, 2, 3];
ans.extend(other_nums); // Adds all elements of `other_nums` to `ans`

impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> {
        let mut ans: Vec<i32> = Vec::new();
        for i in 0..n as usize {
            ans.extend(vec![nums[i], nums[i+n as usize]]);
        }
        ans
    }
}
