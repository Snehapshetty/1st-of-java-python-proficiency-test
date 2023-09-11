Two pointers + Hash Table

Define a hash table to record the characters in the current window. Let i and j represent the start and end positions of the non-repeating substring, respectively. The length of the longest non-repeating substring is recorded by ans.

For each character s[j] in the string s, we call it c. If c exists in the window s[i..j-1], we move to the right until s[i..j-1] does not contain c. Then we add c to the hash table. At this time, the window 
 s[i..j] does not contain repeated elements, and we update the maximum value of ans.

Finally, return ans.

The time complexity is o(n), where n represents the length of the string s.

Two pointers algorithm template:

for (int i = 0, j = 0; i < n; ++i) {
    while (j < i && check(j, i)) {
        ++j;
    }
    // logic of specific problem
}
Python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        i = ans = 0
        for j, c in enumerate(s):
            while c in ss:
                ss.remove(s[i])
                i += 1
            ss.add(c)
            ans = max(ans, j - i + 1)
        return ans
