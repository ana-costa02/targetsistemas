import json

# Faturamento diário
faturamento_diario = [200, 350, 400, 600, 0, 0, 700, 800, 900, 1000, 1200, 1500, 1300, 1100, 900, 800, 750, 500, 450, 300, 200, 0, 0, 600, 700, 800, 1000, 1100, 1400, 1200]

# Cálculo do menor e maior valor de faturamento diário
menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)

# Cálculo da média mensal
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# Número de dias acima da média mensal
dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

print(f"Menor valor de faturamento diário: R${menor_valor}")
print(f"Maior valor de faturamento diário: R${maior_valor}")
print(f"Número de dias com faturamento diário superior à média mensal: {dias_acima_da_media}")
