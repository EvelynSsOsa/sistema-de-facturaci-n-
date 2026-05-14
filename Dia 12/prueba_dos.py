from tkinter import *
import random ## para generrar los recivos
import datetime  ## para generar la fecha de los recivos
from tkinter import filedialog, messagebox

operador = ''## aqui se van a ir cargando todos los números o simbolos  que sean presionados en la calculadora, guardara la operacion completa

precios_comida = [180, 95, 220, 160, 140, 210, 130, 250]
precios_bebida = [85, 70, 45, 55, 60, 75, 120, 140]
precios_postre = [95, 85, 70, 75, 110, 65, 90, 100]# lista de precios de comiditas, postres y bebidas


def click_boton(numero):
    global operador## pasamos a global a "operador" dentro de la función
    operador = operador + numero ## decimos que el operador actual, puede agregar otro numero o simbolo y ser un nuevo operador
    visor_calculadora.delete(0, END) ## aquí decimos que la "pantallita/visor" de la calculadora le vamos a borrar/limpiar el contenido
    ##que tenga , desde el indice 0, hasat el final del contenido
    visor_calculadora.insert(END, operador) # aquí vamos a colocar el operador (los nuemros que haya presionado el usuario) en la pantalla


def borrar():
    global operador ## pasamos a global a "operador" dentro de la función
    operador = '' ## aquí el operador se establece en un espacio en blanco
    visor_calculadora.delete(0, END) ## aquí decimos que la "pantallita/visor" de la calculadora le vamos a borrar/limpiar el contenido
    ##que tenga , desde el indice 0, hasat el final del contenido


def resultado():
    global operador # pasamos a global a "operador" dentro de la función
    ## tenemos una prueba de errores, decimos que si esta ejecución que esta dentro de try, nos sale mal entonces
    try:
        res = str(eval(operador))## eval ejecuta como codigo lo que encontro en la variable "operador" nos dara valor int y con str lo pasamos a caracter para poder imprimirlo en pantalla
        visor_calculadora.delete(0, END) ## borremos lo que teniamos en pantalla
        visor_calculadora.insert(0, res) ## imprimimos en pantalla el resultado
        operador = ''# inicializamos al operador
    except: ## si sale mal lo anterior
        visor_calculadora.delete(0, END) ## borremos lo que teniamos en pantalla
        visor_calculadora.insert(0, "Error") ## y en pantalla imprimimos "Error"
        operador = ''## inicializamos al operador

########################################
## 'revisar_check' es una función que nos ayuda a verificar si alguno de nuestro platillos a sido seleccionado
## tenemos un ciclo for por cada categoria en nuestro menu
###############################
def revisar_check():
    x = 0 ## es la posisción 0
    for c in cuadros_comida: ## decimos que por cada cuadro que tenemos en la categoria comida vamos a:
        if variables_comida[x].get() == 1: ## verificar si en su posión x(dependiendo de la itreación en la que nos encontremos) es igual a 1
            cuadros_comida[x].config(state=NORMAL)## vamos a cofigarla de modo que podamos modificar ese cuadro
            if cuadros_comida[x].get() == '0': ## estamos dentro de el 1er if, entonces decimos que si el cuadrito de texto es equivalente a 0
                cuadros_comida[x].delete(0, END)## decimos que ademas queremos que borre, lo que esta escrito por default en el recuadro
                cuadros_comida[x].focus() ## y que queremos el indice titileando ahí
        else:## en dado caso de que el cuadro no haya sido selecionada con 1
            cuadros_comida[x].config(state=DISABLED) ## necesitamos que se mantega desabilitado y sin posibilidad de editar
            texto_comida[x].set('0')## el cuadrito donde colacamos cuantos paltillos de ese queremos se quedara en 0
        x += 1## por cada iteración iremos aumnetando en uno la posición de x

    ##########################################################################################
    ##### y basicamente ese bucle for se vuelve repetri para cada una de nuestras categorias en el menu
    ######################################################################################
    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
                cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postre:
        if variables_postres[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, END)
                cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1

