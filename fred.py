# import pandas as pd
# df = pd.read_excel("planilhao.xlsx", sheet_name= "BIOM3")
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