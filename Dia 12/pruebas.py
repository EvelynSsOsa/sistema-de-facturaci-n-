from tkinter import *
import random ## para generrar los recivos
import datetime  ## para generar la fecha de los recivos
from tkinter import filedialog, messagebox
operador = '' ## aqui se van a ir cargando todos los números o simbolos  que sean presionados en la calculadora, guardara la operacion completa

# lista de precios de comiditas
precios_comida = [180, 95, 220, 160, 140, 210, 130, 250]

# lista de precios de bebidas
precios_bebida = [85, 70, 45, 55, 60, 75, 120, 140]

# lista de precios de postres
precios_postre = [95, 85, 70, 75, 110, 65, 90, 100]
def click_boton(numero):
    global operador ## pasamos a global a "operador" dentro de la función
    operador = operador + numero ## decimos que el operador actual, puede agregar otro numero o simbolo y ser un nuevo operador
    visor_calculadora.delete(0,END) ## aquí decimos que la "pantallita/visor" de la calculadora le vamos a borrar/limpiar el contenido
    ##que tenga , desde el indice 0, hasat el final del contenido
    visor_calculadora.insert(END, operador)## aquí vamos a colocar el operador (los nuemros que haya presionado el usuario)


def borrar():
    global operador ## pasamos a global a "operador" dentro de la función
    operador = '' ## aquí el operador se establece en un espacio en blanco
    visor_calculadora.delete(0, END)## aquí decimos que la "pantallita/visor" de la calculadora le vamos a borrar/limpiar el contenido
    ##que tenga, desde el indice 0, hasat el final del contenido

def resultado():
    global operador## pasamos a global a "operador" dentro de la función
    res = str (eval(operador)) ## pasamos como parametro a "operador" a la función "eval" que nos ayuda a ejecutar como codigo
    # lo que le pasemos como parametro y con "str" vamos a convertir el int en un str, para poder verlo en la pnatllita de la calculadora
    visor_calculadora.delete(0, END) ## aqui borramos lo que haya habiado antes, ya sabemos que de prinsipio a fin
    visor_calculadora.insert(0, res) ## api pasamos/ insertamos el resultado desde el indice 0
    operador = '' ## y volvemos a restablecer el operador

########################################
## 'revisar_check' es una función que nos ayuda a verificar si alguno de nuestro platillos a sido seleccionado
## tenemos un ciclo for por cada categoria en nuestro menu
###############################
def revisar_check():
    x = 0 ## es la posisción 0
    for c in cuadros_comida: ## decimos que por cada cuadro que tenemos en la categoria comida vamos a:
        if variables_comida[x].get() == 1:## verificar si en su posión x(dependiendo de la itreación en la que nos encontremos) es igual a 1 (el 1 es del check button)
            cuadros_comida[x].config(state = NORMAL) ## vamos a cofigarla de modo que podamos modificar ese cuadro
            ## estamos dentro de el 1er if, entonces decimos que si el cuadrito de texto es equivalente a 0
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0,END)## decimos que ademas queremos que borre, lo que esta escrito por default en el recuadro
                cuadros_comida[x].focus() ## y que queremos el indice titileando ahí
        else: ## en dado caso de que el cuadro no haya sido selecionada con 1
            cuadros_comida[x].config(state = DISABLED) ## necesitamos que se mantega desabilitado y sin posibilidad de editar
            texto_comida[x].set('0')
        x += 1 ## por cada iteración iremos aumnetando en uno la posición de x