########################################
## 'total' es una función que calcula el costo total de todo lo que el cliente ha pedido
## incluyendo comidas, bebidas, postres junto con los impuestos
## luego actualiza las etiquetas de la interfaz con los valores calculados
###############################
def total():
    sub_total_comidita = 0 ## este lo vamos a inicializar en 0, porque aun no sabemos cuanto sera el subtotal de esta categoria "comida"
    p = 0 ## nos sirve como el indice para saber que precio corresponde al platillo de la cajita "texto_comida"
    for cantidad in texto_comida: ## decimos que por cada elemento que encontremos en "texto_comida"
        sub_total_comidita = sub_total_comidita + (float(cantidad.get()) * precios_comida[p]) ## vamos a obtener la cantidad y lo vamos a multiplicar por el precio que corresponde
        p += 1  ## aqui vamos a ir sumando uno a cada iteracion cuando recorramos las cajitas de texto

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postre = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postre[p])
        p += 1 ## y bueno el bucle funciona de la misma manera para todas las categorias, para bebida y postre

    sub_total = sub_total_postre + sub_total_bebida + sub_total_comidita
    impuestos = sub_total * 0.07
    total = sub_total + impuestos
    var_costo_comida.set(f'${round(sub_total_comidita, 2)}') ## actualizamos la etiqueta del costo de comida
    var_costo_bebida.set(f'${round(sub_total_bebida, 2)}') ## actualizamos la etiqueta del costo de bebida
    var_costo_postre.set(f'${round(sub_total_postre, 2)}')   ## actualizamos la etiqueta del costo de postre
    var_subtotal.set(f'${round(sub_total, 2)}')
    var_impuestos.set(f'${round(impuestos, 2)}')
    var_total.set(f'${round(total, 2)}') ## y los mismo con las etiquetas anteriores

########################################
## 'recibo' es una función que genera un ticket/recibo con todos los productos que el cliente pidio
## muestra cantidades, precios unitarios, subtotales por categoria, impuestos y total
## IMPORTANTE: al inicio llama a 'total()' linea 126, para asegurarse de que los costos esten actualizados
###############################

def recibo():
    total()## llamamos a la funcion total para asegurarnos de que los costos esten actualizados antes de generar el recibo
    texto_recibo.delete(1.0, END) ## limpiamos el area de recibo antes de escribir uno nuevo
    num_recibo = f'N# -{random.randint(1000, 9999)}' ## aqui por medio del metodo de "randint" decimos que vamos tomar nuemro del 1000 al 9999 para crear el folio del recibo
    fecha = datetime.datetime.now()## mandamos a llamar a los metodos necesarios para obtener la fecha actual
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}' ## en la variable fecha_recibo vamos a dar formato a la fecha
    texto_recibo.insert(END, f'Datos: \t{num_recibo}\t\t{fecha_recibo}\n') ### insertamos tanto el numero de recibo junto con la fecha
    texto_recibo.insert(END, f'*' * 47 + '\n') ## vamos a imprimir 47 asteriscos para que se vea mas bonito nuestro recibo
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n') ## aqui estamos espaciando los titulos de nuestro ticket
    texto_recibo.insert(END, f'-' * 54 + '\n') ## luego vamos a poner 54 guiones

    x = 0## inicializamos el indice que nos va a servir para recorrer la lista de las diferentes comida
    for comida in texto_comida: ### decimos que por cada elemento de la lista de cajitas de texto de la categoria "comida"
        if comida.get() != '0':   ## si la cantidad es diferente de 0 (el cliente pidio al menos uno de ese platillo)
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t' ## insertamos el nombre del platillo y la cantidad, segun sea la posisción del indice x 
                                     f'${int(int(comida.get()) * precios_comida[x])}\n')## calculamos el costo total de ese platillo (cantidad * precio unitario), segun sea la posición del indice x
        x += 1 ## aumentamos el iterador para pasar al siguiente platillo

