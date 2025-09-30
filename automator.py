from typing import Self
import pyautogui
import time
import subprocess
import pyperclip

class PosAutomator:
    def __init__(self, ruta_app):
        """El constructor inicia la aplicación."""
        self.ruta_app = ruta_app
        self.app_process = None
        print("🚀 Abriendo la aplicación POS...")
        try:
            self.app_process = subprocess.Popen(self.ruta_app)
            time.sleep(5) 
            print("✅ Aplicación iniciada.")
        except FileNotFoundError:
            print(f"❌ ERROR CRÍTICO: No se encontró el ejecutable del POS en la ruta: {self.ruta_app}")
            raise

    def _click_image(self, image_name, description, confidence=0.8, timeout=10):
        """Método interno y genérico para buscar una imagen y hacerle clic."""
        print(f"⏳ Buscando '{description}' ({image_name})...")
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                posicion = pyautogui.locateCenterOnScreen(f'Imagenes/{image_name}', confidence=confidence)
                if posicion:
                    pyautogui.click(posicion)
                    print(f"✅ Clic en '{description}'.")
                    time.sleep(1.5)
                    return True
            except Exception:
                pass
            time.sleep(1)
        print(f"❌ ERROR: No se encontró la imagen para '{description}' después de {timeout} segundos.")
        return False

    def _type_into_field(self, image_name, text_to_type, description, confidence=0.8):
        """Método interno para encontrar un campo, limpiarlo y escribir en él."""
        print(f"✍️  Escribiendo en '{description}'...")
        try:
            posicion = pyautogui.locateCenterOnScreen(f'Imagenes/{image_name}', confidence=confidence)
            if posicion:
                pyautogui.click(posicion.x, posicion.y) 
                time.sleep(0.5)
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('delete')
                pyautogui.write(text_to_type, interval=0.1)
                print(f"✅ Texto '{text_to_type}' escrito en '{description}'.")
                return True
            else:
                print(f"❌ ERROR: No se encontró el campo para '{description}'.")
                return False
        except Exception as e:
            print(f"❌ Ocurrió un error inesperado al escribir en '{description}': {e}")
            return False

    def login(self, pin, image_prefix="boton_"): # <-- 1. Agregamos un prefijo por defecto
        """
        Realiza el proceso de inicio de sesión usando un prefijo para los nombres de imagen.
        Por defecto usa 'boton_', pero puede usar otros como 'editar '.
        """
        print(f"\n--- Intentando ingresar PIN: {pin} (usando prefijo '{image_prefix}') ---")
        for numero in pin:
            # --- 2. Usamos el prefijo para construir el nombre del archivo ---
            nombre_archivo = f"{image_prefix}{numero}.png"
            if not self._click_image(nombre_archivo, f"Botón número {numero}", confidence=0.9, timeout=5):
                return False
        print("✅ PIN ingresado correctamente.")
        time.sleep(5)
        return True
    #----------creacion de orden

    def crear_orden_salon(self):
        """Inicia el flujo para crear una orden en salón."""
        print("\n--- Creando Orden en Salón ---")
        exito = True
        if exito: exito = self._click_image("menu.png", "Menú")
        if exito: exito = self._click_image("Ordenar.png", "Botón 'Ordenar'")
        if exito: exito = self._click_image("crear orden.png", "Botón 'Crear Orden'")
        if exito: exito = self._click_image("Orden salon.png", "Botón 'Orden en Salón'")
        if exito: exito = self._click_image("continuar.png", "Botón 'Continuar'")
        #if exito: exito = self._click_image("sector.png", "Botón 'Sector'")
        if exito: exito = self._click_image("mesa 19.png", "Seleccionar mesa 19")
        if exito: exito = self._click_image("ocupar mesa.png", "Ocupar mesa 19")
        return exito

    def crear_orden_para_llevar(self):
        """Inicia el flujo para crear una orden para llevar."""
        print("\n--- Creando Orden para Llévar ---")
        exito = True
        if exito: exito = self._click_image("menu.png", "Menú")
        if exito: exito = self._click_image("Ordenar.png", "Botón 'Ordenar'")
        if exito: exito = self._click_image("crear orden.png", "Botón 'Crear Orden'")
        if exito: exito = self._click_image("para llevar.png", "Botón 'Para Llevar'")
        if exito: exito = self._click_image("continuar.png", "Botón 'Continuar'")
        return exito
    
    def crear_orden_comer_aca(self):
        """Inicia el flujo para 'comer acá' sin seleccionar mesa."""
        print("\n--- Creando Orden para Comer Acá (Simple) ---")
        exito = True
        if exito: exito = self._click_image("menu.png", "Menú")
        if exito: exito = self._click_image("Ordenar.png", "Botón 'Ordenar'")
        if exito: exito = self._click_image("crear orden.png", "Botón 'Crear Orden'")
        if exito: exito = self._click_image("continuar.png", "Botón 'Continuar'")
        return exito

    def cambio_tipo_orden(self):
        """Inicia el flujo para crear una orden en salón."""
        print("\n--- Creando Orden en Salón ---")
        exito = True
        if exito: exito = self._click_image("menu.png", "Menú")
        if exito: exito = self._click_image("Ordenar.png", "Botón 'Ordenar'")
        if exito: exito = self._click_image("crear orden.png", "Botón 'Crear Orden'")
        if exito: exito = self._click_image("Orden salon.png", "Botón 'Orden en Salón'")
        if exito: exito = self._click_image("continuar.png", "Botón 'Continuar'")
        #if exito: exito = self._click_image("sector.png", "Botón 'Sector'")
        if exito: exito = self._click_image("mesa 19.png", "Seleccionar mesa 19")
        if exito: exito = self._click_image("pedido.png", "Seleccionar mostrador")
        if exito: exito = self._click_image("mostrador.png", "Seleccionar mostrador para orden") 
        if exito: exito = self._click_image("menu.png", "Menú")
        if exito: exito = self._click_image("opa.png", "opa")
        return exito
    
    def finalizar_orden(self):
        """Finaliza la orden"""
        print("\n--- Finalizando Orden ---")
        exito = True
        if exito: exito = self._click_image("continuar orden.png", "Botón 'Continuar Orden'")
        if exito: exito = self._click_image("ordenar orden.png", "Botón 'Ordenar Orden'")
        #--if exito: exito = self._click_image("Ir a cobrar.png", "Botón 'Ir a Cobrar'")
        return exito
    #-----------Productos

    def agregar_producto(self, nombre_producto_a_buscar, imagen_producto_a_clickear):
        """Busca un producto y lo agrega a la orden."""
        print(f"\n--- Agregando Producto: {nombre_producto_a_buscar} ---")
        exito = True
        if self._click_image("buscador.png", "Buscador de productos"):
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')
            pyautogui.write(nombre_producto_a_buscar, interval=0.1)
            print(f"-> Escribiendo '{nombre_producto_a_buscar}'")
            time.sleep(2)
        else:
            exito = False
        
        if exito: exito = self._click_image(imagen_producto_a_clickear, f"Producto '{nombre_producto_a_buscar}'")
        return exito
    

    def aumentar_cantidad(self, veces):
        """Hace clic en el botón '+' un número determinado de veces."""
        print(f"\n--- Aumentando la cantidad del producto {veces} veces ---")
        exito = True
        for i in range(veces):
            print(f"-> Agregando unidad {i + 1} de {veces}...")
            exito = self._click_image("agregar productos.png", "Botón '+' para aumentar cantidad")
            if not exito:
                print(f"❌ FALLÓ: No se pudo agregar la unidad {i + 1}.")
                break 
        return exito
    
    def disminuir_cantidad(self, veces):
        """Hace clic en el botón '-' un número determinado de veces."""
        print(f"\n--- Disminuyendo la cantidad del producto {veces} veces ---")
        exito = True
        for i in range(veces):
            print(f"-> Eliminando unidad {i + 1} de {veces}...")
            exito = self._click_image("des_agregar productos.png", "Botón '-' para disminuir cantidad")
            if not exito:
                print(f"❌ FALLÓ: No se pudo eliminar la unidad {i + 1}.")
                break
        return exito  
    
    def agregar_varios_producto(self, nombre_producto_a_buscar, imagen_producto_a_clickear):
        print(f"\n--- Agregando Producto: {nombre_producto_a_buscar} ---")
        exito = True
        if self._click_image("buscador.png", "Buscador de productos"):
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')
            pyautogui.write(nombre_producto_a_buscar, interval=0.1)
            print(f"-> Escribiendo '{nombre_producto_a_buscar}'")
            time.sleep(2)
        else:
            exito = False
        if exito: exito = self._click_image(imagen_producto_a_clickear, f"Producto '{nombre_producto_a_buscar}'")
        return exito
    
        
    def agregar_producto_modificador(self, nombre_producto_a_buscar, imagen_producto_a_clickear):
        print(f"\n--- Agregando Producto: {nombre_producto_a_buscar} ---")
        exito = True
        if self._click_image("buscador.png", "Buscador de productos"):
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')
            pyautogui.write(nombre_producto_a_buscar, interval=0.1)
            print(f"-> Escribiendo '{nombre_producto_a_buscar}'")
            time.sleep(2)
        else:
            exito = False
        if exito: exito = self._click_image(imagen_producto_a_clickear, f"Producto '{nombre_producto_a_buscar}'")
        if exito: exito = self._click_image("producto 4 macondo.png", "Botón 'Agregar Modificador 1'")
        if exito: exito = self._click_image("postre.png", "Botón 'Segundo modificador'")
        if exito: exito = self._click_image("segundo modificador.png", "Agregar Modificador 2'")
        return exito
    

    def pagar_con_efectivo(self, subtotal, propina):
        """Realiza el flujo de pago con efectivo."""
        print("\n--- Realizando Pago con Efectivo ---")
        exito = True
        if exito: exito = self._click_image("medio de pago .png", "Desplegable de método de pago")
        if exito: exito = self._click_image("efectivo.png", "Opción 'Efectivo'")
        if exito: exito = self._type_into_field("sub total.png", subtotal, "Campo de valor pagado")
        if exito: exito = self._type_into_field("propina.png", propina, "Campo de propina")
        if exito: exito = self._click_image("cerrar orden.png", "Botón 'Cerrar Orden' final")
        return exito
    

    def pagar_con_descuento_y_tarjeta(self, imagen_propina, porcentaje_descuento):
        print(f"\n--- Pagando orden con {porcentaje_descuento}% de descuento y tarjeta ---")
        exito = True
        if exito: exito = self._click_image("Ir a cobrar.png", "Botón 'Ir a Cobrar'")
        if exito: exito = self._click_image(imagen_propina, "Botón de Propina")
        pyautogui.scroll(-500); time.sleep(1)
        if exito: exito = self._click_image("descuento.png", "Botón 'Descuento'")
        if exito: exito = self._type_into_field("escribir descuento.png", str(porcentaje_descuento), "Campo 'Descuento'")
        pyautogui.scroll(-500); time.sleep(1)
        if exito: exito = self._click_image("tarjeta.png", "Método de pago 'Tarjeta'")
        if exito: exito = self._click_image("confirmar.png", "Botón 'Confirmar'")
        return exito

    def iniciar_edicion_y_reautenticar(self, pin):
        print("\n--- Iniciando edición de orden ---")
        exito = True
        if exito: exito = self._click_image("editar orden.png", "Botón 'Editar Orden'")
        if exito:
            print("-> Re-autenticando con PIN de edición...")
            time.sleep(2)
            exito = self.login(pin, image_prefix="editar ")
        return exito

    def llenar_formulario_nit(self, nit_numero, dv, razon_social, correo):
        print(f"\n--- Llenando formulario NIT para: {razon_social} ---")
        exito = True
        if exito: exito = self._click_image("consumidor indentificado.png", "Botón 'consumidor identificado'")
        if exito: exito = self._click_image("nit.png", "Opción de documento 'NIT'")
        if exito: exito = self._type_into_field("numero nit.png", nit_numero, "Campo 'Número de NIT'")
        if exito: exito = self._type_into_field("dv.png", dv, "Campo 'DV'")
        if exito: exito = self._type_into_field("razon social.png", razon_social, "Campo 'Razón Social'")
        if exito: exito = self._paste_into_field("correo consumidor identificado.png", correo, "Campo 'Correo Electrónico'")
        print("-> Bajando en la pantalla para encontrar más opciones...")
        pyautogui.scroll(-500) 
        time.sleep(1)
        if exito: exito = self._click_image("confirmar club.png", "Botón 'Confirmar' del formulario NIT")
        if exito: exito = self._click_image("aplicar.png", "Aplicar'aplicar'")
        if exito: exito = self._click_image("tarjeta.png", "Método de pago 'Tarjeta'")
        return exito

    def cambiar_propina_y_cliente_nit(self, nuevo_valor_propina, nit_numero, dv, razon_social, correo):
        print("\n--- Cambiando propina y datos de facturación a NIT ---")
        exito = True
        if exito: exito = self._click_image("valor de propina.png", "Opción 'Valor de Propina'")
        time.sleep(2)
        if exito:
            if self._type_into_field("titulo_valor_propina.png", nuevo_valor_propina, "Campo 'Valor de Propina'", y_offset=50):
                exito = self._click_image("aplicar.png", "Botón 'Aplicar' propina")
            else:
                exito = False
        if exito: exito = self.llenar_formulario_nit(nit_numero, dv, razon_social, correo)
        if exito: exito = self._click_image("guardar_edicion.png", "Botón final para Guardar Edición")
        return exito

    #------------------------club bacanes
    
    def registrar_cliente_en_orden(self, documento, nombre, apellido, correo, telefono):
        """
        Desde una orden activa, registra un nuevo cliente del club usando los nombres de archivo exactos.
        """
        print(f"\n--- Registrando nuevo cliente en la orden: {nombre} {apellido} ---")
        exito = True
        
        if exito: exito = self._click_image("club bacanes.png", "Botón 'Club Bacanes'")
        if exito: exito = self._type_into_field("buscador club.png", documento, "Escribir documento")
        if exito: exito = self._click_image("buscar cliente club.png", "Botón 'Buscar cliente'")
        if exito: exito = self._click_image("registrar club.png", "Botón 'Registrar'")
        if exito: exito = self._type_into_field("nombre cliente club.png", nombre, "Campo 'Nombre'")
        if exito: exito = self._type_into_field("apellidos club.png", apellido, "Campo 'Apellido'")
        if exito: exito = self._paste_into_field("correo club.png", correo, "Campo 'Correo'")
        if exito: exito = self._type_into_field("telefono club.png", telefono, "Campo 'Teléfono'")
        if exito: exito = self._click_image("confirmar club.png", "Botón 'Confirmar' del registro")
        return exito
    
    def registrar_cliente_en_orden_extranjero(self, documento, nombre, apellido, correo, telefono):
        """
        Desde una orden activa, registra un nuevo cliente del club usando los nombres de archivo exactos.
        """
        print(f"\n--- Registrando nuevo cliente en la orden: {nombre} {apellido} ---")
        exito = True
        
        if exito: exito = self._click_image("club bacanes.png", "Botón 'Club Bacanes'")
        if exito: exito = self._click_image("cedula extranjero.png", "Botón 'Cédula Extranjero'")
        if exito: exito = self._type_into_field("buscador club.png", documento, "Escribir documento")
        if exito: exito = self._click_image("buscar cliente club.png", "Botón 'Buscar cliente'")
        if exito: exito = self._click_image("registrar club.png", "Botón 'Registrar'")
        if exito: exito = self._type_into_field("nombre cliente club.png", nombre, "Campo 'Nombre'")
        if exito: exito = self._type_into_field("apellidos club.png", apellido, "Campo 'Apellido'")
        if exito: exito = self._paste_into_field("correo club.png", correo, "Campo 'Correo'")
        if exito: exito = self._click_image("desplegable club.png", "Desplegable 'Club'")
        if exito: exito = self._type_into_field("ecuador club.png", "Ecuador", "Campo 'Ecuador'")
        if exito: exito = self._type_into_field("telefono club.png", telefono, "Campo 'Teléfono'")
        if exito: exito = self._click_image("confirmar club.png", "Botón 'Confirmar' del registro")
        return exito
    
    #--------------------pagos

    def pagar_con_tarjeta(self, imagen_propina):
        print("\n--- Realizando Pago con Tarjeta ---")
        exito = True
        if exito: exito = self._click_image("Ir a cobrar.png", "Botón 'Ir a Cobrar'")
        if exito: exito = self._click_image(imagen_propina, "Botón de Propina")
        if exito: exito = self._click_image("tarjeta.png", "Método de pago 'Tarjeta'")
        if exito: exito = self._click_image("confirmar.png", "Botón 'Confirmar'")
        return exito

    def pagar_valor_propina(self, valor_propina):
        """Realiza el flujo de pago seleccionando una propina por valor."""
        print(f"\n--- Realizando Pago con Propina por Valor de: {valor_propina} ---")
        exito = True
        if exito: exito = self._click_image("Ir a cobrar.png", "Botón 'Ir a Cobrar'")
        if exito: exito = self._click_image("valor de propina.png", "Opción 'Valor de Propina'")
        print("-> Esperando a que aparezca la ventana de valor de propina...")
        time.sleep(2) 
        if exito: exito = self._type_into_field("escribir valor de propina.png", valor_propina, "Campo 'Valor de Propina'")
        if exito: exito = self._click_image("confirmar propina.png", "Botón 'Confirmar'")
        if exito: exito = self._click_image("tarjeta.png", "Método de pago 'Tarjeta'")
        if exito: exito = self._click_image("confirmar.png", "Botón 'Confirmar'")
        return exito

    def pago_con_descuento(self, imagen_propina, porcentaje_descuento):
        """Realiza el flujo de pago seleccionando un descuento."""
        print(f"\n--- Realizando Pago con Descuento ---")
        exito = True
        if exito: exito = self._click_image("Ir a cobrar.png", "Botón 'Ir a Cobrar'")
        if exito: exito = self._click_image(imagen_propina, "Botón de Propina")
        print("-> Bajando en la pantalla para encontrar más opciones...")
        pyautogui.scroll(-500) 
        time.sleep(1)
        if exito: exito = self._click_image("descuento.png", "Botón 'Descuento'")
        if exito: exito = self._type_into_field("escribir descuento.png", str(porcentaje_descuento), "Campo 'Descuento'")
        if exito: exito = self._click_image("tarjeta.png", "Método de pago 'Tarjeta'")
        if exito: exito = self._click_image("confirmar.png", "Botón 'Confirmar'")
        return exito

    def pagar_consumidor_identificado(self, imagen_propina, documento, nombre, correo):
        print(f"\n--- Registrando nuevo cliente en la orden para consumidor identificado: {nombre} ---")
        exito = True
        if exito: exito = self._click_image("Ir a cobrar.png", "Botón 'Ir a Cobrar'")
        if exito: exito = self._click_image(imagen_propina, "Botón de Propina")
        if exito: exito = self._click_image("consumidor indentificado.png", "Botón 'consumidor identificado'")
        if exito: exito = self._type_into_field("cedula consumidor.png", documento, "Escribir documento")
        if exito: exito = self._type_into_field("nombre consumidor identificado.png", nombre, "Campo 'Nombre'")
        if exito: exito = self._paste_into_field("correo consumidor identificado.png", correo, "Campo 'Correo'")
        print("-> Bajando en la pantalla para encontrar más opciones...")
        pyautogui.scroll(-500) 
        time.sleep(1)
        if exito: exito = self._click_image("confirmar club.png", "Botón 'Confirmar' del registro")
        if exito: exito = self._click_image("aplicar.png", "Aplicar'aplicar'")
        if exito: exito = self._click_image("tarjeta.png", "Método de pago 'Tarjeta'")
        if exito: exito = self._click_image("confirmar.png", "Botón 'Confirmar'")
        return exito
    
    def pagar_consumidor_identificado_extranjero(self, imagen_propina, documento, nombre, correo):
        print(f"\n--- Registrando nuevo cliente en la orden para consumidor identificado: {nombre} ---")
        exito = True
        if exito: exito = self._click_image("Ir a cobrar.png", "Botón 'Ir a Cobrar'")
        if exito: exito = self._click_image(imagen_propina, "Botón de Propina")
        if exito: exito = self._click_image("consumidor indentificado.png", "Botón 'consumidor identificado'")
        if exito: exito = self._click_image("cedula extranjero consumidor.png", "Botón 'consumidor identificado extranjero'")
        if exito: exito = self._type_into_field("cedula consumidor extranjero.png", documento, "Escribir documento")
        if exito: exito = self._type_into_field("nombre consumidor identificado.png", nombre, "Campo 'Nombre'")
        if exito: exito = self._paste_into_field("correo consumidor identificado.png", correo, "Campo 'Correo'")
        print("-> Bajando en la pantalla para encontrar más opciones...")
        pyautogui.scroll(-500) 
        time.sleep(1)
        if exito: exito = self._click_image("confirmar club.png", "Botón 'Confirmar' del registro")
        if exito: exito = self._click_image("aplicar.png", "Aplicar'aplicar'")
        if exito: exito = self._click_image("tarjeta.png", "Método de pago 'Tarjeta'")
        if exito: exito = self._click_image("confirmar.png", "Botón 'Confirmar'")
        return exito
    
    def editar_orden_completa(self, nuevo_valor_propina, nit_numero, dv, razon_social, correo, nuevo_porcentaje_descuento):
        """
        Ya en modo edición, cambia la propina, reasigna el cliente a NIT y aplica un nuevo descuento.
        """
        print("\n--- Cambiando propina, cliente y descuento de la orden ---")
        exito = True
        if exito: exito = self._click_image("valor de propina.png", "Opción 'Valor de Propina'")
        time.sleep(2)
        if exito:
            if exito: exito = self._type_into_field("escribir valor de propina.png", nuevo_valor_propina, "Campo 'Valor de Propina'")
        if exito: exito = self._click_image("confirmar propina.png", "Botón 'Confirmar'")
        else:
                exito = False
        if exito: exito = self.llenar_formulario_nit(nit_numero, dv, razon_social, correo)
        if exito: exito = self._click_image("descuento.png", "Botón 'Descuento'")
        if exito: exito = self._type_into_field("escribir descuento.png", str(nuevo_porcentaje_descuento), "Campo 'Descuento'")
        if exito: exito = self._click_image("guardar_edicion.png", "Botón final para Guardar Edición")
        
        return exito    

    def pagar_consumidor_identificado_nit(self, nit_numero, dv, razon_social, correo):
        """
        Desde la pantalla de pago, selecciona NIT y rellena el formulario.
        """
        print(f"\n--- Llenando formulario NIT para: {razon_social} ---")
        exito = True
        
        if exito: exito = self._click_image("consumidor indentificado.png", "Botón 'consumidor identificado'")
        if exito: exito = self._click_image("nit.png", "Opción de documento 'NIT'")
        if exito: exito = self._type_into_field("numero nit.png", nit_numero, "Campo 'Número de NIT'")
        if exito: exito = self._type_into_field("dv.png", dv, "Campo 'DV'")
        if exito: exito = self._type_into_field("razon social.png", razon_social, "Campo 'Razón Social'")
        if exito: exito = self._paste_into_field("correo consumidor identificado.png", correo, "Campo 'Correo Electrónico'")
        print("-> Bajando en la pantalla para encontrar más opciones...")
        pyautogui.scroll(-500) 
        time.sleep(1)
        if exito: exito = self._click_image("confirmar club.png", "Botón 'Confirmar' del formulario NIT")
        if exito: exito = self._click_image("aplicar.png", "Aplicar'aplicar'")
        if exito: exito = self._click_image("tarjeta.png", "Método de pago 'Tarjeta'")
        if exito: exito = self._click_image("confirmar.png", "Botón 'Confirmar'")
        
        return exito
    
    def _paste_into_field(self, image_name, text_to_paste, description, confidence=0.8, timeout=10):
        """Versión mejorada: Encuentra un campo durante un tiempo y PEGA texto."""
        print(f"📋 Pegando en '{description}'...")
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                posicion = pyautogui.locateCenterOnScreen(f'Imagenes/{image_name}', confidence=confidence)
                if posicion:
                    pyautogui.click(posicion.x, posicion.y) 
                    time.sleep(0.5)
                    pyperclip.copy(text_to_paste)
                    pyautogui.hotkey('ctrl', 'v')
                    print(f"✅ Texto '{text_to_paste}' pegado en '{description}'.")
                    return True
            except Exception:
                pass
            time.sleep(1)
        print(f"❌ ERROR: No se encontró la imagen de referencia para '{description}' después de {timeout} segundos.")
        return False
    
    def clic_en_icono_usuario(self):
        """
        Hace clic en el ícono de usuario. Diseñado para usarse al final de una prueba.
        Tiene su propio try/except para no detener el cierre de la app si falla.
        """
        print("-> Realizando clic final en el ícono de usuario...")
        try:
            # Llamamos a _click_image pero con un timeout más corto
            self._click_image("usuario.png", "Ícono de Usuario", timeout=5)
        except Exception as e:
            print(f"⚠️  No se pudo hacer clic en el ícono de usuario: {e}")
            pass

    def quit(self):
        """Cierra la aplicación."""
        if self.app_process:
            print("\n--- Cerrando la aplicación ---")
            self.app_process.kill()
            