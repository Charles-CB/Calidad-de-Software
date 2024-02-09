"""
compute_sales.py

Este módulo contiene funciones para cargar datos de archivos JSON
calcular totales de ventas y generar informes de ventas

Autor: Carlos Mendoza
Matricula: A01793027
"""
import sys
import json
import time


def cargar_datos(nombre_archivo):
    """
    Carga los datos del archivo JSON especificado

    Args:
        nombre_archivo (str): El nombre del archivo JSON a cargar

    Returns:
        dict: Los datos cargados del archivo JSON
    """
    try:
        with open(nombre_archivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Archivo '{nombre_archivo}' no encontrado")
        return None
    except json.JSONDecodeError:
        print(f"Error: Archivo '{nombre_archivo}' "
              "no tiene un formato JSON válido")
        return None


def calcular_total_ventas_cat(productos, ventas):
    """
    Calcula el total de ventas por tipo de producto

    Args:
        productos (list): Lista de productos con información de precios
        ventas (list): Lista de ventas con información de productos
                        y cantidades

    Returns:
        dict: Un diccionario con el total de ventas por tipo de producto
    """
    total_ventas_cat = {}
    for venta in ventas:
        producto_vendido = venta.get("Product")
        cantidad_vendida = venta.get("Quantity")
        if producto_vendido is None or cantidad_vendida is None:
            print(f"Error: Datos incompletos en la venta: {venta}")
            continue
        for producto in productos:
            if producto.get("title") == producto_vendido:
                tipo_producto = producto.get("type")
                precio_unitario = producto.get("price")
                if tipo_producto is None or precio_unitario is None:
                    print(f"Error: Datos incompletos en el producto: "
                          f"{producto}")
                    continue
                total_ventas_cat[tipo_producto] = \
                    total_ventas_cat.get(tipo_producto, 0) + \
                    (precio_unitario * cantidad_vendida)
                break
    return total_ventas_cat


def calcular_total_ventas(productos, ventas):
    """
    Calcula el total de ventas

    Args:
        productos (list): Lista de productos
                          con información de precios
        ventas (list): Lista de ventas
                       con información de productos y cantidades

    Returns:
        float: El total de ventas
    """
    total_ventas = 0
    for venta in ventas:
        producto_vendido = venta.get("Product")
        cantidad_vendida = venta.get("Quantity")
        if producto_vendido is None or cantidad_vendida is None:
            print(f"Error: Datos incompletos en la venta: {venta}")
            continue
        for producto in productos:
            if producto.get("title") == producto_vendido:
                precio_unitario = producto.get("price")
                if precio_unitario is None:
                    print(f"Error: Datos incompletos "
                          f"en el producto: {producto}")
                    continue
                total_ventas += precio_unitario * cantidad_vendida
                break
    return total_ventas


def imprimir_totales_ventas_txt(totales_ventas_cat,
                                total_ventas,
                                tiempo_transcurrido):
    """
    Imprime los totales de ventas en un archivo de texto

    Args:
        totales_ventas_cat (dict): Totales de ventas por categoría
        total_ventas (float): Total de ventas
        tiempo_transcurrido (float): Tiempo transcurrido en segundos
    """
    with open("SalesResults.txt", "w") as results_file:
        results_file.write("-------------------\n")
        results_file.write("TOTAL VENTAS POR CATEGORÍA\n")
        results_file.write("-------------------\n")
        for tipo_producto, total_venta in totales_ventas_cat.items():
            results_file.write(f"{tipo_producto}\t{total_venta:.2f}\n")
        results_file.write("-------------------\n")
        results_file.write("TOTAL DE VENTAS\n")
        results_file.write("-------------------\n")
        results_file.write(f"{total_ventas:.2f}\n")
        results_file.write("\nTiempo transcurrido: "
                           f"{tiempo_transcurrido:.4f} segundos\n")


def imprimir_totales_ventas_cat(totales_ventas_cat_local,
                                archivo_ventas_local):
    """
    Imprime los totales de ventas por categoría en la consola

    Args:
        totales_ventas_cat_local (dict): Totales de ventas por categoría
        archivo_ventas_local (str): Nombre del archivo de ventas
    """
    print(f"Archivo: {archivo_ventas_local}")
    print("-------------------")
    print("TOTAL VENTAS POR CATEGORÍA")
    print("-------------------")
    for tipo_producto, total_venta in totales_ventas_cat_local.items():
        print(f"{tipo_producto}\t{total_venta:.2f}")


def imprimir_total_ventas(total_ventas):
    """
    Imprime el total de ventas en la consola

    Args:
        total_ventas (float): Total de ventas
    """
    print("-------------------")
    print("TOTAL DE VENTAS")
    print("-------------------")
    print(f"{total_ventas:.2f}\n")


if __name__ == "__main__":
    inicio_tiempo = time.time()

    if len(sys.argv) != 3:
        print("Error: Se requieren exactamente "
              "dos archivos tipo JSON como parámetros")
        print("Uso: python computeSales.py "
              "priceCatalogue.json "
              "salesRecord.json")
        sys.exit(1)

    archivo_productos = sys.argv[1]
    archivo_ventas = sys.argv[2]

    productos_globales = cargar_datos(archivo_productos)
    ventas_globales = cargar_datos(archivo_ventas)

    if productos_globales is None or ventas_globales is None:
        sys.exit(1)

    totales_ventas_cat_global = calcular_total_ventas_cat(
                                        productos_globales,
                                        ventas_globales)
    total_ventas_calculado = calcular_total_ventas(
                                        productos_globales,
                                        ventas_globales)

    tiempo_transcurrido_global = time.time() - inicio_tiempo

    imprimir_totales_ventas_cat(totales_ventas_cat_global, archivo_ventas)
    imprimir_total_ventas(total_ventas_calculado)
    imprimir_totales_ventas_txt(totales_ventas_cat_global,
                                total_ventas_calculado,
                                tiempo_transcurrido_global)
    print(f"Tiempo transcurrido: {tiempo_transcurrido_global:.4f} segundos")