##########################################################################################
##### y basicamente ese bucle for se vuelve repetri para cada una de nuestras categorias en el menu
######################################################################################

    x = 0## es la posisción 0
    for c in cuadros_bebida:  ## decimos que por cada cuadro que tenemos en la categoria comida vamos a:
        if variables_bebida[x].get() == 1: ## verificar si en su posión x(dependiendo de la itreación en la que nos encontremos) es igual a 1
            cuadros_bebida[x].config(state=NORMAL) ## vamos a cofigarla de modo que podamos modificar ese cuadro
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)# decimos que ademas queremos que borre, lo que esta escrito por default en el recuadro
                cuadros_bebida[x].focus()## y que queremos el indice titileando ahí
        else:## en dado caso de que el cuadro no haya sido selecionada con 1
            cuadros_bebida[x].config(state=DISABLED)## necesitamos que se mantega desabilitado y sin posibilidad de editar
            texto_bebida[x].set('0')
        x += 1 ## por cada iteración iremos aumnetando en uno la posición de x

    ##########################################################################################
    ##### y basicamente lo mismo para postres
    ######################################################################################

    x = 0## es la posisción 0
    for c in cuadros_postre: ## decimos que por cada cuadro que tenemos en la categoria comida vamos a:
        if variables_postres[x].get() == 1: ## verificar si en su posión x(dependiendo de la itreación en la que nos encontremos) es igual a 1
            cuadros_postre[x].config(state=NORMAL)  ## vamos a cofigarla de modo que podamos modificar ese cuadro
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, END) ### decimos que ademas queremos que borre, lo que esta escrito por default en el recuadro
                cuadros_postre[x].focus() ## y que queremos el indice titileando ahí
        else: # en dado caso de que el cuadro no haya sido selecionada con 1
            cuadros_postre[x].config(state=DISABLED) ## necesitamos que se mantega desabilitado y sin posibilidad de editar
            texto_postre[x].set('0')
        x += 1## por cada iteración iremos aumnetando en uno la posición de x



def total():
    sub_total_comidita = 0 ## este lo vamos a inicailizar en 0, porque aun no sabemos cuanto sera el subtotal de esta categoria de "comida"
    p = 0 ## nos sirve como el indice para saber que precio corresponde a el platillo de la cajita "texto_comida"
    for cantidad in texto_comida: ## decimos que por cada elemento que encontremos en "texto_comida"
        sub_total_comidita = sub_total_comidita + (float(cantidad.get()) * precios_comida[p]) ## vamos a obtener la catidad y lo vamos a multiplicar por el precio que corresponde
        p += 1 ## aqui vamos a ir sumando uno a cada iteración cuando recorramos las cajitas de texto
##############
    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1
############## y para estos 2 bucles de bebida y de postre pasa exacatemnte lo mismo, es decir:
    ###p es un índice que correlaciona cada cajita de cantidad (texto_comida[p]) con su precio correspondiente
    ##(precios_comida[p]). Ambos están alineados por posición en sus respectivas listas (ej: la primera comida usa el primer precio)
    #############################################################
    sub_total_postre = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postre[p])
        p += 1

    sub_total = sub_total_postre + sub_total_bebida + sub_total_comidita ## aqui estamos sacando el subtotal de postre, bebida y comida
    impuestos = sub_total * 0.07 ## le agregamos el impuesto
    total = sub_total + impuestos ## y ahora obetenmos el total ya con todo y los impuestos
    var_costo_comida.set(f'${round(sub_total_comidita,2)}')
    var_costo_bebida.set(f'${round(sub_total_bebida,2)}')
    var_costo_postre.set(f'${round(sub_total_postre, 2)}')
    var_subtotal.set(f'${round(sub_total, 2)}')
    var_impuestos.set(f'${round(impuestos, 2)}')
    var_total.set(f'${round(total,2)}') ## etsas son etiquetas que creamos a las que les estamos estableciendo lo que se vera en ellas

