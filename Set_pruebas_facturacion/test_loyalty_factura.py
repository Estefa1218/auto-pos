
from automator import PosAutomator
from test_base import setup_and_login
from faker import Faker
import random
import unidecode

fake = Faker('es_CO') 
DOCUMENTO = str(random.randint(100000000, 999999999))
NOMBRE = fake.first_name()
NOMBRE_SIN_TILDE = unidecode.unidecode(NOMBRE)
APELLIDO = fake.last_name()
APELLIDO_SIN_TILDE = unidecode.unidecode(APELLIDO)
CORREO = f"{NOMBRE_SIN_TILDE.lower().split()[0]}.{APELLIDO_SIN_TILDE.lower().split()[0]}@baco.com"
TELEFONO = f"310{fake.random_number(digits=7, fix_len=True)}"#aqui el cambio de telefono
def test_nuevo_cliente_club_bacanes():
    pos = setup_and_login(f"Orden con registro de nuevo cliente club bacanes: {NOMBRE}")
    if pos:
        try:
            exito = True
            
            if exito: exito = pos.crear_orden_comer_aca()
            if exito: exito = pos.agregar_producto("ruby", "Primer producto.png")
            if exito: exito = pos.registrar_cliente_en_orden(DOCUMENTO, NOMBRE, APELLIDO, CORREO, TELEFONO)
            if exito: exito = pos.finalizar_orden()
            if exito: exito = pos.pagar_con_tarjeta_club_bacanes("5 de propina.png")
            if pos.pagar_con_efectivo("14000", "648"):
                if exito:
                    print("\n🎉 ¡ESCENARIO COMPLETO FINALIZADO CON ÉXITO!")
            else:
                print("\n❌ EL ESCENARIO FALLÓ EN ALGÚN PUNTO.")
                
                if not exito:
                    assert False, "El escenario falló en algún punto."
                if exito:
                    assert True, "El escenario de Orden con registro de nuevo cliente club bacanes finalizó con éxito."
                
        finally:
            print("\n--- Realizando pasos de finalización ---")
            pos.clic_en_icono_usuario()
            pos.quit()
