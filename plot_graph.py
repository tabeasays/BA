import retrieve_data
import networkx as nx
import matplotlib.pyplot as plt


def networkx_plot(graph):
    networkx_graph = graph.to_networkx()

    pos = retrieve_data.set_coords(graph)
    node_labels = retrieve_data.node_labels(graph)
    node_color = list(retrieve_data.nx_node_color(graph))
    regular_edges, variant_edges, signal_edges, init_met_edge, other_edges, trypsin_edges, regular_cleaved_edges,\
        variant_cleaved_edges, following_vars_edges = retrieve_data.nx_edge_color(graph)

    print("Kanten, die übergeben werden: ", regular_edges)
    regulars = nx.DiGraph()
    regulars.add_edges_from(regular_edges)

    variants = nx.DiGraph()
    variants.add_edges_from(variant_edges)
    signals = nx.DiGraph()
    signals.add_edges_from(signal_edges)
    init_mets = nx.DiGraph()
    init_mets.add_edges_from(init_met_edge)
    trypsins = nx.DiGraph()
    trypsins.add_edges_from(trypsin_edges)
    others = nx.DiGraph()
    others.add_edges_from(others)
    reg_cleaved = nx.DiGraph()
    reg_cleaved.add_edges_from(regular_cleaved_edges)
    var_cleaved = nx.DiGraph()
    var_cleaved.add_edges_from(variant_cleaved_edges)
    following_vars = nx.DiGraph()
    following_vars.add_edges_from(following_vars_edges)

    print("Kanten, die im Graph enthalten sind: ", regulars.edges.data())

    fig, ax = plt.subplots()
    # ax.xaxis.set_view_interval(0, 8, True)
    # Draw nodes and edges
    nx.draw_networkx_nodes(networkx_graph,
                           pos,
                           node_color=node_color,
                           node_shape='o')
    nx.draw_networkx_edges(regulars,
                           pos,
                           edge_color='b',
                           arrows=True)
    nx.draw_networkx_edges(variants,
                           pos,
                           edge_color="green",
                           arrows=True,
                           connectionstyle="arc3,rad=0.3")
    nx.draw_networkx_edges(signals,
                           pos,
                           edge_color="red",
                           arrows=True,
                           connectionstyle="arc3,rad=0.3")
    nx.draw_networkx_edges(trypsins,
                           pos,
                           edge_color="orange",
                           arrows=True,
                           connectionstyle="arc3,rad=0.3")
    nx.draw_networkx_edges(others,
                           pos,
                           edge_color="brown",
                           arrows=True,
                           connectionstyle="arc3,rad=0.3")
    nx.draw_networkx_edges(init_mets,
                           pos,
                           edge_color="yellow",
                           arrows=True,
                           connectionstyle="arc3,rad=0.3")
    nx.draw_networkx_edges(reg_cleaved,
                           pos,
                           edge_color="blue",
                           arrows=True,
                           style="dotted",
                           connectionstyle="arc3,rad=0.3")
    nx.draw_networkx_edges(var_cleaved,
                           pos,
                           edge_color="green",
                           arrows=True,
                           style="dotted",
                           connectionstyle="arc3,rad=0.3")
    nx.draw_networkx_edges(following_vars,
                           pos,
                           edge_color="green",
                           arrows=True,
                           connectionstyle="arc3,rad=0.3")
    nx.draw_networkx_labels(networkx_graph,
                            pos,
                            labels=node_labels)
  #  ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
#    ax.set_xlim(left=-2, right=9)
 #   ax.set_ylim(bottom=-2, top=9)
   # fig.tight_layout()
    plt.savefig("plot.png", dpi=1500, bbox_inches='tight')



def networkx_plot_regualar(graph):

    pos, nx_graph = retrieve_data.set_regular_coords(graph)
    nodes_list = list(nx_graph.nodes)
    node_labels = retrieve_data.regular_node_labels(graph, nodes_list)
    node_color = retrieve_data.regular_node_colors(graph, nodes_list)
    graphy = graph.to_networkx()
    for i in range(0, len(graph.vs)):
        if i not in nodes_list:
            graphy.remove_node(i)

    fig, ax = plt.subplots()

    nx.draw_networkx_nodes(nx_graph,
                           pos,
                           node_color= node_color,
                           node_shape='o')
    nx.draw_networkx_labels(nx_graph,
                            pos,
                            labels=node_labels)
    nx.draw_networkx_edges(graphy,
                           pos,
                           edge_color='DeepSkyBlue')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.savefig("plot.png", dpi=1500, bbox_inches='tight')