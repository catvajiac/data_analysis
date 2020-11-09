# _utils.py
# Other necessary utilities
# Author: Catalina Vajiac

import pandas

def read_csv(self, filename, date_str='trans_date', source_str='source_id', target_str='target_id'):
    ''' import data and keep track of dates '''
    self.df = pandas.read_csv(filename)
    self.date_str = date_str
    self.date_range = sorted(self.df[self.date_str].unique())
    self.date_to_index = {dat: i for i, dat in enumerate(self.date_range)}
    self.index_to_date = {i: dat for i, dat in enumerate(self.date_range)}
    self.source = source_str
    self.target = target_str 
    self.weight = 'transaction_amount'
    self.filename = os.path.basename(filename)
    self.nodes = set(self.data[self.source].unique())
    self.nodes.update(set(self.data[self.target].unique()))


def seven_day_avg(self, stat):
    ''' given lst of nums, return 7-day moving average '''
    avg, lst = [], []
    for s in stat:
        if len(lst) >= 7:
            lst.pop(0)
        lst.append(s)
        avg.append(sum(lst) / len(lst))

    return avg


def subset(self, data, node):
    ''' return any relevant rows from data to node '''
    return data[(data[self.source] == node) | (data[self.target] == node)]


if __name__ == '__main__':
    d = Data()
