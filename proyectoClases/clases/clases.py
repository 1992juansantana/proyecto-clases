class Cajero:
    
    def menu(self):
        repetir_menu = True # bandera/flag
        while repetir_menu:
            print('''
        ==============
            Menu
        ==============
        1. Retirar efectivo.
        2. Cambiar contraseña.
        3. Salir
            ''')

            opcion_elegida = input('Ingrese la operacion a realizar: ')
            if opcion_elegida == '1':
                self.retirar_efectivo()
            elif opcion_elegida == '2':
                self.cambiar_contrasenia()
            elif opcion_elegida == '3':
                print('Hasta luego!')
                repetir_menu = False
            else:
                print('Vuelva a intentar con una opcion valida.')
                
                
    def cambiar_contrasenia(self):
        new_contrasenia = input("Ingrese su nueva contraseña: ")
        new_repcontrasenia = input("repita su nueva contraseña: ")
        print( f"felicidades su contrasenia se cambio con exito!! y es {new_contrasenia}")
        
    
    
    def retirar_efectivo(self):
        monto = input("Ingrese el monto que desea retirar")
        print( f"retiro con exito!! usted ah retirado {monto}")
        


cajero = Cajero()
cajero.menu()
cajero.cambiar_contrasenia()
cajero.retirar_efectivo()
    
    

    
    
    
    
