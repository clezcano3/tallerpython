import random

def generarDatosApple():
    tipoProductos=["musica","tv","aplicaciones","pc","celulares","tablets","accesorios"]
    datos=[]
    for producto in tipoProductos:
        dataapple={}
        categoria=random.choice(["plus","mega","basic"])
        dataapple=[producto,categoria]
        datos.append(dataapple)

    return datos
print(generarDatosApple())