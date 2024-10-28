def consumo(distancia, litros):
   
    consumo_km_l = distancia / litros
    
    if consumo_km_l < 8:
        return "Venda o carro!"
    elif 8 <= consumo_km_l <= 12:
        return "Econômico!"
    else:
        return "Super econômico!"
    
resultado1 = consumo(100, 10)
print(resultado1)  

resultado2 = consumo(30, 4.5)
print(resultado2)  

resultado3 = consumo(150, 10)
print(resultado3)  