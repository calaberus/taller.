import csv

def cargar_productos(nombre_archivo):
    lista = []
    archivo = open(nombre_archivo, 'r', encoding='utf-8')
    lector = csv.DictReader(archivo)
    for linea in lector:
        lista.append(linea)
    archivo.close()
    return lista

def ordenar_merge(datos):
    if len(datos) <= 1:
        return datos
    
    medio = len(datos) // 2
    parte_izq = ordenar_merge(datos[:medio])
    parte_der = ordenar_merge(datos[medio:])
    
    return mezclar(parte_izq, parte_der)

def mezclar(lista1, lista2):
    ordenado = []
    idx1 = 0
    idx2 = 0
    
    while idx1 < len(lista1) and idx2 < len(lista2):
        calificacion1 = float(lista1[idx1]['calificacion'])
        calificacion2 = float(lista2[idx2]['calificacion'])
        precio1 = float(lista1[idx1]['precio'])
        precio2 = float(lista2[idx2]['precio'])
        
        if calificacion1 > calificacion2:
            ordenado.append(lista1[idx1])
            idx1 += 1
        elif calificacion1 < calificacion2:
            ordenado.append(lista2[idx2])
            idx2 += 1
        else:
            if precio1 <= precio2:
                ordenado.append(lista1[idx1])
                idx1 += 1
            else:
                ordenado.append(lista2[idx2])
                idx2 += 1
    
    ordenado.extend(lista1[idx1:])
    ordenado.extend(lista2[idx2:])
    
    return ordenado

def mostrar_producto(producto, numero):
    print(f"\n{numero}. {producto['nombre']}")
    print(f"   ID: {producto['id']}")
    print(f"   Precio: ${producto['precio']}")
    print(f"   Calificacion: {producto['calificacion']}")
    print(f"   Stock: {producto['stock']}")

nombre = "productos.csv"

print("TALLER DIVIDE Y VENCERAS")
print("=" * 60)

productos = cargar_productos(nombre)
print(f"\nProductos cargados: {len(productos)}")

print("\nAplicando Merge Sort...")
productos_ordenados = ordenar_merge(productos)

print("\n" + "=" * 60)
print("MEJORES PRODUCTOS")
print("=" * 60)

for i in range(20):
    mostrar_producto(productos_ordenados[i], i + 1)

print("\n" + "=" * 60)
print("Fin del programa")