""" Utils"""

import datetime

def datetime_serializer(dt):
    if isinstance(dt, datetime.datetime):
        return dt.__str__()

def find_all_key_values(dict_list_path, ktf, keys=None, values=None):
    if values == None:
        values = []
    if keys == None:
        keys = []
    for index, key_index in enumerate(dict_list_path):
        if isinstance(dict_list_path, dict):
            ref = key_index
        elif isinstance(dict_list_path, list):
            # ref = dict_list_path.index(key_index)
            ref = index
        value = dict_list_path[ref]
        if key_index == ktf:
            values.append((keys + [key_index], value))
        if isinstance(value, (dict, list)):
            keys.append(ref)
            find_all_key_values(value, ktf, keys, values)
            keys.pop()
    return values


def get_key_value(dict_list, key):
    values_found = find_all_key_values(dict_list, key)
    if len(values_found) == 1:
        return values_found[0][1]
    else:
        raise ValueError(f'Warning - Found {len(values_found)} values - {values_found}')


dict_3 = [{'a': 1, 'x': [{'z': '222'}, {'y': 100}], 'b': 2, 'c': {'d': 3, 'e': [{'f': 4, 'y': 5}, {'h': 6, 'i': 7}]}},
          {'aa': 1, 'bb': 2, 'cc': {'dd': 3, 'ed': [{'bf': 4, 'jg': 5},
                                                    {'hj': [{'bvf': 404, 'jvg': 5}, {'hnj': 16, 'ibi': 89}],
                                                     'ii': 77}]}}]

if __name__ == "__main__":
    print(find_all_key_values(dict_3, 'bvf'))
    print(find_all_key_values(dict_3, 'y'))
    print(get_key_value(dict_3, 'bvf'))
