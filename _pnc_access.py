# pnc_access.py
# Includes PNC-specific functions (using extraneous ids)
# Author: Catalina Vajiac

def get_pnc_healthcare_nodes(self):
    ''' get all nodes with HEALTHCARE segment or lob '''
    hc_nodes = set()
    for attrbute in ['segment', 'lob']:
        for s in ['source', 'target']:
            attr = '{}_{}'.format(s, attribute)
            id_ = '{}_id'.format(s)
            nodes = set(self.df[self.df[attr] == 'HEALTHCARE'][id_].values)
            hc_nodes.update(nodes)


def get_pnc_node_metadata(s, row):
    industry = row['{}_industry'.format(s)]
    lob = row['{}_lob'.format(s)]
    segment = row['{}_segment'.format(s)]
    return {'industry': industry, 'lob': lob, 'segment': segment}


def get_pnc_edge_metadata(row):
    id_ = row['transaction_id']
    amount = row['transaction_amount']
    type_ = row['payment_type']
    return {'id': id_, 'amount': amount, 'type': type_}


if __name__ == '__main__':
    d = Data()
