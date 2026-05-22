class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> zeroes(26);
        if (s.length() != t.length()) {
            return false;
        }
        for (int i = 0; i < s.length(); ++i) {
            zeroes[s[i] - 'a']++;
            zeroes[t[i] - 'a']--;
        }
        for (int i = 0; i < 26; ++i) {
            if (zeroes[i] != 0) {
                return false;
            }
        }
        return true;
    }
};
