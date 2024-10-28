def estacionamento(hora_entrada, minuto_entrada, hora_saida, minuto_saida):
    if (hora_saida, minuto_saida) < (hora_entrada, minuto_entrada):
        hora_saida += 24
    
    total_minutos = (hora_saida * 60 + minuto_saida) - (hora_entrada * 60 + minuto_entrada)
    
    horas = (total_minutos + 59) // 60  

    if horas <= 2:
        valor = horas * 1.00
    elif 3 <= horas <= 4:
        valor = horas * 1.40
    else:
        valor = horas * 2.00

    return round(valor, 2)  
resultado1 = estacionamento(18, 50, 22, 49)
print(f'Preço: R$ {resultado1}')  

resultado2 = estacionamento(20, 30, 8, 0)
print(f'Preço: R$ {resultado2}')  