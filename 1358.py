def numberOfSubstrings(self, s):
        seen={'a':-1,'b':-1,'c':-1}
        count=0

        for i,char in enumerate(s):
            if char in seen:
                seen[char] = i
            count += min(seen.values()) + 1
        return count