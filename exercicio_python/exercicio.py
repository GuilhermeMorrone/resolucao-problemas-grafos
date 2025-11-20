
# Trabalho de Grafos - DFS e Detecção de Ciclos

#  Implementação de Grafo usando Lista de Adjacência
# Inclui:
#  1. Busca em Profundidade (DFS)
#   2. Detecção de Ciclos usando DFS


class Grafo:
    def __init__(self, num_vertices):
        # quantidade de vértices
        self.V = num_vertices
        # cria um dicionário onde cada vértice tem uma lista de vizinhos
        self.adj = {i: [] for i in range(num_vertices)}

    def adicionar_aresta(self, u, v):
        """
        Adiciona uma aresta entre u e v.
        Aqui estamos considerando um grafo NÃO-DIRECIONADO.
        Se o grafo fosse direcionado, bastaria remover a segunda linha.
        """
        self.adj[u].append(v)
        self.adj[v].append(u)

    # 1. DFS PADRÃO

    def dfs(self, inicio, visitados=None):
        """
        Executa a Busca em Profundidade (DFS).
        imprime a ordem de visita.
        """
        if visitados is None:
            visitados = set()

        visitados.add(inicio)
        print(inicio, end=" ")

        # visita os vizinhos ainda não visitados
        for vizinho in self.adj[inicio]:
            if vizinho not in visitados:
                self.dfs(vizinho, visitados)

   
    # 2. DETECÇÃO DE CICLOS (usando DFS)

    def ha_ciclo(self):
        """
        Verifica se o grafo contém ciclo.
        Chama a função recursiva _dfs_ciclo.
        """
        visitados = set()

        for v in range(self.V):
            if v not in visitados:
                if self._dfs_ciclo(v, visitados, parent=-1):
                    return True

        return False

    def _dfs_ciclo(self, atual, visitados, parent):
        """
        Função recursiva para detectar ciclos.
        Se encontrarmos um vizinho já visitado e que não é o pai,
        então existe um ciclo.
        """
        visitados.add(atual)

        for viz in self.adj[atual]:
            if viz not in visitados:
                if self._dfs_ciclo(viz, visitados, atual):
                    return True
            elif viz != parent:
                # Encontrou um vizinho visitado que não é o pai → ciclo
                return True

        return False


if __name__ == "__main__":
    g = Grafo(5)

    # adicionando algumas arestas
    g.adicionar_aresta(0, 1)
    g.adicionar_aresta(1, 2)
    g.adicionar_aresta(2, 3)
    g.adicionar_aresta(3, 1)  # essa cria um ciclo (1-2-3-1)
    g.adicionar_aresta(3, 4)

    print("DFS a partir do vértice 0:")
    g.dfs(0)

    print("\n\nO grafo possui ciclo?")
    print("Sim" if g.ha_ciclo() else "Não")
