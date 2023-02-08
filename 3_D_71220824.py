MA = int(input("Masukan angka: "))
print("")

for i in range (MA):
    print('* '*i, ('* '(MA-i))+('* '*(MA(i+1))))
