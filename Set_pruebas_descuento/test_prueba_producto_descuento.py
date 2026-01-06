from automator import PosAutomator
from test_base import setup_and_login

PROPINA_IMG = "5 de propina.png"
DESCUENTO_VALOR = "30 de descuento" 
def test_orden_en_salon_con_descuento():
    pos = setup_and_login("Orden en Salón con Descuento")
    if pos:
        try:
            exito = True

            if exito:
                exito = pos.crear_orden_salon()
            if pos.agregar_producto("producto 6", "Prodcuto descuento.png"):
                if exito:
                    exito = pos.finalizar_orden()
                    if exito: exito = pos.pago_con_descuento(PROPINA_IMG, DESCUENTO_VALOR)
                    if pos.pagar_con_efectivo("29750", "0"):
                        if exito:
                            print("\n🎉 ¡ESCENARIO FINALIZADO CON ÉXITO!")
            else:
                print("\n❌ EL ESCENARIO FALLÓ EN ALGÚN PUNTO.")

            if not exito:
                assert False, "El escenario falló en algún punto."
            if exito:
                assert True, "El escenario de Orden en Salón finalizó con éxito."

        finally:
            print("\n--- Realizando pasos de finalización ---")
            pos.clic_en_icono_usuario()
            pos.quit()