def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# -{random.randint(1000,9999)}' ## aquí generamos un numero de folio en aleatorio
    fecha = datetime.datetime.now() ## madamos a llamar a los metodods necesarios para obtener la fehca
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} -{fecha.hour}:{fecha.minute}' ## en la variable feche_recibo vamos a dar formato a la fecha, mandando a llamar a un atributo especial de fecha
    texto_recibo.insert(END, f'Datos: \t{num_recibo}\t\t{fecha_recibo}\n') ## entonces insertamos tanto el numero de recibo junto con la fecha
    texto_recibo.insert(END,f'*' * 47 +'\n') ## vamos a imprimir 47 asteriscos para que se vea mas bonito nuestro recibo
    texto_recibo.insert(END,'Items\t\tCant.\tCosto Items\n') ## aqui estamos espcaiando los titulos de nuestro tiket
    texto_recibo.insert(END,f'-' * 54 + '\n') ## y luego vamos a poner a 54 asteriscos

    x = 0 ## inicializamos al indice que nos va a servir para recorrer la lista de las difernetes comidas
    for comida in texto_comida: ## decimos que por cada elemento de la lista de cajitas de texto de la categoria "comida"
        if comida.get() !='0': ## decimos que si uno de los elementos es diferente de 0 entonces:
            #### entonces en el recibo vamos a insertar "la comida selecionada según sea la iteración/ el indice que corresponde segun lo que el usuario haya selecionado "
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t' ## y con "comida.get" decimos que vamos a obtener el elemento que contenga esa cajita de texto_comida(cuantos quiere de ese platillo)
                                     f'${int(int(comida.get()) * precios_comida[x])}\n') ## tenemos a " int(comida.get())" que nos ayuda a convertir la variable a integer y lo
            ## multiplicamos por el precio de la comida segun correponda con la cajita de texto
        x += 1 ## y vamos a ir aumentando en uno nuestro iterador para poder ir viendo como se va afetando nuestra categoria con la selección de nuestro cliente

    x = 0### pasa exactamente lo mismo con estos 2 bucles de aquí mira
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                     f'${int(int(bebida.get()) * precios_bebida[x])}\n')
        x += 1

    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t'
                                     f'${int(int(postre.get()) * precios_postre[x])}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 54 + '\n') ## luego imprimimos a 54 de estos " - "
    texto_recibo.insert(END,f'Costo de la Comida: \t\t\t {var_costo_comida.get()}\n') ## aquí ya solo vamos a pasar a la cantidad
    texto_recibo.insert(END, f'Costo de la Bebida: \t\t\t {var_costo_bebida.get()}\n') # y con "var_costo_comida.get()" traemos el costo del platillo en especifico que seleciono el usuario
    texto_recibo.insert(END, f'Costo de los Postres: \t\t\t {var_costo_postre.get()}\n') ## para cada categoria vamos a dar un salto de linea
    texto_recibo.insert(END, f'-' * 54 + '\n') ## volvemos a imprimir 54 de estos " - "
    texto_recibo.insert(END, f'Sub Total: \t\t\t {var_subtotal.get()}\n') ## luego ya solo nos traemos el subtotal (total a pagar sin los impuestos)
    texto_recibo.insert(END, f'Impuestos: \t\t\t {var_impuestos.get()}\n')## traemos a los impuestos tambien
    texto_recibo.insert(END, f'Total: \t\t\t {var_total.get()}\n') ## y luego traemos al total
    texto_recibo.insert(END, f'*' * 47 + '\n') ## vamos a imprimir 47 de estos " * " asteriscos
    texto_recibo.insert(END,f'Vuelve pronto :) ') ## imprimimos un mensajito bonito


def guardar(): ## y bueno esta función de aquí nos sirve para poderle guardare el recibo que se genero
    info_recibo = texto_recibo.get(1.0,END) ## vamos a obetener toda la información que haya en el panel de recibo desde el indice 1 hasta el final
    archivo = filedialog.asksaveasfile(mode = 'w', defaultextension= '.txt') ## queremos que se cree un archivo de tipo txt y que este en modo escritura (el modo escritura es este 'w')
    archivo.write(info_recibo) ## y decimos que queremos que en el archivo que acabamos de crear, vamos a escribir toda la informacion que guardamos en "info_recibo"
    archivo.close() ## una vez ya terminamos de escribir en el archivo vamos a cerrar ese documento
    messagebox.showinfo('Información','Su recibo a sido guardado exitosamente :D') ## esto es el letrerito que nos va a salir despues de guardarlo correctamente

def resetear(): ## con esta función de aquí lo que estoy haciendo es recetear toda la pantalla
    texto_recibo.delete(1.0,END) ## voy a borrar todo lo que hay encontrado en la pantalla de recibo desde el indice 1 hasta el final

    for texto in texto_comida: ## decimos que por cada texto (caracter/simbolo) que encuentre en la lista de cajitas
        texto.set('0') ## lo va a setera en 0

    for texto in texto_bebida:
        texto.set('0')

    for texto in texto_postre:
        texto.set('0') ## y pasa exactamente lo mismo para cada caetgoria en este caso para postres y bebida
