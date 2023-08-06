# Dados do problema
velocidade_inicial_ms = 30  # velocidade inicial em m/s
velocidade_final_ms = 20    # velocidade final em m/s
tempo_segundos = 10         # intervalo de tempo em segundos

# Calculando a aceleração média
variacao_velocidade_ms = velocidade_final_ms - velocidade_inicial_ms
aceleracao_media_ms2 = variacao_velocidade_ms / tempo_segundos

print("A aceleração média do veículo no intervalo de tempo de 10 segundos é de",
      aceleracao_media_ms2, "m/s².")
