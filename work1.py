N = int(input("Введите количество монет "))
ol = reshka = 0
for i in range(N):
    x = int(input("Орел(1) или решка(0)? "))
    if x == 1:
        ol += 1
    else:
        reshka += 1
if ol < reshka:
    print(f"Переверните {ol} монет с орла на решку, их меньше всего")
elif ol == reshka:
    print(f"Количество орлов и решек одинаково, по {ol} штук")
else:
    print((f"Переверните {reshka} монет с решки на орла, их меньше всего"))
    