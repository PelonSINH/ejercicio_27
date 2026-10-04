# --- Ingresos del día (Multiplicación) ---
# Vendimos 25 vasos de limonada a $15 cada uno.
ingreso_total = 25 * 15
print("El ingreso total del día fue de: $")
print(ingreso_total)

# --- Gastos del día (Suma) ---
# Gastamos $70 en limones y azúcar, y $30 en vasos y hielo.
gastos_totales = 70 + 30
print("El gasto total en materiales fue de: $")
print(gastos_totales)

# Asigna los valores que calculamos en la parte anterior
ingreso_total = 375
gastos_totales = 100

# --- Paso 1: Calcular la ganancia neta (Resta) ---
# Para obtener la ganancia, resta los gastos totales al ingreso total.
# Escribe tu código aquí:
ganancia_neta = ingreso_total - gastos_totales
print("La ganancia neta es de: $")
print(ganancia_neta)

# --- Paso 2: Dividir la ganancia entre los socios (División) ---
# Hay 2 socios. Divide la ganancia neta entre 2.
# Escribe tu código aquí:
ganancia_por_socio = ganancia_neta / 2
print("La ganancia por socio es de: $")
print(ganancia_por_socio)

# --- Paso 3: Imprime un resumen final ---
# Este código ya está listo para mostrar todos tus resultados.
print("\n--- Resumen del Día ---")
print("Ingresos Totales:", ingreso_total)
print("Gastos Totales:", gastos_totales)
print("Ganancia Final:", ganancia_neta)
print("A cada socio le corresponden:", ganancia_por_socio)
