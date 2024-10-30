def fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

num = int(input("Digite um número: "))

if fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
