// Problem Link -
// https://leetcode.com/problems/number-of-good-pairs/

impl Solution {
    pub fn num_identical_pairs(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut cnt = 0;
        for i in 0..n {
            for j in i+1..n {
                if nums[i]==nums[j] {
                    cnt += 1;
                }
            }
        }
        cnt
    }
}