### y bien ahora decimos que por cada cuadro, lo vamos a volver a establcer en desabilitado, ya que el chechk button de cada comida ya no estara marcado, lo que provoca
    ## que no podamos decir cunatos queremos de ese platillo
    for cuadro in cuadros_comida:
        cuadro.config(state = DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state = DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state = DISABLED) ## pasa lo mismo para categoria de nuestro menu, para bebidas, comida y postres

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postres:
        v.set(0)


    var_costo_comida.set('') ## aun no habria nada de gatsos en la categoria de comida
    var_costo_bebida.set('')## ni la bebida
    var_costo_postre.set('')## o la de comida
    var_subtotal.set('') ## por lo tanto tampoco hay un subtotal
    var_impuestos.set('')## ni impuestos
    var_total.set('') ## ni un total

#iniciar tkinter
aplicacion = Tk()

##tamaño de la ventana:
##1020 -> Ancho
##630 -> Alto
## luego colocamos la posisción de donde queremos que salga pantalla en x & y
aplicacion.geometry('1300x750+0+0')  #1020x630+0+0 1300x750+0+0

##evitar maximizar... esto es para que no nos de opcion de estender la pantalla
aplicacion.resizable(0,0)

aplicacion.title("Mi restaurante - Sistema de Facturación")

aplicacion.config(bg='#DEB887')

## panel superior
panel_superior = Frame(aplicacion, bd=1, relief = FLAT)
panel_superior.pack(side=TOP) ## aquí decimos en que parte de la pantalla queremos arrojas a nuestro "panel_superior"

##ETIQUETA DEL TITULO
## por medio del metodo "label" vamos dandole formato a nuestra etiqueta, podemos indicar entonces:
## el texto que tendra nuestra etiqeuta -> text='Sistema de Facturacion'
## el color que tendrán las letras -> fg='azure4'
## la fuente -> font=('Dosis',58)
## el fondo ->  bg='burlywood'
## y la altura de esta etiqueta - >  width=27
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='azure4',
                        font=('Dosis',58), bg='burlywood', width=27)

## entonces mandamos a llamar a la etiqueta y le aplicamos una cudricula
etiqueta_titulo.grid(row=0, column=0)
##############################################################################
## VAMOS A EMPEZAR CON LA CONSTRUCIÓN DE LOS DIFERENTES PANELES
##############################################################################

##############################################################################
## 1ERO EL PANEL IZQUIERDO
##############################################################################

## 1ero Construimos el panel izquierdo
## con ayuda del metodo "Frame", le decimos que estara dentro de "aplicación"
panel_izquierdo = Frame(aplicacion, bd=1, relief = FLAT)
panel_izquierdo.pack(side = LEFT) ## la arrojamos del lado izquierdo con el metodo ".pack(side)" y le ponemos "LEFT"

## panel de costos
## este tiene que ir dentro del panel que creamos arriba
## rntoces con ayuda del metodo "Frame", le pasamos a "panel_izquierdo"
panel_costos = Frame(panel_izquierdo, bd=1, relief = FLAT, bg='azure4', padx=50)
panel_costos.pack(side = BOTTOM)
## y lo arrojamos a la parte de abajo del panel izquierdo, con ayuda de ".pack(side = BOTTOM)"

##panel comidas:
## este lo queremos dentro del panel izquierdo tambien
##aqui si le vamos a dar formato, por medio del metodod "LabelFrame" es como una etiqueta que ela mismo tiempo es un panel
##que esta dentro del panel_izquierdo
panel_comidas = LabelFrame(panel_izquierdo, text = 'Comida', font=('Dosis', 19, 'bold'),
                           bd = 1, relief=FLAT, fg='azure4') ## decimos que esta etiqueta va a tener el texto que diga "comida"
##que la fuente va a ser tipo "Dosis" y de tamaño "19" y en negritas

