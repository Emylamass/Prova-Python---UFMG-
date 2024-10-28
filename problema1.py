def progressoes(a1, r, n):
    
    an_pa = a1 + (n - 1) * r
    
    
    q = r  
    an_pg = a1 * (q ** (n - 1))
    
   
    if an_pa > an_pg:
        
        Sn_pa = n * (a1 + an_pa) / 2
        return Sn_pa
    else:
       
        if q == 1:
            
            Sn_pg = n * a1
        else:
            Sn_pg = a1 * (q ** n - 1) / (q - 1)
        return Sn_pg


resultado1 = progressoes(0, 2, 10)
print(f'Resultado 1: {resultado1}')  

resultado2 = progressoes(1, 1, 100)
print(f'Resultado 2: {resultado2}')  

resultado3 = progressoes(3, 3, 3)
print(f'Resultado 3: {resultado3}')  