class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        need = Counter(t)
        have = {}
        need_count = len(need)
        have_count = 0
        res, res_len = [-1, -1],float("inf")
        left = 0

        for right, c in enumerate(s):
            have[c] = have.get(c, 0) + 1
            if c in need  and have[c] == need[c]:
                have_count += 1

            while have_count == need_count:
                if(right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    have_count -= 1
                left += 1
            
        l, r = res
        return s[l:r + 1] if res_len != float("inf") else ""
