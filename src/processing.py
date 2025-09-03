def filter_by_state(data_list, state='EXECUTED'):
    return [item for item in data_list if item.get('state') == state]


def sort_by_date(sort_data_list, descending=True):
    return sorted(sort_data_list, key=lambda x: x.get('date'), reverse=descending)