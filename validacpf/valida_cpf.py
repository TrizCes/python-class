import re

def remove_nao_numericos(cpf):
    """Remove caracteres nao numericos do CPF."""
    return re.sub(r'\D', '', cpf)

def valida_cpf(cpf):
    # Remove caracteres nao numericos
    cpf = remove_nao_numericos(cpf)

    # Valida se tem 11 digitos
    if len(cpf) != 11:
        return False, "O CPF deve conter 11 digitos."

    # Valida se todos os digitos nao sao iguais
    if cpf == cpf[0] * 11:
        return False, "CPF invalido: todos os digitos sao iguais."

    # Calcula o primeiro digito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    primeiro_digito = (soma * 10) % 11
    if primeiro_digito == 10:
        primeiro_digito = 0

    if primeiro_digito != int(cpf[9]):
        return False, "Primeiro digito verificador invalido."

    # Calcula o segundo digito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    segundo_digito = (soma * 10) % 11
    if segundo_digito == 10:
        segundo_digito = 0

    if segundo_digito != int(cpf[10]):
        return False, "Segundo digito verificador invalido."

    return True, "CPF valido."

cpf_teste = input(f'Digite o CPF:')  # Insira o CPF para testar aqui
valido, mensagem = valida_cpf(cpf_teste)
print(mensagem)
