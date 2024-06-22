import numpy as np
from random import random, randint
from copy import deepcopy
from queue import PriorityQueue


class Graph:
	def __init__(self, graph=None):
		if graph is None:
			graph = {}
		self.graph = graph
		self.weighted = False

	def __str__(self):
		res = ""
		for v in self.graph:
			res += f"{v}:"
			for u in self.graph[v]:
				res += f" {u}"
			res += "\n"
		return res
	
	@staticmethod
	def random_graph(nodes_num: int, prob: float, weighed: bool = False):
		"""
		Generates a random graph provided a number of nodes and probability of generating an edge.
		"""
		rand_graph = Graph()
		for i in range(1, nodes_num + 1):
			rand_graph.add_node(i)
			for j in range(1, i):
				if random() < prob:
					weight = randint(1, 10)
					rand_graph.add_edge([i, j], weight)
		return rand_graph

	def add_node(self, node):
		"""
		Adds a node to a graph.
		"""
		if node not in self.graph:
			self.graph[node] = []

	def del_node(self, node):
		"""
		Recursively removes a node from a graph.
		"""
		if node in self.graph:
			self.graph.pop(node)
			for key in [*self.graph.keys()]:
				if node in self.graph[key]:
					self.graph[key].remove(node)

	def add_arc(self, arc: list):
		"""
		Adds arc to a graph provided a list of nodes.
		"""
		u, v = arc
		self.add_node(u)
		self.add_node(v)
		if v not in self.graph[u]:
			self.graph[u].append(v)

	def add_edge(self, edge: list, weight: int):
		"""
		Adds edge to a graph provided a list of nodes.
		"""
		u, v = edge
		if u == v:
			raise ValueError("Pętla!")
		self.add_node(u)
		self.add_node(v)
		if v not in self.graph[u]:
			self.graph[u].append((v, weight))
		if u not in self.graph[v]:
			self.graph[v].append((u, weight))

def MinSpanningTree(graph: Graph):
	"""
	Algorytm Jarnika-Prima -- minimalne drzewa spinające
	Dla nieskierowanych grafów ważonych (wagi to liczby całkowite)
	Zwraca parę (waga, drzewo), gdzie waga to łączna waga drzewa
	a drzewo to minimalne drzewo spinające w formie grafu ważonego
	"""
	if not graph.weighted: # jak graf nie jest ważony - zwróć nic
		return None, None
	for v in graph.graph: # wybieram jakiś wierzchołek  grafu
		break
	tree = {v:[]}       # zalążek drzewa
	weight = 0          # łączna waga
	q = PriorityQueue() # pusta kolejka priorytetowa
	for (u, w) in graph.graph[v]:
		q.put((int(w), v, u))
	while not q.empty():
		(w, v, u) = q.get()
		if u not in tree:
			weight += w
			tree[u] = [(v, w)]
			tree[v].append((u, w))
			for (x, w) in graph.graph[u]:
				if not x in tree:
					q.put((int(w), u, x))
	if len(tree) < len(graph.graph):
		print("Graf niespójny - zwrócone drzewo dla jednej składowej")
	wtree = Graph(tree)
	wtree.weighted = True
	return wtree
