# 🔍 Buscador de Caminho Inteligente com Obstáculos e Regras Especiais usando o algoritmo A*

Este projeto implementa uma busca de caminho em um cenário 2D com regras específicas, utilizando **Python (Flask)** no backend e **HTML/CSS/JS** no frontend.

## 🚀 Sobre o Projeto

Você controla um personagem (`C`) que deve alcançar a saída (`S`) em um cenário repleto de obstáculos:

### Legenda:
- `C` - Começo (posição inicial do personagem)
- `S` - Saída (objetivo final)
- `_` - Caminho livre
- `B` - Barreira intransponível (só pode passar após pegar a fruta)
- `F` - Fruta que permite ultrapassar barreiras
- `A` - Meia-barreira (custo 2)

O algoritmo de busca encontra o caminho mais curto possível, considerando os custos e regras acima.

---

## 🧠 Lógica Utilizada

- Algoritmo de busca com heurística de **distância de Manhattan**.
- Utiliza a técnica A* simplificada para encontrar o menor caminho.
- Considera estados como posição atual, custo, e se o personagem já pegou a fruta (`tem_fruta`).

---

## 💻 Tecnologias

- Python 3.x
- Flask
- HTML + CSS (com estilo pastel)
- JavaScript (fetch API)

---
