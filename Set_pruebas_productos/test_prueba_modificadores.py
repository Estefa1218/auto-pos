
from automator import PosAutomator
from test_base import setup_and_login
def test_orden_para_llevar_con_modificadores():
 pos = setup_and_login("Orden en para llevar con modificadores")
 if pos:
    try:
        exito = True
        
        if exito: exito = pos.crear_orden_para_llevar()
        if pos.agregar_producto_modificador("producto 4", "Segundo producto.png"): 
            if exito: exito = pos.finalizar_orden()
            if pos.pagar_con_tarjeta("5 de propina.png"):
              if pos.pagar_con_efectivo("27100", "1254"):
                if exito:
                 print("\n🎉 ¡ESCENARIO FINALIZADO CON ÉXITO!")
        else:
            print("\n❌ EL ESCENARIO FALLÓ EN ALGÚN PUNTO.")
            
        if not exito:
                assert False, "El escenario falló en algún punto."
        if exito:
                assert True, "El escenario de Orden en para llevar con modificadores finalizó con éxito."
            
    finally:
        print("\n--- Realizando pasos de finalización ---")
        pos.clic_en_icono_usuario()
        pos.quit()