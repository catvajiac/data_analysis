# _graph_vis.py
# For visualization of graph attributes (subgraphs, etc)
# Author: Catalina Vajiac

import networkx as nx
from collections import defaultdict


def basic_graph_stats(self):
    ''' gather data for easy-to-compute stats '''
    graph_stats = defaultdict(list)
    for i, graph in enumerate(self.graph_snapshots):
        graph_stats['density'].append(nx.density(graph))
        first, second = self.compute_eigs(graph, k=2)
        graph_stats['first_eval'].append(first)
        graph_stats['second_eval'].append(second)
        graph_stats['gcc'].append(len(greatest_component))
        graph_stats['#cc'].append(len(nx.weakly_connected_components(graph)))
        graph_stats['#nodes'].append(graph.number_of_nodes())
        graph_stats['#edges'].append(graph.number_of_edges())

    return graph_stats


def plot_graph_stats(self, graph_stats, filename):
    ''' plot graph stats: expects dict of {name, data} pairs '''
    for name, stat in graph_stats.items():
        ax = plt.axes()
        ticker.Locator.MAXTICKS = 2100
        ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
        plt.xticks(rotation=70, fontsize=10)
        plt.plot(self.date_range, stat, label=name)
        plt.plot(self.date_range, self.seven_day_avg(stat), label='{} 7-day avg'.format(name))
        plt.legend()
        plt.xlabel('Time')
        plt.xlabel('Value')
        plt.tight_layout()
        plt.savefig('./plots/{}-{}_plots.png'.format(filename, name))
        plt.show()


def node_importance(self, graph, k=0.8):
    ''' return nodes that contribute to top k% of degrees '''
    degree = lambda g, n: len(set(list(g.in_edges(n)) + list(g.out_edges(n))))

    total_edges = len(graph.edges())
    if not total_edges:
        return set()

    scores = sorted([(degree(graph, n) / total_edges, n) for n in graph])
    total = sum(score[0] for score in scores)
    important_nodes = set()
    curr_score = 0
    for score, node in scores:
        if not score:
            continue
        if curr_score >= k*total:
            break
        curr_score += score
        important.add(node)

    return important


def plot_graph_snapshot(self, graph):
    pass

def plot_time_graph(self, graphs):
    pass


if __name__ == '__main__':
    d = Data()
