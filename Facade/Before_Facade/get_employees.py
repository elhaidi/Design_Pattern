import pyodbc

CONSTR= "Driver{SQL Server},SERVER=mfnf5rf.database.windows.net;DATABASE=fkfrzz;UID=sqlfamiff"

    def get_employees():
        connection = pyodbc.connect(CONSTR)

        query ='''
        SELECT DISTINCT TOP 5 FirstNale,LastName
        FROM Person.Person
        ORDER BY LastName
        '''
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            print(rwo.FirstName, row.LastName)
        connection.commit()
        connection.close()
    
get_employees()