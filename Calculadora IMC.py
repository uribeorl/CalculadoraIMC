#pedimos al usuario que registre sus datos
while True:
    nombre = str(input("coloque su nombre por favor: "))
    if nombre: break

while True:
    apellido_Paterno = str(input("coloque su apellido paterno por favor: "))
    if apellido_Paterno: break

while True:
    apellido_Materno = str(input("coloque su apellido materno por favor: "))
    if apellido_Materno: break
#pasamos a verificar que los datos se coloquen con numeros
while True:
     try:
        edad = int(input("coloque su edad por favor: "))
     except ValueError:
         print("datos incorrectos, utilize numeros para este apartado")
         continue
     break

while True:
     try:
        peso = float(input("coloque su peso por favor: "))
     except ValueError:
         print("datos incorrectos, utilize numeros para este apartado")
         continue
     break

while True:
     try:
        estatura = float(input("coloque su estatura por favor: "))
     except ValueError:
         print("datos incorrectos, utilize numeros para este apartado")
         continue
     break
IMC=peso/estatura**2
print(
    "nombre completo: "+ nombre +" "+ apellido_Paterno +" "+ apellido_Materno + "\n"
    "edad: "+ str(edad) +"\n"
    "peso: "+ str(peso) + "\n"
    "estatura: " + str(estatura) + "\n"
    "IMC: " + str(IMC)
)
 
