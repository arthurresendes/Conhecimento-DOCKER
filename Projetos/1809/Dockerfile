FROM node:20.14

WORKDIR /app

RUN npm init -y && npm install express

COPY api.js . 

EXPOSE 3000

CMD ["node", "api.js"]