from os import system 
system ("cls")

print("---------------------------")
print("--------creativos.cl-------")
print("---------------------------")

import datetime
import time

# Precios de las entradas
precios = {
    "Platinum": 120000,
    "Gold": 80000,
    "Silver": 50000
}

# Estado de las ubicaciones
ubicaciones = {
    "Platinum": [['X' if 1 <= (i*10 + j + 1) <= 20 else ' ' for j in range(10)] for i in range(10)],
    "Gold": [['X' if 21 <= (i*10 + j + 1) <= 50 else ' ' for j in range(10)] for i in range(10)],
    "Silver": [['X' if 51 <= (i*10 + j + 1) <= 100 else ' ' for j in range(10)] for i in range(10)]
}

# Listado de asistentes
asistentes = []

def validar_run(run):
    run = run.replace("-", "").replace(".", "")
    if len(run) != 8 or not run[:-1].isdigit() or (run[-1] != "K" and not run[-1].isdigit()):
        return False
    return True

def comprar_entradas():
    cantidad = int(input("Ingrese la cantidad de entradas a comprar (entre 1 y 3): "))
    while cantidad < 1 or cantidad > 3:
        print("Cantidad inválida. Intente nuevamente.")
        time.sleep(0.5)
        cantidad = int(input("Ingrese la cantidad de entradas a comprar (entre 1 y 3): "))

    print(f"Precios de las entradas:")
    for tipo, precio in precios.items():
        print(f"{tipo}: ${precio}")

    print("Asientos disponibles:")
    for i in range(10):
        for j in range(10):
            seat_number = i * 10 + j + 1
            for tipo, estado in ubicaciones.items():
                if estado[i][j] == "X":
                    print(f"{seat_number:<4d} {tipo}")
                    break
            else:
                print(f"{seat_number:<4d} Disponible")

    for _ in range(cantidad):
        asiento = int(input("Seleccione un número de asiento (1-100): ")) - 1
        while not (0 <= asiento < 100):
            print("Asiento inválido. Intente nuevamente.")
            time.sleep(0.5)
            asiento = int(input("Seleccione un número de asiento (1-100): ")) - 1

        fila = asiento // 10
        columna = asiento % 10

        tipo_entrada = None
        for tipo, estado in ubicaciones.items():
            if estado[fila][columna] == "X":
                tipo_entrada = tipo
                break

        if tipo_entrada is None:
            print("Asiento ocupado. Seleccione otro.")
            time.sleep(0.5)
            continue

        ubicaciones[tipo_entrada][fila][columna] = "X"

        run = input("Ingrese el RUN de la persona que ocupará la ubicación (sin guiones ni puntos): ")
        while not validar_run(run):
            print("RUN inválido. Intente nuevamente.")
            time.sleep(0.5)
            run = input("Ingrese el RUN de la persona que ocupará la ubicación (sin guiones ni puntos): ")

        if run[-1] == "K":
            run = run[:-1] + "-" + run[-1]

        asistentes.append((run, tipo_entrada, fila + 1, columna + 1))

    mostrar_ubicaciones_disponibles()
    print("Operación realizada correctamente.")

def mostrar_ubicaciones_disponibles():
    print("Estado actual de la venta de entradas:")
    time.sleep(0.5)
    for tipo, estado in ubicaciones.items():
        print(f"Categoría: {tipo}")
        print(f"Precio: ${precios[tipo]}")
        print("Asientos disponibles:")
        for i in range(10):
            for j in range(10):
                seat_number = i * 10 + j + 1
                if ubicaciones[tipo][i][j] == "X":
                    print(f"{seat_number:<4d}", end="")
                else:
                    print(f"{seat_number:<4d}", end="")
            print()
        print()
        time.sleep(0.5)

def ver_listado_asistentes():
    asistentes_ordenados = sorted(asistentes, key=lambda x: x[0])
    print("Listado de asistentes:")
    for asistente in asistentes_ordenados:
        print("RUN:", asistente[0], "Ubicación:", asistente[1], "Fila:", asistente[2], "Columna:", asistente[3])

def mostrar_ganancias_totales():
    total_ganancias = 0
    print("Ventas realizadas:")
    time.sleep(0.5)
    print("Tipo Entrada Cantidad Total")
    for tipo, estado in ubicaciones.items():
        vendidas = sum(1 for fila in estado for asiento in fila if asiento == "X")  # Contar asientos vendidos
        total_tipo = vendidas * precios[tipo]
        total_ganancias += total_tipo
        print(f"{tipo:9s} ${precios[tipo]:,} {vendidas:8d} ${total_tipo:,}")
        time.sleep(0.5)
    print("TOTAL     {:8d} ${:12,}".format(sum(1 for estado in ubicaciones.values() for fila in estado for asiento in fila if asiento == "X"), total_ganancias))

def salir():
    now = datetime.datetime.now()
    print("Saliendo")
    time.sleep(0.5)
    print("Nombre: Claudio")
    time.sleep(0.5)
    print("Apellido: Valverde")
    time.sleep(0.5)
    print("Fecha actual:", now.strftime("%Y-%m-%d %H:%M:%S"))

def menu():
    while True:
        print("\n--- MENU ---")
        time.sleep(0.5)
        print("1. Comprar entradas")
        print("2. Mostrar ubicaciones disponibles")
        print("3. Ver listado de asistentes")
        print("4. Mostrar ganancias totales")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            comprar_entradas()
        elif opcion == "2":
            mostrar_ubicaciones_disponibles()
        elif opcion == "3":
            ver_listado_asistentes()
        elif opcion == "4":
            mostrar_ganancias_totales()
        elif opcion == "5":
            salir()
            break
        else:
            print("Opcion invalida. Reintentar.")
            time.sleep(0.3)

menu()
