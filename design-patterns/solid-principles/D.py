"""
D stands for Dependency Inversion
==> High Level Modules should not depend on Low Level Modules, rather on their Abstraction
"""
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name

class Relationship:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT,child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0] == name and r[1] == Relationship.PARENT:
                yield r[2].name

class Research:
    def __init__(self, relationships):
        self.relations = relationships.relations

