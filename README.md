# Docker

---

## Como rodar — caminho curto
1. Construir imagem a partir do Dockerfile:
   - docker build -t meuapp:latest .
2. Rodar container:
   - docker run --rm -it -p 8000:8000 --name meuapp meuapp:latest
3. Com docker-compose (se houver docker-compose.yml):
   - docker compose up --build
   - docker compose down --volumes

---

## Comandos Docker essenciais (rápido)
- Listar containers: docker ps
- Listar todos (incl. parados): docker ps -a
- Parar: docker stop <container>
- Iniciar: docker start <container>
- Remover container: docker rm <container> (use -f para forçar)
- Listar imagens: docker image ls
- Remover imagem: docker image rm <image> (use -f para forçar)
- Construir imagem: docker build -t nome:tag .
- Rodar imagem: docker run --name nome -p host:container -e VAR=valor nome:tag
- Entrar em container em execução: docker exec -it <container> /bin/bash
- Ver logs: docker logs -f <container>
- Copiar arquivo para/fora do container: docker cp src container:/dest
- Inspecionar: docker inspect <container|image>
- Limpeza: docker system prune -a (cuidado — remove imagens e containers não usados)

---

## Comandos importantes por stack

1) Dockerfile (princípios e comandos)
- Construir:
  - docker build -t meuapp:1.0 .
- Construir com build-arg:
  - docker build --build-arg ENV=prod -t meuapp:1.0 .
- Forçar sem cache:
  - docker build --no-cache -t meuapp:latest .
- Multistage (recomendado para binários/Python static): usar `FROM ... AS build` e depois copiar artefatos.
- Expor porta e healthcheck no Dockerfile:
  - EXPOSE 8000
  - HEALTHCHECK --interval=30s CMD curl -f http://localhost:8000/health || exit 1

Boas práticas:
- Usar .dockerignore
- Ordernar camadas para aproveitar cache (instalar deps antes de copiar código variável)
- Usar imagens oficiais leves (python:3.11-slim, node:18-alpine)

2) docker-compose.yml
- Subir em background:
  - docker compose up -d --build
- Ver logs:
  - docker compose logs -f servicename
- Rodar um comando numa service:
  - docker compose exec servicename bash
- Parar e remover volumes:
  - docker compose down --volumes --remove-orphans
- Reconstruir imagens sem cache (compose):
  - docker compose build --no-cache

3) Python (app-python)
- Dockerfile exemplo (multi-stage):
  - FROM python:3.11-slim AS base
    WORKDIR /app
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    COPY . .
    CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
- Comandos úteis:
  - docker build -t my-python-app:latest app-python/
  - docker run --rm -p 8000:8000 -e ENV=dev -v $(pwd)/app-python/src:/app/src my-python-app:latest
  - Em dev: monte o código e instale deps no container ou use volumes + reloader (uvicorn --reload)

4) Node.js / JavaScript (app-node)
- Dockerfile comum:
  - FROM node:18-alpine
    WORKDIR /app
    COPY package*.json ./
    RUN npm ci --only=production
    COPY . .
    CMD ["node", "index.js"]
- Comandos:
  - docker build -t my-node-app:latest app-node/
  - docker run --rm -p 3000:3000 my-node-app:latest
- Para dev: usar volumes, npm run dev, ou docker compose com nodemon

5) PHP (app-php)
- Composer no Dockerfile:
  - FROM php:8.1-fpm
    WORKDIR /var/www/html
    COPY composer.json composer.lock ./
    RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
    RUN composer install --no-dev --no-scripts --no-interaction
- Comandos:
  - docker build -t my-php-app:latest app-php/
  - docker run --rm -p 9000:9000 my-php-app:latest
- Se usar Nginx/PHP-FPM, combine serviços no docker-compose

6) Hack / HHVM
- Se houver código Hack, base image pode ser `hhvm/hhvm` (ou imagem oficial compatível)
- Exemplo de build:
  - docker build -t my-hack-app:latest app-hack/
- Rodar HHVM dev server conforme docs do HHVM

---

## Exemplos práticos

1) Build + run simples
- docker build -t minha-aplicacao:dev .
- docker run --rm -it -p 8080:8080 -e APP_ENV=dev --name minha-aplicacao minha-aplicacao:dev

2) Debug / shell
- docker run --rm -it --entrypoint /bin/bash minha-aplicacao:dev
- docker exec -it minha-aplicacao /bin/bash

3) Com docker-compose (multi-serviço)
- docker compose up --build --detach
- docker compose exec web python manage.py migrate
- docker compose logs -f

4) Remover tudo (cuidado)
- docker compose down --volumes
- docker system prune -af


---

## Stacks:

<a href="https://github.com/arthurresendes/Conhecimento-DOCKER"><img src="https://skillicons.dev/icons?i=docker" alt="Docker" height="48"></a>
