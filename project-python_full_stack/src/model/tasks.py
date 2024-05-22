from db.controller import Controller

class Model():
    """Clase que gestiona la lógica del proyecto entre el ususario y la BBDD"""
    def __init__(self):
        """Constructor"""
        self.CLASS_NAME="Model"
        self.controller=Controller()#Instanciamos un objecto de clase Controller() para comunicarnos con BBDD
    
    def __print_rows(self,rows):
        """Método privado.Este método printa las finas recibidas por argumento"""
        frame="*"*100
        print(frame)
        print("Table: TAREA")
        headers="ID_TASK","TASK_NAME","STATUS","CREATED_DATE","UPDATE_DATE"
        print(headers)       
        for row in rows:
            print(row)
        print(frame)

    def list_all(self):
        """Método público.Método que recupera todas la filas de la tabla TAREA y las printa en consola"""
        fun_name="list_all"
        try:
            print("Executing {}/{}".format(self.CLASS_NAME,fun_name))
            rows=self.controller.list_all()#Recuperamos los datos
            self.__print_rows(rows)#Printamos los datos
            print("Executed {}/{}".format(self.CLASS_NAME,fun_name))
           
        except Exception as e:
            raise Exception("ERROR in  {}/{} msg: {}".format(self.CLASS_NAME,fun_name,e))
        
    def show_task(self,id_task):
        """Método público.Método que recupera la fila asociada al código de tarea recibido por arguemnto"""
        fun_name="show_task"
        try:
            print("Executing {}/{}".format(self.CLASS_NAME,fun_name))
            rows=self.controller.execute_stmt(type_stmt="select",id_task=id_task)#Recupera datos
            self.__print_rows(rows)#Printa los datos
            print("Executed {}/{}".format(self.CLASS_NAME,fun_name))
        except Exception as e:
            raise Exception("ERROR in  {}/{} msg: {}".format(self.CLASS_NAME,fun_name,e))
     

    def update_task(self,id_task,status):
        """Método públio.Método que actualiza en la BBDD la tarea asociada al código de tarea reacibido"""
        fun_name="update_task"
        try:
            print("Executing {}/{}".format(self.CLASS_NAME,fun_name))
            stmt=self.controller.execute_stmt(type_stmt="update",id_task=id_task,status=status)#Ejecuta la instrucción en BBDD
            print("Executed {}/{}".format(self.CLASS_NAME,fun_name))
        except Exception as e:
            raise Exception("ERROR in  {}/{} msg: {}".format(self.CLASS_NAME,fun_name,e))

        
    def insert_task(self,task_name):
        """Método público.Método que inserta una nueva tarea en la tabla TAREA"""
        fun_name="insert_task"
        try:
            print("Executing {}/{}".format(self.CLASS_NAME,fun_name))
            stmt=self.controller.execute_stmt(type_stmt="insert",task_name=task_name)#Ejecuta la instrucción en BBDD
            print("Executed {}/{}".format(self.CLASS_NAME,fun_name))
        except Exception as e:
            raise Exception("ERROR in  {}/{} msg: {}".format(self.CLASS_NAME,fun_name,e))

    def delete_task(self,id_task):
        """Método público.Método que borra la tarea asociada al código de tarea redibido por arugmento"""
        fun_name="delete_task"
        try:
            print("Executing {}/{}".format(self.CLASS_NAME,fun_name))
            stmt=self.controller.execute_stmt(type_stmt="delete",id_task=id_task)#Ejecuta la instrucción en BBDD
            print("Executed {}/{}".format(self.CLASS_NAME,fun_name))
        except Exception as e:
            raise Exception("ERROR in  {}/{} msg: {}".format(self.CLASS_NAME,fun_name,e))





if __name__=="__main__":
    print("model")
