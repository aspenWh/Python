
def is_odd(numero: int):
    odd = True
    if numero % 2 == 0:
        odd = False
    if numero % 2 != 0:
        odd = True

    return odd 

numbers = [1,3,6,7,5]

for num in numbers:
    if is_odd(num):
        print(f"{num} is odd")
    else:
        print(f"{num} is even")

print("odd")

    #landa function is_odd = lambda numero: numero % 2 != 0