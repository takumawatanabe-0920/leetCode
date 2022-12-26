use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut s_map = HashMap::<char, i32>::new();
        for s_word in s.chars() {
            let num = s_map.get(&s_word);

            match num {
                None => {
                    s_map.insert(s_word, 1);
                    None
                }
                Some(n) => {
                    println!("Num: {}", n);
                    Some(s_map.insert(s_word, n + 1))
                }
            };
        }

        for t_word in t.chars() {
            let num = s_map.get(&t_word);

            match num {
                None => {
                    s_map.insert(t_word, -1);
                    None
                }
                Some(n) => {
                    println!("Num: {}", n);
                    Some(s_map.insert(t_word, n - 1))
                }
            };
        }

        for (_, value) in &s_map {
            if *value != 0 {
                return false;
            }
        }

        return true;
    }
}
