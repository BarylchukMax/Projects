import random
a=random.randint(1,10)
print("Вгадай число від 1 до 10")
b=int(input())
while a!=b:
    print("Спробуй ще раз")
    b=int(input())
else:
    print("Вгадав")
    
    