panel_comidas.pack(side = LEFT)## lo vamos a arrojar del lado izquierdo de nuestro Frame "panel_izquierdo"

##panel bedidas:
## aqui podemos ver exactamente lo mismo que con el panel de comidas, solo que aqui son bebidas, pero bascimente tiene
#el mismo formato
panel_bebidas = LabelFrame(panel_izquierdo, text = 'Bedidas', font=('Dosis', 19, 'bold'),
                           bd = 1, relief=FLAT, fg='azure4')
## lo que vamos a ver aquí es, que antes ya habiasmoa arrojado al frame de comida al lado "LEFT", pero este de bebidas,
## va a quedar a continuación del de comida
panel_bebidas.pack(side = LEFT)

##panel postres
panel_postres= LabelFrame(panel_izquierdo, text = 'Postres', font=('Dosis', 19, 'bold'),
                           bd = 1, relief=FLAT, fg='azure4')

panel_postres.pack(side = LEFT) ## y este queda a continuación del de bedidas

##############################################################################
## 2do EL PANEL DERECHO
##############################################################################

##Panel derecha:
#Contruimos el lado derecho, entonces decimos que lo queremos dentro "apliacion"
panel_derecha = Frame(aplicacion, bd=1, relief = FLAT)
panel_derecha.pack(side = RIGHT) ## y arrojamos el frame principal al lado derecho

##Panel Calculadora:
## le pasamos el panel_derecho a nuestro panel de "calculadora"
## decimos que queremos que tenga un color "bullywood"
panel_calculadora = Frame(panel_derecha, bd =1, relief = FLAT, bg = 'burlywood')
panel_calculadora.pack()## y lo arrojamos


##Panel Calculadora:
## le pasamos el panel_derecho a nuestro panel de "recivo"
## decimos que queremos que tenga un color "bullywood"
panel_recivo= Frame(panel_derecha, bd =1, relief = FLAT, bg = 'burlywood')
panel_recivo.pack()


##Panel Calculadora:
## le pasamos el panel_derecho a nuestro panel de "botones"
## decimos que queremos que tenga un color "bullywood"
panel_botones = Frame(panel_derecha, bd =1, relief = FLAT, bg = 'burlywood')
panel_botones.pack()

## listas de prodcutos
lista_comidas = ['Lasagna','Tacos de Pastor','Sushi','Hamburguesa BBQ','Dumplings','Pizza Margarita','Alitas','Paella']
lista_bebidas = ['Malteada de chocolate','Frappé de café','Agua de Horchata','Limonada mineral','Chocolate Caliente','Smoothie','Piña Colada','Margarita']
lista_postres = ['Cheesecake de fresa','Brownie con helado','Flan napolitano','Pay de limon','Tiramisu','Churros','Crepas','Mil hojas']

