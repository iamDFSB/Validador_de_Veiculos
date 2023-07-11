from classes import Executor,Aviao,Car
import os
  
dicionario = Executor.base()

lista_nomes_veiculo = list(dicionario.keys())

#  Loop para o Print da informação
for veiculo in lista_nomes_veiculo:
  tipo = int(input('Digite o tipo do veiculo 1 para [Avião] e 2 para [Carro]: '))
  nome,cor,speed = dicionario[veiculo]
  
  if tipo == 1:
    veiculo = Aviao(nome,cor,speed)
    tipo_name = 'Avião'
    
  elif tipo == 2:
    veiculo = Car(nome,cor,speed)
    tipo_name = 'Carro'
  
  else:
    raise Exception('Esse valor não é permitido apenas 1 para [Avião] e 2 para [Carro]')
  
  try:
    nome_lista, cor_lista, speed_lista, tipo_lista = Executor.join_to_list(nome,cor,speed,tipo_name)
    veiculo.chave_liga()
    veiculo.chave_desligou()
  except:
    print('Não deu certo tente novamente')
  else:
    print('🙏....Success....🙏')

  print(' ')
  print('.'*20)

# Verifica o comprimento das listas e ajusta se necessário
os.system('cls') 

# Print do dataframe
print('Hora da Tabela :)')
df_final = Executor.criar_df(nome_lista, cor_lista, speed_lista, tipo_lista)
print(df_final)

# Output para arquivo csv
Executor.export_df(df_final,'tabela_tipada')