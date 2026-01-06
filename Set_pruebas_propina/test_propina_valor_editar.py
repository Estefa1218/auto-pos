# test_cliente_nit_identificado_extranjero.py

from automator import PosAutomator
from test_base import setup_and_login, generar_nit_valido
from faker import Faker
import unidecode
import time

# --- DATOS DE PRUEBA ---
fake = Faker('es_CO')
NIT_NUMERO, DV = generar_nit_valido()
RAZON_SOCIAL = fake.company()
CORREO = fake.company_email()
PIN = "220725"
NUEVA_PROPINA = "1000"
DESCUENTO_INICIAL = "30 de descuento.png" 
DESCUENTO_FINAL = "20 de descuento.png"

# --- EJECUCIÓN DEL ESCENARIO ---
def test_cliente_nit_identificado_extranjero():
    pos = setup_and_login(f"Edición completa con NIT para {RAZON_SOCIAL}")

    if pos:
        try:
            exito = True
            
            # --- FASE 1: Crear y pagar una orden inicial ---
            print("\n--- FASE 1: Creando y pagando orden inicial ---")
            if exito: exito = pos.crear_orden_para_llevar()
            if exito: exito = pos.agregar_producto("ruby", "Primer producto.png")
            if exito: exito = pos.finalizar_orden()
            if exito: exito = pos.pagar_con_descuento_y_tarjeta("5 de propina.png", DESCUENTO_INICIAL)
            
            # --- FASE 2: Editar la orden que acabamos de pagar ---
            if exito:
                time.sleep(3)
                print("\n--- FASE 2: Editando la orden pagada ---")
                if exito: exito = pos.iniciar_edicion_y_reautenticar(PIN)
                if exito: exito = pos.editar_orden_completa(NUEVA_PROPINA, NIT_NUMERO, DV, RAZON_SOCIAL, CORREO, DESCUENTO_FINAL)
            
            if exito:
                print("\n🎉 ¡ESCENARIO DE EDICIÓN FINALIZADO CON ÉXITO!")
                assert True
            else:
                print("\n❌ EL ESCENARIO FALLÓ EN ALGÚN PUNTO.")
                assert False

        finally:
            pos.quit()
    else:
        assert False, "El setup y login inicial fallaron."