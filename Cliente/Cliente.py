import requests

url = 'http://servers1-a-b-1461907413.us-east-2.elb.amazonaws.com/'
ruta = ""
autor = ""

while (True):
    print("1. Ingresa ruta.")
    print("2. Ingresa autor.")
    print("3. Ver datos.")
    print("4. Enviar datos.")
    print("5. Salir.")
    print(">")

    opcion = input()
    if (opcion == "1"):
        print("Ingresar ruta del archivo a cargar.")
        ruta = input()
        continue

    elif (opcion == "2"):
        print("Ingresar nombre del autor.")
        autor = input()
        continue

    elif (opcion == "5"):
        break
      
    elif (opcion != "3" and opcion != "4"):
        continue

    if (not ruta or not autor):
        print('Para enviar o ver los datos se debe de agregar ruta y autor.')
        continue
    	
    f = None
    try:
        f = open(ruta,'r', encoding='UTF-8')
    except:
        print("Error al abrir el archivo con el nombre: \""+ruta+"\".")
        continue

    print(f)
    if (not f):
        print("La ruta es invalida.")
        continue

    texto = f.read()
    oraciones = texto.split(".")

    if (opcion == "3"):
        contador = 1
        print(autor)
        for oracion in oraciones:
            print(str(contador)+"- "+oracion.strip()+".")
            contador += 1 
        input()
        continue
    elif (opcion == "4"):
        for oracion in oraciones:
            json = {
                "autor":autor,
                "nota":oracion.strip()
            }
            requests.post(url+"/insertar", json=json)
        input()
        continue
    else:
        continue





   
   


    