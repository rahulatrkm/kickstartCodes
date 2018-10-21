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
    temp = list(map(int,lines[line].split()))
    line += 1
    n = temp[0]
    m = temp[1]
    e = temp[2]
    sr = temp[3]
    sc = temp[4]
    tr = temp[5]
    tc = temp[7]
    v = []
    for i in range(n):
        v.append(list(map(int,lines[line].split())))
        line += 1
