import json
import sqlite3

class DataClient:

    def getTasks(self):
        connection = sqlite3.connect("fastapi.db")
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM todo")
        data = cursor.fetchall()
        connection.commit()
        connection.close()
        print(data)
        return data
    
    def getTask(self, task_id):
        connection = sqlite3.connect("fastapi.db")
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM todo WHERE id = {task_id}")
        data = cursor.fetchone()
        connection.commit()
        connection.close()
        return data
    
    def updateTask(self, task_id:int, tasktitle:str, taskcompleted:str):
        connection = sqlite3.connect("fastapi.db")
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(f"UPDATE todo SET title = ?, completed = ? WHERE id = ?",(tasktitle, taskcompleted, task_id))
        connection.commit()
        connection.close()



    def initDB(self):
        connection = sqlite3.connect("fastapi.db")
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS todo (
                              id INTEGER PRIMARY KEY,
                              title VARCHAR(100),
                              completed VARCHAR(100) NOT NULL)""")
        connection.commit()
        connection.close()

    def createtask(self, taskid, tasktitle, taskcompleted):
        connection = sqlite3.connect("fastapi.db")
        cursor = connection.cursor()
        cursor.execute(f"""INSERT INTO todo(id, title, completed)
                    VALUES
                    ({taskid}, '{tasktitle}', '{taskcompleted}');""")
        connection.commit()
        connection.close()

    def deletetask(self, task_id):
        connection = sqlite3.connect("fastapi.db")
        cursor = connection.cursor()
        cursor.execute(f"""DELETE FROM todo WHERE id = {task_id};""")
        connection.commit()
        connection.close()

        
    # def updateTasks(self, tasks):
    #     with open("tasks.json", "w") as file:
    #         file.write(json.dumps(tasks))