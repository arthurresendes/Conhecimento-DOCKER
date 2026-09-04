from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def rota_base():
    return {'Nome': 'Projeto 04/09/2026'}

@app.get("/lista_funcionarios")
async def lista_funcionarios():
    return {'Funcionarios': ['Jose', 'Maria', 'Gustavo']}

if __name__ == "__main__":
    uvicorn.run("app:app",host="0.0.0.0", port=8080)