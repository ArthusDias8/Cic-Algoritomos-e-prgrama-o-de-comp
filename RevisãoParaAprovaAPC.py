'''def transformacao(r):
    new = ''
    if r // 16 == 10:
        new += 'A'
    if r // 16 == 11:
        new += 'B'
    if r // 16 == 12:
        new += 'C'
    if r // 16 == 13:
        new += 'D'
    if r // 16 == 14:
        new += 'E'
    if r // 16 == 15:
        new += 'F'
    if r // 16 < 10:
        inteiro = r // 16
        inteiro = str(inteiro)
        new += inteiro

    if r % 16 == 10:
        new += 'A'
    if r % 16 == 11:
        new += 'B'
    if r % 16 == 12:
        new += 'C'
    if r % 16 == 13:
        new += 'D'
    if r % 16 == 14:
        new += 'E'
    if r % 16 == 15:
        new += 'F'
    if r % 16 < 10:
        resto = r % 16
        resto = str(resto)
        new += resto
    return new


cor, R, G, B = input().split(',')
R = int(R)
G = int(G)
B = int(B)
hex_r = transformacao(R)
hex_g = transformacao(G)
hex_b = transformacao(B)

print(f'{cor} #{hex_r}{hex_g}{hex_b}')

peixe, valor = input().split()
valor = float(valor)
menor_peixe = ''
menor_valor = 9999999999
count = 0

print("\n+--------------------+--------------------+")
print("|        peixe       |      preço   R$    |")
print("+--------------------+--------------------+")
while peixe != 'fim':
    count += 1
    if valor <= menor_valor:
        menor_valor = valor
        menor_peixe = peixe
    print(f"| {peixe:<19}|{valor:>19.2f} |")
    print("+--------------------+--------------------+")
    peixe, valor = input().split()
    valor = float(valor)

if count == 0:
    print("|           Hoje não tem peixe            |")
    print("+--------------------+--------------------+")
if count > 1:
    print("+--------------------+--------------------+")
    print("|         Cambada de menor preço          |")
    print(f"| {menor_peixe:<19}|{menor_valor:>19.1f} |")
    print("+--------------------+--------------------+")'''


def tranformacao_hex(valor):
    new_color = ''
    if valor//16 < 10:
        new_inteiro = valor//16
        new_inteiro = str(new_inteiro)
        new_color += new_inteiro
    elif valor//16 == 10:
        new_color += 'A'
    elif valor//16 == 11:
        new_color += 'B'
    elif valor//16 == 12:
        new_color += 'C'
    elif valor//16 == 13:
        new_color += 'D'
    elif valor//16 == 14:
        new_color += 'E'
    elif valor//16 == 15:
        new_color += 'F'

    if valor % 16 < 10:
        new_resto = valor % 16
        new_resto = str(new_resto)
        new_color += new_resto
    elif valor % 16 == 10:
        new_color += 'A'
    elif valor % 16 == 11:
        new_color += 'B'
    elif valor % 16 == 12:
        new_color += 'C'
    elif valor % 16 == 13:
        new_color += 'D'
    elif valor % 16 == 14:
        new_color += 'E'
    elif valor % 16 == 15:
        new_color += 'F'
    return new_color


cor, r, g, b = input().split(',')
r = int(r)
g = int(g)
b = int(b)

hex_r = tranformacao_hex(r)
hex_g = tranformacao_hex(g)
hex_b = tranformacao_hex(b)

print(f'{cor} #{hex_r}{hex_g}{hex_b}')