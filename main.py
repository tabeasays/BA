import PIL
from pywebio.input import input
from pywebio.output import put_text
from igraph import Graph
import pywebio
import open_file
import plot_graph
from PIL import Image
import time
import pickle


def plot():

    data = pywebio.input.input_group("ProteinPlot", [
        input('Enter protein', name='protein'),
        pywebio.input.select(label="Choose Filetype", options=["PNG (static)","FILETYPE (interactive)"], name='choice'),
        pywebio.input.select(label="Select elements to show", options=["regular graph", "show variants and signals"], name='elements',
                               value=["regular graph", "variants"])
    ], validate=next_step)

def next_step(data):

  #  protein = input("Enter Protein")
   # pywebio.input.select(label="choice", options=["PNG (static)","FILETYPE (interactive"])
   # put_text("Plotting "+protein+"...")

    protein = data['protein']

    graph = open_file.open_pickle("exported_graphs/"+protein+".pickle")
    [__start_node__] = graph.vs.select(aminoacid="__start__")
    [__stop_node__] = graph.vs.select(aminoacid="__end__")

    with pywebio.output.put_loading().style('shape:grow; width:5rem; height:5rem; position:1'):
        time.sleep(3)  # Some time-consuming operations
        if data['elements'] == 'regular graph':
            print("HERE: ", data['elements'])
        if data['elements'] == 'regular graph':
            plot_graph.networkx_plot_regualar(graph)
        else:
            plot_graph.networkx_plot(graph)

        image = PIL.Image.open(r'plot.png')
        content = open('plot.png', 'rb').read()
        pywebio.output.put_image(image, title="Plot of Protein")
        pywebio.output.put_file('plot.png', content, 'Download as PNG')

   # pywebio.output.put_success("Done")

if __name__ == '__main__':
    #plot()
    pywebio.start_server(plot, port=80)
