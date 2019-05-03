import sqlite3


class ServiceUno(object):
    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()

    def Close(self):
        self.cursor.close()
        self.connection.close()

    def CreateDb(self):
        query = """CREATE TABLE service
                    (id INTEGER PRIMARY KEY, Q1 TEXT, Q2 TEXT, Q3 TEXT, Q4 TEXT, Q5 TEXT, Q6 TEXT, Q7 TEXT)"""#Add Questions to Table
        self.cursor.execute(query)
        self.connection.commit()
        #self.cursor.close()

    def AddService(self, Q1, Q2, Q3, Q4, Q5, Q6, Q7): #add questions to table
        self.cursor.execute("""INSERT INTO service
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (None, Q1, Q2, Q3, Q4, Q5, Q6, Q7)) #ADD questions to Table
        self.connection.commit()

    def GetService(self, index = None):
        if index:
            self.cursor.execute("""SELECT * FROM service WHERE id=?""", (index))
        else:
            self.cursor.execute("""SELECT * FROM service
                                    ORDER BY RANDOM()
                                    LIMIT 1""")

            res = self.cursor.fetchone()
            return res
    

if __name__ == "__main__":
    
    ss=ServiceUno("service.db")
    ss.CreateDb()
    ss.AddService("Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7") #Add questions to table Need to get from NewWindow.py
    ss.Close()


