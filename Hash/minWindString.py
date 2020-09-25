import collections

t= 'bca'
s='bsldjflkbca'

i = I = J = 0
need, missing = collections.Counter(t), len(t)
print(i,I,J)
for j, c in enumerate(s, 1):
    missing -= need[c] > 0
    need[c]-=1
    if not missing:
        while i<j and need[s[i]]<0:
            need[s[i]]+=1
            i+=1
        if not J or j-i<=J-I:
            I,J = i,j
    print(missing,need[c])