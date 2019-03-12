""" Contains class Node """


class Node(object):
    """ Create a node """

    def __init__(self, name, parent=''):
        """ Creates a node """

        # string with wiki subject name
        self.name = name

        # parent node name
        self.parent = parent

    def __str__(self):
        return self.name
