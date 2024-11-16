// Problem Link:
// https://leetcode.com/problems/longest-repeating-character-replacement/


use std::collections::HashMap;
use std::cmp::max;

impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let (mut l, mut ans, n) = (0,0,chars.len());
        let mut map = HashMap::new();
        let mut max_freq = 0;
        for r in 0..n {
            *map.entry(chars[r]).or_insert(0) += 1;
            max_freq = max(max_freq, *map.get(&chars[r]).unwrap());
            if (r-l+1) as i32 - max_freq > k {
                if let Some(freq) = map.get_mut(&chars[l]){
                    *freq -= 1;
                }
                l+=1;
            }
            ans = max(ans, r-l+1);
        }
        ans as i32
    }
}
