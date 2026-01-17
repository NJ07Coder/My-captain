n0 = 0
n1 = 1

endNum = input("Enter the number of terms: ")
for i in range(int(endNum)):
    print(n0)
    nth = n0 + n1
    n0 = n1
    n1 = nth
    
