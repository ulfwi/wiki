""" Contains class Tree """
from node import Node

class Tree(object):
    """ Creates a tree containing nodes """

    def __init__(self):
        """ Creates a tree containing nodes """
        # list containing all nodes
        self.node_list = []

    def add_node(self, name, parent_name=''):
        """ Creates a node with parent """

        node = Node(name, parent_name)
        self.node_list.append(node)

        return node

    def create_child(self, child_name, parent_node):
        """ Creates a child node with parent_node as a parent """
        return self.add_node(child_name, parent_node.name)

    def find(self, name):
        """ Finds a node with the name 'name' """
        for node in self.node_list:
            if node.name == name:
                return node

        return None

    def get_ancestors_list(self, node):
        """ Returns a list with all ancestors, oldest first """

        parent = node.parent
        ancestor_list = [parent]
        while parent != '':
            parent = self.find(parent).parent
            ancestor_list.insert(0, parent)

        return ancestor_list

    def get_ancestors_str(self, node):
        """ Returns a string with all ancestors, oldest first """

        ancestor_list = self.get_ancestors_list(node)
        ancestors_str = ''
        if len(ancestor_list) > 1:
            for name in ancestor_list[1:]:
                # check if it contains .html (offline names only)
                if '.html' in name:
                    # remove parts of file path (find three first /) and .html
                    split_list = name.split('/')
                    name = split_list[-1][:-len('.html')]

                ancestors_str += name + '/'

        if '.html' in node.name:
            # remove parts of file path (find three first /) and .html
            split_list = node.name.split('/')
            ancestors_str += split_list[-1][:-len('.html')]
        else:
            ancestors_str += node.name

        return ancestors_str
