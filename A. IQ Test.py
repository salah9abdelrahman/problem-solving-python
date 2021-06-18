""""
####
.#..
####
....

####
....
####
....


"""

s = []
doable = False
for i in range(4):
    s.append(input())


for i in range(3):
    j, x = 0, 2
    if doable:
        break
    l1 = s[i]
    l2 = s[i+1]
    for l in range(3):
        s1 = l1[j:x]
        s2 = l2[j:x]
        dots, hashes = s1.count("."), s1.count("#")
        dots += s2.count(".")
        hashes += s2.count("#")
        j += 1
        x += 1
        if max(dots, hashes) >= 3:
            doable = True
            break

if doable:
    print("YES")
if not doable:
    print("NO")
