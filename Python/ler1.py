def primo_bool(x: int) -> bool:
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


n = int(input("Digite um número: "))

for i in range(1, n + 1):
    if primo_bool(i):
        print(i)