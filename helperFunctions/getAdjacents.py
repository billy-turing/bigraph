def getAdj2(graph, input_list, n):
    """

    :param graph: NetworkX graph object
    :param input_list: Input list
    :param n: Hop N
    :return: N hop neighbours of the input list's items
    """
    full_list = []
    while (n > 0):
        n -= 1
        output_list = []
        for node in graph.nbunch_iter(input_list):
            for neigh in graph[node]:
                if neigh not in full_list:
                    full_list.append(neigh)
                    output_list.append(neigh)
    return output_list
