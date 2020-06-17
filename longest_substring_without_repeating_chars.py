def lengthOfLongestSubstring(s: str) -> int:
    if s == "":
        return 0
    charset = {}
    charset[s[0]] = 1
    head = 0
    tail = 1
    maxLength = 1

    while tail != len(s):
        while(s[tail] in charset and charset[s[tail]] > 0 and head < tail):
            charset[s[head]] -= 1
            head += 1
        if s[tail] in charset:
            charset[s[tail]] += 1
        else:
            charset[s[tail]] = 1
        tail += 1
        # update maxLength
        if tail - head > maxLength:
            maxLength = tail - head
    return maxLength


print(lengthOfLongestSubstring("pwwkew"))
