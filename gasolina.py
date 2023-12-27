import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv('gasolina.csv')
print(f'Dataframe criado com sucesso, contendo {gasolina_df.shape[0]} linhas e {gasolina_df.shape[1]} séries.')

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=gasolina_df, marker='o', color='b', label='Preço da Gasolina')

plt.title('Preço da Gasolina ao Longo do Tempo')
plt.xlabel('Dia')
plt.ylabel('Preço (US$)')

plt.legend()

plt.savefig('gasolina.png')

plt.show()
