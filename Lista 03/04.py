fibo = [1, 1]
i = 0
num = int(input("Insira um número: "))
while(num > len(fibo)):
    fibo.append(fibo[i] + fibo[i+1])
    i= i+ 1
print("Fibo(%d) = %d" % (num, fibo[num -1]))    
