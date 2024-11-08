// Problem link:
// https://leetcode.com/problems/permutation-difference-between-two-strings/

use std::collections::HashMap;

impl Solution {
    pub fn find_permutation_difference(s: String, t: String) -> i32 {
        let mut temp = HashMap::new();
        let mut ans: i32 = 0;
        for (i,v) in t.chars().enumerate() {
            temp.insert(v,i as i32);
        }
        for (i,v) in s.chars().enumerate() {
            if let Some(&p) = temp.get(&v) {
                ans += (i as i32 - &p).abs();
            }
        }
        ans
    }
}
