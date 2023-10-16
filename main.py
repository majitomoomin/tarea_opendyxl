#desafio generador de informe de gastos
#María José del Carmen Portillo Lopez 0907-23-4166

import openpyxl
archivo_excel = "C:/Users/ACER/Downloads/opendyxl/informe_gastos.xlsx"
libro_trabajo = openpyxl.load_workbook(archivo_excel)
hoja = libro_trabajo.active

def ingresar_datos():
    gastos = []
    continuar = True
    while continuar:
        fecha = input("Ingrese la fecha en la que se realizó el gasto (DD/MM/AA): ")
        descripcion = input("Ingrese la descripción del gasto: ")
        monto = float(input("Ingrese el monto del gasto: "))
        gastos.append((fecha, descripcion, monto))
        respuesta = input("¿Desea ingresar otro gasto? (s/n): ")
        if respuesta.lower() != 's':
            continuar = False
    return gastos

def resumen(gastos):
    num_gastos = len(gastos)
    if num_gastos > 0:
        gastos.sort(key=lambda x: x[2])
        gasto_barato = gastos[0]
        gasto_caro = gastos[-1]

        print(f'\nNúmero total de gastos: {num_gastos}')
        print(f'Fecha y descripción del gasto más barato: {gasto_barato[0]} - {gasto_barato[1]}')
        print(f'Fecha y descripción del gasto más caro: {gasto_caro[0]} - {gasto_caro[1]}')
        total_gastos = sum(gasto[2] for gasto in gastos)
        print(f'Monto total de gastos: {total_gastos}')

# bloque principal
nuevos_gastos = ingresar_datos()
resumen(nuevos_gastos)
for gasto in nuevos_gastos:
    hoja.append(gasto)
libro_trabajo.save(archivo_excel)

