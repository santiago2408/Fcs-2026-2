class AgenteReactivoSimple:
    def __init__(self, reglas):
        # El agente tiene una representación interna estática: un sistema de reglas[cite: 2]
        self.reglas = reglas

    def actuar(self, percepcion):
        # Percibe cómo está el mundo ahora[cite: 2]
        estado = percepcion
        
        # Evalúa las reglas de condición-acción: Regla-Coincidencia(estado, reglas)[cite: 2]
        # Decide qué acción tomar ahora basándose únicamente en la percepción actual[cite: 2]
        accion = self.reglas.get(estado, "No hacer nada")
        
        # El actuador ejecuta la acción[cite: 2]
        return accion


# =====================================================================
# EJEMPLO 1: EL MUNDO DE LA ASPIRADORA (Tomado del material)
# =====================================================================
print("=== SIMULACIÓN: AGENTE ASPIRADORA ===")

# Reglas de condición-acción para la aspiradora[cite: 2]
reglas_aspiradora = {
    "Casilla_Sucia": "Aspirar",
    "Casilla_Limpia": "Moverse a la otra casilla"
}

# Instanciación del agente reactivo simple
agente_aspiradora = AgenteReactivoSimple(reglas_aspiradora)

# Simulación de percepciones que recibe el sensor a lo largo del tiempo
percepciones_aspiradora = ["Casilla_Sucia", "Casilla_Limpia", "Casilla_Sucia"]

for p in percepciones_aspiradora:
    # El agente percibe y actúa sin tener historial de percepciones[cite: 2]
    print(f"Percibe: '{p}' -> Acción: {agente_aspiradora.actuar(p)}")


print("\n")


# =====================================================================
# EJEMPLO 2: SISTEMA DE RIEGO AUTOMÁTICO (Ejemplo nuevo)
# =====================================================================
print("=== SIMULACIÓN: AGENTE DE RIEGO AUTOMÁTICO ===")

# Reglas de condición-acción predefinidas para el sensor de humedad[cite: 2]
reglas_riego = {
    "Suelo_Seco": "Abrir válvula (Regar)",
    "Suelo_Humedo": "Cerrar válvula (No regar)"
}

# Instanciación del agente reactivo simple
agente_riego = AgenteReactivoSimple(reglas_riego)

# Simulación de percepciones del higrómetro (sensor de humedad del suelo)
percepciones_riego = ["Suelo_Seco", "Suelo_Humedo", "Suelo_Humedo", "Suelo_Seco"]

for p in percepciones_riego:
    # El agente percibe y actúa sin aprendizaje continuo ni razonamiento a largo plazo[cite: 2]
    print(f"Percibe: '{p}' -> Acción: {agente_riego.actuar(p)}")