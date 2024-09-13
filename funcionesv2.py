print("Funciones version 2")
print("Rogelio Bejarano")
celulares=["Samsung S23 ultra","Chaifon 16 pro","iPhone 15 pro max"]
Banquistas=["Juliux Maddos","Joshua Baker","Roger"]

# Set
Set1={"No se que poner1","No se que poner2","No se que poner3"}

# Tuplas
cars=["Pagani","Koenigsegg","Bugatti"]

# Diccionarios 
EpicDiccionario = {
    "Banca":"120kg",
    "Competencia":"17 años",
    "BW":"102.5kg"
}

# zona de funciones
def verlista(telefonos):
    for v1 in celulares:
        print("<",v1,">")

def funcion1(funcion11):
    for v2 in Banquistas:
        print("<",v2,">")

# llamadas a funciones
print("Llamada a celulares de una lista: ")
verlista(celulares)

print("Mejores banquistas del mundo")
funcion1(Banquistas)

# Llamada con diccionario
print("Stats de Roger: ")
for x in EpicDiccionario:
    print(EpicDiccionario[x])


# Llamada a tupla
print("Tipos de marcas de coches exóticas")
print(cars)

# Llamada set
print("Llamada con set: ")
print(Set1)
