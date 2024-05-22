import os
import sqlite3 as sql
       
class Controller():
    """Clase que contiene los métodos para interactuar con la BBDD SQLite Embedida"""
    def __init__(self):
        self.CLASS_NAME="Controller"
        self.db_name="project_full_stak.db"

    def deployDB(self):
        """Método público.Método que crea la bbdd, la tabla tarea y realiza los inserts iniciales"""
        fun_name="deployDB"
        try:
            self.createDB() #Creamos BBDD
            self.createTable() #Creamos tabla TAREA
            self.initialInserts() # Creamos inserts iniciales
            print("Executed {}/{}".format(self.CLASS_NAME,fun_name))
        except Exception as e:
            raise Exception("ERROR in  {}/{} msg: {}".format(self.CLASS_NAME,fun_name,e))

    def createDB(self):
        """Método que crea la BBDD"""
        fun_name="createDB"
        try:
            conn=sql.connect(self.db_name)#Conectamos a la BBDD
            conn.commit()#Efectuamos la confirmación para generarl el fichero "project_full_stack_db"
            conn.close() #Cerramos conexión
            print("Executed {}/{}".format(self.CLASS_NAME,fun_name))
        except Exception as e:
           raise Exception("ERROR in  {}/{} msg: {}".format(self.CLASS_NAME,fun_name,e))


    def createTable(self):
        """Método público.Método que crea la tabla TAREA en la BBDD """
        fun_name="createTable"
        try:
            ddl="""
            CREATE  TABLE TAREA (
            ID_TASK INTEGER PRIMARY KEY AUTOINCREMENT,
            TASK_NAME VARCHAR(100),
            STATUS VARCHAR(50),
            CREATED_DATE DATETIME,
            UPDATE_DATE DATETIME
            );"""
            conn=sql.connect(self.db_name) #Creamos conexión a BBDD
            cursor=conn.cursor() #Creamos un cursos para poder ejecutar sentencias SQL
            cursor.execute("DROP TABLE IF EXISTS TAREA") #Borramos lat abla si existe previamente
            cursor.execute(ddl) #Crea la tabla
            conn.commit() # Confirma las instrucciones
            conn.close() #Cerramos conexión
            print("Executed {}/{}".format(self.CLASS_NAME,fun_name))
        except Exception as e:
           raise Exception("ERROR in  {}/{} msg: {}".format(self.CLASS_NAME,fun_name,e))
        

    def initialInserts(self):
        """Método público.Método que genera los inserts iniciales sobre la tabla TAREA"""
        fun_name="initialInsert"
        try:
            conn=sql.connect(self.db_name)#Creamos conexión a BBDD
            cursor=conn.cursor() #Creamos cursor para poder ejecutar instrucciones SQL sobre la BBDD
            #Lanzamos las diferentes instrucciones SQL
            cursor.execute("DELETE FROM TAREA;")
            cursor.execute("INSERT INTO TAREA (TASK_NAME,STATUS,CREATED_DATE,UPDATE_DATE) VALUES('TAREA1','PENDING',DATETIME('now'),DATETIME('now'));")
            cursor.execute("INSERT INTO TAREA (TASK_NAME,STATUS,CREATED_DATE,UPDATE_DATE) VALUES('TAREA2','PENDING',DATETIME('now'),DATETIME('now'));")
            cursor.execute("INSERT INTO TAREA (TASK_NAME,STATUS,CREATED_DATE,UPDATE_DATE) VALUES('TAREA3','PENDING',DATETIME('now'),DATETIME('now'));")
            cursor.execute("INSERT INTO TAREA (TASK_NAME,STATUS,CREATED_DATE,UPDATE_DATE) VALUES('TAREA4','PENDING',DATETIME('now'),DATETIME('now'));")
            cursor.execute("INSERT INTO TAREA (TASK_NAME,STATUS,CREATED_DATE,UPDATE_DATE) VALUES('TAREA5','PENDING',DATETIME('now'),DATETIME('now'));")
            conn.commit() #Confirmamos las instrucciones
            conn.close() #Cerramos conexión
            print("Executed {}/{}".format(self.CLASS_NAME,fun_name))
        except Exception as e:
           raise Exception("ERROR in  {}/{} msg: {}".format(self.CLASS_NAME,fun_name,e))
        
    def __get_stmt(self,type_stmt,task_name="",status="",id_task=-1):
        """Función privada.Función que recibe el timpo de instrucción SQL a ejecutar y devuelve su sentencia SQL montada"""
        fun_name="get_stmt"
        try:
            stmt_select="SELECT *  FROM TAREA WHERE ID_TASK ={}".format(id_task) 
            stmt_insert="INSERT INTO TAREA (TASK_NAME,STATUS,CREATED_DATE,UPDATE_DATE) VALUES('{}','PENDING',DATETIME('now'),DATETIME('now'));".format(task_name)
            stmt_update="UPDATE TAREA SET STATUS='{}',UPDATE_DATE=DATETIME('now') WHERE ID_TASK ={}".format(status,id_task)    
            stmt_delete="DELETE FROM TAREA WHERE ID_TASK ={}".format(id_task) 
            #Creamos un diccionario para casar tipo de sentencia con su isntrucción SQL generada
            stmt={"select":stmt_select,"insert":stmt_insert,"update":stmt_update, "delete":stmt_delete}
            print("Executed {}/{}".format(self.CLASS_NAME,fun_name))
            return stmt[type_stmt] #rdevolvemos la sentencia SQL a ejecutar
        except Exception as e:
           raise Exception("ERROR in  {}/{} msg: {}".format(self.CLASS_NAME,fun_name,e))

    def list_all(self):
        """Método público.Método que lista todos los registros de la tabla TAREA"""
        fun_name="list_all"
        try:
            conn=sql.connect(self.db_name)#Creamos conexión
            cursor=conn.cursor() # Creamos cursos para ejecutar la instrucción SQL
            query=f"SELECT * FROM TAREA" #Definimos la instrucción SQL
            cursor.execute(query) #Ejecutamos la instrucción SQL
            rows=cursor.fetchall() #Recuperamos los datos desde BBDD
            conn.commit() #Confirmamos la ejecución
            conn.close() #Cerramos conexión
            print("Executed {}/{}".format(self.CLASS_NAME,fun_name))
            return rows
        except Exception as e:
           raise Exception("ERROR in  {}/{} msg: {}".format(self.CLASS_NAME,fun_name,e))


    

    def execute_stmt(self,type_stmt,task_name="",status="",id_task=-1):
        fun_name="execute_stmt"
        try:
            stmt=self.__get_stmt(type_stmt,task_name=task_name,status=status,id_task=id_task)
            conn=sql.connect(self.db_name)
            cursor=conn.cursor()
            cursor.execute(stmt)
            if type_stmt:
                rows=cursor.fetchall()  
            else:
                rows=None
            conn.commit()        
            conn.close()   
    
            print("Executed {}/{}".format(self.CLASS_NAME,fun_name))
            return rows
        except Exception as e:
           raise Exception("ERROR in  {}/{} msg: {}".format(self.CLASS_NAME,fun_name,e))


if __name__=="__main__":
    print("controller")



