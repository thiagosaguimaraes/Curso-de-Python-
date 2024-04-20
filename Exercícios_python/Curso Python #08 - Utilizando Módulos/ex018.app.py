from math import sin, cos, tan, radians

ângulo = float(input('Digite um angulo: '))

print(f'''O ângulo {ângulo}° tem:
Seno de {sin(radians(ângulo)):.2f}°
Cosseno de {cos(radians(ângulo)):.2f}°
Tangente de {tan(radians(ângulo)):.2f}°''')
