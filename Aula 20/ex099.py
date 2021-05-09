from time import sleep


def maior(* num):
    print(f'Analisando os valores recebidos...')
    sleep(1.5)
    for v in num:
        print(v, end=' ')
        sleep(0.5)
    print()
    sleep(1)
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) != 0:
        print(f'O maior valor informado foi {max(num)}.')
    print("=-" * 30)


print("=-" * 30)
maior(2, 9, 4, 5, 7, 1)
maior(3, 19, 0, 2, 65, 18)
maior()
maior(-1, 10)
maior(34, 1000, 5, 2, -1000)
maior(9)