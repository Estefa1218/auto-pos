
from automator import PosAutomator
from test_base import setup_and_login

VALOR_PROPINA = "1300" 
def test_orden_propina_valor_para_editar():

    pos = setup_and_login(f"Pago con Propina por Valor de {VALOR_PROPINA}")

    if pos:
        try:
            exito = True
            if exito: exito = pos.crear_orden_comer_aca()
            if exito: exito = pos.agregar_producto("ruby", "Primer producto.png")
            if exito: exito = pos.finalizar_orden()
            if exito: exito = pos.pagar_valor_propina(VALOR_PROPINA)
            if pos.pagar_con_efectivo("14000", "1300"):
                if exito:
                    print("\n🎉 ¡ESCENARIO FINALIZADO CON ÉXITO!")
            else:
                print("\n❌ EL ESCENARIO FALLÓ EN ALGÚN PUNTO.")

            if not exito:
                assert False, "El escenario falló en algún punto."
            if exito:
                assert True, "El escenario de Pago con Propina por Valor definalizó con éxito."
                
        finally:
            print("\n--- Realizando pasos de finalización ---")
            pos.clic_en_icono_usuario()
            pos.quit()