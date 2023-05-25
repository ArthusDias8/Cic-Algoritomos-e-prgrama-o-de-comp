valores_dos_peixes = []
todos_os_peixe = []
peixe, valor = input().split()
valor = float(valor)
valores_dos_peixes.append(valor)
todos_os_peixe.append(peixe)
if peixe == 'fim':
    print("+--------------------+--------------------+")
    print("|        peixe       |      preço   R$    |")
    print("+--------------------+--------------------+")
    print("|           Hoje não tem peixe            |")
    print("+--------------------+--------------------+")
while peixe != 'fim':
    peixe, valor = input().split()
    valor = float(valor)
    valores_dos_peixes.append(valor)
    todos_os_peixe.append(peixe)
todos_os_peixe.pop()
valores_dos_peixes.pop()
if len(todos_os_peixe) == 1:
    print("+--------------------+--------------------+")
    print("|        peixe       |      preço   R$    |")
    print("+--------------------+--------------------+")
    print("| {}               |              {:.2f} |".format(todos_os_peixe[0],valores_dos_peixes[0]))
    print("+--------------------+--------------------+")
if len(todos_os_peixe) > 1:
    valores_dos_peixes.pop()
    todos_os_peixe.pop()
    print("+--------------------+--------------------+")
    print("|        peixe       |      preço   R$    |")
    for i in range(len(valores_dos_peixes)):
        print("+--------------------+--------------------+")
        print(f"| {todos_os_peixe[i]:<19}|{ valores_dos_peixes[i]:>19.2f} |")
    menor_valor = min(valores_dos_peixes)
    indiceDoMenorPreco = valores_dos_peixes.index(menor_valor)
    peixeMenorPrexo = todos_os_peixe[indiceDoMenorPreco]
    print("+--------------------+--------------------+")
    print("|         Cambada de menor preço          |")
    print(f"| {peixeMenorPrexo:<19}|{menor_valor:>19} |")
    print("+--------------------+--------------------+")
