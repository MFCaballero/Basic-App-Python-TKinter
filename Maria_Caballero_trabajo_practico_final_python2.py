import tkinter as tk
from tkinter import ttk, font
from tkinter import messagebox as mb
from tkinter import scrolledtext
import ConexionDB 
import os
from PIL import ImageTk,Image

class Biblioteca:
    def __init__(self):
        self.conexion = ConexionDB.ConnectionDB() 
        self.conexion.DBLibros()
        self.conexion2 = ConexionDB.ConnectionDB2()
        self.conexion2.DBPrestamos()
        self.root = tk.Tk()
        self.root.configure(bg = '#FFB43A')
        self.fondo = ImageTk.PhotoImage(Image.open('./biblioteca.png'))
        self.fondo_label = tk.Label(image = self.fondo)
        self.fondo_label.grid(row = 0 , column = 0)
        self.root.title("Gestion Biblioteca")
        self.root.geometry('600x400')
        self.root.resizable(0, 0)
        self.agregarMenu()
        tupla = self.conexion.mostrar_titulos()
        self.listaLibros = []
        for fila in tupla:
            self.listaLibros.append(fila[0])
        self.root.mainloop() 

 #FUNCIONES ESTRUCTURALES DEL FRONT 

    def agregarMenu(self):
        my_menu= tk.Menu(self.root) 
        self.root.config(menu=my_menu)
        menu_libros = tk.Menu(my_menu, tearoff=0) 
        my_menu.add_cascade(label = 'Libros', menu = menu_libros)
        menu_libros.add_command(label="Alta Libros", command = self.alta_libros) 
        menu_libros.add_command(label="Modificacion Libros", command = self.modific_libros)
        menu_libros.add_command(label="Consulta y Baja", command = self.baja_libros)
        menu_libros.add_command(label="Listado de Libros", command = self.listado)
        menu_prestamos = tk.Menu(my_menu, tearoff=0)  
        my_menu.add_cascade(label = 'Prestamos', menu = menu_prestamos)
        menu_prestamos.add_command(label="Registro Prestamos", command = self.registros)
        menu_prestamos.add_command(label="Consulta y Baja", command = self.baja_registros)
        menu_prestamos.add_command(label="Listado a Reclamar", command = self.reclamos)

    def crear_notebook(self):
        self.fondo_label.grid_forget()
        self.cuaderno = ttk.Notebook(self.root) 
        self.cuaderno.place(x=25, y=5 , width = 550, height = 390) 

    def eliminar_notebook(self):
        self.cuaderno.destroy()
         
    def alta_libros(self):
        try:
            self.eliminar_notebook()
        except AttributeError:
            self.crear_notebook()
            self.carga_libros()    
        else:
            self.crear_notebook()
            self.carga_libros() 
        
    def modific_libros(self):
        try:
            self.eliminar_notebook()
        except AttributeError:
            self.crear_notebook()
            self.modificacion_libros()    
        else:
            self.crear_notebook()
            self.modificacion_libros()
            
    def baja_libros(self):
        try:
            self.eliminar_notebook()
        except AttributeError:
            self.crear_notebook()
            self.consulta_por_nombre()     
        else:
            self.crear_notebook()
            self.consulta_por_nombre() 
              
    def listado(self):
        try:
            self.eliminar_notebook()
        except AttributeError:
            self.crear_notebook()
            self.listado_completo()     
        else:
            self.crear_notebook()
            self.listado_completo() 
       
    def registros(self):
        try:
            self.eliminar_notebook()
        except AttributeError:
            self.crear_notebook()
            self.carga_registros()    
        else:
            self.crear_notebook()
            self.carga_registros()
    
    def baja_registros(self):  
        try:
            self.eliminar_notebook()
        except AttributeError:
            self.crear_notebook()
            self.consulta_prestamos()     
        else:
            self.crear_notebook()
            self.consulta_prestamos()      

    def reclamos(self):
        try:
            self.eliminar_notebook()
        except AttributeError:
            self.crear_notebook()
            self.listado_reclamos()    
        else:
            self.crear_notebook()
            self.listado_reclamos() 
        
        

        
 #FUNCIONES DE CONEXION CON LA BASE DE DATOS    

    #PARTE LIBROS
    def agregar_libros(self):
        try:
            datos = (self.titulocarga.get(), self.autorcarga.get(), self.edicioncarga.get(), self.impresioncarga.get(),
                        self.editorialcarga.get(), self.paginascarga.get(), self.traduccioncarga.get(), self.condicioncarga.get()) 
            self.conexion.alta_libros(datos) 
            mb.showinfo("Información", "Los datos fueron cargados") 
            self.titulocarga.set("") 
            self.autorcarga.set("") 
            self.edicioncarga.set("")
            self.impresioncarga.set("")
            self.editorialcarga.set("")
            self.paginascarga.set("")
            self.traduccioncarga.set("")
            self.condicioncarga.set("")
        except tk.TclError:
            mb.showerror("Error", "No ingreso un numero en el campo numero de paginas. Por Favor ingrese un numero entero")
            

    def modificar_libros(self):
        try:
            datos = (self.autorcarga2.get(), self.edicioncarga2.get(), self.impresioncarga2.get(),
                        self.editorialcarga2.get(), self.paginascarga2.get(), self.traduccioncarga2.get(),
                        self.condicioncarga2.get(), self.combotitulo.get()) 
            self.conexion.modificar_datos_libros(datos)
            mb.showinfo("Información", "Los datos fueron modificados")  
            self.autorcarga2.set("")
            self.edicioncarga2.set("")
            self.impresioncarga2.set("")
            self.editorialcarga2.set("")
            self.paginascarga2.set("")
            self.traduccioncarga2.set("")
            self.condicioncarga2.set("")
            self.combotitulo.set("")
        except tk.TclError:
            mb.showerror("Error", "No ingreso un numero en el campo numero de paginas. Por Favor ingrese un numero entero")

    def titulocombo_selected(self,event):
        datos = (self.combotitulo.get(),)   
        respuesta = self.conexion.consulta_combotitulo(datos)
        if len(respuesta)>0:
            self.autorcarga2.set(respuesta[0][0])
            self.edicioncarga2.set(respuesta[0][1])
            self.impresioncarga2.set(respuesta[0][2])
            self.editorialcarga2.set(respuesta[0][3])
            self.paginascarga2.set(respuesta[0][4])
            self.traduccioncarga2.set(respuesta[0][5])
            self.condicioncarga2.set(respuesta[0][6])
        else:
            self.autorcarga2.set("")
            self.edicioncarga2.set("")
            self.impresioncarga2.set("")
            self.editorialcarga2.set("")
            self.paginascarga2.set("")
            self.traduccioncarga2.set("")
            self.condicioncarga2.set("")

    def eliminar_libros(self):
        datos = (self.combotitulo.get(),)
        self.conexion.eliminar_datosLibros(datos)
        mb.showinfo("Información", "Los datos fueron eliminados")  
        self.autorcarga2.set("")
        self.edicioncarga2.set("")
        self.impresioncarga2.set("")
        self.editorialcarga2.set("")
        self.paginascarga2.set("")
        self.traduccioncarga2.set("")
        self.condicioncarga2.set("")
        self.combotitulo.set("")
        

    #PARTE PRESTAMOS
    def agregar_prestamo(self):

        inicio = self.combodia.get() + '-' + self.combomes.get() + '-' + self.comboyear.get()
        fin = self.combodia1.get() + '-' + self.combomes1.get() + '-' + self.comboyear1.get()

        try:
            datos = (self.nombrecarga.get(), self.apellidocarga.get(), self.telefonocarga.get(),
                        self.mailcarga.get(), inicio, fin, self.combolibro.get()) 
            self.conexion2.alta_prestamos(datos)
            mb.showinfo("Información", "Los datos fueron cargados") 
            self.nombrecarga.set("") 
            self.apellidocarga.set("") 
            self.telefonocarga.set("")
            self.mailcarga.set("")
            self.combolibro.set("")
            self.combodia.set("")
            self.combodia1.set("")
            self.combomes.set("")
            self.combomes1.set("")
            self.comboyear.set("")
            self.comboyear1.set("")
        except tk.TclError:
            mb.showerror("Error", "No ingreso un numero en el campo telefono. Por Favor ingrese un numero entero")

    def librocombo_selected(self,event):
        datos = (self.combolibro1.get(),)   
        respuesta = self.conexion2.consulta_combolibro(datos)
        if len(respuesta)>0:
            self.nombrecarga2.set(respuesta[0][0])
            self.apellidocarga2.set(respuesta[0][1])
            self.telefonocarga2.set(respuesta[0][2])
            self.mailcarga2.set(respuesta[0][3])
            self.iniciocarga.set(respuesta[0][4])
            self.fincarga.set(respuesta[0][5])
        else:
            self.nombrecarga2.set("")
            self.apellidocarga2.set("")
            self.telefonocarga2.set("")
            self.mailcarga2.set("")
            self.iniciocarga.set("")
            self.fincarga.set("")
        
    def eliminar_prestamo(self):
        datos = (self.combolibro1.get(),) 
        self.conexion2.eliminar_datosPrestamos(datos)
        mb.showinfo("Información", "Los datos fueron eliminados")  
        self.nombrecarga2.set("")
        self.apellidocarga2.set("")
        self.telefonocarga2.set("")
        self.mailcarga2.set("")
        self.iniciocarga.set("")
        self.fincarga.set("")
        self.combolibro1.set("")

        



 #FUNCIONALIDADES PARA LIBROS Y PRESTAMOS
        
    #PARTE LIBROS:
    def carga_libros(self):
        style = ttk.Style() 
        style.configure("TLabelframe.Label", font = 
               ('calibri', 16, 'bold'), 
                foreground = '#FFB43A')
        style.configure("TLabel", font = 
               ('calibri', 12), 
                foreground = 'black')
        fuente = font.Font(family='calibri', size=15, weight='bold')       
        self.pagina1 = ttk.Frame(self.cuaderno) 
        self.cuaderno.add(self.pagina1, text="                                                                CARGA DE DATOS DE UN LIBRO                                                             ") 
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Libro")       
        self.labelframe1.place(x = 15, y = 3 , width = 520, height = 350)
        self.label0 = ttk.Label(self.labelframe1, text = 'Título:')
        self.label0.place(x = 25, y = 10)
        self.titulocarga = tk.StringVar() 
        self.entrytitulo=ttk.Entry(self.labelframe1, textvariable=self.titulocarga)
        self.entrytitulo.place(x = 180 , y = 10, width = 300, height = 25)
        self.label1=ttk.Label(self.labelframe1, text="Autor:") 
        self.label1.place(x = 25 , y = 40)
        self.autorcarga = tk.StringVar()
        self.entryautor=ttk.Entry(self.labelframe1, textvariable=self.autorcarga)
        self.entryautor.place(x = 180 , y = 40, width = 300, height = 25)
        self.label2=ttk.Label(self.labelframe1, text="Edición:")        
        self.label2.place(x = 25, y = 70)
        self.edicioncarga=tk.StringVar() 
        self.entryedicion=ttk.Entry(self.labelframe1, textvariable=self.edicioncarga)
        self.entryedicion.place(x = 180 , y = 70, width = 300, height = 25)
        self.label3=ttk.Label(self.labelframe1, text="Impresión (lugar):")        
        self.label3.place(x = 25, y = 130)
        self.impresioncarga=tk.StringVar() 
        self.entryimpresion=ttk.Entry(self.labelframe1, textvariable=self.impresioncarga)
        self.entryimpresion.place(x = 180 , y = 130, width = 300, height = 25)
        self.label4=ttk.Label(self.labelframe1, text="Editorial:")        
        self.label4.place(x = 25, y = 100)
        self.editorialcarga=tk.StringVar() 
        self.entryeditorial=ttk.Entry(self.labelframe1, textvariable=self.editorialcarga)
        self.entryeditorial.place(x = 180 , y = 100, width = 300, height = 25)
        self.label5=ttk.Label(self.labelframe1, text="Páginas (cantidad):")        
        self.label5.place(x = 25, y = 160)
        self.paginascarga=tk.IntVar() 
        self.entrypaginas=ttk.Entry(self.labelframe1, textvariable=self.paginascarga)
        self.entrypaginas.place(x = 180 , y = 160, width = 300, height = 25)
        self.label5=ttk.Label(self.labelframe1, text="Traducción:")        
        self.label5.place(x = 25, y = 190)
        self.traduccioncarga = tk.StringVar()
        self.radio_1=ttk.Radiobutton(self.labelframe1, text = 'Si', variable = self.traduccioncarga, value='Si')
        self.radio_1.place(x = 115, y = 190)
        self.radio_2=ttk.Radiobutton(self.labelframe1, text = 'No', variable = self.traduccioncarga, value='No')
        self.radio_2.place(x = 155, y = 190)
        self.label6=ttk.Label(self.labelframe1, text="Condición:")        
        self.label6.place(x = 25, y = 220)
        self.condicioncarga = tk.StringVar()
        self.radio_3=ttk.Radiobutton(self.labelframe1, text = 'Disponible', variable = self.condicioncarga, value='Disponible')
        self.radio_3.place(x = 115, y = 220)
        self.radio_4=ttk.Radiobutton(self.labelframe1, text = 'Préstamo en proceso', variable = self.condicioncarga, value='Préstamo en proceso')
        self.radio_4.place(x = 200, y = 220)
        self.radio_5=ttk.Radiobutton(self.labelframe1, text = 'Retraso', variable = self.condicioncarga, value='Retraso')
        self.radio_5.place(x = 342, y = 220)
        self.radio_6=ttk.Radiobutton(self.labelframe1, text = 'En restauración', variable = self.condicioncarga, value='En restauración')
        self.radio_6.place(x = 412, y = 220)
        self.boton1=tk.Button(self.labelframe1, text="Agregar", command= self.agregar_libros, bg = '#FFB43A', fg = 'white', width = 30, relief='flat') 
        self.boton1['font'] = fuente
        self.boton1.place( x = 100, y = 260)
        
        
    def modificacion_libros(self):
        style = ttk.Style() 
        style.configure("TLabelframe.Label", font = 
               ('calibri', 16, 'bold'), 
                foreground = '#FFB43A')
        style.configure("TLabel", font = 
               ('calibri', 12), 
                foreground = 'black')
        fuente = font.Font(family='calibri', size=15, weight='bold') 
        self.pagina2 = ttk.Frame(self.cuaderno) 
        self.cuaderno.add(self.pagina2, text="                                                      MODIFICACION DE DATOS DE UN LIBRO                                                             ") 
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Libro")       
        self.labelframe2.place(x = 15, y = 3 , width = 520, height = 350)
        self.label02 = ttk.Label(self.labelframe2, text = 'Título:')
        self.label02.place(x = 25, y = 10)
        self.combotitulo=ttk.Combobox(self.labelframe2, value = self.listaLibros, state = 'readonly')
        self.combotitulo.place(x = 180 , y = 10, width = 300, height = 25)
        self.label12=ttk.Label(self.labelframe2, text="Autor:") 
        self.label12.place(x = 25 , y = 40)
        self.autorcarga2 = tk.StringVar()
        self.entryautor2=ttk.Entry(self.labelframe2, textvariable=self.autorcarga2)
        self.entryautor2.place(x = 180 , y = 40, width = 300, height = 25)
        self.label22=ttk.Label(self.labelframe2, text="Edición:")        
        self.label22.place(x = 25, y = 70)
        self.edicioncarga2=tk.StringVar() 
        self.entryedicion2=ttk.Entry(self.labelframe2, textvariable=self.edicioncarga2)
        self.entryedicion2.place(x = 180 , y = 70, width = 300, height = 25)
        self.label32=ttk.Label(self.labelframe2, text="Impresión (lugar):")        
        self.label32.place(x = 25, y = 130)
        self.impresioncarga2=tk.StringVar() 
        self.entryimpresion2=ttk.Entry(self.labelframe2, textvariable=self.impresioncarga2)
        self.entryimpresion2.place(x = 180 , y = 130, width = 300, height = 25)
        self.label42=ttk.Label(self.labelframe2, text="Editorial:")        
        self.label42.place(x = 25, y = 100)
        self.editorialcarga2=tk.StringVar()
        self.entryeditorial2=ttk.Entry(self.labelframe2, textvariable=self.editorialcarga2)
        self.entryeditorial2.place(x = 180 , y = 100, width = 300, height = 25)
        self.label52=ttk.Label(self.labelframe2, text="Páginas (cantidad):")        
        self.label52.place(x = 25, y = 160)
        self.paginascarga2=tk.IntVar() 
        self.entrypaginas2=ttk.Entry(self.labelframe2, textvariable=self.paginascarga2)
        self.entrypaginas2.place(x = 180 , y = 160, width = 300, height = 25)
        self.label52=ttk.Label(self.labelframe2, text="Traducción:")        
        self.label52.place(x = 25, y = 190)
        self.traduccioncarga2 = tk.StringVar()
        self.radio_12=ttk.Radiobutton(self.labelframe2, text = 'Si', variable = self.traduccioncarga2, value='Si')
        self.radio_12.place(x = 115, y = 190)
        self.radio_22=ttk.Radiobutton(self.labelframe2, text = 'No', variable = self.traduccioncarga2, value='No')
        self.radio_22.place(x = 155, y = 190)
        self.label62=ttk.Label(self.labelframe2, text="Condición:")        
        self.label62.place(x = 25, y = 220)
        self.condicioncarga2 = tk.StringVar()
        self.radio_32=ttk.Radiobutton(self.labelframe2, text = 'Disponible', variable = self.condicioncarga2, value='Disponible')
        self.radio_32.place(x = 115, y = 220)
        self.radio_42=ttk.Radiobutton(self.labelframe2, text = 'Préstamo en proceso', variable = self.condicioncarga2, value='Préstamo en proceso')
        self.radio_42.place(x = 200, y = 220)
        self.radio_52=ttk.Radiobutton(self.labelframe2, text = 'Retraso', variable = self.condicioncarga2, value='Retraso')
        self.radio_52.place(x = 342, y = 220)
        self.radio_62=ttk.Radiobutton(self.labelframe2, text = 'En restauración', variable = self.condicioncarga2, value='En restauración')
        self.radio_62.place(x = 412, y = 220)
        self.combotitulo.bind("<<ComboboxSelected>>", self.titulocombo_selected)
        self.boton2=tk.Button(self.labelframe2, text="Modificar", command= self.modificar_libros, bg = '#FFB43A', fg = 'white', width = 30, relief='flat') 
        self.boton2['font'] = fuente
        self.boton2.place( x = 100, y = 260)


    def consulta_por_nombre(self):
        style = ttk.Style() 
        style.configure("TLabelframe.Label", font = 
               ('calibri', 16, 'bold'), 
                foreground = '#FFB43A')
        style.configure("TLabel", font = 
               ('calibri', 12), 
                foreground = 'black')
        fuente = font.Font(family='calibri', size=15, weight='bold')       
        self.pagina1 = ttk.Frame(self.cuaderno) 
        self.cuaderno.add(self.pagina1, text="                                             CONSULTA Y ELIMINACION DE DATOS DE UN LIBRO                                                             ") 
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Libro")       
        self.labelframe1.place(x = 15, y = 3 , width = 520, height = 290)
        self.label0 = ttk.Label(self.labelframe1, text = 'Título:')
        self.label0.place(x = 25, y = 10)
        self.combotitulo=ttk.Combobox(self.labelframe1, value = self.listaLibros, state = 'readonly')
        self.combotitulo.place(x = 180 , y = 10, width = 300, height = 25)
        self.label1=ttk.Label(self.labelframe1, text="Autor:") 
        self.label1.place(x = 25 , y = 40)
        self.autorcarga2 = tk.StringVar()
        self.labelautor=ttk.Label(self.labelframe1, textvariable=self.autorcarga2)
        self.labelautor.configure(background = 'white', width = 20, borderwidth = 4, relief = "solid", padding = (1,1))
        self.labelautor.place(x = 180 , y = 40, width = 300)
        self.label2=ttk.Label(self.labelframe1, text="Edición:")        
        self.label2.place(x = 25, y = 70)
        self.edicioncarga2=tk.StringVar() 
        self.labeledicion=ttk.Label(self.labelframe1, textvariable=self.edicioncarga2)
        self.labeledicion.configure(background = 'white', width = 20, borderwidth = 4, relief = "solid", padding = (1,1))
        self.labeledicion.place(x = 180 , y = 70, width = 300)
        self.label3=ttk.Label(self.labelframe1, text="Impresión (lugar):")        
        self.label3.place(x = 25, y = 130)
        self.impresioncarga2=tk.StringVar() 
        self.labelimpresion=ttk.Label(self.labelframe1, textvariable=self.impresioncarga2)
        self.labelimpresion.configure(background = 'white', width = 20, borderwidth = 4, relief = "solid", padding = (1,1))
        self.labelimpresion.place(x = 180 , y = 130, width = 300)
        self.label4=ttk.Label(self.labelframe1, text="Editorial:")        
        self.label4.place(x = 25, y = 100)
        self.editorialcarga2=tk.StringVar() 
        self.labeleditorial=ttk.Label(self.labelframe1, textvariable=self.editorialcarga2)
        self.labeleditorial.configure(background = 'white', width = 20, borderwidth = 4, relief = "solid", padding = (1,1))
        self.labeleditorial.place(x = 180 , y = 100, width = 300)
        self.label5=ttk.Label(self.labelframe1, text="Páginas (cantidad):")        
        self.label5.place(x = 25, y = 160)
        self.paginascarga2=tk.StringVar() 
        self.labelpaginas=ttk.Label(self.labelframe1, textvariable=self.paginascarga2)
        self.labelpaginas.configure(background = 'white', width = 20, borderwidth = 4, relief = "solid", padding = (1,1))
        self.labelpaginas.place(x = 180 , y = 160, width = 300)
        self.label5=ttk.Label(self.labelframe1, text="Traducción:")        
        self.label5.place(x = 25, y = 190)
        self.traduccioncarga2 = tk.StringVar() 
        self.labeltraduccion=ttk.Label(self.labelframe1, textvariable=self.traduccioncarga2)
        self.labeltraduccion.configure(background = 'white', width = 20, borderwidth = 4, relief = "solid", padding = (1,1))
        self.labeltraduccion.place(x = 180 , y = 190, width = 300)
        self.label6=ttk.Label(self.labelframe1, text="Condición:")        
        self.label6.place(x = 25, y = 220)
        self.condicioncarga2 = tk.StringVar()
        self.labelcondicion=ttk.Label(self.labelframe1, textvariable=self.condicioncarga2)
        self.labelcondicion.configure(background = 'white', width = 20, borderwidth = 4, relief = "solid", padding = (1,1))
        self.labelcondicion.place(x = 180 , y = 220, width = 300)
        self.combotitulo.bind("<<ComboboxSelected>>", self.titulocombo_selected)
        self.boton2=tk.Button(self.cuaderno, text="Eliminar", command=self.eliminar_libros, bg = '#FFB43A', fg = 'white', width = 30, relief='flat') 
        self.boton2['font'] = fuente
        self.boton2.place( x = 120, y = 333)
        
        
    def listado_completo(self):
        self.pagina1 = ttk.Frame(self.cuaderno) 
        self.cuaderno.add(self.pagina1, text="                                                               LISTADO COMPLETO DE LIBROS                                                            ") 
        self.tabla = ttk.Treeview(self.cuaderno, selectmode ='browse')
        self.tabla.place(x = 5, y = 28, width=528, height=356)
        self.listadoCompleto = ttk.Scrollbar(self.cuaderno,  
                           orient ="vertical",  
                           command = self.tabla.yview) 
        self.listadoCompleto.pack(side = 'right')
        self.tabla["columns"] = ("1",'2') 
        self.tabla.heading('1', text = 'Libro')
        self.tabla.heading('#0', text = 'N')
        self.tabla.column('#0', width = 138, anchor ='c')
        self.tabla.column('1', width =195, minwidth = 195, anchor ='c')
        self.tabla.heading('2', text = 'Condicion')
        self.tabla.column('2', width = 190, minwidth = 190, anchor ='c')
        tupla = self.conexion.recuperar_todos()
        contador = 0
        for i in range(len(tupla)):
            contador += 1
            text = 'L' + str(contador)
            fila = self.tabla.insert("", 'end',text = text, values = (tupla[i][0],tupla[i][7]))
            self.tabla.insert(fila, 'end', text = 'Autor:', values = (tupla[i][1]))
            self.tabla.insert(fila, 'end', text = 'Edicion:', values = (tupla[i][2]))
            self.tabla.insert(fila, 'end', text = 'Impresion:', values = (tupla[i][3]))
            self.tabla.insert(fila, 'end', text = 'Editorial:', values = (tupla[i][4]))
            self.tabla.insert(fila, 'end', text = 'Paginas:', values = (tupla[i][5]))
            self.tabla.insert(fila, 'end', text = 'Traduccion:', values = (tupla[i][6]))
            
        


       
    #PARTE REGISTROS
    def carga_registros(self):
        style = ttk.Style() 
        style.configure("TLabelframe.Label", font = 
               ('calibri', 16, 'bold'), 
                foreground = '#FFB43A')
        style.configure("TLabel", font = 
               ('calibri', 12), 
                foreground = 'black')
        fuente = font.Font(family='calibri', size=15, weight='bold')       
        self.pagina1 = ttk.Frame(self.cuaderno) 
        self.cuaderno.add(self.pagina1, text="                                                                    REGISTRO DE PRESTAMOS                                                                     ")  
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Préstamo")       
        self.labelframe1.place(x = 15, y = 3 , width = 520, height = 350)
        self.label0 = ttk.Label(self.labelframe1, text = 'Nombre:')
        self.label0.place(x = 25, y = 10)
        self.nombrecarga = tk.StringVar() 
        self.entrynombre=ttk.Entry(self.labelframe1, textvariable=self.nombrecarga)
        self.entrynombre.place(x = 180 , y = 10, width = 300, height = 25)
        self.label1=ttk.Label(self.labelframe1, text="Apellido:") 
        self.label1.place(x = 25 , y = 40)
        self.apellidocarga = tk.StringVar()
        self.entryapellido=ttk.Entry(self.labelframe1, textvariable=self.apellidocarga)
        self.entryapellido.place(x = 180 , y = 40, width = 300, height = 25)
        self.label2=ttk.Label(self.labelframe1, text="Teléfono:")        
        self.label2.place(x = 25, y = 70)
        self.telefonocarga=tk.IntVar() 
        self.entrytelefono=ttk.Entry(self.labelframe1, textvariable=self.telefonocarga)
        self.entrytelefono.place(x = 180 , y = 70, width = 300, height = 25)
        self.label3=ttk.Label(self.labelframe1, text="Mail:")        
        self.label3.place(x = 25, y = 100)
        self.mailcarga=tk.StringVar() 
        self.entrymail=ttk.Entry(self.labelframe1, textvariable=self.mailcarga)
        self.entrymail.place(x = 180 , y = 100, width = 300, height = 25)
        self.label4=ttk.Label(self.labelframe1, text="Inicio Préstamo:")        
        self.label4.place(x = 25, y = 130)
        dia = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        self.combodia=ttk.Combobox(self.labelframe1, value = dia, state = 'readonly')
        self.combodia.place(x = 180 , y = 130, width = 100, height = 25)
        mes = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
        self.combomes=ttk.Combobox(self.labelframe1, value = mes, state = 'readonly')
        self.combomes.place(x = 280 , y = 130, width = 100, height = 25)
        year = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030]
        self.comboyear=ttk.Combobox(self.labelframe1, value = year, state = 'readonly')
        self.comboyear.place(x = 380 , y = 130, width = 100, height = 25)
        self.label5=ttk.Label(self.labelframe1, text="Fin Préstamo:") 
        self.label5.place(x = 25, y = 160)
        self.combodia1=ttk.Combobox(self.labelframe1, value = dia, state = 'readonly')
        self.combodia1.place(x = 180 , y = 160, width = 100, height = 25)
        self.combomes1=ttk.Combobox(self.labelframe1, value = mes, state = 'readonly')
        self.combomes1.place(x = 280 , y = 160, width = 100, height = 25)
        self.comboyear1=ttk.Combobox(self.labelframe1, value = year, state = 'readonly')
        self.comboyear1.place(x = 380 , y = 160, width = 100, height = 25)
        self.label5=ttk.Label(self.labelframe1, text="Libro:")        
        self.label5.place(x = 25, y = 190)
        tupla1 = self.conexion.mostrar_libros_disponibles()
        listaLD = []
        for fila in tupla1:
            listaLD.append(fila[0])
        self.combolibro=ttk.Combobox(self.labelframe1, value = listaLD, state = 'readonly')
        self.combolibro.place(x = 180 , y = 190, width = 300, height = 25) 
        self.boton1=tk.Button(self.labelframe1, text="Registrar", command=self.agregar_prestamo, bg = '#FFB43A', fg = 'white', width = 30, relief='flat') 
        self.boton1['font'] = fuente
        self.boton1.place( x = 100, y = 255)
        

    def consulta_prestamos(self):
        style = ttk.Style() 
        style.configure("TLabelframe.Label", font = 
               ('calibri', 16, 'bold'), 
                foreground = '#FFB43A')
        style.configure("TLabel", font = 
               ('calibri', 12), 
                foreground = 'black')
        fuente = font.Font(family='calibri', size=15, weight='bold') 
        self.pagina2 = ttk.Frame(self.cuaderno) 
        self.cuaderno.add(self.pagina2, text="                                         CONSULTA Y ELIMINACION DE REGISTRO DE PRESTAMOS                                                   ")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Registro")       
        self.labelframe2.place(x = 15, y = 3 , width = 520, height = 350)
        self.label6=ttk.Label(self.labelframe2, text="Libro:") 
        self.label6.place(x = 25 , y = 10)
        tupla2 = self.conexion2.mostrar_libros() 
        listaP = []
        for fila in tupla2:
            listaP.append(fila[0])
        self.combolibro1=ttk.Combobox(self.labelframe2, value = listaP, state = 'readonly')
        self.combolibro1.place(x = 180 , y = 10, width = 300, height = 25)
        self.label7=ttk.Label(self.labelframe2, text="Nombre:") 
        self.label7.place(x = 25 , y = 40)
        self.nombrecarga2 = tk.StringVar()
        self.labelnombre=ttk.Label(self.labelframe2, textvariable=self.nombrecarga2)
        self.labelnombre.configure(background = 'white', width = 20, borderwidth = 4, relief = "solid", padding = (1,1))
        self.labelnombre.place(x = 180 , y = 40, width = 300)
        self.label8=ttk.Label(self.labelframe2, text="Apellido:")        
        self.label8.place(x = 25, y = 70)
        self.apellidocarga2 = tk.StringVar()
        self.labelapellido=ttk.Label(self.labelframe2, textvariable=self.apellidocarga2)
        self.labelapellido.configure(background = 'white', width = 20, borderwidth = 4, relief = "solid", padding = (1,1))
        self.labelapellido.place(x = 180 , y = 70, width = 300)
        self.label9=ttk.Label(self.labelframe2, text="Teléfono:")        
        self.label9.place(x = 25, y = 100)
        self.telefonocarga2 = tk.IntVar()
        self.labeltelefono=ttk.Label(self.labelframe2, textvariable=self.telefonocarga2)
        self.labeltelefono.configure(background = 'white', width = 20, borderwidth = 4, relief = "solid", padding = (1,1))
        self.labeltelefono.place(x = 180 , y = 100, width = 300)
        self.label10=ttk.Label(self.labelframe2, text="Mail:")        
        self.label10.place(x = 25, y = 130) 
        self.mailcarga2 = tk.StringVar()
        self.labelmail=ttk.Label(self.labelframe2, textvariable=self.mailcarga2)
        self.labelmail.configure(background = 'white', width = 20, borderwidth = 4, relief = "solid", padding = (1,1))
        self.labelmail.place(x = 180 , y = 130, width = 300)
        self.label11=ttk.Label(self.labelframe2, text="Inicio Préstamo:") 
        self.label11.place(x = 25, y = 160)
        self.iniciocarga = tk.StringVar()
        self.labelinicio=ttk.Label(self.labelframe2, textvariable=self.iniciocarga)
        self.labelinicio.configure(background = 'white', width = 20, borderwidth = 4, relief = "solid", padding = (1,1))
        self.labelinicio.place(x = 180 , y = 160, width = 300)
        self.label12=ttk.Label(self.labelframe2, text="Fin Préstamo:")        
        self.label12.place(x = 25, y = 190)
        self.fincarga = tk.StringVar()
        self.labelfin=ttk.Label(self.labelframe2, textvariable=self.fincarga)
        self.labelfin.configure(background = 'white', width = 20, borderwidth = 4, relief = "solid", padding = (1,1))
        self.labelfin.place(x = 180 , y = 190, width = 300)
        self.combolibro1.bind("<<ComboboxSelected>>", self.librocombo_selected)
        self.boton3=tk.Button(self.labelframe2, text="Terminar Préstamo", command=self.eliminar_prestamo, bg = '#FFB43A', fg = 'white', width = 30, relief='flat') 
        self.boton3['font'] = fuente
        self.boton3.place( x = 100, y = 255)







    def listado_reclamos(self):
        self.pagina1 = ttk.Frame(self.cuaderno) 
        self.cuaderno.add(self.pagina1, text="                                                LISTADO DE PERSONAS QUE ADEUDAN LIBROS                                                            ")  
        self.tabla = ttk.Treeview(self.cuaderno, selectmode ='browse')
        self.tabla.place(x = 5, y = 28, width=528, height=356)
        self.listadoReclamos = ttk.Scrollbar(self.cuaderno,  
                           orient ="vertical",  
                           command = self.tabla.yview) 
        self.listadoReclamos.pack(side = 'right')
        self.tabla["columns"] = ("1",'2') 
        self.tabla.heading('1', text = 'Libro')
        self.tabla.heading('#0', text = 'N')
        self.tabla.column('#0', width = 138, anchor ='c')
        self.tabla.column('1', width =195, minwidth = 195, anchor ='c')
        self.tabla.heading('2', text = 'Condicion')
        self.tabla.column('2', width = 190, minwidth = 190, anchor ='c')
        tupla = self.conexion.recuperar_retrasos()
        detalle = self.conexion2.recuperar_deudores(tupla)
        contador = 0
        for i in range(len(tupla)):
            contador += 1
            text = 'L' + str(contador)
            fila = self.tabla.insert("", 'end',text = text, values = (tupla[i][0],'Retraso'))
            self.tabla.insert(fila, 'end', text = 'Nombre:', values = (detalle[i][0][0]))
            self.tabla.insert(fila, 'end', text = 'Apellido:', values = (detalle[i][0][1]))
            self.tabla.insert(fila, 'end', text = 'Telefono:', values = (detalle[i][0][2]))
            self.tabla.insert(fila, 'end', text = 'Mail:', values = (detalle[i][0][3]))
            self.tabla.insert(fila, 'end', text = 'Inicio Prestamo:', values = (detalle[i][0][4]))
            self.tabla.insert(fila, 'end', text = 'Fin Prestamo:', values = (detalle[i][0][5]))   
        


os.system("cls")


app = Biblioteca()