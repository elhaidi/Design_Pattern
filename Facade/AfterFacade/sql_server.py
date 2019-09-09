import pyodbc
from . import CONNSTER,QUERY
from abs_facade import AbsFacade

class GetEmployee(AbsFacade):
    def get_employees(self):
        connection = pyodbc.connect(CONNSTER)
        cursor = connection.cursor()
        cursor.execute(QUERY)
        for row in cursor:
            print(row.FirstName,row.LastName)
        
        connection.commit()
        connection.close()