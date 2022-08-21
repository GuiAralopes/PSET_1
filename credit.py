def main():
    #imput do número de cartão
    card = input("Número: ")

  
    #verifica se o cartão é válido, caso seja, mostrará a bandeira do cartão
    if alg_luhn(card):
        card_bandeira(card)
    #Caso não seja válido
    else:
        print("INVÁLIDO")



def alg_luhn(num):
    #calcula a soma a partir do algoritmo de Luhn
    checksum = 0
    for n, n2 in enumerate(reversed(str(num))): #enumera a string em ordem inversa
        if n % 2 == 0:
            checksum += int(n2)
        else:
            for n2 in str(int(n2) * 2):
                checksum += int(n2)
               
    #verifica se a soma é divisível por 10
    if checksum % 10 == 0:
        return True
    else:
        return False



def card_bandeira(card):
    # Remove os digitos do cartáo exceto os dois primeiros
    num = int(str(card)[0:2])
  
    #verifica a bandeira do cartão
    if (num == 34 or num == 37) and len(str(card)) == 15:
        print("AMEX")
    elif num > 51 and num < 56 and len(str(card)) == 16:
        print("MASTERCARD")
    elif num >= 40 and num < 50 and (len(str(card)) == 13 or len(str(card)) == 16):
        print("VISA")
    else:
        print("INVÁLIDO")



if __name__ == "__main__":
    main()
