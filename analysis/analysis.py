from generator.generator import generarDatosApple
import pandas as pd

def analizarDatos():
    datos=generarDatosApple()
    tabla=pd.DataFrame(datos,columns=["producto" ,"categoria"])
    tabla.to_csv("./productos.csv",index=False)
analizarDatos()