### los siguientes bucles funcionan igualito que el bucle de comidas

    x = 0 ##reiniciamos el indice para las bebidas
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                     f'${int(int(bebida.get()) * precios_bebida[x])}\n')
        x += 1 ## aumentamos el iterador para pasar a la siguiente bebida

    x = 0  ## reiniciamos el indice para los postres
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t'
                                     f'${int(int(postre.get()) * precios_postre[x])}\n')
        x += 1## aumentamos el iterador para pasar al siguiente platillo en postre

    texto_recibo.insert(END, f'-' * 54 + '\n') ### en forma de linea de sepración vamos a imprimir 54 de estos " * " asteriscos
    texto_recibo.insert(END, f'Costo de la Comida: \t\t\t {var_costo_comida.get()}\n') ## mostramos el subtotal de comidas
    texto_recibo.insert(END, f'Costo de la Bebida: \t\t\t {var_costo_bebida.get()}\n') ## mostramos el subtotal de bebidas
    texto_recibo.insert(END, f'Costo de los Postres: \t\t\t {var_costo_postre.get()}\n') ## mostramos el subtotal de postres
    texto_recibo.insert(END, f'-' * 54 + '\n') ## otra linea de separacion, ahora vamos a impirmir 54 de estos " - "
    texto_recibo.insert(END, f'Sub Total: \t\t\t {var_subtotal.get()}\n') ## mostramos el subtotal (sin impuestos)
    texto_recibo.insert(END, f'Impuestos: \t\t\t {var_impuestos.get()}\n') ## mostramos los impuestos
    texto_recibo.insert(END, f'Total: \t\t\t {var_total.get()}\n')  ## mostramos el total final
    texto_recibo.insert(END, f'*' * 47 + '\n') ## asteriscos decorativos al final, imprimimos 47
    texto_recibo.insert(END, f'Vuelve pronto :) ') ## aquí dejamos un mensajito bonito de despedida

########################################
## 'guardar' es una funcion que nos permite guardar el recibo generado en un archivo de texto
## abre un cuadro de dialogo para que el usuario elija donde guardarlo
###############################
def guardar():
    info_recibo = texto_recibo.get(1.0, END)  ## vamos a obtener toda la informacion que haya en el panel de recibo desde el indice 1.0 hasta el final
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt') ## abrimos un cuadro de dialogo para guardar archivo
    ## queremos que se cree un archivo de tipo txt y que este en modo escritura (el modo escritura es este 'w')
    if archivo:## verificamos que el usuario no haya cancelado la operacion (si archivo no es None)
        archivo.write(info_recibo) ## escribimos toda la informacion del recibo en el archivo
        archivo.close() ## una vez terminamos de escribir, cerramos el archivo
        messagebox.showinfo('Información', 'Su recibo ha sido guardado exitosamente :D')
## aqui ya solo dejamos un mensajito indicando al usuario que ya guardamos su recibo

########################################
## 'resetear' es una funcion que reinicia/resetea toda la pantalla
## borra el recibo actual, limpia todas las cantidades, deja en 0 a  todos los checkboxes
## y resetea todas las etiquetas de costos a valores vacios
###############################
def resetear():
    texto_recibo.delete(1.0, END)  ## borramos todo el contenido del area de recibo

    for texto in texto_comida: ## recorremos cada cajita de cantidad de comida
        texto.set('0') ## la establecemos a 0

    for texto in texto_bebida:
        texto.set('0')

    for texto in texto_postre:
        texto.set('0') ## y hacemos lo mismo para las otras categorias de bebida y de postre

