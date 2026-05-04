# 💧Controle de Níveis de Água💧

## 🔎Objetivo
Criei este programa com o objetivo de simular um sistema simples de monitoriamneto de controle de níveis de água em reservatório.
Será aprensentado no código, cinco diferentes níveis (1 a 5), cada um deles representado com uma cor, para melhorar no entendimento do código.
- 🔴 Nível 1: Muito baixo (crítico)
- 🟡 Nível 2: Baixo
- 🟢 Nível 3: Médio
- 🧊 Nível 4: Alto
- 🔵 Nível 5: Muito alto (alerta)
Ao final, o sistema irá retornar a situação do reservatório.

## ⚙️ Estrutura
- Colorama: Uso da biblioteca para manipular as cores no terminal;
- Lista (mensagens): Estrutura que guarda os níveis de água, cada um com três informaçõe (Prefixo, Situação, Cor);
- Função (def exibir_mensagem): Recebe um nível e mostra a mensagem correspondente, garantindo que o valor esteja dentro do intervalo válido.
- For: Repete de 1 a 5 para exibir todas as mensagens de níveis;
- If/else: Verifica se o nível informado está dentro do intervalo permitido (1 a 5);
 
## 💻 Linguagem Utilizada
![python](https://img.shields.io/badge/language-python-black?style=flat&logo=python&logoColor=3776AB&labelColor=white&color=3776AB)