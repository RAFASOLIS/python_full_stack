from model.tasks import Model
from db.controller import Controller


class Menu():
    def __init__(self):
        self.CLASS_NAME="View"
        self.model=Model()
        self.TEXT_MENU="""
            MENU:

            0. Crear BBDD (esta opción borrará registros insertados/actualizados desde la creación anterior).
            1. Listar todas las tareas.
            2. Listar una tarea.
            3. Añadir una tarea.
            4. Actualizar una tarea.
            5. Borrar Una tarea.
            6. Salir del menú.
            """

    def start(self):
        fun_name="start"
        try:
            op=-1
            while op != 6:
                print(self.TEXT_MENU)
                op=int(input("Introduzca opción:"))
                if(op==0):
                    self.__op_0_createDB()
                elif(op==1):
                    self.__op_1_list_all_tasks()
                elif(op==2):
                    self.__op_2_list_taks()
                elif(op==3):
                    self.__op_3_insert_task()
                elif(op==4):
                    self.__op_4_update_task()
                elif(op==5):
                    self.__op_5_delete_task()
                elif(op<0  or op>6):
                    print("El número de opción no está incluida en el menú.")
        except Exception as e:
                raise Exception("ERROR in  {}/{} msg: {}".format(self.CLASS_NAME,fun_name,e))


    def __op_0_createDB(self):
        controller=Controller()
        controller.deployDB()

    def __op_1_list_all_tasks(self):
        fun_name="__op_1_list_all_tasks"
        try:
            self.model.list_all()
        except Exception as e:
                raise Exception("ERROR in  {}/{} msg: {}".format(self.CLASS_NAME,fun_name,e))

    def __op_2_list_taks(self):
        fun_name="__op_2_list_taks"
        try:
            id_task=int(input("Introduzca el código de la tarea a mostrar:"))
            self.model.show_task(id_task=id_task)
        except Exception as e:
                raise Exception("ERROR in  {}/{} msg: {}".format(self.CLASS_NAME,fun_name,e))

    def __op_3_insert_task(self):
        fun_name="__op_3_insert_task"
        try:
            task_name=input("Introduzca el nombre de la tarea a insertar:")
            self.model.insert_task(task_name=task_name)
            self.model.list_all()
        except Exception as e:
                raise Exception("ERROR in  {}/{} msg: {}".format(self.CLASS_NAME,fun_name,e))

    def __op_4_update_task(self):
        fun_name="__op_4_update_task"
        try:
            id_task=int(input("Introduzca el código de la tarea a actualizar:"))
            status=input("Introduzca el nuevo estado de la tarea a actualizar:")
            self.model.update_task(id_task=id_task,status=status)
            self.model.list_all()
        except Exception as e:
                raise Exception("ERROR in  {}/{} msg: {}".format(self.CLASS_NAME,fun_name,e))

    def __op_5_delete_task(self):
        fun_name="__op_5_delete_task"
        try:
            id_task=int(input("Introduzca el código de la tarea a borrar:"))
            self.model.delete_task(id_task=id_task)
            self.model.list_all()
        except Exception as e:
                raise Exception("ERROR in  {}/{} msg: {}".format(self.CLASS_NAME,fun_name,e))

if __name__=="__main__":
    print("view")