## por cada categoria del menu, vamos a recorrer las listas de cuadros de texto/ cajita de texto y las vamos a establecer en "dessbilitadas"
## lo que provoca que no podamos indicar cuantos platillos voy a quere de esa comida en especial
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    ## desmarcamos todos los checkboxes (los ponemos en 0) para cada categoria del menu
        ## decimos que por cada elemento de la lista de los checkboxes vamos a marcarlo en 0
    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postres:
        v.set(0)

        ## reseteamos todas las etiquetas de costos a valores vacios
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')


# ==================== VENTANA PRINCIPAL ====================
aplicacion = Tk() ## iniciamos tkinter
## tamaño de la ventana:
## 1300 -> Ancho
## 750 -> Alto
## luego colocamos la posicion de donde queremos que salga la pantalla en x & y (0,0 significa esquina superior izquierda)
aplicacion.geometry('1300x750+0+0')  # <--- VENTANA MÁS GRANDE(este es nuestro superficie donde vamos a ir dibujando cada categoria)
aplicacion.resizable(0, 0) ## evitamos maximizar... esto es para que no nos de la opcion de estirar/expandir la pantalla
aplicacion.title("Mi restaurante - Sistema de Facturación") ## le ponemos un titulo a nuestra ventana
aplicacion.config(bg='#DEB887') ## configuramos el color de fondo de la ventana principal

# ==================== PANEL SUPERIOR ====================
## creamos el panel superior que contendra el titulo
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP, fill=X) ## lo ubicamos en la parte superior y hacemos que se expanda horizontalmente

## ETIQUETA DEL TITULO
## por medio del metodo "Label" vamos dandole formato a nuestra etiqueta
## el texto que tendra nuestra etiqueta -> text='Sistema de Facturacion'
## el color que tendran las letras -> fg='azure4'
## la fuente -> font=('Helvetica', 58)
## el fondo -> bg='burlywood'
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='azure4',
                        font=('Helvetica', 58), bg='burlywood')
etiqueta_titulo.pack()## empaquetamos la etiqueta en el panel

# ==================== PANEL IZQUIERDO ====================
## construimos el panel izquierdo donde iran las comidas, bebidas y postres
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT, bg='#DEB887')
panel_izquierdo.pack(side=LEFT, fill=BOTH, expand=True) ## lo arrojamos del lado izquierdo y permitimos que se expanda

## panel de costos (va en la parte inferior del panel izquierdo)
## con ayuda del metodo "Frame", le pasamos "panel_izquierdo" como contenedor
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=50, pady=10)
panel_costos.pack(side=BOTTOM, fill=X, pady=10) ## lo ubicamos en la parte inferior y que ocupe todo el ancho
## este panel es el que va a contener el subtotal de cada categoria ademas de tener el subtotal, total y los impuestos( ESTO NO ES EL RECIBO)

# Paneles de comidas, bebidas y postres:
## usamos "LabelFrame" que es como una etiqueta que al mismo tiempo es un panel

################PANEL COMIDAS:
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Helvetica', 16, 'bold'),
                           bd=2, relief=GROOVE, fg='azure4', bg='#DEB887') ## damos formasto a la estiqueta
panel_comidas.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5) ## lo arrojamos a la izquierda

################PANEL BEBIDAS:
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Helvetica', 16, 'bold'),
                           bd=2, relief=GROOVE, fg='azure4', bg='#DEB887') ## damos formasto a la estiqueta
panel_bebidas.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5) ## lo arrojamos a la izquierda, (ESTO VA A PROVOCAR QUE SE COLOQUE A UN LADO DEL PANEL DE COMIDAS )

################PANEL POSTRES:
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Helvetica', 16, 'bold'),
                           bd=2, relief=GROOVE, fg='azure4', bg='#DEB887') ## damos formasto a la estiqueta
panel_postres.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)## lo arrojamos a la izquierda, (ESTO VA A PROVOCAR QUE SE COLOQUE A UN LADO DEL PANEL DE BEBIDAS )

