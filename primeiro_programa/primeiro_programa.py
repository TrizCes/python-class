# Precos dos produtos
preco_arroz = 5.50   # Preco por unidade de arroz
preco_feijao = 7.30  # Preco por unidade de feijao
preco_macarrao = 3.20  # Preco por unidade de macarrao

# Solicita ao cliente a quantidade de cada produto
quantidade_arroz = int(input("Digite a quantidade de arroz: "))
quantidade_feijao = int(input("Digite a quantidade de feijao: "))
quantidade_macarrao = int(input("Digite a quantidade de macarrao: "))

# Calcula o total para cada produto
total_arroz = quantidade_arroz * preco_arroz
total_feijao = quantidade_feijao * preco_feijao
total_macarrao = quantidade_macarrao * preco_macarrao

# Calcula o valor total da compra
total_compra = total_arroz + total_feijao + total_macarrao

# Exibe o resultado para o cliente
print("\nResumo da compra:")
print(f"Arroz: {quantidade_arroz} x R$ {preco_arroz:.2f} = R$ {total_arroz:.2f}")
print(f"Feijao: {quantidade_feijao} x R$ {preco_feijao:.2f} = R$ {total_feijao:.2f}")
print(f"Macarrao: {quantidade_macarrao} x R$ {preco_macarrao:.2f} = R$ {total_macarrao:.2f}")
print(f"\nTotal da compra: R$ {total_compra:.2f}")
