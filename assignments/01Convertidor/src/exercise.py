# Escribe tus funciones abajo de esta línea
def pies_cm(pies): 
    piescm=(pies*30.48)
    return(piescm)
def pulgadas_cm(pulgadas):
    pulgcm=(pulgadas*2.54)
    return (pulgcm)
def yardas_cm(yardas): 
    yardascm=(yardas*91.44)
    return(yardascm)
def main():
    # Escribe tu código abajo de esta línea
    print("1. pies a cm, 2. pulgadas a cm, 3. yardas a cm")
    opcion=str(input("Introduce una opcion: "))
    cantidad=int(input("Introduce la cantidad: "))
    if cantidad>0 : 
        if opcion=="1": 
            piescm=pies_cm(cantidad)
            print(piescm)
        elif opcion=="2": 
            pulgcm=pulgadas_cm(cantidad)
            print(pulgcm)
        elif opcion=="3":
            yardascm=yardas_cm(cantidad)
            print(yardascm)
        else:
            print("Error")
    else: 
        print("Error")
if __name__ == '__main__':
    main()
