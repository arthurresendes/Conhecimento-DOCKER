from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def rota_base():
    return {'Message': 'sucesss'}

@app.get('/nome/{nome}')
def retorna_nome(nome: str):
    return {'nome': nome}

if __name__ == '__main__':
    uvicorn.run('main:app',host='0.0.0.0', port=8080, reload=True)