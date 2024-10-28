def valor_energia(consumo_kwh, tipo_instalacao):
    preco_por_kwh = 0.0
    
    if tipo_instalacao == 'R':  
        if consumo_kwh <= 500:
            preco_por_kwh = 0.40
        else:
            preco_por_kwh = 0.65
    elif tipo_instalacao == 'C':  
        if consumo_kwh <= 1000:
            preco_por_kwh = 0.55
        else:
            preco_por_kwh = 0.60
    elif tipo_instalacao == 'I':  
        if consumo_kwh <= 5000:
            preco_por_kwh = 0.55
        else:
            preco_por_kwh = 0.60
    else:
        return "Tipo de instalação inválido"

    
    total_a_pagar = consumo_kwh * preco_por_kwh
    
    return round(total_a_pagar, 2)  
resultado1 = valor_energia(580, 'R')
print(f'Preço a pagar: {resultado1}')  

resultado2 = valor_energia(4200, 'I')
print(f'Preço a pagar: {resultado2}')  