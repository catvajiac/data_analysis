# _graph_utils.py
# Basic utilities for graph functionality
# Author: Catalina Vajiac

import networkx as nx
import scipy


def compute_eigs(self, graph, k=2):
    ''' return first k eigenvalues, sorted by largest first '''
    A = nx.to_scipy_sparse_matrix(graph).asfptype()
    return sorted(scipy.sparse.linalg.eigs(A, k=k)[0], reverse=True)


def greatest_component(self, graph):
    ''' return largest connected component '''
    max(nx.connected_components(graph.to_undirected()), key=len)


def construct_graph(self, node_metadata, edge_metadata):
    ''' from dataframe, create time-evolving graph (list of DiGraphs) '''
    dates_dict = {d: i for i, d in enumerate(self.date_range)}
    self.graph_snapshots = []
    for _, row in self.df.iterrows():
        date_index = dates_dict[row[self.date_str]]
        s = row[source_str]
        t = row[target_str]
        
        g = nx.DiGraph()
        g.add_node(s, **node_metadata('source', row))
        g.add_node(t, **node_metadata('target', row))
        g.add_edge(s, t, **edge_metadata(row))

    pickle.dump('{}-total_graph.pkl'.format(self.filename))


def construct_subgraph(self, filtered_nodes):
    ''' given nodeset to filter, return appropriate subgraph snapshots 
        assumes construct_graph has already been called'''
    return [graph(filtered_nodes) for graph in self.graph_snapshots]


if __name__ == '__main__':
    d = Data()
