import math
import networkx as nx
import numpy as np
import scipy
import pandas
import pickle
import os

from collections import defaultdict

class Data(object):
    def __init__(self):
        #if not os.path.exists('./pkl_files/'):
        #    os.mkdir(['./pkl_files/'])

    from ._utils import read_csv, seven_day_avg
    from ._graph_utils import compute_eigs, greatest_component, construct_graph, construct_subgraph
    from ._graph_vis import basic_graph_stats, plot_graph_stats, node_importance, plot_graph_snapshot, plot_time_graph
    from ._pnc_access import get_pnc_healthcare_nodes, get_pnc_node_metadata, get_pnc_edge_metadata


if __name__ == '__main__':
    d = Data()
    d.read_csv('fake file')
