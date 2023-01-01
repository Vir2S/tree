def build_tree(source):
    tree = {}

    for parent, offspring in source:

        if parent not in tree:
            tree[parent] = {}

        if offspring not in tree:
            tree[offspring] = {}

        tree[parent][offspring] = tree[offspring]

    return tree[None]


def test_build_tree():
    source = [
        (None, 'a'),
        (None, 'b'),
        (None, 'c'),
        ('a', 'a1'),
        ('a', 'a2'),
        ('a2', 'a21'),
        ('a2', 'a22'),
        ('b', 'b1'),
        ('b1', 'b11'),
        ('b11', 'b111'),
        ('b', 'b2'),
        ('c', 'c1'),
    ]

    expected = {
        'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
        'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
        'c': {'c1': {}},
    }

    assert build_tree(source) == expected


test_build_tree()
