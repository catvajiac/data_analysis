#!/bin/env python3
# Author: Catalina Vajiac
# Discover churn nodes in dataset

import math
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn')


def find_churn_nodes(self, data):
    ''' find nodes that decreased in weight, # unique neighbors, # interactions '''
    def is_lower_n_days(lst, n=90):
        if len(lst) < n:
            return False
        return sum(lst) / len(lst) * 0.2 > sum(lst[-n:]) / len(lst[-90:])

    churn_nodes = set()
    for node in self.nodes:
        subset = self.subset(data, nodes)
        
        weight, neighbors, interactions= [], [], []
        for dat in self.dates:
            date_subset = data[data[self.date] == dat]
            weight.append(date_subset[self.weight].sum())
            neighbors.append(len(date_subset))
            interactions.append(len(date_subset[self.target].unique()))

        if sum([is_lower_n_days(lst) for lst in (weight, neighbors, interactions)]):
            churn_nodes.add(user)

    return churn_nodes


def filter_churn_nodes(self, nodes, data):
    ''' nodes must have sufficient # interactions & weight '''
    filtered_nodes = set()
    for node in nodes:
        subset = self.subset(data, node)
        if len(subset[self.date].unique()) < 50:
            continue

        if subset[self.weight].sum() < 10000:
            continue

        filtered_nodes.add(node)

    return filtered_nodes


def plot_matrix(self, nodes, data):
    ''' given nodes, visualize $ amount transacted as a matrix '''
    matrix = np.zeros(len(nodes), len(self.dates))

    node_to_index = {node: i for i, node in enumerate(nodes)}
    for node in nodes:
        subset = data[(data[self.source] == node) | (data[self.target] == node)]
        
        for dat in self.dates:
            date_subset = data[data[self.date] == dat]
            matrix[node_to_index[node], self.date_to_index[dat]] += row[self.weight]


    plt.imshow(np.log(m), aspect='auto')
    plt.colorbar()
    plt.show()

    return matrix


def plot_churn_nodes(self, nodes, data, mode='$amt'):
    ''' plot first 9 churn nodes time series.
        mode can be $amt, neighbors, transactions '''
    if mode == '$amt':
        aggregator = lambda df: df[self.weight].sum()
    elif mode == 'neighbors':
        aggregatgor = lambda df: len(df[self.target].unique())
    elif mode == 'transactions':
        aggregator = lambda df: len(df)
    else:
        raise "Pick a supported mode ('$amt', 'neighbors', 'transactions')"


    # gen time series
    time_series = defaultdict(lambda: [0 for dat in self.dates])
    for node in nodes:
        subset = self.subset(data, node)
        
        for dat in self.dates:
            date_subset = data[data[self.date] == dat]
            time_series[source] = aggregator(date_subset)
            time_series[target] = aggregator(date_subset)


    # actual plotting
    fig, axes = plt.subplots(nrows=3, ncols=3, sharex=True, figsize=(20, 12))
    axes = [ax for row in axes for ax in row]


    for ax, node in zip(axes, nodes):
        ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
        ax.xaxis.set_major_locator(ticker.MultipleLocator(100))
        ax.tick_params('x', labelrotation=70)
        ax.plot(self.dates, time_series[node])

    fig.suptitle(mode)
    plt.show()
