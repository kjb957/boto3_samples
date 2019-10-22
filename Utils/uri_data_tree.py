uris = ['/home/apple/red/cookie',
'/home/apple/red/brownie',
'/home/orange/red/brownie',
'/away/pear/red/pie',
'/away/pear/blue/pie']

def create_tree_dict(uris):
    '''Create a nested dictionary where the path section of a URI is a key
       and its value is a dict containing the next path section or empty.
    '''
    tree_dict = {}
    for uri in uris:
        paths = uri.split('/')
        # first entry is an empty string and is discarded
        paths.pop(0)
        path_ref = tree_dict
        for path in paths:
            # if the key does not exist add the key with a value of an empty dict
            # subsequent paths will fill this empty dict with key value(dict) pairs
            path_ref.setdefault(path, {})
            # advance the path pointer to the new dict created
            path_ref = path_ref[path]
    return tree_dict



def print_tree(d, indent=0):
    '''Recursively run through the nested dictionary and print out the contents
    '''
    for key, value in d.items():
        # if not empty then print a dash
        if d[key]:
            dash = '-'
        else:
            dash = ''
        print('\t' * indent + dash + str(key))
        if isinstance(value, dict):
            print_tree(value, indent+1)
        else:
            print('\t' * (indent+1) + str(value))


tree_dict = create_tree_dict(uris)            
print(tree_dict)

print()            
print_tree(tree_dict)
