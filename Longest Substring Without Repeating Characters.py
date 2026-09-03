class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n

        '''
        hold max length seen yet in out

        at each index i in range(s)
            update end to current-pos
            check if sth char exists in current substring
                if yes, update start to current-pos-of-sth-char-plus-one
            check new length against max length 'out', update if greater

        return out


        '''

        out = 1
        d: dict[str, int] = {} # letter to index lookup dictionary
        start = 0
        for end in range(n):
            char = s[end]
            if char not in d:
                d[char] = end
                out = max(out, end - start + 1)
            else:
                new_start = d[char] + 1
                for letter in s[start:new_start]:
                    del d[letter]
                
                start = new_start
                d[char] = end

        assert out <= n
        return out