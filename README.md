# Visualizador de Algoritmo A*

Este projeto é uma implementação interativa e visual do algoritmo de busca de caminho A* (A-Star). Ele utiliza um backend em Python com Flask para a lógica do algoritmo e um frontend em HTML/CSS/JavaScript para a visualização e interação com o usuário, criando uma experiência de aprendizado dinâmica e engajante.

![image](https://github.com/user-attachments/assets/34d26700-e30e-4807-aa97-22ceae5fc119)
![image](https://github.com/user-attachments/assets/bd4a1a24-791f-4487-9e92-09ff9fd81bae)

## ✨ Funcionalidades Principais

-   **Editor de Cenário Interativo:** Crie seus próprios desafios clicando e desenhando no grid.
-   **Implementação do A*:** O backend calcula o caminho de menor custo entre o ponto inicial e final.
-   **Regras Complexas de Travessia:** A lógica vai além do simples "obstáculo". O personagem precisa coletar "frutas" para atravessar certos tipos de barreiras.
-   **Animação Visual Fluida:** Assista ao personagem percorrer o caminho calculado em tempo real, com movimentos suaves entre as células.
-   **Custo de Movimento Variável:** Diferentes tipos de terreno (como a água) possuem custos de movimento maiores.
-   **Arquitetura Cliente-Servidor:** Demonstração clara da separação de responsabilidades entre o backend (lógica) e o frontend (apresentação).

## 📜 Regras do Algoritmo

O cenário é composto por diferentes tipos de células, cada uma com um comportamento específico:

| Emoji | Elemento | Código | Custo | Regra de Travessia |
| :---: | :--- | :---: | :---: | :--- |
| 😀 | **Início** | `C` | 1 | Ponto de partida do personagem. |
| 🏁 | **Saída** | `S` | 1 | Objetivo final do personagem. |
| 🍎 | **Fruta** | `F` | 1 | Ao passar, o personagem coleta a fruta (incrementa o contador em 1). |
| 🧱 | **Barreira** | `B` | 1 | Só pode ser atravessada se o personagem possuir ao menos 1 fruta. Ao atravessar, 1 fruta é consumida. |
| 💧 | **Água** | `A` | 2 | Pode ser atravessada com ou sem fruta, mas possui um custo total de 2.

A regra principal é **"uma fruta, uma barreira"**. Cada fruta coletada permite atravessar um único obstáculo (`B` ou `A`).

## 🛠️ Tecnologias Utilizadas

-   **Backend:**
    -   ![Python](https://img.shields.io/badge/python-3.10+-blue.svg?style=for-the-badge&logo=python)
    -   ![Flask](https://img.shields.io/badge/flask-2.2.2-black.svg?style=for-the-badge&logo=flask)
-   **Frontend:**
    -   ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
    -   ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
    -   ![JavaScript](https://img.shields.io/badge/javascript-%23F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=black)
