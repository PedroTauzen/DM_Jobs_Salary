import pandas as pd

# Carregar os dados do arquivo CSV.
dados = pd.read_csv("Original_Files/jobs_in_data.csv")
print(dados.head())

# Verificar valores ausentes
print("Valores ausentes por coluna:")
print(dados.isnull().sum())

# Verificar valores duplicados.
print("Valores duplicados.")
print(dados.duplicated())

# Taxa de câmbio de USD para EUR
taxa_usd_para_eur = 0.92619879594  # Taxa de câmbio atualizada de USD para EUR


# Função para converter salários de USD para EUR usando a taxa de câmbio
def converter_para_eur(row):
    return round(row['salary_in_usd'] * taxa_usd_para_eur)


# Adicionar a coluna "salary_in_eur" ao conjunto de dados convertendo os salários de USD para EUR
dados['salary_in_eur'] = dados.apply(converter_para_eur, axis=1)

# Exibir as primeiras linhas do conjunto de dados com a nova coluna de salário em EUR
print(dados[['salary_in_usd', 'salary_in_eur']].head())

# Selecionar os dados relevantes para análise
dados_selecionados = dados[['work_year', 'job_title', 'job_category', 'salary_in_eur', 'employee_residence',
                            'experience_level', 'employment_type', 'work_setting']]

# Exibir as primeiras linhas do conjunto de dados selecionado
print(dados_selecionados.head())

# Gravar os dados transformados no arquivo especificado
dados_selecionados.to_csv("Transformed_Files/jobs_in_data.csv", index=False)