# ==================== PANEL DERECHO ====================
## construimos el panel derecho donde ira la calculadora, el recibo y los botones
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT, bg='#DEB887')
panel_derecha.pack(side=RIGHT, fill=Y, padx=10, pady=10) ## lo arrojamos a la derecha, ESTE PANEL ES UN (FONDO NUEVO ) VA SEGUIDO DE LAS CATEGORIAS PERO AGRUPA VARIOS ELEMENTOS

# Panel Calculadora (donde se muestra el ticket)
panel_calculadora = Frame(panel_derecha, bd=2, relief=GROOVE, bg='burlywood', padx=10, pady=10)
panel_calculadora.pack(pady=10)

# Panel Recibo (donde se muestra el ticket)
panel_recibo = Frame(panel_derecha, bd=2, relief=GROOVE, bg='burlywood', padx=10, pady=10)
panel_recibo.pack(pady=10)

# Panel Botones principales (Total, Recibo, Guardar, Resetear)
panel_botones = Frame(panel_derecha, bd=2, relief=GROOVE, bg='burlywood', padx=10, pady=10)
panel_botones.pack(pady=10)

# ==================== LISTAS DE PRODUCTOS ====================
lista_comidas = ['Lasagna', 'Tacos de Pastor', 'Sushi', 'Hamburguesa BBQ', 'Dumplings', 'Pizza Margarita', 'Alitas',
                 'Paella']
lista_bebidas = ['Malteada de chocolate', 'Frappé de café', 'Agua de Horchata', 'Limonada mineral',
                 'Chocolate Caliente', 'Smoothie', 'Piña Colada', 'Margarita']
lista_postres = ['Cheesecake de fresa', 'Brownie con helado', 'Flan napolitano', 'Pay de limon', 'Tiramisu', 'Churros',
                 'Crepas', 'Mil hojas']

# ==================== CREAR CHECKBOXES DE COMIDA ====================
## aqui estamos creando los checkboxes y cajitas de texto para cada comida
variables_comida = []  ## lista para almacenar el estado de cada checkbox (marcado o no) es decir 0 o 1
cuadros_comida = []  ## lista de las cajitas de texto donde el usuario escribe la cantidad
texto_comida = [] ## lista que conecta las cajitas de texto con sus valores (StringVar)
contador = 0 ## contador que nos ayuda a recorrer la lista de comidas y asignar posiciones

for comida in lista_comidas: ## por cada comida en nuestra lista de comidas
    variables_comida.append('')## en la lista "variables_comida" agregamos un espacio (luego sera remplazado por IntVar)
    variables_comida[contador] = IntVar()  ## IntVar guarda valores booleanos (1 o 0) en nuestra lista "variables_comida" que indican si el checkbox esta marcado
    ## creamos el checkbox:
    ## decimos que queremos que estos chechbuttons salgan en el panel de comida, que por cada comida traiga el titulo de cada una y damos formato a ese titulo del platillo
    comida_widget = Checkbutton(panel_comidas, text=comida.title(), font=('Helvetica', 12, 'bold'),
                                ## " onvalue=1, offvalue=0,"->  luego decimos que esta encedido cuando esta en uno y apagado cuando esta en 0
                                onvalue=1, offvalue=0, variable=variables_comida[contador], ## "variable=variables_comida[contador]," decimos que vamoas
                                # a identificar el checkbutton, que se guardo en la lista "variables_comida"
                                command=revisar_check) ## luego con "command=revisar_check" decimos que vamos a mandar a llamar a la función "revisar_cehck" linea 41 a 83
    comida_widget.grid(row=contador, column=0, sticky=W, padx=5, pady=2) ## vamos a colocar a cada check button creado en una cuadricula
    ## por eso la fila va tomando el valor del contador en cada iteración

    ##es importante ver que "texto_comida.append" abre lo que vendría siendo la lectura de nuestras cajas de texto
    texto_comida.append('') ## es decir que vamos a darle un espacio a nuestra lista, que luego sera remplazado por algún caracter en la lista "texto_comida"
    texto_comida[contador] = StringVar()  ## decimos que por cada iteración y conforme vaya avanzando el contador vamoas a agregar un "StringVar()" que nos ayuda a guardar el texto que
    ## el usuario escriba, ahora tenemos una lista de "StringVar()" que nos ayudara a leer
    texto_comida[contador].set('0') ## atodos los elementos de esta lista los vamos a establecer en 0
    cuadros_comida.append('') ## ahora para la lista de "cuadros_comida" vamos a agreagr a un espacio en blanco

    ## ahora decimos que por cada cuadro de comida en cada iteración, vamos a crear un "Entry" en el "panel_comidas"
    cuadros_comida[contador] = Entry(panel_comidas, font=('Helvetica', 14, 'bold'),## le damos formato a la letra, decimos que tipo de fueste, estilo y el tamaño
                                     bd=1, width=6, state=DISABLED,## y lo establecemos como desabilitado
                                     textvariable=texto_comida[contador])  ## aqui es donde pasa la magia porque con "textvariable=texto_comida[contador]"
    # decimos que vamos a relacionar a cada "Entry" con el lector de cuadritos, esto nos va a permitir saber cuantos platillos va a querer el usuario de ese platillo, por cada iteración
    cuadros_comida[contador].grid(row=contador, column=1, padx=5, pady=2)
    ## aqui vamos a colocar a los Entry uno debajo del otro, por eso "row" va tomando el valor de CONTADOR
    contador += 1 ## Contador va a ir aumentando en uno

