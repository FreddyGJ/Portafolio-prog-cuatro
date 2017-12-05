import pymysql

db = pymysql.connect("localhost", "root", "root123", "test")
cursor = db.cursor()

# PRUEBA DE NSTALACION DE MARIADB
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print("Verion de MariaDB: %s" % data)

# ELIMINACION/CREACION DE TABLAS
# cursor.execute("DROP TABLE IF EXISTS EMPLEADO")
# sql = """CREATE TABLE EMPLEADO (
#    NOMBRE VARCHAR(20) NOT NULL,
#    APELLIDO VARCHAR(20),
#    EDAD INT,
#    SEXO CHAR(1),
#    SALARIO FLOAT
#    )"""
# cursor.execute(sql)

# INSERTAR DATOS A LA TABLA
# sql = """INSERT INTO EMPLEADO(NOMBRE,APELLIDO,EDAD,SEXO,SALARIO)
#       VALUES('Petra', 'Petrov', 17, 'F', 2000)"""
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()

# LEER DATOS DE LA TABLA EMPLEADO
# e = int(input("EDAD DE PETRA > "))
# salarios = []
# sql = "SELECT * FROM EMPLEADO WHERE EDAD > '%d'" % e

# try:
#     cursor.execute(sql)
#     resultados = cursor.fetchall()
#     for resgistro in resultados:
#         salario = resgistro[4]
#         salarios.append(salario)
# except:
#     print("Error al obtener datos!")
# db.close()
#
# if len(salarios) > 0:
#     print("El salario mas alto de Petra fue de $", + str(max(salarios)))
# else:
#     print("No hay salario de Petra para ese rango de edad")

# ACTUALIZAR DATOS
# sql = "UPDATE EMPLEADO SET EDAD = EDAD + 1 WHERE SEXO = 'F'"
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# db.close()

# BORRAR DATOS
sql = "DELETE FROM EMPLEADO WHERE EDAD < 18"
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()