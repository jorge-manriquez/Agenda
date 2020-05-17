from mysql import connector

class Model:
    """
    *****************************************
    * a data model with MySQL for a store DB*
    *****************************************
    """
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d={}
        with open(self.config_db_file ) as f_r:
            for line in f_r: 
                (key, val) = line.strip().split(':')
                d[key] = val
        return d
        
    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    """
    **************
    * CP methods *
    **************
    """
    def create_zip(self, CP, ciudad, estado):
        try:
            sql = 'INSERT INTO cp (`CP`, `cp_ciudad`, `cp_estado`) VALUES (%s, %s, %s)'
            vals = (CP, ciudad, estado)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_zip(self, CP):
        try:
            sql = 'SELECT * FROM cp WHERE CP = %s'
            vals = (CP,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_zips(self):
        try:
            sql = 'SELECT * FROM cp'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_zips_city(self, ciudad):
        try:
            sql = 'SELECT * FROM cp where cp_ciudad = %s'
            vals = (ciudad,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_zip(self, fields, vals):
        try:
            sql = 'UPDATE cp SET '+','.join(fields)+'WHERE CP = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_zip(self, CP):
        try:
            sql = 'DELETE FROM cp WHERE CP = %s'
            vals = (CP,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount()
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ****************
    * lugar methods*
    ****************
    """
    
    def create_place(self, calle, noext, noint, col, cp, descrip):
        try:
            sql = 'INSERT INTO lugar (`l_calle`, `l_noext`, `l_noint`, `l_col`, `l_cp`, `l_descrip`) VALUES (%s, %s, %s, %s, %s, %s)'
            vals = (calle, noext, noint, col, cp, descrip)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_place(self, id_lugar):
        try:
            sql = 'SELECT * FROM lugar WHERE id_lugar = %s'
            vals = (id_lugar,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_places(self):
        try:
            sql = 'SELECT * FROM lugar'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_place(self, fields, vals):
        try:
            sql = 'UPDATE lugar SET '+','.join(fields)+' WHERE id_lugar = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def delete_place(self, id_lugar):
        try:
            sql = 'DELETE FROM lugar WHERE id_lugar = %s'
            vals = (id_lugar,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ******************
    *contacto methods*
    ******************
    """
    def create_contact(self, nombre, apaterno, amaterno, correo, telefono):
        try:
            sql = 'INSERT INTO contactos (`c_nombre`, `c_apaterno`, `c_amaterno`, `c_correo`,`c_telefono`) VALUES (%s, %s, %s, %s, %s)'
            vals = (nombre, apaterno, amaterno, correo, telefono)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_contact(self, id_contacto):
        try:
            sql = 'SELECT * FROM contactos WHERE id_contacto = %s'
            vals = (id_contacto,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_contacts(self):
        try:
            sql = 'SELECT * FROM contactos'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_contact(self, fields, vals):
        try:
            sql = 'UPDATE contactos SET '+','.join(fields)+' WHERE id_contacto = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_contact(self, id_contacto):
        try:
            sql = 'DELETE FROM contactos WHERE id_contacto = %s'
            vals = (id_contacto,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ****************
    * citas methods*
    ****************
    """
    def create_cita(self, fecha, hora, asunto, id_contacto, id_lugar):
        try:
            sql = 'INSERT INTO cita (`cita_fecha`,`cita_hora`,`cita_asunto`,`id_contacto`, `id_lugar`) VALUES (%s, %s, %s, %s, %s)'
            vals = (fecha, hora, asunto, id_contacto, id_lugar)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def read_a_cita(self, id_cita):
        try:
            sql = 'SELECT * FROM cita WHERE id_cita = %s'
            vals = (id_cita,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            print(err)
            return err

    def read_citas_fecha(self, fecha):
        try:
            sql = 'SELECT * FROM cita WHERE fecha = %s'
            vals = (fecha,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_all_citas(self):
        try:
            sql = 'SELECT * FROM cita'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_cita(self, fields, vals):
        try:
            sql = 'UPDATE cita SET '+','.join(fields)+' WHERE id_cita = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def delete_cita(self, id_cita):
        try:
            sql = 'DELETE FROM cita WHERE id_cita = %s'
            vals = (id_cita,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err