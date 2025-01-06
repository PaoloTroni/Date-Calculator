#importações
import datetime

# Função que calcula uma data em base a uma quantidade de días
def calculate_date():
    #Primeiro necessitamos conhecer se a data que o usuario quer saber é no futuro ou no passado
    print('\nPor favor, digite "p" se deseja conhecer uma data passada ou digite qualquer tecla para conhecer uma data futura\n')    
    futur_or_past_option= input().upper()

    #Pedimos que o usuario diga os dias de distância que deseja conhecer a data
    while True:
        try: 
            days_to_calculate = int(input('Por favor, digite um número que represente a quantidade de dias que deseja calular: '))
            print(days_to_calculate)
            break
        except ValueError:
            print("Opção não válida!\nPor favor, digite um número que represente a quantidade de dias que deseja calular:")

    # No caso se deseja encontrar uma data passada entramos nesse "if"
    if futur_or_past_option =="P":
        days_to_calculate = days_to_calculate*-1

    # Obtemos a data atual
    today = datetime.date.today()

   # Calculamos a data desejada usando o método timedelta de datetime
    date_calculated = today + datetime.timedelta(days=days_to_calculate)

    print(f"A data desejada é: {date_calculated.strftime('%d/%m/%Y')}.")