###################################################################################
## aqui estamos creando el contador de todas comidas y ademas los botones para poder ir selecionando
##cada una de las comidas, es decir los "Checkbutton"
variables_comida = [] ## creamos una lista vacia para poder dar una posición a esa comida en especifico
cuadros_comida = []## lista de las cajitas de texto que vamos a ir poniendo por comida(pueden estar habilitadas o no, segun haya sido selecionada la comida)
texto_comida =[]## este sera la lista que nos permita conectar con la cajita de texto y colocar cuanto queremos de alguna comidita en especifico
contador = 0 ## tenemos un contador que nos va a ayudar a recorrer la "lista_comida", mientras que al mismo
# tiempo se asigna una posición a cada una en la fila
for comida in lista_comidas: ## decimos que por cada comida que tenemos en la "lista_comidas":
    ## vamos a agregar esa comida a la lista "variable_comida[]", por eso despues de ".append()" pasamos las comillas
    variables_comida.append('') ## las comillas nos dan un espacio, que despues sera remplazado por "IntVar()"
    variables_comida[contador]= IntVar() ## decimos que por cada posición, vamos a guardar un valor..."IntVar" guarda valores boleanos
    ## nos indica si esa posición a sido selecionada o no, 1 o 0
    ## en la variable "comida" estamos guardando un "CheckButton" que se ira plazmando en el panel_comidas, pasamos como
    ## parametro tambien a la comida de la iteración actual y le damos formato de titulo, ademas de darle una fuente,tamaño y en negritas
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis',19,'bold'),
                         onvalue=1, offvalue=0, variable = variables_comida[contador],
                         command = revisar_check)
    ## aqui hacemos los checkbuttons y les damos formato, ademas tenemos a "variable = variables_comida[contador]" que nos indica si ese
    ## check button esta marcado o no
    comida.grid(row=contador, column=0, sticky=W)## vamos a hacer una cuadricula con el metodo "grid" nos pide como parametro un
    ## row, que sera igual al contador, es decir que row tomara el numero de iteración en el que estemos dentro de la "lista_comidas"

    cuadros_comida.append('')## aquí al principio a esta lista se inicializa con un espacio en blanco (que luego sera rempalzado con un cajita/entry)
    texto_comida.append('')## aquí igual un espacio en blanco con el que se inicializa la lista, pero sera remplazado con un 0
    texto_comida[contador] = StringVar() ## 'StringVar()' es el que nos ayuda a poder guardar el texto(numero) de platillos que queremos
    texto_comida[contador].set('0') ## aquí lo establecemos con un valor inicial de 0
    cuadros_comida[contador] = Entry(panel_comidas, #indicamos en que panel queremos que se visualice esta cajita
                                     font=('Dosis',18,'bold'), ## tamaño de la fuente y estilo
                                     bd=1, ## borde
                                     width = 6, ## Ancho
                                     state=DISABLED,## establecemos a esta cajita e desabilitada
                                     textvariable = texto_comida[contador]) ##esta linea nos ayuda a conectar cuantas queremos de ese platillo
    cuadros_comida[contador].grid(row=contador,column=1)
    contador += 1 ## aqui va ir aumnetando el contador
######################################################################################


###################################################################################
## aqui estamos creando el contador de todas bebidas y ademas los botones para poder ir selecionando
##cada una de las bebidas, es decir los "Checkbutton"
variables_bebida = [] ## entonces creamos una lista vacia para poder dar posición a cada una de las bebidas con sus respectivos "IntVar()"
cuadros_bebida = [] ## lista de las cajitas de texto que vamos a ir poniendo por bebida(pueden estar habilitadas o no, segun haya sido selecionada la bebida)
texto_bebida =[] ## este sera la lista que nos permita conectar con la cajita de texto y colocar cuanto queremos de alguna bebida en especifico
contador = 0 ## nos va a ayudar a recorrer cade bebida de la lista_bebidas
for bebida in lista_bebidas: ## entonces decimos que por bebida en la lista_bebidas
    variables_bebida.append('') ## 1ero vamos a agregar un espacio, por eso los ''
    variables_bebida[contador]= IntVar() ## decimos que por cada posición que se va recorriendo en cada iteraación de la lista_bebidas, contador ira tomando un valor diferente
    # ese valor correponde a la posición o valor, que tiene ese elemento de la lista_bebidas, al cual le vamos ir asignando su respectiva variable "IntVar()" que guarda un valor
    ##1 o 0 segpun haya sido selecionado

    ##"bebida = Checkbutton(panel_bebidas,"-> ahora en la variable "bebida" tenemos un checkbutton, entoneces le pasamos como parametro donde queremos que se localice el checkbutoon en este caso en el panel_bebidas
    ##"text=bebida.title()," -> luego pasamos como parametro, la bebida de la iteración actual, y le damos formato de titulo
    ## "font=('Dosis',19,'bold')" -> aqui le dasmo formato a nuestro texto, decimos cual sera la fuente, tamaño, y que la queremos en negritas
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis',19,'bold'),
                         onvalue=1, offvalue=0, variable = variables_bebida[contador],
                         command = revisar_check)
    ##" onvalue=1," -> quiere decir que si fue selecionada
    ##"offvalue=0" -> quiere decir que aun no ha sido selecionada
    ##"variable = variables_comida[bebida])" -> literalmete es la que nos va ayudar a saber si fue selecionada o no
    ## una vez ya tenemos bien armado nuestro "checkbutton" entonces...
    bebida.grid(row=contador, column=0, sticky=W) ## vamos a ponerlo en un grid, decimos que
    ## row va a ser igual al contador... esto lo que va a provocar es que nuestros butones se coloquen uno abajo del otro como si fuera una listita
    ## en "column" lo dejamos igualado a 0 por que en relidad no queremos hacer ninguna columna con nuestro botones, soli queremos que una bebida vaya abajo de la otra
    ## "sticky=W" -> es solo un fromato que nos ayuda a que se vea bonito
    cuadros_bebida.append('') ## aquí al principio a esta lista se inicializa con un espacio en blanco (que luego sera rempalzado con un cajita/entry)
    texto_bebida.append('') ## aquí igual un espacio en blanco con el que se inicializa la lista, pero sera remplazado con un 0
    texto_bebida[contador] = StringVar() ## 'StringVar()' es el que nos ayuda a poder guardar el texto(numero) de platillos que queremos
    texto_bebida[contador].set('0') ## aquí lo establecemos con un valor inicial de 0
    cuadros_bebida[contador] = Entry(panel_bebidas, #indicamos en que panel queremos que se visualice esta cajita
                                     font=('Dosis', 18, 'bold'), ## tamaño de la fuente y estilo
                                     bd=1, ## tamaño de bordes
                                     width=6, ## altura de la cajita
                                     state=DISABLED, ## ## establecemos a esta cajita e desabilitada
                                     textvariable=texto_bebida[contador]) ##esta linea nos ayuda a conectar cuantas queremos de ese platillo
    cuadros_bebida[contador].grid(row=contador, column=1)
    contador += 1 ## y aquí es cuando le vamos agregando uno al contador, hasta llegar a las 8 posisciones dentro de la lista_bebidas
