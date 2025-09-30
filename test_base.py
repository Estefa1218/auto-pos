# test_base.py

from automator import PosAutomator
import random


# --- CONFIGURACIÓN CENTRALIZADA ---
# Si algo cambia, solo lo modificas aquí.
RUTA_APP_POS = r"C:\Users\estef\OneDrive\Documentos\Ejecucion pruebas\nPos-v0.5.9-4-Release-windows\pos.exe"
PIN_A_INGRESAR = "220725"

def setup_and_login(nombre_escenario):
    """
    Esta función se encarga de toda la preparación repetitiva:
    1. Imprime el inicio del escenario.
    2. Abre la aplicación POS.
    3. Realiza el login.
    4. Devuelve el objeto 'pos' si todo fue exitoso, o 'None' si falló.
    """
    print(f"--- INICIANDO ESCENARIO: {nombre_escenario} ---")
    
    try:
        # 1. Abrimos el POS usando nuestra clase
        pos = PosAutomator(RUTA_APP_POS)

        # 2. Hacemos el login
        if pos.login(PIN_A_INGRESAR):
            return pos # Devolvemos el objeto 'pos' listo para usarse
        else:
            print("\n❌ EL LOGIN FALLÓ. No se puede continuar.")
            pos.quit() # Cerramos la app si el login falla
            return None
    except Exception as e:
        print(f"\n❌ ERROR durante la preparación del escenario: {e}")
        return None


def generar_nit_valido():
    """Genera un número de NIT colombiano aleatorio de 9 dígitos y su DV."""
    base = str(random.randint(100000000, 999999999))
    factores = [71, 67, 59, 53, 47, 43, 41, 37, 29, 23, 19, 17, 13, 7, 3]
    suma = 0
    for i, digito in enumerate(reversed(base)):
        suma += int(digito) * factores[i]
    
    residuo = suma % 11
    if residuo < 2:
        dv = residuo
    else:
        dv = 11 - residuo
        
    return base, str(dv)