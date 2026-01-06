from automator import PosAutomator
from test_base import setup_and_login
from faker import Faker

# --- CONFIGURACIÓN DE LOS PAGOS ---
# Supongamos que la cuenta da 30.000 (ajusta estos valores según tus productos)
LISTA_PAGOS = [
    {"monto": "4666", "propina": "216"},
    {"monto": "4666", "propina": "216"},
    {"monto": "4666", "propina": "216"}
] 
IMAGEN_PROPINA = "5 de propina.png"
IMAGEN_EFECTIVO = "metodo efectivo.png"
IMAGEN_IMPUESTO = "impuestos.png" # La imagen del botón efectivo

def test_pago_tres_partes_efectivo():
    pos = setup_and_login("Pago dividido en 3 partes de Efectivo")

    if pos:
        try:
            exito = True
            print("\n--- FASE 1: Creando Orden ---")
            if exito: exito = pos.crear_orden_comer_aca()
            if exito: exito = pos.agregar_producto("ruby", "Primer producto.png")
            if exito: exito = pos.finalizar_orden()
            print("\n--- FASE 2: Ingresando a pantalla de pagos ---")
            if exito: exito = pos.iniciar_pago_con_propina_y_confirmar(IMAGEN_PROPINA, IMAGEN_EFECTIVO)
            if exito:
                cantidad_total = len(LISTA_PAGOS)
                lineas_extra = cantidad_total - 1 
                if exito: exito = pos.agregar_lineas_de_pago(lineas_extra)
                if exito: exito = pos.diligenciar_lista_de_pagos_completa(LISTA_PAGOS)
                if exito: exito = pos._click_image("cerrar orden.png", "Botón 'Cerrar Orden' final")
            print("\n--- FASE 3: Finalizando transacción ---")
            if exito:
                print("\n🎉 ¡PAGO DE 3 PARTES EN EFECTIVO COMPLETADO!")
                assert True
            else:
                assert False, "Falló el flujo de pagos múltiples"
        finally:
            pos.quit()