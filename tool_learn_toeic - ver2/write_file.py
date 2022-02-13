l = "a a ab c c d a"
l = l.split()
l = [i+"\n" for i in l]

def write_file(l):
    with open("test.txt", encoding = 'utf-8', mode='w') as f:
        f.writelines(l)


write_file(l)