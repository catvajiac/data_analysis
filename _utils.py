# _utils.py
# Other necessary utilities
# Author: Catalina Vajiac

import pandas

def read_csv(self, filename, date_str='trans_date', source_str='source_id', target_str='target_id'):
    ''' import data and keep track of dates '''
    self.df = pandas.read_csv(filename)
    self.date_str = date_str
    self.date_range = sorted(self.df[self.date_str].unique())
    self.filename = os.path.basename(filename)


def seven_day_avg(self, stat):
    ''' given lst of nums, return 7-day moving average '''
    avg, lst = [], []
    for s in stat:
        if len(lst) >= 7:
            lst.pop(0)
        lst.append(s)
        avg.append(sum(lst) / len(lst))

    return avg


if __name__ == '__main__':
    d = Data()
