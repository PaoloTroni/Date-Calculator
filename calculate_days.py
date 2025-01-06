#importações
import datetime

# Função que calcula a diferença em dias entre duas datas
def calculate_days():
    ask_date_message = "Introduza a data a partir da qual deseja calcular a distância em dias, considerando que esse programa somente calcula datas entre os anos 1 DC e 9999 DC.\nPor favor, digite a data no formato DD/MM/AAAA:\n"

    while True: #loop que repete até que o usuario introduza uma data válida
        user_date = input(ask_date_message)
        print(f"\nVocê digitou: {user_date}\n")

        # Antes mesmo do controle da aplicação em si, damos a opção para o usuario corrigir ou modificar a data antes de proseguir
        continue_or_retry = input( 
            '\nSe é correto digite enter para continuar. Em caso contrário, digite "n" para fornecer outra data. '
        ).upper() 

        if continue_or_retry == "N":
            user_date = input("\nPor favor, digite a data desejada: ")
        
        #Tentamos efetuar os calculos com a data fornecida 
        try:
            # Convertemos a string introduzida pelo usuario para um objeto "date"
            date_for_calculate = datetime.datetime.strptime(
                user_date, "%d/%m/%Y"
            ).date()

            # Obtemos a data atual
            today = datetime.date.today()
           
            # Calculamos a diferença em dias
            difference = date_for_calculate - today
            difference_days = difference.days

            # Personalizamos a resposta do programa em base a se se trata de uma data passada ou futura
            if difference_days < 0:
                print(f"\nSe passaram {difference_days * -1} dias desde {user_date}\n")
            else:
                print(f"\nFaltam {difference_days} dias para chegar em {user_date}\n")
            break
        # No caso em que o usuario tenha inserido uma data inválida, lançamos um erro e seguimos no while. 

        except ValueError:
            print("\n!! Data errada !!\nPor favor, digite a data corretamente!\n")
