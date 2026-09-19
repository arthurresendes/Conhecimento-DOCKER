const express = require("express");

const app = express();
const PORT = 3000;

app.use(express.json());

app.get("/", (req, res) => {
  res.json({ mensagem: "Olá! Sua API com Express está funcionando." });
});

app.get("/api", (req, res) => {
  res.json({ mensagem: "Rota base das APIS." });
});

app.get("/api/users", (req, res) => {
  res.json({ users: ["Arthur", "Davi", "Matheus"] });
});

app.listen(PORT, () => {
  console.log(`Servidor rodando com sucesso na porta ${PORT}`);
});
