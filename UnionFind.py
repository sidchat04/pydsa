#!/bin/python3

class UnionFind:
    def __init__(self):
        self.ranks = {}
        self.parents = {}
        self.size = 0
    def create(self, object):
        self.parents[object] = object
        self.ranks[object] = 0
        self.size = self.size + 1
    def find(self, object):
        if object not in self.parents:
            self.create(object)
            return object
        if self.parents[object] != object:
            self.parents[object] = self.find(self.parents[object])
        return self.parents[object]
    def union(self, object1, object2):
        parent1 = self.find(object1)
        parent2 = self.find(object2)
        if parent1 == parent2:
            return
        if self.ranks[parent1] > self.ranks[parent2]:
            self.parents[parent2] = parent1
        else:
            self.parents[parent1] = parent2
            if self.ranks[parent1] == self.ranks[parent2]:
                self.ranks[parent2] = self.ranks[parent2] + 1
        self.size = self.size - 1
    def same_parent(self, object1, object2):
        if self.find(object1) == self.find(object2):
            return True
        else:
            return False
