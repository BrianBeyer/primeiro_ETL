import pandas as pd

#Extrai as informacoes de um arquivo csv com o id, nome e um espaco para mensagem
#Insere uma mensagem para cada usuario
#Atualiza o arquivo salvando-o com a mensagem

#Extract
df = pd.read_csv(r'C:\Users\bbpim\OneDrive\Desktop\Python\usuarios.csv')

lista_usuarios= []

for indice, linha in df.iterrows():
    user_id = linha['id']
    name = linha['name']

    user_dict = {
        'id': user_id,
        'name': name,
        'news': []  
    }

    lista_usuarios.append(user_dict)

print(lista_usuarios)

#Transform
for user in lista_usuarios:
    mensagem = (input(f"Entre com a mensagme para o(a) {user['name']}: "))
    user['news'].append(mensagem)
print(lista_usuarios)

# Update
mensagens = [user['news'][0] for user in lista_usuarios]
df['mensagem'] = mensagens
df.to_csv(r'C:\Users\bbpim\OneDrive\Desktop\Python\usuarios.csv', index=False)
print("Arquivo 'usuarios.csv' atualizado com sucesso!")
print(df.head())


