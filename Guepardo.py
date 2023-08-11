# Dados do problema
# velocidade inicial em milhas por hora (pois parte do repouso)
velocidade_inicial_mph = 0
velocidade_final_mph = 72     # velocidade final em milhas por hora
tempo_segundos = 2            # intervalo de tempo em segundos

# Convertendo as velocidades para ml/s
velocidade_inicial_mls = velocidade_inicial_mph * \
    (1 / 3600)  # 1 mph = 1 milha / 3600 segundos
velocidade_final_mls = velocidade_final_mph * (1 / 3600)

# Calculando a aceleração média
variacao_velocidade_mls = velocidade_final_mls - velocidade_inicial_mls
aceleracao_media_mls2 = variacao_velocidade_mls / tempo_segundos

print("A aceleração média do guepardo é de", aceleracao_media_mls2, "ml/s².")
