#arrayObs= input("Ingrese las coordenadas:")
#arrayObs=[5, 2, 6, 7, 9,12]
arrayObs=[5, 3, 6, 7, 9]
#count 0 -> n
#obst=true ?
def minimumJump(arr):
    obst=True
    salto=0
    cambio=0
    count=0
    tamano=len(arr)
    n=0
    for i in range(0,101):
      if count==tamano:
        obst=False
      else:
        if n!=arr[count]:
           n+=1
           salto+=1
        else:
            n=0
            count+=1
            if cambio == 0 or cambio > salto:
             cambio=salto
            salto=0
    return "The minimum jump to avoid all obstacles is: {}".format(cambio+1)      
        
salida=minimumJump(arrayObs)
print(salida)
    

