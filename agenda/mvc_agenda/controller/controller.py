from model.model import Model
from view.view import View
from datetime import date
import time

class Controller:
    """
    *******************************
    * A Controller for a Agenda DB *
    *******************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.main_menu()

    """
    ***********************
    * General controllers *
    ***********************
    """
    def main_menu(self):
        o = '0'
        while o != '5':
            self.view.main_menu()
            self.view.option('5')
            o = input()
            if o == '1':
                self.cps_menu()
            elif o == '2':
                self.lugares_menu()
            elif o == '3':
                self.contactos_menu()
            elif o == '4':
                self.citas_menu()
            elif o == '5':
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f, v in zip(fs, vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals

    """
    ************************
    * Controllers for cps *
    ************************
    """
    def cps_menu(self):
        o = '0'
        while o != '7':
            self.view.cps_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_cp()
            elif o == '2':
                self.read_a_cp()
            elif o == '3':
                self.read_all_cps()
            elif o == '4':
                self.read_cps_city()
            elif o == '5':
                self.update_cp()
            elif o == '6':
                self.delete_cp()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_cp(self):
        self.view.ask('Ciudad: ')
        city = input()
        self.view.ask('Estado: ')
        state = input()
        return [city, state]
    
    def create_cp(self):
        self.view.ask('CP: ')
        i_zip = input()
        city, state = self.ask_cp()
        out = self.model.create_zip(i_zip, city, state)
        if out == True:
            self.view.ok(i_zip, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL CP ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL CP. REVISA.')
        return

    def read_a_cp(self):
        self.view.ask('CP: ')
        i_zip = input()
        zip = self.model.read_a_zip(i_zip)
        if type(zip) == tuple:
            self.view.show_cp_header(' Datps del CP '+i_zip+' ')
            self.view.show_a_cp(zip)
            self.view.show_cp_midder()
            self.view.show_cp_footer()
        else:
            if zip == None:
                self.view.error('EL CP NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CP. REVISA')
        return

    def read_all_cps(self):
        zips = self.model.read_all_zips()
        if type(zips) == list:
            self.view.show_cp_header(' Todos los CPs ')
            for zip in zips:
                self.view.show_a_cp(zip)
            self.view.show_cp_midder()
            self.view.show_cp_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS CPs. REVISA')
        return

    def read_cps_city(self):
        self.view.ask('Ciudad: ')
        city = input()
        zips = self.model.read_zips_city(city)
        if type(zips) == list:
            self.view.show_cp_header(' CPs para la ciudad de '+city+' ')
            for zip in zips:
                self.view.show_a_cp(zip)
            self.view.show_cp_midder()
            self.view.show_cp_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS CPs. REVISA')
        return

    def update_cp(self):
        self.view.ask('CP a modificar: ')
        i_zip = input()
        zip = self.model.read_a_zip(i_zip)
        if type(zip) == tuple:
            self.view.show_cp_header(' Datos del CP '+i_zip+' ')
            self.view.show_a_cp(zip)
            self.view.show_cp_midder()
            self.view.show_cp_footer()
        else:
            if zip == None:
                self.view.error('EL CP NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CP. REVISA')
            return
        self.view.msg('Ingrese los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_cp()
        fields, vals = self.update_lists(['cp_ciudad', 'cp_estado'], whole_vals)
        vals.append(i_zip)
        vals = tuple(vals)
        out = self.model.update_zip(fields, vals)
        if out == True:
            self.view.ok(i_zip, 'actualizado')
        else:
             self.view.error('NO SE PUDO ACTUALIZAR EL CP. REVISA.')
        return

    def delete_cp(self):
        self.view.ask('CP a borrar: ')
        i_zip = input()
        count = self.model.delete_zip(i_zip)
        if count != 0:
            self.view.ok(i_zip, 'borro')
        else:
            if count == 0:
                self.view.error('EL CP NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL CP. REVISA')
        return

    """
    ***************************
    * Controllers for lugares *
    ***************************
    """
    def lugares_menu(self):
        o = '0'
        while o != '6':
            self.view.lugar_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_lugar()
            elif o == '2':
                self.read_a_lugar()
            elif o == '3':
                self.read_all_lugares()
            elif o == '4':
                self.update_lugar()
            elif o == '5':
                self.delete_lugar()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_lugar(self):
        self.view.ask('Calle: ')
        street = input()
        self.view.ask('No exterior: ')
        noext = input()
        self.view.ask('No interior: ')
        noint = input()
        self.view.ask('Colonia: ')
        col = input()
        self.view.ask('CP: ')
        zip = input()
        self.view.ask('Descripcion: ')
        descrip = input()
        return [street, noext, noint, col, zip, descrip]
    
    def create_lugar(self):
        street, noext, noint, col, zip, descrip = self.ask_lugar()
        out = self.model.create_place(street, noext, noint, col, zip, descrip)
        if out == True:
            self.view.ok(street+' '+noext, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL LUGAR ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL LUGAR. REVISA.')
        return

    def read_a_lugar(self):
        self.view.ask('ID lugar: ')
        id_lugar = input()
        lugar = self.model.read_a_place(id_lugar)
        if type(lugar) == tuple:
            self.view.show_lugar_header(' Datos del lugar '+id_lugar+' ')
            self.view.show_a_lugar(lugar)
            self.view.show_lugar_midder()
            self.view.show_lugar_footer()
        else:
            if lugar == None:
                self.view.error('EL LUGAR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL LUGAR. REVISA')
        return

    def read_all_lugares(self):
        lugares = self.model.read_all_places()
        if type(lugares) == list:
            self.view.show_lugar_header(' Todos los lugares ')
            for lugar in lugares:
                self.view.show_a_lugar(lugar)
            self.view.show_lugar_midder()
            self.view.show_lugar_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS LUGARES. REVISA')
        return

    def update_lugar(self):
        self.view.ask('ID de el lugar a modificar: ')
        id_lugar = input()
        lugar = self.model.read_a_place(id_lugar)
        if type(lugar) == tuple:
            self.view.show_lugar_header(' Datos del lugar '+id_lugar+' ')
            self.view.show_a_lugar(lugar)
            self.view.show_lugar_midder()
            self.view.show_lugar_footer()
        else:
            if lugar == None:
                self.view.error('EL LUGAR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL LUGAR. REVISA')
            return
        self.view.msg('Ingrese los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_lugar()
        fields, vals = self.update_lists(['l_calle', 'l_noext', 'l_int', 'l_col', 'l_cp', 'l_descrip'], whole_vals)
        vals.append(id_lugar)
        vals = tuple(vals)
        out = self.model.update_place(fields, vals)
        if out == True:
            self.view.ok(id_lugar, 'actualizado')
        else:
             self.view.error('NO SE PUDO ACTUALIZAR EL LUGAR. REVISA.')
        return

    def delete_lugar(self):
        self.view.ask('ID de el lugar a borrar: ')
        id_lugar = input()
        count = self.model.delete_place(id_lugar)
        if count != 0:
            self.view.ok(id_lugar, 'borro')
        else:
            if count == 0:
                self.view.error('EL LUGAR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL LUGAR. REVISA')
        return

    """
    *****************************
    * Controllers for contactos *
    *****************************
    """
    def contactos_menu(self):
        o = '0'
        while o != '6':
            self.view.contacto_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_contacto()
            elif o == '2':
                self.read_a_contacto()
            elif o == '3':
                self.read_all_contactos()
            elif o == '4':
                self.update_contacto()
            elif o == '5':
                self.delete_contacto()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_contacto(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Apellido paterno: ')
        sname1 = input()
        self.view.ask('Apellido materno ')
        sname2 = input()
        self.view.ask('Email: ')
        email = input()
        self.view.ask('Telefono: ')
        phone = input()
        return [name, sname1, sname2, email, phone]

    def create_contacto(self):
        name, sname1, sname2, email, phone = self.ask_contacto()
        out = self.model.create_contact(name, sname1, sname2, email, phone)
        if out == True:
            self.view.ok(name+' '+sname1+' '+sname2, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL CLIENTE. REVISA.')
        return
    
    def read_a_contacto(self):
        self.view.ask('ID contacto: ')
        id_contacto = input()
        contacto = self.model.read_a_contact(id_contacto)
        if type(contacto) == tuple:
            self.view.show_contacto_header(' Datos del cliente '+id_contacto+' ')
            self.view.show_a_contacto(contacto)
            self.view.show_contacto_midder()
            self.view.show_contacto_footer()
        else:
            if id_contacto == None:
                self.view.error('EL CONTACTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CONTACTO. REVISA')
        return
    
    def read_all_contactos(self):
        contactos = self.model.read_all_contacts()
        if type(contactos) == list:
            self.view.show_contacto_header(' Todos los contactos ')
            for contacto in contactos:
                self.view.show_a_contacto(contacto)
                self.view.show_contacto_midder()
            self.view.show_contacto_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS CONTACTOS. REVISA')
        return
    
    def update_contacto(self):
        self.view.ask('ID de contacto a modificar: ')
        id_contacto = input()
        contacto = self.model.read_a_contact(id_contacto)
        if type(contacto) == tuple:
            self.view.show_contacto_header(' Datos del contacto '+id_contacto+' ')
            self.view.show_a_contacto(contacto)
            self.view.show_contacto_midder()
            self.view.show_contacto_footer()
        else:
            if contacto == None:
                self.view.error('EL CONTACTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CONTACTO. REVISA')
            return
        self.view.msg('Ingrese los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_contacto()
        fields, vals = self.update_lists(['c_nombre', 'c_apaterno', 'c_amaterno', 'c_correo', 'c_telefono'], whole_vals)
        vals.append(id_contacto)
        vals = tuple(vals)
        out = self.model.update_contact(fields, vals)
        if out == True:
            self.view.ok(id_contacto, 'actualizado')
        else:
             self.view.error('NO SE PUDO ACTUALIZAR EL CONTACTO. REVISA.')
        return

    def delete_contacto(self):
        self.view.ask('ID de contacto a borrar: ')
        id_contacto = input()
        count = self.model.delete_contact(id_contacto)
        if count != 0:
            self.view.ok(id_contacto, 'borro')
        else:
            if count == 0:
                self.view.error('EL CONTACTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL CONTACTO. REVISA')
        return

    """
    ***************************
    * Controllers for citas *
    ***************************
    """
    def citas_menu(self):
        o = '0'
        while o != '7':
            self.view.cita_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_cita()
            elif o == '2':
                self.read_a_cita()
            elif o == '3':
                self.read_all_citas()
            elif o == '4':
                self.read_cita_fecha()
            elif o == '5':
                self.update_cita()
            elif o == '6':
                self.delete_cita()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_cita(self):
        self.view.ask('Fecha: ')

    def create_cita(self):
        self.view.ask('ID contacto: ')
        id_contacto = input()
        self.view.ask('ID lugar:')
        id_lugar = input()
        self.view.ask('Asunto: ')
        cita_asunto = input()
        today = date.today()
        cita_date = today.strftime('%y-%m-%d')
        cita_hour = time.strftime("%H:%M:%S")
        out = self.model.create_cita(cita_date, cita_hour, cita_asunto, id_contacto, id_lugar)
        if out == True:
            self.view.ok(cita_date+' '+cita_hour+' '+cita_asunto+' '+id_contacto, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA CITA. REVISA.')
        return

    def read_a_cita(self):
        self.view.ask('ID Cita: ')
        id_cita = input()
        cita = self.model.read_a_cita(id_cita)
        if type(cita) == tuple:
            self.view.show_cita_header(' Datos del cliente '+id_cita+' ')
            self.view.show_a_cita(cita)
            self.view.show_cita_midder()
            self.view.show_cita_footer()
        else:
            if id_cita == None:
                self.view.error('LA CITA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA CITA. REVISA')
        return

    def read_all_citas(self):
        citas = self.model.read_all_citas()
        if type(citas) == list:
            self.view.show_cita_header(' Todos las citas ')
            for cita in citas:
                self.view.show_a_cita(cita)
                self.view.show_cita_midder()
            self.view.show_cita_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS CITAS. REVISA')
        return
    
    def read_cita_fecha(self):
        self.view.ask('Fecha: ')
        date = input()
        citas = self.model.read_citas_fecha(date)
        if type(date) == list:
            self.view.show_cp_header(' Citas para la fecha '+date+' ')
            for cita in citas:
                self.view.show_a_cita(cita)
            self.view.show_cita_midder()
            self.view.show_cita_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS CITAS. REVISA')
        return

    def update_cita(self):
        self.view.ask('ID de la cita a modificar: ')
        id_cita = input()
        cita = self.model.read_a_cita(id_cita)
        if type(cita) == tuple:
            self.view.show_cita_header(' Datos de la orden  '+id_cita+' ')
            self.view.show_a_cita(cita)
            self.view.show_cita_midder()
            self.view.show_cita_footer()
        else:
            if cita == None:
                self.view.error('LA CITA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA CITA. REVISA')
            return
        self.view.msg('Ingrese los valores a modificar (vacio para dejarlo igual): ')
        self.view.ask('ID Contacto')
        id_contacto = input()
        self.view.ask('ID lugar: ')
        id_lugar = input()
        self.view.ask('Fecha (yyyy/mm/dd):')
        cita_date = input()
        self.view.ask('Hora (HH:MM:SS): ')
        cita_hour = input()
        self.view.ask('Asunto: ')
        cita_asunto = input()
        whole_vals = [cita_date, cita_hour, cita_asunto, id_contacto, id_lugar]
        fields, vals = self.update_lists(['cita_fecha', 'cita_hora', 'cita_asunto', 'id_contacto', 'id_contacto'], whole_vals)
        vals.append(id_cita)
        vals = tuple(vals)
        out = self.model.update_cita(fields, vals)
        if out == True:
            self.view.ok(id_cita, 'actualizado')
        else:
             self.view.error('NO SE PUDO ACTUALIZAR EL CLIENTE. REVISA.')
        return

    def delete_cita(self):
        self.view.ask('Id de cita a borrar: ')
        id_cita = input()
        count = self.model.delete_cita(id_cita)
        if count != 0:
            self.view.ok(id_cita, 'borro')
        else:
            if count == 0:
                self.view.error('LA CITA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA CITA5. REVISA')
        return