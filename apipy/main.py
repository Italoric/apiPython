from models.grafo import Grafo
from fastapi import FastAPI


app = FastAPI()

Banco_de_Dados = []

@app.post("/grafo")
def add_Grafo(novo_grafo: Grafo):
    Banco_de_Dados.append(novo_grafo)
    return novo_grafo

@app.get("/grafo")
def list_grafo():
    return Banco_de_Dados