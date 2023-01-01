use std::collections::HashMap;
use std::string::String;
struct Solution {}

impl Solution {
    fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut h = HashMap::<String, Vec<String>>::new();

        for s in strs {
            h.entry(Self::get_sorted(&s)).or_default().push(s);
        }

        h.into_iter().map(|(_, v)| v).collect()
    }

    fn get_sorted(s: &str) -> String {
        let mut chars: Vec<_> = s.chars().collect();
        chars.sort();
        chars.iter().collect()
    }
}
