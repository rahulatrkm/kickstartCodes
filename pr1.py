f = open("A-large.in", "r")
lines = f.readlines()
#print(lines)
fo = open("opr1.txt", "w")
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
    tr = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if (a[i] == (a[j]*a[k])) or (a[j] == (a[i]*a[k])) or (a[k] == (a[i]*a[j])):
                    tr += 1
    fo.write("Case #{}: {}\n".format(case, tr))
    print("Case #{}: {}".format(case, tr))
