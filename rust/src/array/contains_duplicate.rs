use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut map = HashMap::new();

        for num in nums {
            if map.contains_key(&num) {
                return true;
            } else {
                map.insert(num, 1);
            }
        }

        return false;
    }
}
