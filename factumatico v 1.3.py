print(r"______         _          ___  ___      _   _           ")
print(r"|  ___|       | |         |  \/  |     | | (_)          ")
print(r"| |_ __ _  ___| |_ _   _  | .  . | __ _| |_ _  ___ ___  ")
print(r"|  _/ _` |/ __| __| | | | | |\/| |/ _` | __| |/ __/ _ \ ")
print(r"| || (_| | (__| |_| |_| | | |  | | (_| | |_| | (_| (_) |")
print(r"\_| \__,_|\___|\__|\__,_| \_|  |_/\__,_|\__|_|\___\___/ ")
print(r"                                                        V 1.3 ")


dolar = float(input("Ingrese tasa cambiaria:"))

while True:
    mode = float(input("Ingrese precio REF:"))

    print(r"´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´")

    dolar = dolar
    unoseis = float(1.16)
    zeroseis = float(0.16)

    Total = mode * dolar
    ALIC = Total / unoseis
    IVA = ALIC * zeroseis

    print("Total a pagar :", round(Total, 2))
    print("Precio sin IVA:", round(ALIC, 2))
    print("        I.V.A.:", round(IVA, 2))
    print("")
    print("Tasa cambiaria de operacion:", round(dolar, 2))
    print("_______________________________________________")
    print("_______________________________________________")
    print("_______________________________________________")
    







