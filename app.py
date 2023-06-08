import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pessoa import Pessoa
from pessoaDTO import PessoaDTO


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/registros")
def listar_registros():
    return Pessoa.listar()

@app.post("/api/registros")
def adicionar_registro(dto: PessoaDTO):
    pessoa = Pessoa.salvar(vars(dto))
    
    return f'Pessoa {pessoa.to_dict()} salva com sucesso!'
