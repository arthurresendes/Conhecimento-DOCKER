# Linguagem ou framework utilizado
FROM node 

# Cria a pasta app e roda o container dentro dela, todos comandos seguintes rodam no app
WORKDIR /app

# Copiar o que precisa para executar, no caso o package.json, o * faz pegar os dois package, e o . joga para dentro do app
COPY package*.json .

# Roda o package.json
RUN npm install

#  Copia todos os restantes dos arquivos para dentro do container
COPY . .

# Expor a porta que será executada
EXPOSE 3000

# Roda o node e o arquivo executavel é o app.js, poderia ser ["python", "main.py"] se fosse em python
CMD ["node", "app.js"]