import json
locations = [ # we might retrieve these from an API or DB
    ('Athlone','ie'),
    ('Galway','ie'),
    ('Hull','uk'),
    ('Canberra','aus'),
    ('Berlin','de'),
    ('Budapest', 'hu'),
    ('Madrid','es')
]

l_str = json.dumps(locations)

print(l_str, type(l_str))