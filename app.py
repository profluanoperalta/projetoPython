import json

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def ler_arquivo():  
    with open('registros.json', 'r') as dados:
        try:
            return list(json.load(dados))
        except:
            return []









@app.get("/")
def ola_mundo():
    return "Ola Mundo"







@app.get("/")
def listar_registros():
    
    
    
    registros = ler_arquivo()

    if not registros:
        return {"message": "Nenhum registro encontrado"}
    
    return registros


@app.post("/api/registros")
def adicionar_registro(nome: str = Body(...), nascimento: str = Body(...)):
    registros = ler_arquivo()

    novo_registro = {"nome": nome, "nascimento": nascimento}
    registros.append(novo_registro)

    with open('registros.json', 'w') as dados:
        dados.write(json.dumps(registros, indent=4))
