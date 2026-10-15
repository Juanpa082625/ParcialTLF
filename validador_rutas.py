import sys

def es_simbolo_valido(c):
    return (
            ('a' <= c <= 'z') or
            ('A' <= c <= 'Z') or
            ('0' <= c <= '9') or
            c in {'_', '-', '.'}
    )

def validar_ruta(cadena):
    if not cadena:
        return False

    estado_actual = 'q0'

    for c in cadena:
        if c == '/':
            tipo_entrada = '/'
        elif es_simbolo_valido(c):
            tipo_entrada = 'x'
        else:
            return False  # Carácter fuera del alfabeto Σ

        # Tabla de transición del AFD M2
        if estado_actual == 'q0':
            if tipo_entrada == 'x':
                estado_actual = 'q2'
            elif tipo_entrada == '/':
                estado_actual = 'q1'
        elif estado_actual == 'q1':
            if tipo_entrada == 'x':
                estado_actual = 'q2'
            elif tipo_entrada == '/':
                estado_actual = 'q3'
        elif estado_actual == 'q2':
            if tipo_entrada == 'x':
                estado_actual = 'q2'
            elif tipo_entrada == '/':
                estado_actual = 'q1'
        elif estado_actual == 'q3':
            estado_actual = 'q3'

    return estado_actual in {'q1', 'q2'}


def ejecutar_pruebas():
    casos = [
        ("/", True, "Raíz del sistema"),
        ("/home/user/docs", True, "Ruta absoluta válida"),
        ("/etc/nginx/nginx.conf", True, "Ruta absoluta con punto en nombre"),
        ("/var/log/", True, "Ruta absoluta con barra final"),
        ("./run.sh", True, "Ruta relativa con punto inicial"),
        ("../data/file_1.txt", True, "Ruta relativa con directorio padre y guion bajo"),
        ("src/main-v2.c", True, "Ruta relativa con guion medio"),
        ("", False, "Cadena vacía (inválida)"),
        ("//etc", False, "Dos barras seguidas al inicio"),
        ("/home//user", False, "Dos barras seguidas en medio"),
        ("docs//a.txt", False, "Dos barras seguidas"),
        ("/home/mi carpeta", False, "Contiene espacio (carácter no válido)"),
        ("/tmp/a*.txt", False, "Contiene asterisco (carácter no válido)")
    ]

    print("=== EJECUCIÓN DE PRUEBAS PARA LA TEMÁTICA 38 ===")
    exitosas = 0
    total = len(casos)

    for cadena, esperado, descripcion in casos:
        resultado = validar_ruta(cadena)
        estado_prueba = "EXITOSA" if resultado == esperado else "FALLIDA"
        if resultado == esperado:
            exitosas += 1

        representacion_cadena = f"'{cadena}'" if cadena else "'' (cadena vacía)"
        print(f"[{estado_prueba}] Cadena: {representacion_cadena:25} | Esperado: {str(esperado):5} | Obt: {str(resultado):5} | Desc: {descripcion}")

    print(f"\nPruebas superadas: {exitosas} de {total}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        ruta_ingresada = sys.argv[1]
        valida = validar_ruta(ruta_ingresada)
        print(f"La ruta '{ruta_ingresada}' {'SÍ' :>2} es válida en L." if valida else f"La ruta '{ruta_ingresada}' {'NO' :>2} es válida en L.")
    else:
        ejecutar_pruebas()