# Sistema de Desconto Progressivo
# Este programa calcula o desconto de acordo com o valor informado

# Solicita ao usuário o valor total da compra
print ("===== Programa Desconto Progressivo =====")
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Verifica qual percentual de desconto deve ser aplicado
if valor_compra < 200:
    percentual_desconto = 0.05
elif valor_compra < 300:
    percentual_desconto = 0.10
else:
    percentual_desconto = 0.15

# Calcula o valor do desconto
valor_desconto = valor_compra * percentual_desconto

# Calcula o valor final após o desconto
valor_final = valor_compra - valor_desconto

# Exibe os resultados para o usuário
print("\n===== RESUMO DA COMPRA =====")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {percentual_desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor a pagar: R$ {valor_final:.2f}")
