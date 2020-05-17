class View:
    """
    **************************
    * A view for a agenda DB *
    **************************
    """
    def start(self):
        print('==============')
        print('= Bienvenido =')
        print('==============')

    def end(self):
        print('================================')
        print('=        Hasta la vista!       =')
        print('================================')

    def main_menu(self):
        print('================================')
        print('=        Menu Principal        =')
        print('================================')
        print('1. CPs')
        print('2. Lugares')
        print('3. Contactos')
        print('4. Citas')
        print('5. Salir')

    def option(self,last):
        print('Selecciona un opcion (1-'+last+'): ', end = '')

    def not_valid_option(self):
        print('Opcion no valida!\nIntenta de nuevo')
    
    def ask(self, output):
        print(output, end = '' )
    
    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))
    
    def error(self, err):
        print(' Error! '.center(len(err)+4,'-'))
        print('-'+err+'-')
        print('-'*(len(err)+4))
    
    """
    ******************
    *  View for CPs *
    ******************
    """
    def cps_menu(self):
        print('*********************')
        print('* -- Submenu CPs -- *')
        print('*********************')
        print('1. Agregar CP')
        print('2. Mostrar CP')
        print('3. Mostrar todos los CPs')
        print('4. Mostrar CPs de una ciudad')
        print('5. Actualizar CP')
        print('6. Borrar CP')
        print('7. Regresar')

    def show_a_cp(self, record):
        print(f'{record[0]:<6}|{record[1]:<35}|{record[2]:<35}')

    def show_cp_header(self, header):
        print(header.center(78,'*'))
        print('CP'.ljust(6)+'|'+'Ciudad'.ljust(35)+'|'+'Estado'.ljust(35))
        print('-'*78)

    def show_cp_midder(self):
        print('-'*78)
    
    def show_cp_footer(self):
        print('*'*78)

    """
    *********************
    *  View for Lugares *
    *********************
    """
    def lugar_menu(self):
        print('*************************')
        print('* -- Submenu Lugares -- *')
        print('*************************')
        print('1. Agregar lugar')
        print('2. Mostrar lugar')
        print('3. Mostrar todos los lugares')
        print('4. Actualizar lugar')
        print('5. Borrar lugar')
        print('6. Regresar')

    def show_a_lugar(self, record):
        print('ID lugar:', record[0])
        print('Calle:', record[1])
        print('No exterior:', record[2])
        print('No interior:', record[3])
        print('Colonia:', record[4])
        print('CP:', record[5])
        print('Descripcion:', record[6])
    
    def show_lugar_header(self, header):
        print(header.center(57,'*'))
        print('-'*57)

    def show_lugar_midder(self):
        print('-'*78)
    
    def show_lugar_footer(self):
        print('*'*78)
    
    """
    **********************
    *  View for Contacto *
    **********************
    """
    def contacto_menu(self):
        print('**************************')
        print('* -- Submenu Contacto -- *')
        print('**************************')
        print('1. Agregar contacto')
        print('2. Mostrar contacto')
        print('3. Mostrar todos los contactos')
        print('4. Actualizar contacto')
        print('5. Borrar contacto')
        print('6. Regresar')
    
    def show_a_contacto(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Apellido paterno:', record[2])
        print('Apellido materno:', record[3])
        print('Correo:', record[4])
        print('Telefono:', record[5])
    
    def show_a_contacto_bref(self, record):
        print('Nombre: '+record[1]+' '+record[2]+' '+record[3])
        print('Telefono: '+record[5])

    def show_contacto_header(self, header):
        print(header.center(61,'*'))
        print('-'*61)

    def show_contacto_midder(self):
        print('-'*61)
    
    def show_contacto_footer(self):
        print('*'*61)

    """
    ******************
    *  View for Cita *
    ******************
    """
    def cita_menu(self):
        print('**********************')
        print('* -- Submenu Cita -- *')
        print('**********************')
        print('1. Agregar cita')
        print('2. Mostrar cita')
        print('3. Mostrar todos las citas')
        print('4. Mostrar cita por fecha')
        print('5. Actualizar cita')
        print('6. Borrar cita')
        print('7. Regresar')
    
    def show_a_cita(self, record):
        print('ID cita:', record[0])
        print('Fecha:', record[1])
        print('Hora:', record[2])
        print('Asunto:', record[3])

    def show_cita_header(self, header):
        print(header.center(57,'*'))
        print('-'*57)

    def show_cita_midder(self):
        print('-'*57)
    
    def show_cita_footer(self):
        print('*'*57)