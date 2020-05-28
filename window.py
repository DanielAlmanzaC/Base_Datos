from tkinter import*
import mysql.connector
# conexión a la base de datos
dbConnect = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'proyecto_bases'
}
# se abre la base
root = Tk()
root.title("Inserción de datos.")
root.iconbitmap("balon.ico")
# tamaño
b_Menu = Menu(root)
root.config(menu=b_Menu, width=650, height=440)

# EQUIPO
# variables que se leen, se tienen que definir como StringVar o IntVar
vnombre_equipo = StringVar()
vjugadores = IntVar()
vpuntos = IntVar()
vpresupuesto = IntVar()


# función que ingresa los datos a la base
def insercionE():
    nombre = vnombre_equipo.get()  # se usa el get para ingresar al contenido
    jugadores = vjugadores.get()
    puntos = vpuntos.get()
    presupuesto = vpresupuesto.get()
    conexion = mysql.connector.connect(**dbConnect)
    cursor = conexion.cursor()
    sqlInsertar = "insert into equipo(Nombre,Jugadores,Puntos,Presupuesto)values(%s,%s,%s,%s)"  # instrucción de mysql
    cursor.execute(sqlInsertar, (nombre, jugadores, puntos, presupuesto))
    conexion.commit()
    cursor.close()
    conexion.close()


etiqueta1 = Label(root, text="Nombre del equipo").place(x=10, y=10)
wnombre = Entry(root, textvariable=vnombre_equipo).place(x=160, y=10)
etiqueta2 = Label(root, text="Número de jugadores").place(x=10, y=40)
wjugadores = Entry(root, textvariable=vjugadores).place(x=160, y=40)
etiqueta3 = Label(root, text="Número de puntos").place(x=10, y=70)
wpuntos = Entry(root, textvariable=vpuntos).place(x=160, y=70)
etiqueta4 = Label(root, text="Presupuesto del equipo").place(x=10, y=100)
wpresupuesto = Entry(root, textvariable=vpresupuesto).place(x=160, y=100)
boton = Button(root, text="Ingresar", command=insercionE).place(x=10, y=130)

# LIGA
vnombre_liga = StringVar()
# función para ingresar la liga


def insercionL():
    nombre = vnombre_liga.get()
    equipo = vnombre_equipo.get()
    conexion = mysql.connector.connect(**dbConnect)
    cursor = conexion.cursor()
    sqlInsertar = "insert into liga(nombre,equipo) values(%s,%s)"
    cursor.execute(sqlInsertar, (nombre, equipo))
    conexion.commit()
    cursor.close()
    conexion.close()


etiqueta7 = Label(root, text="Nombre de la liga").place(x=10, y=180)
wnombre_liga = Entry(root, textvariable=vnombre_liga).place(x=160, y=180)
etiqueta8 = Label(root, text="Nombre del equipo").place(x=10, y=210)
wnombre_equipo = Entry(root, textvariable=vnombre_equipo).place(x=160, y=210)
boton2 = Button(root, text="Ingresar", command=insercionL).place(x=10, y=240)

# JUGADOR
vnumero = IntVar()
vnombre_jugador = StringVar()
vanotaciones = IntVar()
vminutos = IntVar()
vdinero = IntVar()


# función para ingresar jugador
def insercionJ():
    numero = vnumero.get()
    nombre_e = vnombre_equipo.get()
    nombre_j = vnombre_jugador.get()
    anotaciones = vanotaciones.get()
    minutos = vminutos.get()
    dinero = vdinero.get()
    conexion = mysql.connector.connect(**dbConnect)
    cursor = conexion.cursor()
    sqlInsertar = "insert into jugador(Numero,Equipo,Nombre,Anotaciones,Minutos,Salario)values(%s,%s,%s,%s,%s,%s)"
    cursor.execute(sqlInsertar, (numero, nombre_e, nombre_j, anotaciones, minutos, dinero))
    conexion.commit()
    cursor.close()
    conexion.close()


etiqueta9 = Label(root, text="Número del jugador").place(x=330, y=10)
wnumero = Entry(root, textvariable=vnumero).place(x=460, y=10)
etiqueta10 = Label(root, text="Nombre de su equipo").place(x=330, y=40)
wnombre_e = Entry(root, textvariable=vnombre_equipo).place(x=460, y=40)
etiqueta11 = Label(root, text="Nombre").place(x=330, y=70)
wnombre_j = Entry(root, textvariable=vnombre_jugador).place(x=460, y=70)
etiqueta12 = Label(root, text="Anotaciones ").place(x=330, y=100)
wanotaciones = Entry(root, textvariable=vanotaciones).place(x=460, y=100)
etiqueta13 = Label(root, text="Minutos jugados").place(x=330, y=130)
wminutos = Entry(root, textvariable=vminutos).place(x=460, y=130)
etiqueta14 = Label(root, text="Dinero actual").place(x=330, y=160)
wdinero = Entry(root, textvariable=vdinero).place(x=460, y=160)
boton3 = Button(root, text="Ingresar", command=insercionJ).place(x=330, y=190)

# TRANSFERENCIA
vnombre_T = StringVar()
vnumero_T = IntVar()
vcantidad = IntVar()


# función para transferencia de dinero
def insercionT():
    nombre = vnombre_T.get()
    numero = vnumero_T.get()
    cantidad = vcantidad.get()
    conexion = mysql.connector.connect(**dbConnect)
    cursor = conexion.cursor()
    sqlInsertar = "Update Equipo set Presupuesto = Presupuesto -%s where nombre = %s"
    cursor.execute(sqlInsertar, (cantidad, nombre))
    sqlInsertar2 = "Update Jugador set Salario = Salario +%s where numero = %s"
    cursor.execute(sqlInsertar2, (cantidad, numero))
    conexion.commit()
    cursor.close()
    conexion.close()


etiqueta15 = Label(root, text="Nombre del equipo").place(x=180, y=290)
wnombre_T = Entry(root, textvariable=vnombre_T).place(x=310, y=290)
etiqueta16 = Label(root, text="Número del jugador").place(x=180, y=320)
wnumero_T = Entry(root, textvariable=vnumero_T).place(x=310, y=320)
etiqueta17 = Label(root, text="Cantidad a pagar").place(x=180, y=350)
wcantidad = Entry(root, textvariable=vcantidad).place(x=310, y=350)
boton4 = Button(root, text="Ingresar", command=insercionT).place(x=180, y=380)

boton5 = Button(root, text="Salir", command=root.quit).place(x=585, y=405)
root.mainloop()

print("Gracias por usar la base de datos:)")