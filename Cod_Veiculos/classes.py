from time import sleep
import pandas as pd

# Cria Classe Base para printar as informações
class Veiculo:
  def __init__(self,nome,cor,speed):
      self.nome = nome
      self.cor = cor
      self.speed = speed
  
  def liga(self):
      sleep(1)
      print("Ligou")
      sleep(1)
      print(f'Nome === {self.nome}')
      print(f'Cor === {self.cor}')
      print(f'Velocidade === {self.speed}km/h')
      
  def desligou(self):
      sleep(1)
      print("Desligou")
      
  
# Cria a Classe Avião
class Aviao(Veiculo):
  def __init__(self,nome,cor,speed):
     self.nome = nome
     self.cor = cor
     self.speed = speed
     super().__init__(self.nome,self.cor,self.speed)
    
  def chave_liga(self):
     super().liga()
    
  def chave_desligou(self):
     super().desligou()

# Cria a Classe Carro
class Car(Veiculo):
   def __init__(self,nome,cor,speed):
     self.nome = nome
     self.cor = cor
     self.speed = speed
     super().__init__(self.nome,self.cor,self.speed)
     
   def chave_liga(self):
     super().liga()
     
   def chave_desligou(self):
     super().desligou()

# Cria a Classe para executar os comandos
class Executor:

  # Criação do Dataframe
  @staticmethod
  def criar_df(nome_lista, cor_lista, speed_lista, tipo_lista):
     df = pd.DataFrame({
      'Nome':nome_lista,
      'Cor':cor_lista,
      'Velocidade':speed_lista,
      'Tipo': tipo_lista,
    })  
     return df
  
  @staticmethod
  def export_df(df,nome):
     arquivo = df.to_csv(f'{nome}.csv')
     return arquivo
  
  # Base para inserir os tipos
  @staticmethod
  def base(): 
    # Dicionario com os dados
    dicionario = {
      'veiculo1':['Volvo','Vermelho','200'],
      'veiculo2':['Celta','Verde','120'],
      'veiculo3':['Jaguar','Preto','300'],
    }
    return dicionario

  # Retornar listas para df
  nome_lista = []
  cor_lista = []
  speed_lista = []
  tipo_lista = []

  @classmethod
  def join_to_list(cls,nome,cor,speed,tipo_name):
     
     cls.nome_lista.append(nome)
     cls.cor_lista.append(cor)
     cls.speed_lista.append(speed)
     cls.tipo_lista.append(tipo_name)

     return cls.nome_lista, cls.cor_lista, cls.speed_lista, cls.tipo_lista