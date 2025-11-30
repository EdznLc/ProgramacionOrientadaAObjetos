from conexionBD import *

class Coches:
    @staticmethod
    def insert(marca, color, modelo, velocidad, caballaje, plazas):
        try:
            cursor.execute("insert into coches values (null, %s, %s, %s, %s, %s, %s)", (marca, color, modelo, velocidad, caballaje, plazas))
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM coches")
            operacion = cursor.fetchall()
            return operacion
        except:
            return []
    
    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, id):
        try:
            cursor.execute("UPDATE coches SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s where id=%s", (marca, color, modelo, velocidad, caballaje, plazas, id))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("DELETE FROM coches WHERE id=%s", (id,))
            conexion.commit()
            return True
        except:
            return False
