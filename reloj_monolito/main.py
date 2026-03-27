from reloj_digital import RelojDigital

def ejecutar_simulacion():
    """Función principal para probar el funcionamiento del reloj."""
    # Instanciar el objeto
    mi_reloj = RelojDigital()
    
    # Configurar hora inicial y alarma
    mi_reloj.configurar_hora(23, 59, 58)
    mi_reloj.configurar_alarma(0, 0)
    
    print(f"Hora inicial (24h): {mi_reloj.mostrar_formato_24h()}")
    print(f"Hora inicial (12h): {mi_reloj.mostrar_formato_12h()}")
    
    # Simular el paso de los segundos
    print("\nAvanzando 3 segundos...")
    for _ in range(3):
        mi_reloj.avanzar_segundo()
        print(f"Actual: {mi_reloj.mostrar_formato_24h()} | {mi_reloj.mostrar_formato_12h()}")

if __name__ == "__main__":
    ejecutar_simulacion()