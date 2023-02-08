print("---------- Nilai Ke 1 ----------")
N1 = int(input("Nilai Harian : "))
N2 = int(input("Nilai UTS : "))
N3 = int(input("Nilai UAS : "))

print("---------- Nilai Ke 2 ----------")
M1 = int(input("Nilai Harian : "))
M2 = int(input("Nilai UTS : "))
M3 = int(input("Nilai UAS : "))

print("---------- Total Nilai ----------")
Nh1  = int((N1) *30/100)
Nu1  = int((N2) *30/100)
Nus1 = int((N3) *40/100)

Nh2  = int((M1) *30/100)
Nu2  = int((M2) *30/100)
Nus2 = int((M3) *40/100)

tot= ((Nh1+Nu1+Nus1) + (Nh2+Nu2+Nus2)) /2

print(tot)