# ==================== CREAR CHECKBOXES DE BEBIDA ==================== es la misma logica para todas las categorias del menu, en este caso bebidas
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0

for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida_widget = Checkbutton(panel_bebidas, text=bebida.title(), font=('Helvetica', 12, 'bold'),
                                onvalue=1, offvalue=0, variable=variables_bebida[contador],
                                command=revisar_check)
    bebida_widget.grid(row=contador, column=0, sticky=W, padx=5, pady=2)

    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida.append('')
    cuadros_bebida[contador] = Entry(panel_bebidas, font=('Helvetica', 14, 'bold'),
                                     bd=1, width=6, state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, column=1, padx=5, pady=2)
    contador += 1

# ==================== CREAR CHECKBOXES DE POSTRE ==================== es la misma logica para todas las categorias del menu, en este caso bebidas
variables_postres = []
cuadros_postre = []
texto_postre = []
contador = 0

for postre in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postre_widget = Checkbutton(panel_postres, text=postre.title(), font=('Helvetica', 12, 'bold'),
                                onvalue=1, offvalue=0, variable=variables_postres[contador],
                                command=revisar_check)
    postre_widget.grid(row=contador, column=0, sticky=W, padx=5, pady=2)

    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre.append('')
    cuadros_postre[contador] = Entry(panel_postres, font=('Helvetica', 14, 'bold'),
                                     bd=1, width=6, state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador, column=1, padx=5, pady=2)
    contador += 1

# ==================== PANEL DE COSTOS ====================
## aqui creamos las variables que van a almacenar los valores de los costos se utilizan mucho en las funciones de arriba del codigo
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

## Fila 0 (Costo Comida e Impuestos)
Label(panel_costos, text='Costo Comida', font=('Helvetica', 12, 'bold'), bg='azure4', fg='white').grid(row=0, column=0,
                                                                                                       padx=5, pady=5)
Entry(panel_costos, font=('Helvetica', 12, 'bold'), bd=1, width=12, state='readonly',
      textvariable=var_costo_comida).grid(row=0, column=1, padx=5, pady=5)

Label(panel_costos, text='Impuestos', font=('Helvetica', 12, 'bold'), bg='azure4', fg='white').grid(row=0, column=2,
                                                                                                    padx=5, pady=5)
Entry(panel_costos, font=('Helvetica', 12, 'bold'), bd=1, width=12, state='readonly', textvariable=var_impuestos).grid(
    row=0, column=3, padx=5, pady=5)

