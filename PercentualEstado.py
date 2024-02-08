faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Cálculo do faturamento total
faturamento_total = sum(faturamento_por_estado.values())

# Cálculo do percentual de representação de cada estado
percentual_por_estado = {estado: (faturamento / faturamento_total) * 100 for estado, faturamento in faturamento_por_estado.items()}

# Exibindo os percentuais
for estado, percentual in percentual_por_estado.items():
    print(f"{estado}: {percentual:.2f}%")
