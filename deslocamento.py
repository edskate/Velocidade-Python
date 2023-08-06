# Dados do problema
velocidade_inicial_mph = 4  # velocidade inicial em m/s
aceleracao_media_ms2 = 2    # aceleração média em m/s²
tempo_segundos = 5          # intervalo de tempo em segundos

# Convertendo a velocidade inicial para m/s
velocidade_inicial_ms = velocidade_inicial_mph * \
    (1000 / 3600)  # 1 mph = 1000 m/3600 s

# Calculando a velocidade final
velocidade_final_ms = velocidade_inicial_ms + \
    (aceleracao_media_ms2 * tempo_segundos)

print("A velocidade final do automóvel é de", velocidade_final_ms, "m/s.")
