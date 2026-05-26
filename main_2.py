# import pandas as pd
# df = pd.read_excel("planilhao.xlsx", sheet_name= "FLRY3")
# df
# #Seleciona as colunas Cona que tenham o valor
# filtro = df["Conta"] == "EBIT"
# df.columns
# colunas = ['20254T', '20252T',
#        '20251T', '20244T', '20243T', '20242T', '20241T', '20234T', '20233T',
#        '20232T', '20231T', '20224T', '20223T', '20222T', '20221T', '20214T',
#        '20213T', '20212T', '20211T', '20204T', '20203T', '20202T', '20201T',
#        '20194T', '20193T', '20192T', '20191T', '20184T', '20183T', '20182T',
#        '20181T', '20174T', '20173T', '20172T', '20171T', '20164T', '20163T',
#        '20162T', '20161T', '20154T']
# colunas = sorted (colunas)
# ebit = df [filtro][colunas].iloc[0]

# import seaborn as sn
# sn.lineplot(ebit)
# sn.histplot(ebit)
# sn.boxplot(ebit)


# import pandas as pd
# df = pd.read_excel("planilhao.xlsx", sheet_name= "FLRY3")
# df
# filtro = df ["Conta"] == "Lucro Líquido"
# df.columns
# colunas = ['20254T', '20252T',
#        '20251T', '20244T', '20243T', '20242T', '20241T', '20234T', '20233T',
#        '20232T', '20231T', '20224T', '20223T', '20222T', '20221T', '20214T',
#        '20213T', '20212T', '20211T', '20204T', '20203T', '20202T', '20201T',
#        '20194T', '20193T', '20192T', '20191T', '20184T', '20183T', '20182T',
#        '20181T', '20174T', '20173T', '20172T', '20171T', '20164T', '20163T',
#        '20162T', '20161T', '20154T']
# colunas = sorted (colunas)
# lucro_liq = df [filtro][colunas].iloc[0]

# import seaborn as sn
# sn.lineplot(lucro_liq)
# sn.histplot(lucro_liq)
# sn.boxplot(lucro_liq)



# # 2. Calculando o Lucro Bruto (Receita - Custos)
# df['Lucro_Bruto'] = df['Receita'] - df['Custos']

# # 3. Calculando o Lucro Líquido (Lucro Bruto - Impostos)
# df['Lucro_Liquido'] = df['Lucro_Bruto'] - df['Impostos']

# # 4. Somando o total da coluna para saber o lucro final do período
# total_lucro = df['Lucro_Liquido'].sum()










# import pandas as pd
# import seaborn as sn
# import matplotlib.pyplot as plt

# df=pd.read_excel("planilhao.xlsx",sheet_name="Sheet1")
# df.columns
# #grafico de barras
# plt.figure(figsize=(10,6)) #tamanho da figra do grafico
# sn.countplot(data=df, x="setor", 
#              order=df["setor"].value_counts().index,
#              palette="viridis")
# plt.title("Grafico de Barras por Setor")
# plt.xlabel("Numero de empresas")
# plt.ylabel("Setor")
# plt.xticks(rotation=45)
# plt.show()


# #horizontal
# df=pd.read_excel("planilhao.xlsx",sheet_name="Sheet1")
# df.columns
# #grafico de barras
# plt.figure(figsize=(10,6)) #tamanho da figra do grafico
# sn.countplot(data=df, y="setor", 
#              order=df["setor"].value_counts().index,
#              palette="viridis")
# plt.title("Grafico de Barras por Setor")
# plt.xlabel("Numero de empresas")
# plt.ylabel("Setor")
# plt.xticks(rotation=45)
# plt.show()

# #Grafico de pizza
# setor=df["setor"].value_counts()
# cores=sn.color_palette("Blues_r", len(setor))
# plt.figure(figsize= (10,6)) #tamanho do grafico
# plt.pie(setor,
#         labels=setor.index,
#         autopct="%1.1f%%",
#         startangle=140,
#         colors=cores,
#         pctdistance=0.4, #afasta porcentagem do centro
#         wedgeprops={'linewidth':3, 'edgecolor': 'white'})
# plt.show()
# #Grafico de Histograma
# filtro =df['setor'] == 'saúde'
# df_setor = df[filtro]
# sn.histplot(df_setor['roe'], bins=20, kde= True, color='blue')


