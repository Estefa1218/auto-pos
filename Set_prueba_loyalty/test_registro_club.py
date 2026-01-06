from automator import PosAutomator
from test_base import setup_and_login
from faker import Faker

fake = Faker('es_CO')
DOCUMENTO_EXISTENTE = "80147567" 

def test_registro_club_existente():
    pos = setup_and_login(f"Venta a cliente Club existente: {DOCUMENTO_EXISTENTE}")
    
    if pos:
        try:
            exito = True
            
            print("\n--- FASE 1: Creando Orden ---")
            if exito: exito = pos.crear_orden_comer_aca()
            if exito: exito = pos.agregar_producto("ruby", "Primer producto.png")
            if exito: exito = pos.usuario_registrado_en_club(DOCUMENTO_EXISTENTE)
            if exito: exito = pos.finalizar_orden()
            if exito: exito = pos.pagar_con_tarjeta("5 de propina.png")
            if pos.pagar_con_efectivo("14000", "648"):
                if exito:
                    print("\n🎉 ¡ESCENARIO COMPLETO FINALIZADO CON ÉXITO!")
                assert True
            else:
                print("\n❌ EL ESCENARIO FALLÓ EN ALGÚN PUNTO.")
                assert False, "El flujo se interrumpió."
                
        finally:
            print("\n--- Realizando pasos de finalización ---")
            pos.clic_en_icono_usuario()
            pos.quit()