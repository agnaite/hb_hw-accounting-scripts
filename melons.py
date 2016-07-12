def add_classification(classification):
    for melon in melons:
        melons[melon][classification] = melons[melon].get(classification, None)


melons = {
    "Honeydew": {"price": 0.99, "seedlessness": True},
    "Crenshaw": {"price": 2.00, "seedlessness": False},
    "Crane": {"price": 2.50, "seedlessness": False},
    "Casaba": {"price": 2.00, "seedlessness": False},
    "Cantaloupe": {"price": 0.99, "seedlessness": False}
    }

add_classification("flesh_color")
add_classification("weight")
add_classification("rind_color")
