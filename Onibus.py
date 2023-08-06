# Dados do problema
velocidade_onibus_kmh = 50
distancia_percorrida_km = 100

# Convertendo a velocidade para m/s
velocidade_onibus_ms = velocidade_onibus_kmh * \
    (1000 / 3600)  # 1 km/h = 1000 m/3600 s

# Calculando o tempo gasto no percurso
tempo_gasto_horas = distancia_percorrida_km / velocidade_onibus_kmh
tempo_gasto_minutos = tempo_gasto_horas * 60
tempo_gasto_segundos = tempo_gasto_minutos * 60

print("O tempo gasto no percurso é de:")
print(f"{tempo_gasto_horas:.2f} horas")
print(f"{tempo_gasto_minutos:.2f} minutos")
print(f"{tempo_gasto_segundos:.2f} segundos")
