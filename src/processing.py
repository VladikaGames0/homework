def filter_by_state(data_list, state='EXECUTED'):
    return [item for item in data_list if item.get('state') == state]