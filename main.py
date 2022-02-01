from mimetypes import init
from unicodedata import name
import numpy as np
import json

class Tree:
    
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.size = data['size']

    def get_data(self) -> dict:
        tree = {
            self.id : {
                "name": self.name,
                "size": self.size
            }
        }
        return tree

    def __str__(self) -> str:
        return json.dumps(self.get_data())

class Terrain:

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass

class TreeRegister ():

    def __init__(self) -> None:
        self.register = []
        self.id_register = []

    def add_tree (self, tree:Tree) -> None:
        if type(tree) is Tree:
            if tree not in self.register:
                self.register.append(tree)
                self.id_register.append(tree.id)
        else:
            raise TypeError("Only 'Tree' can be added to the register.")

    def get_tree (self, id) -> dict:
        if id in self.id_register:
            return self.register[self.id_register.index(id)]
        else:
            raise ValueError("Tree not in register.")


class Forest:

    def __init__(self, size:int, environment_temperature:list, tree_list:list, terrain:Terrain) -> None:
        self.size = size
        self.env_temp = environment_temperature
        self.trees = self.init_trees(tree_list)

    def init_trees (tree_list) -> dict:
        """
        Initialize the trees in the forest based on a given list of tree
        """
        trees = {}
        for tree in tree_list:
            trees[tree] = 1
        return trees

    def add_tree(self, tree:Tree) -> None:
        if type(tree) is Tree:
            if tree in self.trees:
                self.trees[tree] += 1
            else:
                self.trees[tree] = 1
        else:
            raise TypeError("Only 'Tree' can be added to the register.")



if __name__ == "__main__":
    ecosia = Tree({"id":"eco10","name":"ecosia","size":10})
    print(ecosia)