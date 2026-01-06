from automator import PosAutomator
from test_base import setup_and_login
from faker import Faker
import random
import unidecode

fake = Faker('es_CO') 
DOCUMENTO = str(random.randint(500000000, 999999999))
NOMBRE = fake.first_name()
NOMBRE_SIN_TILDE = unidecode.unidecode(NOMBRE)
CORREO = f"{NOMBRE_SIN_TILDE.lower().split()[0]}@baco.com"
def test_cliente_fe_identificado_extranjero():
    pos = setup_and_login(f"Orden con registro de nuevo cliente fe indentificado extranjero: {NOMBRE}")

    if pos:
        try:
            exito = True
            
            if exito: exito = pos.crear_orden_para_llevar()
            if pos.agregar_producto_modificador("producto 4", "Segundo producto.png"): 
                if exito: exito = pos.finalizar_orden()
                if exito: exito = pos.pagar_consumidor_identificado_extranjero("5 de propina.png", DOCUMENTO, NOMBRE, CORREO)
                if pos.pagar_con_efectivo("27100", "1254"):
                    if exito:
                        print("\n🎉 ¡ESCENARIO FINALIZADO CON ÉXITO!")
            else:
                print("\n❌ EL ESCENARIO FALLÓ EN ALGÚN PUNTO.")
                
                if not exito:
                    assert False, "El escenario falló en algún punto."
                if exito:
                    assert True, "El escenario de Orden con registro de nuevo cliente fe indentificado extranjero finalizó con éxito."
                
        finally:
            print("\n--- Realizando pasos de finalización ---")
            pos.clic_en_icono_usuario()
            pos.quit()