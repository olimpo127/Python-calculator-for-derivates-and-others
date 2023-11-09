
usuarios = [
    {
    "id": 1,
    "nombre": "Felipe", 
    "apellido": "Ojeda",
    "edad": 30,
    "direccion": "Calle 1",
    "telefono": 123456,
    "email": "fojedai47@gmail.com"
    },
    { 
    "id": 2,
    "nombre": "Javiera", 
    "apellido": "Lazo",
    "edad": 28,
    "direccion": "Calle 1",
    "telefono": 12345678,
    "email": "j.lazocabello@gmail.com"
    }
    ]

def crear_usuario(id, nombre, apellido, edad, direccion, telefono, email):
    nuevo_usuario = {
        "id": id,
        "nombre": nombre, 
        "apellido": apellido,
        "edad": edad,
        "direccion": direccion,
        "telefono": telefono,
        "email": email
    }
    usuarios.append(nuevo_usuario)

def modificar_usuario(id, nuevos_datos):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuario.update(nuevos_datos)
            break

def eliminar_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            break

eliminar_usuario(0)

crear_usuario(3, "Trinidad", "Ojeda", 1, "Calle 2", 789012, "nini@gmail.com")

#modificar_usuario(2, {"nombre": "Javiera2", "apellido": "Lazo2", "edad": 282, "direccion": "Calle 221", "telefono": 1234567822, "email": "nuevomail@gmail.com"})

for usuario in usuarios:
    print(usuario["edad"])
