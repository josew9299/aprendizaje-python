import time

def semaforo():

    tl_1 = ("RED","YELLOW","GREEN")
    tl_2 = ("RED","YELLOW","GREEN")
    tl_3 = ("RED","YELLOW","GREEN")
    tl_4 = ("RED","YELLOW","GREEN")
    
    #Posición inicial
    "1 y 3 inician en verde"
    "2 y 4 inician en rojo"
    print(tl_1[2])
    print(tl_2[0])
    print(tl_3[2])
    print(tl_4[0])
    time.sleep(7)
    
    print("")
    print("")
    print("")
    
    "1 y 3 pasan a amarillo"
    "2 y 4 permanecen en rojo"
    print(tl_1[1])
    print(tl_2[0])
    print(tl_3[1])
    print(tl_4[0])
    time.sleep(3)

    print("")
    print("")
    print("")


    "1 y 3 pasan a rojo"
    "2 y 4 pasan a amarillo"
    #Primer cambio
    print(tl_1[0])
    print(tl_2[1])
    print(tl_3[0])
    print(tl_4[1])
    time.sleep(10)

    print("")
    print("")
    print("")

    "1 y 3 permanecen en rojo"
    "2 y 4 pasan a verde"
    print(tl_1[0])
    print(tl_2[2])
    print(tl_3[0])
    print(tl_4[2])
    time.sleep(5)

    #Segundo cambio
    print(tl_1[2])
    print(tl_2[1])
    print(tl_3[2])
    print(tl_4[1])
    time.sleep(10)

    print("")
    print("")
    print("")

    print(tl_1[0])
    print(tl_2[1])
    print(tl_3[0])
    print(tl_4[1])
    time.sleep(5)

    print("")
    print("")
    print("")
    
semaforo()

while True:
    semaforo()