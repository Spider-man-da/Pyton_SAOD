from datetime import datetime as t

haystack = "jjabcdefg"
needle = "bcd"

def prefix(s):
    v = [0]*len(s)
    for i in range(1,len(s)):
        k = v[i-1]
        while k > 0 and s[k] != s[i]:
            k = v[k-1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v
def Knuth_morris_pratt(needle,haystack):
    index = -1
    f = prefix(haystack)
    k = 0
    for i in range(len(needle)):
        while k > 0 and haystack[k] != needle[i]:
            k = f[k-1]
        if haystack[k] == needle[i]:
            k = k + 1
        if k == len(haystack):
            index = i - len(haystack) + 1
            break
    return index

def for_boyer_more(x):
    d = {}
    lenX = len(x)
    for i in range(len(x)):
        d[ord(x[i])] = lenX - i
    return d
def Boyer_moore(haystack, needle):
    d = for_boyer_more(needle)
    lenX = i = j = k = len(needle)
    while j > 0 and i<=len(haystack):
        if haystack[k - 1] == needle[j - 1]:
            k -= 1
            j -= 1
        else:
            i += d[ord(haystack[i])]
            j = lenX
            k = i
    if j <= 0:
        return k
    return -1


class last_occurrence(object):
    def __init__(self, pattern, alphabet):
        self.occurrences = dict()
        for letter in alphabet:
            self.occurrences[letter] = pattern.rfind(letter)

    def __call__(self, letter):
        return self.occurrences[letter]
def boyer_moore(text, pattern):
    alphabet = set(text)
    last = last_occurrence(pattern, alphabet)
    m = len(pattern)
    n = len(text)
    i = m - 1  # text index
    j = m - 1  # pattern index
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            l = last(text[i])
            i = i + m - min(j, 1 + l)
            j = m - 1
    return -1


haystack = input("Enter string: ")
needle = input("Enter substring: ")
start_time = t.now()
print("Index:", Knuth_morris_pratt(haystack.lower(),needle.lower()))
print(t.now() - start_time)


haystack = input("Enter string: ")
needle = input("Enter substring: ")
start_time = t.now()
print("Index:", boyer_moore(haystack.lower(),needle.lower()))
print(t.now() - start_time)

