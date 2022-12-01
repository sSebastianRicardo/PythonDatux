#7.Hacer un programa que consulte el valor del dolar (compra y venta ) de la fecha actual
#segun sunat (url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat')

def impresion7():
    import requests # me sirve para conectarme al sitio web
    from lxml import html # para extraer texto o navegar por el arbol html

    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'

    response = requests.get(url)

    response.json()
    res=response.json()

    dolar_compra = res['compra']
    dolar_venta = res['venta']
    fecha_actual = res['fecha']

    print(f"El dolar para compra es {dolar_compra} y para venta {dolar_venta}, hoy {fecha_actual} ")

impresion7()