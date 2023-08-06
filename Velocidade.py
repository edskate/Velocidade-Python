# Convertendo as velocidades para m/s
velocidade_inicial_kmh = 108
velocidade_final_kmh = 37

velocidade_inicial_ms = velocidade_inicial_kmh * \
    (1000 / 3600)  # 1 km/h = 1000 m/3600 s
velocidade_final_ms = velocidade_final_kmh * (1000 / 3600)

# Calculando a aceleração média
tempo_segundos = 4

aceleracao_media = (velocidade_final_ms -
                    velocidade_inicial_ms) / tempo_segundos

print("A aceleração média é:", aceleracao_media, "m/s²")
