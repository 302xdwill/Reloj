class RelojDigital:
    """Clase que modela el comportamiento de un reloj digital con alarmas."""

    def __init__(self, horas=0, minutos=0, segundos=0):
        self._horas = horas % 24
        self._minutos = minutos % 60
        self._segundos = segundos % 60
        self._alarma_h = None
        self._alarma_m = None

    def configurar_hora(self, h, m, s=0):
        """Establece la hora actual del reloj."""
        self._horas = h % 24
        self._minutos = m % 60
        self._segundos = s % 60

    def configurar_alarma(self, h, m):
        """Define una hora y minuto para activar la alarma."""
        self._alarma_h = h % 24
        self._alarma_m = m % 60

    def avanzar_segundo(self):
        """Incrementa el tiempo y verifica si la alarma debe sonar."""
        self._segundos += 1
        if self._segundos >= 60:
            self._segundos = 0
            self._minutos += 1
            
        if self._minutos >= 60:
            self._minutos = 0
            self._horas += 1
            
        self._horas %= 24
        self._verificar_alarma()

    def _verificar_alarma(self):
        """Método interno para validar la alarma."""
        if (self._horas == self._alarma_h and 
            self._minutos == self._alarma_m and 
            self._segundos == 0):
            print("\n🔔 ¡ALARMA SONANDO!")

    def mostrar_formato_24h(self):
        """Devuelve la hora en formato 24 horas (HH:MM:SS)."""
        return f"{self._horas:02d}:{self._minutos:02d}:{self._segundos:02d}"

    def mostrar_formato_12h(self):
        """Devuelve la hora en formato 12 horas con AM/PM."""
        periodo = "AM" if self._horas < 12 else "PM"
        h_12 = self._horas % 12
        h_12 = 12 if h_12 == 0 else h_12
        return f"{h_12:02d}:{self._minutos:02d}:{self._segundos:02d} {periodo}"