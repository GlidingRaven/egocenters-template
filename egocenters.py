import networkx as nx


def find_impostor(newedges, newpseudocenters):
    G = nx.Graph()
    G.add_edges_from(newedges)
    
    neighbors = {el:list(G.neighbors(el)) for el in newpseudocenters}
    
    for el in newpseudocenters:
        pseudocenters_without_el = [ell for ell in newpseudocenters if ell != el]

        # список альтеров всех егоцентров, кроме рассматриваемого
        all_neighbors_of_egos = list(set([value for key in pseudocenters_without_el for value in neighbors.get(key, [])]))

        # счётчик, что альтер является чужим альтером
        cnt_ngh_is_other_ngh = 0

        # проверяем всех альтеров
        for neigh in neighbors[el]:
            if neigh in all_neighbors_of_egos:
                cnt_ngh_is_other_ngh += 1

        if len(neighbors[el]) == cnt_ngh_is_other_ngh:
            return el
        
    return None