## Fila 1 (Costo Bebida y Subtotal)
Label(panel_costos, text='Costo Bebida', font=('Helvetica', 12, 'bold'), bg='azure4', fg='white').grid(row=1, column=0,
                                                                                                       padx=5, pady=5)
Entry(panel_costos, font=('Helvetica', 12, 'bold'), bd=1, width=12, state='readonly',
      textvariable=var_costo_bebida).grid(row=1, column=1, padx=5, pady=5)

Label(panel_costos, text='Subtotal', font=('Helvetica', 12, 'bold'), bg='azure4', fg='white').grid(row=1, column=2,
                                                                                                   padx=5, pady=5)
Entry(panel_costos, font=('Helvetica', 12, 'bold'), bd=1, width=12, state='readonly', textvariable=var_subtotal).grid(
    row=1, column=3, padx=5, pady=5)

# ## Fila 2 (Costo Postre y Total)
Label(panel_costos, text='Costo Postre', font=('Helvetica', 12, 'bold'), bg='azure4', fg='white').grid(row=2, column=0,
                                                                                                       padx=5, pady=5)
Entry(panel_costos, font=('Helvetica', 12, 'bold'), bd=1, width=12, state='readonly',
      textvariable=var_costo_postre).grid(row=2, column=1, padx=5, pady=5)

Label(panel_costos, text='Total', font=('Helvetica', 12, 'bold'), bg='azure4', fg='white').grid(row=2, column=2, padx=5,
                                                                                                pady=5)
Entry(panel_costos, font=('Helvetica', 12, 'bold'), bd=1, width=12, state='readonly', textvariable=var_total).grid(
    row=2, column=3, padx=5, pady=5)

# ==================== BOTONES PRINCIPALES ====================
botones = ['Total', 'Recibo', 'Guardar', 'Resetear'] ## creamos una lista de botones que traera consigo el nombre de cada boton
botones_creados = [] ## creamos una lista vacia que nos va ayudar a que los bototnes tomen una posición en el panel
## tenemos un ciclo for donde decimos que por cada boton en la lista de botones
for i, boton in enumerate(botones):
    ## vamos a crear un boton, donde le pasamos como paramtero el panel de botones, para indicar que ahí queremos que se encuntren los botones
    ## nos traemos al bototn con su titulo y le damos formato, indicando el tipo de fuente, tamaño y estilo
    btn = Button(panel_botones, text=boton.title(), font=('Helvetica', 12, 'bold'),
                 fg='black', bg='azure4', bd=2, width=10) ## decimos que queremos que las letras sean de color negro
    btn.grid(row=0, column=i, padx=5, pady=5)## acodamos a los botones en la misma fila "row = 0" y que la columna es que avance con el iterador "i"
    ## esto nos ayuda a que los botones queden en un solo renglon
    botones_creados.append(btn) ## entonces a la lista de "botones_creados" le vamos agregando el boton con ".append(btn)"

## tomando en cuenta que los botones van ir tomando posisción en la lista segun hayan estado acomodados en la lista "botones"
botones_creados[0].config(command=total) ##la posisción 0 correponde al boton "Total" y con ayuda del metodo "command" puedo mandar a llamar a la función "total"
botones_creados[1].config(command=recibo) ##la posisción 1 correponde al boton "Recibo" y con ayuda del metodo "command" puedo mandar a llamar a la función "recibo"
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)## así con estos ultimos 2 botones, tambien cree una función para cad auno de ellos

# ==================== AREA DE RECIBO ====================
texto_recibo = Text(panel_recibo, font=('Helvetica', 11), bd=2, width=50, height=12, relief=SUNKEN)
texto_recibo.pack(padx=5, pady=5) # aqui solo estpy definiendo el area en donde se encontrara el recibo el tipo de fuente etc

