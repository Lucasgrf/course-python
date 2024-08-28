# Dada uma lista de números inteiros, escreva uma função que converta declarativamente cada número em sua 
# representação textual em formato de palavra (por exemplo, 5 em “cinco”) e retorne a lista resultante.

def converter_para_palavras(lista):
    numeros_por_extenso = {
        0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro',
        5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove',
        10: 'dez', 11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze',
        15: 'quinze', 16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove',
        20: 'vinte', 30: 'trinta', 40: 'quarenta', 50: 'cinquenta',
        60: 'sessenta', 70: 'setenta', 80: 'oitenta', 90: 'noventa',
        100: 'cem'
    }
    
    def numero_para_palavra(n):
        if n in numeros_por_extenso:
            return numeros_por_extenso[n]
        elif n < 100:
            return numeros_por_extenso[n // 10 * 10] + ' e ' + numeros_por_extenso[n % 10]
        else:
            return 'Número fora do alcance'

    return [numero_para_palavra(num) for num in lista]

numeros = [1, 5, 12, 23, 45, 100]
palavras = converter_para_palavras(numeros)
print(palavras)
