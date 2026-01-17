inpList = input("Enter numbers separated by spaces: ").split()
outList = []

for num in inpList:
    if int(num) >= 0:
        outList.append(num)
        
print("Positive numbers:", ' '.join(outList))