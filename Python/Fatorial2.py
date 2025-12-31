#Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

def fatorial(num: int) -> int:
    
    if num == 0:
        return 1
    
    return num * fatorial(num - 1)

try:
    num = fatorial(int(input(': ')))
    print(num)
except RecursionError:
    print('Número gigante irmão, tão gigante que cê causou um erro que tive que tratar')
except ValueError:
    print('CÊ NÃO SABE O QUE É NÚMERO NÃO IRMÃO?')