######################################################################################


###################################################################################
## aqui estamos creando el contador de todas postres y ademas los botones para poder ir selecionando
##cada una de los postres, es decir los "Checkbutton" ...... y es la misma logic que trae comidas y bebidas, solo que aquí lo vamos a hacer con postres
variables_postres= [] ## por eso aqui ya no documente jijijijijijiji
cuadros_postre = []
texto_postre =[]
contador = 0
for postre in lista_postres:
    variables_postres.append('')
    variables_postres[contador]= IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis',19,'bold'),
                         onvalue=1, offvalue=0, variable = variables_postres[contador],
                         command = revisar_check)

    postre.grid(row=contador, column=0, sticky=W)

    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador, column=1)
    contador += 1
######################################################################################

################################Solo comida
##variables
var_costo_comida = StringVar()

##etiqeuta de costos y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text= 'Consto Comida',
                              font=('Dosis',12, 'bold' ),
                              bg = 'azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0,column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable = var_costo_comida)
texto_costo_comida.grid(row=0,column=1, padx = 41)
##############
##### Solo para comida
###########################################################################################


######################################################################################
#############################Solo bebida
##variables
var_costo_bebida = StringVar()

##etiqeuta de costos y campos de entrada
etiqueta_costo_bebida= Label(panel_costos,
                              text= 'Consto Bebida',
                              font=('Dosis',12, 'bold' ),
                              bg = 'azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1,column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable = var_costo_bebida)
texto_costo_bebida.grid(row=1,column=1, padx = 41)
##############
##### Solo para bebida
###########################################################################################


######################################################################################
#############################Solo postre
##variables
var_costo_postre = StringVar()

##etiqeuta de costos y campos de entrada
etiqueta_costo_postre= Label(panel_costos,
                              text= 'Costo Postre',
                              font=('Dosis',12, 'bold' ),
                              bg = 'azure4',
                              fg='white')
etiqueta_costo_postre.grid(row=2,column=0)

texto_costo_postre = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable = var_costo_postre)
texto_costo_postre.grid(row=2,column=1, padx = 41)
##############
##### Solo para postre
###########################################################################################



######################################################################################
#############################Solo subtotal
##variables
var_subtotal = StringVar()

