# Simulador de tienda de boletos de cine

print("*** Tienda de Tickets ***")

# Solicitar datos al usuario
edad_usuario = int(input("Ingresa tu edad: "))
precio_entrada=0
if edad_usuario <= 0:
    print("Edad no valida")
else:
    if edad_usuario < 5:
        precio_entrada = 0
    elif edad_usuario < 13:
        precio_entrada = 8000
    elif edad_usuario < 18:
        precio_entrada = 10000
    elif edad_usuario < 61:
        precio_entrada = 15000
    else:
        precio_entrada = 5000

    if precio_entrada == 0:
        print("Tu entrada es gratis\nDisfruta la pelicula")
    else:
        print(f"Tu entrada vale: ${precio_entrada}\nGracias por tu compra. Disfruta la pelicula")