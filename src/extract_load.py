#import
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

#import das variaveis de ambiente 
commodities = ['CL=F', 'GC=F', 'SI=F']

def buscar_dados_commodities(simbolo, periodo='5y', intevalo='1d'):
  ticker = yf.Ticker('CL=F')
  dados=ticker.history(period=periodo, interval=intevalo)[['Close']]
  dados['simbolo'] = simbolo
  return dados

def buscar_todos_dados_commodities():
  todos_dados = []
  for simbolo in commodities:
    dados = buscar_dados_commodities(simbolo)
    todos_dados.append(dados)
  return pd.concat(todos_dados)

if __name__ == "__main__":
  dados_concatenados =  buscar_todos_dados_commodities()
  print(dados_concatenados)
  
#pega a cotação dos meus ativos

#concatenar meus ativos (1..2..3 => 1)

#salvar no bdd