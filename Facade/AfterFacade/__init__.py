PROVIDER ='sql_server'

CONNSTER=(
    "string for sql server connection"
)

QUERY = """
SELECT DINSTINCT TOP 5 FirstName,LastName
FROM Person.Person
ORDER BY LastName,FIRstName
"""