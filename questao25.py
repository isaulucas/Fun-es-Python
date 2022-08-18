Inicie_Aqui = 3
Termine_Aqui = 73
  
for numero in range(Inicie_Aqui, Termine_Aqui+1): 
  if numero>1: 
    for var2 in range(2,numero): 
        if(numero % var2==0): 
            break
    else: 
        print(numero)  
        
