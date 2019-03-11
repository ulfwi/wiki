""" Contains class Node """


class Node(object):
    """ Create a node and add it to a node tree """

    # list containing all nodes
    node_list = []

    def __init__(self, name, parent=''):
        """ Creates a node and adds it to the node_list """
        self.name = name  # string with wiki subject name
        self.parent = parent  # parent node name
        Node.node_list.append(self)

    def create_child(self, child_name):
        """ Creates a child node with this node as a parent """
        child = Node(child_name, self.name)
        Node.node_list.append(child)
        return child

    @staticmethod
    def find(name):
        """ Finds a node with the name 'name' """
        for node in Node.node_list:
            if node.name == name:
                return node

        return None

    def get_ancestors_list(self):
        """ Returns a list with all ancestors, oldest first """
        parent = self.parent
        ancestor_list = [parent]
        while parent != '':
            parent = Node.find(parent).parent
            ancestor_list.insert(0, parent)

        return ancestor_list

    def get_ancestors_str(self):
        """ Returns a string with all ancestors, oldest first """
        ancestor_list = Node.get_ancestors_list(self)
        ancestors_str = ''
        if len(ancestor_list) > 1:
            for name in ancestor_list[1:]:
                # check if it contains .html (offline names only)
                if '.html' in name:
                    # remove parts of file path and .html
                    name = name[6:-5]
                ancestors_str += name + '/'

        if '.html' in self.name:
            # remove parts of file path and .html
            ancestors_str += self.name[6:-5]
        else:
            ancestors_str += self.name

        return ancestors_str

    def __str__(self):
        return Node.get_ancestors_str(self)
