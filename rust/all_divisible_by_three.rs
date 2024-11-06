// Problem link -
// https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let mut cnt = 0;
        for i in nums {
            let rem = i % 3;
            if rem < 3-rem {
                cnt += rem;
            } else {
                cnt += 3-rem
            }
        }
        cnt
    }
}
