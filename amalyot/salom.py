file = open ("familiya.txt", "r")
a=file.read().split('\n')

sorted_list = sorted(a, key=lambda b: b.split()[0])


for i in sorted_list:
    print(i)

file.close()

