# duplicate
def duplicate(s):
    if len(s) == 0:
        return True
    if len(s) % 2 !=0:
       return False
    mid = len(s)//2
    s1 = s[0 : mid]
    s2= s[mid : ]
    if s1 == s2:
        s1 = s1[1 : mid]
        return duplicate(s1)
    else:
        return False

print(duplicate("allall"))
print(duplicate("htmmtmmhtmmtmm"))
print(duplicate("mhamh"))