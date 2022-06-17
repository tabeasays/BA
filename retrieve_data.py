import igraph
import networkx as nx


def sortNodes(graph):
    nodes_list = {}
    count = 0
    for i in range(0, len(graph.vs)):
        #print(count)
        attr = graph.vs[i].attributes()
        pos = attr["position"]
        amino = attr["aminoacid"]
        dicty = dict(zip(str(pos), amino))
       # nodes_list.append(dicty)
        if pos == None:
            nodes_list[1000+count] = i
            count += 1
            continue
        nodes_list[pos] = i
    #print(nodes_list)
    res = {key: val for key, val in sorted(nodes_list.items(), key=lambda ele: ele[0])}
    #print(res)
    return res



def setEdgeColors(graph):
    networkx_graph = graph.to_networkx()
    edge_color = {}
    #print(graph)
    for x in range(0, len(graph.vs)):
        edge_data = graph.vs[x].out_edges()
        #print(edge_data)
        if not graph.vs[x].out_edges(): continue
        c = 0
        for y in range(0, len(graph.vs)):
            if networkx_graph.has_edge(x, y):
                #print("exists: ", x, y)
                #if not edge_data[c]['qualifiers']: continue
               # print("vor None ",c, len(edge_data))
                if c < len(edge_data):
                    if not edge_data[c]['qualifiers']:
                        #print("x: ", x, "y: ", y)
                        #print("NONE")
                        edge_color[x, y] = 'b'
                        c += 1
                        continue

                if c < len(edge_data):
                    if edge_data[c]['qualifiers'] == None:
                        #print("x: ", x, "y: ", y)
                        #print("NONE")
                        edge_color[x, y] = 'b'
                        c += 1
                        continue

                if c < len(edge_data):
                    if edge_data[c]['qualifiers'][0].type == 'SIGNAL':
                        #print("x: ", x, "y: ", y)
                        #print("SIGNAL")
                        edge_color[x, y] = 'r'
                        c += 1
                        continue

                if c < len(edge_data):
                    if edge_data[c]['qualifiers'][0].type == 'INIT_MET':
                        #print("x: ", x, "y: ", y)
                        #print("INIT_MET")
                        edge_color[x, y] = 'yellow'
                        c += 1
                        continue

                if c < len(edge_data):
                    if edge_data[c]['qualifiers'][0].type == 'VARIANT':
                        #print("x: ", x, "y: ", y)
                        #print("VAR")
                        edge_color[x, y] = 'g'
                        c += 1
                        continue

                if c < len(edge_data):
                    if edge_data[c]['qualifiers'][0].type == 'TRYPSIN':
                        #print("x: ", x, "y: ", y)
                        #print("TRYPSIN")
                        edge_color[x, y] = 'orange'
                        c += 1
                        continue

                else:
                    edge_color[x, y] = 'brown'
                    #print("x: ", x, "y: ", y)
                    #print("else")
                    c += 1


    #print(edge_color)
    return edge_color




def set_coords(graph):
    networkx_graph = graph.to_networkx()
    nodes_dict = sortNodes(graph)
    node_positions = {}
    nodes_list = list(nodes_dict)
    #print(nodes_dict)
    #print(nodes_list)
    j = 0
    node_positions[0] = (0, 0)
    for i in nodes_list:
        if i >= 1000: continue
        position = nodes_dict[i]
        node_positions[position] = (j, 0)
        j += 1


    counter = 0
    for i in range(1, len(graph.vs)):
        if i not in node_positions:
            for j in range(0, len(graph.vs)):
                if networkx_graph.has_edge(j, i):
                    for c in range(0, len(graph.vs[i].out_edges())):
                        if graph.vs[i].out_edges()[c]:
                            if graph.vs[i].out_edges()[c].attributes()["qualifiers"]:
                                pos = list(graph.vs[i].out_edges()[c].attributes()["qualifiers"][0].location)[0]
                                node_positions[i] = (pos, 1)

                    counter += 1
   # print("POSIS: ", node_positions)
    node_positions[8] = (5, 1)
    return node_positions

def node_labels(graph):
    node_labels = {}
    node_labels[0] = "s"
    for i in range(1, len(graph.vs)):
        node_attr = graph.vs[i].attributes()
        if node_attr["aminoacid"] == "__end__":
            node_labels[i] = "e"
        else:
            node_labels[i] = node_attr["aminoacid"]

    return node_labels

def node_edge_color(graph):
    node_edge_color = {}
    node_edge_color[0] = "r"

    for i in range(1, len(graph.vs)):
        node_attr = graph.vs[i].attributes()
        if node_attr["aminoacid"] == "__end__":
            node_edge_color[i] = "r"
        else:
            node_edge_color[i] = "darkseagreen"

    return node_edge_color

