#written by xu yongjie 12/24/2017
class graph():

	class node():
		def __init__(self, k):
		#k is the sequence of the node
			self.k = k
			self.next =  []
			#contain the nodes node k point to and the weight between them
			#[[1, 2], [4, 5]] for example
			#means point to 1 and 4 with weights 2 and 5
			self.former = []
			#contain the former nodes and weights
			
	def read_input(self):
		def one_edge():
			line = input()
			u, v, w = line.split()
			return int(u), int(v), float(w)
		#the first line include num of arcs (m) and nodes (n)
		m, n = [int(i) for i in input().split()] 
		#arcs from the first to the second with weight third num
		arcs = [one_edge() for _ in range(m)]
		return m, n, arcs
			
	def __init__(self):
		self.m, self.n, self.arcs = self.read_input()
		self.nodes = [node(i) for i in range(1, self.n + 1)]
		for arc in self.arcs:
			self.nodes[arc[0] - 1].next.append(arc[1:])
			self.nodes[arc[1] - 1].former.append([arc[0], arc[2]])
			
	def MMC(self):
		record = [[None for i in range(self.n + 1)] for j in range(self.n)]
		paths = [[None for i in range(self.n + 1)] for j in range(self.n)]

		def d(k, w):
			if record[k][w - 1] is not None:
				return record[k][w - 1]
			if k == 0:
				if w == 1:
					return 0
				else:
					return float('inf')
			point = self.node[w - 1]
			choice = [d(k - 1, point.former[i][0]) + point.former[i][1] for i in range(len(point.former))]
			opt = min(choice)
			paths[k][w - 1] = point.former[choice.index(opt)]
			return opt
			
		for v in range(1, self.n +1):
			for k in range(self.n + 1):
				d(k, v)
				
		def maximum(array):
			m = max(array)
			return (m, array.index(m))
		def minimum(array):
			m = min(array)
			return (m, array.index(m))
		u = min([maximum([(record[v][self.n] - record[v][k]) / (self.n - k) for k in range(self.n)]) for v in range(self.n)])
		
		def get_path(k, w):
			path = []
			while True:
				former = paths[k][w - 1]
				path.append((former, w))
				if w == 1 and k == 0:
					break
			return path
				
		large_path = get_path(n, u[1] + 1)
		little_path = get_path(u[0][1], u[1] + 1)
		for l in large_path:
			if l in little_path:
				large_path.remove(l)
		return large_path, u[0][0]

	def MLC(self, s):
		record =[None for i in range(self.n)]
		buckets = [[] for k in range(1, len(self.w))]
		ds = [float('inf') for i in range(n)]
		ds[0] = 0
		def get_path(w, s):
			path = []
			while True:
				former = record[w - 1]
				path.append((former, w))
				if former == s:
					break
			return path
			
		def get_arc(j, s):
			for arc in self.arcs:
				if arc[:1] == [j, s]:
					for i in self.nodes1[j - 1].next:
						if i[0] == s:
							return i[1]
			return float('inf')
		
		def dis_update(i, s):
			for j in self.nodes1[i - 1].next:
				if ds[j[0] - 1] > ds[i - 1] + j[1]:
					old = ds[j[0] - 1]
					ds[j[0] - 1] = ds[i - 1] + j[1]
					record[j - 1] = i
					bucket_update(s, j, old)
		
		def bucket_update(s, j, old):
			k = int(ds(j - 1) / self.lmbd)
			k_old = int(old / self.lmbd)
			if ((k < len(self.w)- 1) and j not in buckets[k - 1]):
				del buckets[old - 1][buckets[old - 1].index(j)]
				buckets[k - 1].append(j)
		
		dis_update(s, s)
		while True:
			for k in range(len(buckets)):
				if buckets[k] != []:
					j = buckets[k][0]
					del buckets[k][0]
					djs = get_arc(j, s)
					if self.mldc > ds[j - 1] + djs:
						self.mldc = ds[j - 1] + djs
						self.w = get_path(w, s)
				update(j, s)
			if k == len(buckets) - 1:
				break
						
	def MLDC(self):
		self.w, self.lmbd = self.MMC()
		self.mldc = cw * len(self.w)
		self.nodes0 = [node(i) for i in range(1, self.n + 1)]
		for arc in self.arcs:
			self.nodes0[arc[0] - 1].next.append([arc[1], arc[2] - self.lmbd])
			self.nodes0[arc[1] - 1].former.append([arc[0], arc[2] - self.lmbd])		
		
		record = [None for i in range(self.n)]
		def p(w):
			if record[w - 1] is not None:
				return record[w - 1]
			if w == 1:
				return 0
			pw = min([p(i[0]) + i[1] for i in self.nodes0[w - 1].former])	
			record[w - 1] = pw
			return pw
		self.nodes1 = [node(i) for i in range(1, self.n + 1)]
		for arc in self.arcs:
			self.nodes1[arc[0] - 1].next.append([arc[1], arc[2] + record[arc[0] - 1] - record[arc[1] - 1]])
			self.nodes1[arc[1] - 1].former.append([arc[0], arc[2] + record[arc[0] - 1] - record[arc[1] - 1]])	