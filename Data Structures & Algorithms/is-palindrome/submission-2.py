class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = []
        for c in "".join(s.lower().split()):
            if c.isalnum():
                ans.append(c)
        print(ans)
        i, j = 0, len(ans) - 1
        while i <= j:
            if ans[i] != ans[j]:
                return False
            i += 1
            j -=1
        return True
            