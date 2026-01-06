
from automator import PosAutomator
from test_base import setup_and_login, generar_nit_valido 
from faker import Faker
fake = Faker('es_CO')
NIT_NUMERO, DV = generar_nit_valido() 
RAZON_SOCIAL = fake.company()
CORREO = fake.company_email()
def test_cliente_nit_identificado_extranjero():
    pos = setup_and_login(f"Factura con NIT para fe {RAZON_SOCIAL}")

    if pos:
        try:
            exito = True
            
            if exito: exito = pos.crear_orden_comer_aca()
            if exito: exito = pos.agregar_producto("ruby", "Primer producto.png")
            if exito: exito = pos.finalizar_orden()
            if exito: exito = pos._click_image("Ir a cobrar.png", "Botón 'Ir a Cobrar'")
            if exito: exito = pos.pagar_consumidor_identificado_nit(NIT_NUMERO, DV, RAZON_SOCIAL, CORREO)
            if pos.pagar_con_efectivo("14000", "1296"):
                if exito:
                    print("\n🎉 ¡ESCENARIO DE FACTURA CON NIT FINALIZADO CON ÉXITO!")
            else:
                print("\n❌ EL ESCENARIO FALLÓ EN ALGÚN PUNTO.")
                
                if not exito:
                    assert False, "El escenario falló en algún punto."
                if exito:
                    assert True, "El escenario de Orden con registro de nuevo cliente nit finalizó con éxito."
                
        finally:
            print("\n--- Realizando pasos de finalización ---")
            pos.clic_en_icono_usuario()
            pos.quit()