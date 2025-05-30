from flask import Flask, request, jsonify
from flask_cors import CORS
import copy

app = Flask(__name__)
CORS(app)

class Node:
    def __init__(self, pos, distancia_percorrida=0, fe=0, caminho=None, num_frutas=0):
        self.pos = pos
        self.distancia_percorrida = distancia_percorrida
        self.fe = fe
        self.caminho = caminho if caminho else []
        self.num_frutas = num_frutas

    def __hash__(self):
        return hash((self.pos, self.num_frutas))

    def __eq__(self, other):
        return isinstance(other, Node) and self.pos == other.pos and self.num_frutas == other.num_frutas

def funcao_heuristica(pos_atual, pos_saida):
    return abs(pos_atual[0] - pos_saida[0]) + abs(pos_atual[1] - pos_saida[1])

def custo_movimento(cenario, pos_proxima, num_frutas):
    char = cenario[pos_proxima[0]][pos_proxima[1]]
    
    if (char == 'B' or char == 'A') and num_frutas == 0:
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
    visitados = set()

    no_inicial = Node(pos=pos_inicial, fe=funcao_heuristica(pos_inicial, pos_saida), num_frutas=0)
    estados.append(no_inicial)
    visitados.add((no_inicial.pos, no_inicial.num_frutas))
    
    final = None

    while estados:
        pai = get_min(estados)

        if pai.pos == pos_saida:
            final = pai
            break

        movimentos = [(0,1), (1,0), (0,-1), (-1,0)]
        for dx, dy in movimentos:
            nova_pos = (pai.pos[0] + dx, pai.pos[1] + dy)

            if 0 <= nova_pos[0] < len(cenario) and 0 <= nova_pos[1] < len(cenario[0]):
                
                custo = custo_movimento(cenario, nova_pos, pai.num_frutas)
                if custo == float('inf'):
                    continue

                char_proximo = cenario[nova_pos[0]][nova_pos[1]]
                num_frutas_novo = pai.num_frutas
                if char_proximo == 'F':
                    num_frutas_novo += 1
                elif char_proximo == 'B' or char_proximo == 'A':
                    num_frutas_novo -= 1
                
                if (nova_pos, num_frutas_novo) in visitados:
                    continue

                distancia = pai.distancia_percorrida + custo
                heuristica = funcao_heuristica(nova_pos, pos_saida)
                
                novo_caminho = copy.deepcopy(pai.caminho)
                novo_caminho.append(pai.pos)
                
                filho = Node(
                    pos=nova_pos,
                    distancia_percorrida=distancia,
                    fe=distancia + heuristica,
                    caminho=novo_caminho,
                    num_frutas=num_frutas_novo
                )
                
                estados.append(filho)
                visitados.add((filho.pos, filho.num_frutas))

    if final:
        return jsonify({
            'mensagem': 'Caminho encontrado!',
            'caminho': final.caminho + [final.pos],
            'custo': final.distancia_percorrida
        })
    else:
        return jsonify({'mensagem': 'Não foi possível encontrar um caminho até a saída.'})

if __name__ == '__main__':
    app.run(debug=True)