def node_color(graph):
    node_color = {}
    node_color[0] = "palegreen"

    for i in range(1, len(graph.vs)):
        node_attr = graph.vs[i].attributes()
        if node_attr["aminoacid"] == "__end__":
            node_color[i] = "palegreen"
        else:
            node_color[i] = "palegreen"

    return node_color

def edge_layout(graph, edge_color):
    edge_layout = {}
    es = igraph.EdgeSeq(graph)
    for e in graph.es:
        if edge_color[e.tuple] == 'b':
            edge_layout[e.tuple] = 'straight'
        else:
            edge_layout[e.tuple] = 'curved'
    print('EDGE_LAYOUT: ', edge_layout)

    return edge_layout

def nx_node_color(graph):
    node_color = []
    node_color.insert(0, "lightpink")

    for i in range(1, len(graph.vs)):
        node_attr = graph.vs[i].attributes()
        if node_attr["aminoacid"] == "__end__":
            node_color.insert(i, "lightpink")
        else:
            node_color.insert(i, "lightblue")

    return node_color

def nx_edge_color(graph):
    networkx_graph = graph.to_networkx()
    regular_edges = []
    variant_edges = []
    signal_edges = []
    init_met_edge = []
    other_edges = []
    trypsin_edges = []
    regular_cleaved_edges = []
    variant_cleaved_edges = []
    following_vars = []

    for x in range(0, len(graph.vs)):
        edge_data = graph.vs[x].out_edges()
        if not graph.vs[x].out_edges(): continue
        c = 0
        for y in range(0, len(graph.vs)):
            if networkx_graph.has_edge(x, y):
                if c < len(edge_data):
                    if not edge_data[c]['qualifiers']:
                        if edge_data[c]['cleaved']:
                            regular_cleaved_edges.append((x, y))
                        if not edge_data[c]['cleaved']:
                            regular_edges.append((x, y))
                        c += 1
                        continue

                if c < len(edge_data):
                    if edge_data[c]['qualifiers'] == None:
                        regular_edges.append((x, y))
                        c += 1
                        continue

                if c < len(edge_data):
                    if edge_data[c]['qualifiers'][0].type == 'SIGNAL':
                        signal_edges.append((x, y))
                        c += 1
                        continue

                if c < len(edge_data):
                    if edge_data[c]['qualifiers'][0].type == 'INIT_MET':
                        init_met_edge.append((x, y))
                        c += 1
                        continue

                if c < len(edge_data):
                    if edge_data[c]['qualifiers'][0].type == 'VARIANT':
                        if networkx_graph.has_edge(x, y):
                            if edge_data[c]['cleaved']:
                                variant_cleaved_edges.append((x, y))
                            else: variant_edges.append((x, y))
                            c += 1
                            continue

                if c < len(edge_data):
                    if edge_data[c]['qualifiers'][0].type == 'PEPTIPE':
                        trypsin_edges.append((x, y))
                        c += 1
                        continue

                else:
                    other_edges.append((x, y))
                    c += 1

    return regular_edges, variant_edges, signal_edges, init_met_edge, other_edges, trypsin_edges, regular_cleaved_edges, variant_cleaved_edges, following_vars

def set_regular_coords(graph):

    nx_graph = nx.DiGraph()
    coords = {}
    coords[0] = (0, 0)
    nx_graph.add_node(0)
    for i in range(1, len(graph.vs)):
        attr = graph.vs[i].attributes()
        print("ATTR: ", attr)
        if attr["position"]:
            pos = attr["position"]
            coords[i] = (pos, 0)
            nx_graph.add_node(i)
    return coords, nx_graph

def regular_node_labels(graph, nodes_list):
    node_labels = {}
    node_labels[0] = "s"
    for i in range(1, len(graph.vs)):
        if i in nodes_list:
            node_attr = graph.vs[i].attributes()
            if node_attr["aminoacid"] == "__end__":
                node_labels[i] = "e"
            else:
                node_labels[i] = node_attr["aminoacid"]
    return node_labels

def regular_node_colors(graph, nodes_list):
    node_color = []
    node_color.insert(0, "lightpink")

    for i in range(1, len(graph.vs)):
        if i in nodes_list:
            node_attr = graph.vs[i].attributes()
            if node_attr["aminoacid"] == "__end__":
                node_color.insert(i, "lightpink")
            else:
                node_color.insert(i, "DeepSkyBlue")

    return node_color

