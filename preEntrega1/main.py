import json,time

path_db = 'database.json'


def file_database(mode):
    return open(path_db,mode)

def database_json(file_database):
    return json.load(file_database)

def database(mode):
    file_db = file_database(mode)
    return file_db if mode == "w" else database_json(file_db)

def search(db_json, username):
    for user in db_json["users"]:
        if user['username'] != username:
            continue
        else:
            return user
    return False

def create_user(file,db_json, username, password):
    db_json["users"].append({
        'username': username,
        'password': password
    })
    json.dump(db_json, file,indent=4)
    file.close()
    return f"Usuario {username} creado con exito"

def register(db_json):
    database_file = database("w")
    username = input("Ingrese nombre de usuario: ")
    if(search(db_json,username)):
        print("Usuario no disponible")
    else:
        password = input("Ingrese su password: ")
        print(create_user(database_file,db_json,username,password))

def login(db_json):
    username = input("Ingrese su usuario: ")
    password = input("Ingrese su password: ")
    user = search(db_json, username)
    try:
        if (user['password'] == password):
            print(f"Bienvenido {user['username']}")
        else:
            print("Datos incorrectos")
    except:
        print("Usuario inexistente")


db_json = database("r")
opt = ""
def Main():
    print("Bienvenido al portal")
    print("Ingrese alguna de las siguientes opciones")
    print("1 - Login")
    print("2 - Crear nuevo usuario")
    print("3 - Salir")

    opt = input("Ingrese la opcion deseada: ")
    if opt == "1":
        login(db_json)
        time.sleep(2)
    elif opt == "2":
        register(db_json)
        time.sleep(2)
    elif opt == "3":
        print("Hasta luego")
        return opt

while opt != "3":            
    opt = Main()
