# Programa que permite calcular a distancia entre datas

#importações
import time #biblioteca para poder usar o método "sleep"
# Decidí modularizar as funções para ter o código mais ordenado
from calculate_days import calculate_days 
from calculate_date import calculate_date

def main():
    # Mensagens de intro
    print("\n------Seja bem vindo ao calculador de datas!------\n--------by: Paolo Troni\n")
    time.sleep(2)
    # Estabelecemos um "while True" para que o usuario possa ficar usando o programa até que deseja sair
    while True:
        # Lógica para guiar o usuario nas diferentes funções do programa
        ask_option_message = 'Por favor, digite:\n "1" -> Para calcular a distancia em dias a partir de uma data.\n "2" -> Para calcular uma data em base a uma quantidade de dias.'

        print(ask_option_message)

        user_option = input()

        while user_option != "1" and user_option != "2":
            print("Opção não válida.")
            print(ask_option_message)
            user_option = input()

        print(f'Você escolheu a opção: "{user_option}"\n')
        if user_option == "1":
            # Chamamos a função que calcula os dias entre hoje e uma data determinada
            calculate_days()

        if user_option == "2":
             # Chamamos a função que calcula uma a partir de uma quantidade de dias determinado
            calculate_date()

        # Lógica para finalizar o programa
        end_program = input('\nDigite "fin" para finalizar o programa ou aperte qualquer tecla para continuar calculando datas.\n').upper()

        if end_program == "FIN":
            print("\nObrigado por usar esse programa.\n")
            time.sleep(1)
            print("Até a próxima! ;)\n")
            break
        else:
            print("Seguimos......\n")
            time.sleep(2)

if __name__ == "__main__":
    main()