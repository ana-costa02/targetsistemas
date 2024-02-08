def inverte_string(string):
    # Convertendo a string em uma lista de caracteres
    caracteres = list(string)
    
    # Obtendo o tamanho da string
    tamanho = len(caracteres)

    # Invertendo os caracteres usando um loop
    for i in range(tamanho // 2):  # Percorre apenas metade da string
        # Troca os caracteres simétricos
        caracteres[i], caracteres[tamanho - i - 1] = caracteres[tamanho - i - 1], caracteres[i]

    # Construindo a string invertida
    string_invertida = ''.join(caracteres)
    
    return string_invertida

# Teste
string_original = input("Informe uma string: ")
string_invertida = inverte_string(string_original)
print("String invertida:", string_invertida)



# def inverte_string(string):
#     # Convertendo a string em uma lista de caracteres
#     caracteres = list(string)
    
#     # Invertendo a lista
#     caracteres.reverse()

#     # Construindo a string invertida
#     string_invertida = ''.join(caracteres)
    
#     return string_invertida

# # Teste
# string_original = input("Informe uma string: ")
# string_invertida = inverte_string(string_original)
# print("String invertida:", string_invertida)


