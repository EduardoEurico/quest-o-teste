def contar(texto):
    contador = texto.lower().count('a')
    return contador

texto = "Aqui há algumas palavras com letras A e a."

contador = contar(texto)
print(f"A letra 'a' aparece {contador} vezes na string.")
if contador > 0:
    print("A letra 'a' está presente na string.")
else:
    print("A letra 'a' não está presente na string.")
