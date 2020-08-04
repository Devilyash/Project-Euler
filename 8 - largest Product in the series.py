n = int(input("Enter 1000 digit number: "))
n = str(n)
maximum = 0
for i in range(len(n)-12):
    
    prod = int(n[i])*int(n[i+1])*int(n[i+2])*int(n[i+3])*int(n[i+4])*int(n[i+5])*int(n[i+6])*int(n[i+7])*int(n[i+8])*int(n[i+9])*int(n[i+10])*int(n[i+11])*int(n[i+12])
    maximum = max(maximum, prod)

print(maximum)
