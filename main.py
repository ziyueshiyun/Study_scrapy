def counter_url(fname1: str, fname2: str):
    s1 = ''
    s2 = ''
    with open(fname1, "rt") as fin1:
        for line in fin1.readlines():
            line = line.strip()
            s1 = line
            break
    with open(fname2, "rt") as fin1:
        for line in fin1.readlines():
            line = line.strip()
            s2 = line
            break
    for i in range(0,2000):
        if s1[i] == s2[i]:
            print(i)
        else:
            return

counter_url("url1.txt", "url2.txt")