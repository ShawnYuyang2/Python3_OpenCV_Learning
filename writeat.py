

file = open(r'C:\Users\zx\Desktop\photo2\at.txt', 'a')
for s in range(1,22):
    for i in range((s - 1) * 10 + 1, (s * 10) + 1):
        file.write('C:/Users/zx/Desktop/photo2/s%d/%d.jpg;%d\n' % (s, i, s))

file.close()