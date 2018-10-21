f = open("A-small.in", "r")
lines = f.readlines()
#print(lines)
fo = open("opr.txt", "w")
case = 0
line = 0
t = int(lines[line])
line += 1
#print(t)
for _ in range(t):
    case += 1
    n = int(lines[line])
    line += 1
    #print(line)
    #print(n)
    a = list(map(int, lines[line].split()))
    line += 1
    a = sorted(a, reverse=True)
    #print(a)
    tr = 0
    for i in range(n):
        if ((i+1) < n):
            for j in range(i+1,n):
                if a[j] != 0 :
                    temp = a[i]%a[j]
                    temp1 = int(a[i]/a[j])
                    #print(temp1)
                    if temp == 0 and (a[(j+1):].count(int(temp1)) > 0):
                        tr += 1
    fo.write("Case #{}: {}\n".format(case, tr))
    print("Case #{}: {}".format(case, tr))
