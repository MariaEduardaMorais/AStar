from flask import Flask, request, jsonify
from flask_cors import CORS
import copy

app = Flask(__name__)
CORS(app)

class Node:
    def __init__(self, pos, distancia_percorrida=0, fe=0, caminho=None, tem_fruta=False):
        self.pos = pos
        self.distancia_percorrida = distancia_percorrida
        self.fe = fe
        self.caminho = caminho if caminho else []
        self.tem_fruta = tem_fruta

def funcao_heuristica(pos_atual, pos_saida):
    return abs(pos_atual[0] - pos_saida[0]) + abs(pos_atual[1] - pos_saida[1])

def custo_movimento(cenario, pos_atual, pos_proxima, tem_fruta):
    char = cenario[pos_proxima[0]][pos_proxima[1]]
    if char == 'B' and not tem_fruta:
        return float('inf')
    elif char == 'A':
        return 2
    else:
        return 1

def get_min(estados):
    if not estados:
        return None
    melhor = min(estados, key=lambda e: e.fe)
    estados.remove(melhor)
    return melhor

@app.route('/resolver', methods=['POST'])
def resolver():
    data = request.get_json()
    cenario = data['cenario']

    pos_inicial = None
    pos_saida = None

    for i in range(len(cenario)):
        for j in range(len(cenario[0])):
            if cenario[i][j] == 'C':
                pos_inicial = (i, j)
            elif cenario[i][j] == 'S':
                pos_saida = (i, j)

    if not pos_inicial or not pos_saida:
        return jsonify({'erro': 'Posição inicial (C) ou final (S) não encontrada'}), 400

    estados = []
    pai = Node(pos=pos_inicial)
    final = None
    visitados = set()

    while True:
        movimentos = [(0,1), (1,0), (0,-1), (-1,0)]
        for dx, dy in movimentos:
            nova_pos = (pai.pos[0] + dx, pai.pos[1] + dy)
            if 0 <= nova_pos[0] < len(cenario) and 0 <= nova_pos[1] < len(cenario[0]):
                if nova_pos in pai.caminho:
                    continue
                custo = custo_movimento(cenario, pai.pos, nova_pos, pai.tem_fruta)
                if custo < float('inf'):
                    tem_fruta_novo = pai.tem_fruta or cenario[nova_pos[0]][nova_pos[1]] == 'F'
                    filho = Node(
                        pos=nova_pos,
                        distancia_percorrida=pai.distancia_percorrida + custo,
                        fe=pai.distancia_percorrida + custo + funcao_heuristica(nova_pos, pos_saida),
                        caminho=copy.deepcopy(pai.caminho),
                        tem_fruta=tem_fruta_novo
                    )
                    filho.caminho.append(pai.pos)
                    estados.append(filho)

        pai = get_min(estados)
        if pai is None:
            return jsonify({'mensagem': 'Não foi possível encontrar um caminho até a saída.'})
        if pai.pos == pos_saida:
            final = pai
            break

    return jsonify({
        'mensagem': 'Caminho encontrado!',
        'caminho': final.caminho + [final.pos],
        'custo': final.distancia_percorrida
    })

if __name__ == '__main__':
    app.run(debug=True)
