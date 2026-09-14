 Agenda 6 - Calculadora de Desconto
# Aluna: Michely Valaska - DS I - ETEC

print("=== Calculadora de Desconto - ETEC ===")

valor = float(input("Digite o valor da compra: R$ "))

if valor < 200:
    desconto = valor * 0.05
    perc = 5
elif valor < 300:
    desconto = valor * 0.10
    perc = 10
else:
    desconto = valor * 0.15
    perc = 15

valor_final = valor - desconto

print(f"\nValor da compra: R$ {valor:.2f}")
print(f"Desconto de {perc}%: R$ {desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
