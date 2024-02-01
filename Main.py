import pandas as pd

# Carregar os dados do arquivo CSV.
dados = pd.read_csv("Original_Files/jobs_in_data.csv")
# print(dados)

# Remover linhas com valores ausentes, se houver.
dados_limpos = dados.dropna()

# Remover linhas duplicadas, se houver.
dados_limpos = dados_limpos.drop_duplicates()
print(dados_limpos)


