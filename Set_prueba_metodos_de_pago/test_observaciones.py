from automator import PosAutomator
from test_base import setup_and_login

observaciones = "Cliente estaba feliz"

def test_orden_para_comer_aca():
    pos = setup_and_login("Orden para comer aca")
    if pos:
        try:
            exito = True
            
            if exito: exito = pos.crear_orden_comer_aca()
            if pos.agregar_producto("ruby", "Primer producto.png"):
                if exito: exito = pos.finalizar_orden()
            if pos.pagar_con_tarjeta("5 de propina.png"):
                if pos.pagar_con_observacion("200000", "648", observaciones= "Cliente feliz"):
                    if exito:
                        print("\n🎉 ¡ESCENARIO FINALIZADO CON ÉXITO!")
            else:
                print("\n❌ EL ESCENARIO FALLÓ EN ALGÚN PUNTO.")
                
            if not exito:
                assert False, "El escenario falló en algún punto."
            if exito:
                assert True, "El escenario de Orden para comer aca finalizó con éxito."
                
        finally:
            print("\n--- Realizando pasos de finalización ---")
            pos.clic_en_icono_usuario()
            pos.quit()