// Problem link -
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

use std::collections::HashSet;
use std::cmp::max;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let (mut l, mut r) = (0,0);
        let mut ans = 0;
        let mut n = s.len();
        let mut c = HashSet::new();
        let chars: Vec<char> = s.chars().collect();
        for r in 0..n {
            while c.contains(&chars[r]) {
                c.remove(&chars[l]);
                l+=1;
            }
            ans = max(r-l+1, ans);
            c.insert(chars[r]);
        }
        ans as i32
    }
}