# ==================== CALCULADORA ====================
## ahora vamos a empezar a crear la pantallita de la calculadora, le vamos a dar las medidas, el tipo de letra con la que queramos que se escriba
visor_calculadora = Entry(panel_calculadora, font=('Helvetica', 18, 'bold'), width=20, bd=3, relief=SUNKEN,
                          justify=RIGHT)## queremos que toda salga del lado izquierdo
visor_calculadora.grid(row=0, column=0, columnspan=4, padx=5, pady=5) ## decimos que queremos que aprezca en la columna 0 en la fila 0
## columnspan=4 -> le decimos que ocupe 4 columnas (para que sea mas ancho que los botones)
## padx=5, pady=5 -> le agregamos un poco de espacio alrededor para que no quede pegado

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', 'CL','0', '/','RE']
## luego creamos una lista de los botones que queremos para nuestra calculadora

botones_guardados = [] ## creamos una lista vacia que va ir asignando un valor a cad auno de los botones
fila = 1 ##establecemos a fila en 1
columna = 0 ## establecemos a columna en 0

## vamos a pasar como paramtero el "panel_calculadora" como parametro de que queremos que ahí se creen nuestros botones okey

for boton in botones_calculadora: ## decimos que por cada boton dentro de la lista "botones_calculadora", vamos a
    if boton == 'CL':## decimos que si dentro de esa lista encontramos un boton que sea igual a "CL"
        btn = Button(panel_calculadora, text=boton, font=('Helvetica', 14, 'bold'), fg='black', bg='orange', bd=2, ## damos formato a nuestra feunte
                     width=5, command=borrar) ## por medio del metodo "command" vamos a mandar a llamar a la función de "borrar"
    elif boton == 'RE': ## decimos que si dentro de esa lista encontramos un boton que sea igual a "RE"
        btn = Button(panel_calculadora, text=boton, font=('Helvetica', 14, 'bold'), fg='black', bg='green', bd=2,
                     width=5, command=resultado) ## por medio del metodo "command" vamos a mandar a llamar a la función de "resultado"
    else: ## decimos que si ninguno de los botones en la lista tiene algun caracter espacial como el que marque antes...entonces:
        ## decimos que cree al boton en el panel_calculadora y que le de formato a su carcter, con algun tipo de fuente, tamaño etc
        btn = Button(panel_calculadora, text=boton, font=('Helvetica', 14, 'bold'), fg='black', bg='azure4', bd=2,
                     width=5,
                     command=lambda b=boton: click_boton(b))
# b=boton copia el valor actual de boton en el momento de la iteración, entonces decimos que justo cuando se crea la calucladora, cada boton en la iteración ira guardando
    ## su valor en una cajita y cuando el usuario haga click se usa el valor que se guardo en b
    # Primera iteración: boton = '7'
    # Segunda iteración: boton = '8'
    # Tercera iteración: boton = '9'
    # Cuarta iteración: boton = '+'
    # etc.

    # En CADA iteración, CREAMOS un botón con su comando -> "command=lambda b=boton: click_boton(b)"
    botones_guardados.append(btn) ## ahora en la lista "botones_guardados" vamos a agregar a los botones con ".append(btn)"
    btn.grid(row=fila, column=columna, padx=2, pady=2) ## vamos a colocar el boton en la cuadricula y pasamos la fila y la columna que correponda

    columna += 1
    if columna > 3: ## decimos quqeq si la columna es mayor a 3
        columna = 0 ## que nos refgrese a columna 0
        fila += 1 ## y que a fila le vaya aumentando uno
        ## con esto tendriamos como reusltado algo así
## |  7  |  8  |  9  |  +  |
## |  4  |  5  |  6  |  -  |
## |  1  |  2  |  3  |  *  |
## | CL  |  0  |  /  | RE  |

# ==================== FINAL ====================
aplicacion.mainloop() ## este de aquí nos ayuda a mantener la ventana de tinker abierta mientras ejecutamos nuestro programa o manipulamos
## es un bucle infinito 