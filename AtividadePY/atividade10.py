10. Volume de caixa d'água cilíndrica
python
CopiarEditar
import math
raio = float(input("Raio da base (m): "))
altura = float(input("Altura (m): "))
volume = math.pi * raio ** 2 * altura
print(f"Volume: {volume} m³")