##etiqeuta de costos y campos de entrada
etiqueta_subtotal= Label(panel_costos,
                              text= 'Subtotal',
                              font=('Dosis',12, 'bold' ),
                              bg = 'azure4',
                              fg='white')
etiqueta_subtotal.grid(row=1,column=2)

texto_subtotal= Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable = var_subtotal)
texto_subtotal.grid(row=1,column=3, padx = 41)
##############
##### Solo para subtotal
###########################################################################################

######################################################################################
#############################Solo IMPUESTOS
##variables
var_impuestos = StringVar()

##etiqeuta de costos y campos de entrada
etiqueta_impuestos= Label(panel_costos,
                              text= 'Impuestos',
                              font=('Dosis',12, 'bold' ),
                              bg = 'azure4',
                              fg='white')
etiqueta_impuestos.grid(row=0,column=2)

texto_impuestos= Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable = var_impuestos)
texto_impuestos.grid(row=0,column=3, padx = 41)
##############
##### Solo para impuestos
###########################################################################################




######################################################################################
#############################Solo total
##variables
var_total = StringVar()

##etiqeuta de costos y campos de entrada
etiqueta_total= Label(panel_costos,
                              text= 'Total',
                              font=('Dosis',12, 'bold' ),
                              bg = 'azure4',
                              fg='white')
etiqueta_total.grid(row=2,column=2)

texto_total= Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable = var_total)
texto_total.grid(row=2,column=3, padx = 41)
##############
##### Solo para impuestos
###########################################################################################

###Ahora vamos a contruir nuestros botones
botones = ['Total', 'Recibo', 'Guardar','Resetear']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Helvetica',14,'bold'),
                   fg='white',
                   bg='azure4',## color de fondo
                   bd=1, ## un borde
                   width=9## ancho del boton
                   )

    botones_creados.append(boton)
    boton.grid(row=0,
               column=columnas)
    columnas += 1

botones_creados[0].config(command = total)
botones_creados[1].config(command = recibo)
botones_creados[2].config(command = guardar)
botones_creados[3].config(command = resetear)

## area de recibo
texto_recibo = Text(panel_recivo,
                    font=('Dosis',12,'bold'),
                    bd=1,
                    width=42,
                    height=10)

texto_recibo.grid(row=0,
                  column=0)

###################################################################
#Construyecndo la calculadora
##############################################################
visor_calculadora = Entry(panel_calculadora,
                           font = ('Helvetica',16,'bold'),
                           width=32,
                           bd = 1)

visor_calculadora.grid(row=0,column=0,columnspan=4)


botones_calculadora = ['7','8','9','+','4','5','6','-',
                       '1','2','3','*','Re','Bo','0','/']

botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text = boton.title(),
                   font = ('Dosis',16,'bold'),
                   fg = 'white',
                   bg = 'azure4',
                   bd = 1,
                   width = 8)
    botones_guardados.append(boton)

    boton.grid(row = fila, column = columna )

    if columna == 3: ## cuando el bucle nos de 3 columnas(en la fila actual)
        fila += 1 ## vamos a sumar una fila
        columna +=1 ## vamos a resetear la columna, para poder iniciar en esa nueva fila
    if columna == 4: ## decimos que si el bucle nos devuelve 4 columnas
        columna = 0 ## sera reiniciada 0, y así ya no puede generar mas columnas

###############################################################################
##estos de aquí son los que nos permiten hacer magia con nuestra calculadora
## bueno antes en la linea 512(por el momento) creamos una lista vacia a la que vamos a ir agregando estos botones y la posición
## que ira tomando cada uno
## "botones_guardados[0]" decimos que en la  posisción 0, corresponde al numero 7
## "config()" sirve para modificar características de un widget
##"command"La función que se ejecutará cuando hagas click en la tecla 7
##osea "El boton guardado en la posición 0 cuando sea presionado, ejecutara la función click_boton enviando el valor 7"

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))## es lo mismo para todos los botones
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))## es lo mismo para todos los botones
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*')) ## es lo mismo para todos los botones
botones_guardados[12].config(command=resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))## es lo mismo para todos los botones





## evitar que la pantalla se cierre y espera las acciones de nuestro usuario
aplicacion.mainloop()