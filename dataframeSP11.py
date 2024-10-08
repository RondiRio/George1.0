import pandas as pd

# Lista de habilidades de todas as temporadas (exemplo simplificado)
file_path = r'habilidades_super_onze.xlsx'
dados_habilidades = pd.read_excel(file_path)


# Criando o DataFrame
df_habilidades = pd.DataFrame(dados_habilidades)

# Função para classificar como 'Melhor' ou 'Pior' com base no poder
def classificar_habilidade(poder):
    if poder >= 85:
        return 'Melhor'
    else:
        return 'Pior'

# Aplicando a classificação
df_habilidades['Classificação'] = df_habilidades['Poder'].apply(classificar_habilidade)

# Salvando o DataFrame em um arquivo Excel
file_path = 'habilidades_super_onze.xlsx'
df_habilidades.to_excel(file_path, index=False)

# Exibindo as melhores habilidades
melhores_habilidades = df_habilidades[df_habilidades['Classificação'] == 'Melhor']

print(melhores_habilidades)
