# # Solicita ao usu�rio que insira as tr�s notas
# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
 
# # Calcula a m�dia das notas
# media = (nota1 + nota2 + nota3) / 3
 
# # Mostra o resultado ao usu�rio
# print(f"A media das notas e: {media:.2f}")



# Solicita ao usu�rio as entradas
numeroint = int(input("Digite um numero inteiro: "))
numerofloat = float(input("Digite um numero com duas casas decimais: "))
valor = input("Digite 'True' ou 'False': ")

# Converte a string para booleano
valor_booleano = valor.lower() == "true"

# Exibe os valores convertidos e seus tipos
print(f"Numero inteiro: {numeroint} - tipo: {type(numeroint)}")
print(f"Numero float: {numerofloat} - tipo: {type(numerofloat)}")
print(f"Valor booleano: {valor_booleano} - tipo: {type(valor_booleano)}")
