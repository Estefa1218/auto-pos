
from automator import PosAutomator
from test_base import setup_and_login
def test_orden_para_disminuir_items():
    pos = setup_and_login("Orden para disminuir items")
    if pos:
        exito = True
    try:
        if exito: exito = pos.crear_orden_comer_aca()
        if pos.agregar_producto("ruby", "Primer producto.png"):
            if exito: exito = pos.aumentar_cantidad(4)
            if exito: exito = pos.disminuir_cantidad(2)
            if exito: exito = pos.finalizar_orden()
            if pos.pagar_con_tarjeta("5 de propina.png"):
                if pos.pagar_con_efectivo("42000", "1944"):
                    if exito:
                        print("\n🎉 ¡ESCENARIO FINALIZADO CON ÉXITO!")
        else:
            print("\n❌ EL ESCENARIO FALLÓ EN ALGÚN PUNTO.")
        
        if not exito:
            assert False, "El escenario falló en algún punto."
        if exito:
            assert True, "El escenario de Orden para disminuir items finalizó con éxito."
    finally:
        print("\n--- Realizando pasos de finalización ---")
        pos.clic_en_icono_usuario()
        pos.quit()
        pos.clic_en_icono_usuario()
        pos.quit()