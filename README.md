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
- Rodar imagem: docker run --name nome -p host:container --name nomecontainer nomeimage:tag
- Ver logs: docker logs -f <container>
- Copiar arquivo para/fora do container: docker cp src container:/dest
- Inspecionar: docker inspect <container|image>
- Limpeza: docker system prune -a (— remove imagens e containers não usados)

---

## Comandos importantes por stack

1) Dockerfile
- Construir:
  - docker build -t meuapp:1.0 .
- Construir com build-arg:
  - docker build --build-arg ENV=prod -t meuapp:1.0 .
- Forçar sem cache:
  - docker build --no-cache -t meuapp:latest .

2) docker-compose.yml
- Subir em background:
  - docker compose up -d --build
- Ver logs:
  - docker compose logs -f servicename
- Parar e remover volumes:
  - docker compose down --volumes --remove-orphans
- Reconstruir imagens sem cache (compose):
  - docker compose build --no-cache


---

## Stacks:

<a href="https://github.com/arthurresendes/Conhecimento-DOCKER"><img src="https://skillicons.dev/icons?i=docker" alt="Docker" height="48"></a>
