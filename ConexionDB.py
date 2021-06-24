import sqlite3

#BASE DE DATOS LIBROS
class ConnectionDB:

    def DBLibros(self):
        conexion = self.abrir()
        try:
            conexion.execute("""create table libros (
                              titulo text,
                              autor text,
                              edicion text,
                              impresion text,
                              editorial text,
                              paginas integer,
                              traduccion text,
                              condicion text
                            )""")
            print("se creo la tabla libros")                        
        except sqlite3.OperationalError: 
            print("La tabla libros ya existe") 
    
    def abrir(self):
        conexion = sqlite3.connect("./BaseDeDatos.db")
        return conexion 


    def alta_libros(self, datos):
        cone = self.abrir() 
        cursor = cone.cursor() 
        sql = "insert into libros(titulo, autor, edicion, impresion, editorial, paginas, traduccion, condicion) values (?,?,?,?,?,?,?,?)" 
        cursor.execute(sql, datos) 
        cone.commit() 
        cone.close() 

    def modificar_datos_libros(self,datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "update libros set autor=?, edicion=?, impresion =?, editorial=?, paginas=?, traduccion=?,condicion=? where titulo=?"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close()

    def mostrar_titulos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select titulo from libros"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def mostrar_libros_disponibles(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select titulo from libros where condicion='Disponible' "
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()


    def consulta_combotitulo(self, datos):
        try:
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "select autor, edicion, impresion, editorial, paginas, traduccion, condicion from libros where titulo=?"
            cursor.execute(sql, datos)
            return cursor.fetchall() 
        finally: 
            cone.close()

    def eliminar_datosLibros(self,datos):
        try:
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "delete from libros where titulo=?"
            cursor.execute(sql, datos)
            cone.commit()
        finally: 
            cone.close()
     
    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select titulo, autor, edicion, impresion, editorial, paginas, traduccion, condicion from libros"
            cursor.execute(sql)
            return cursor.fetchall()
            
        finally:
            cone.close()

    def recuperar_retrasos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select titulo from libros where condicion='Retraso'"
            cursor.execute(sql)
            return cursor.fetchall()
            
        finally:
            cone.close()


    
#BASE DE DATOS PRESTAMOS
class ConnectionDB2:

    def DBPrestamos(self):
        conexion = self.abrir()
        try:
            conexion.execute("""create table prestamos (
                              nombre text,
                              apellido text,
                              telefono integer,
                              mail text,
                              inicio text,
                              fin text,
                              libro text
                            )""")
            print("se creo la tabla prestamos")                        
        except sqlite3.OperationalError: 
            print("La tabla prestamos ya existe") 
    
    
    def abrir(self):
        conexion = sqlite3.connect("./BaseDeDatos2.db")
        return conexion 

    def alta_prestamos(self, datos):
        cone = self.abrir() 
        cursor = cone.cursor() 
        sql = "insert into prestamos(nombre, apellido, telefono, mail, inicio, fin, libro) values (?,?,?,?,?,?,?)" 
        cursor.execute(sql, datos) 
        cone.commit() 
        cone.close() 

    def mostrar_libros(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select libro from prestamos"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def consulta_combolibro(self, datos):
        try:
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "select nombre, apellido, telefono, mail, inicio, fin from prestamos where libro=?"
            cursor.execute(sql, datos)
            return cursor.fetchall() 
        finally: 
            cone.close()

    def eliminar_datosPrestamos(self,datos):
        try:
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "delete from prestamos where libro=?"
            cursor.execute(sql, datos)
            cone.commit()
        finally: 
            cone.close()

    def recuperar_deudores(self,titulos):
        try:
            lista = []
            for titulo in titulos:
                cone = self.abrir()
                cursor = cone.cursor()
                sql = "select nombre, apellido, telefono, mail, inicio, fin from prestamos where libro=?"
                cursor.execute(sql, titulo)
                fila = cursor.fetchall() 
                lista.append(fila)
            return lista
        finally: 
            cone.close()

