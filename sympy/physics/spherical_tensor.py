from sympy import symbols, var

"""
This module defines spherical tensors that are used in nuclear physics

T^{k}_{q} = Spherical Tensor of rank k, with sub-index q
q = -k,-k+1, ..., 0, ..., k-1, k

"""

# This Node Class will contain the information required by the Spherical Tensor
class Node:
	
	def __init__(self, k,q,T):
		# The left and rights hand side of the Binary Tree
		self.l = None
		self.r = None
		
		# The values stored inside the Node
		self.k = k # The rank of the Tensor
		self.q = q # The index of the Tensor
		self.name = T # The name of the Tensor
    
    # This prints off the information in the Node as a tensor
	def print_node(self):
		print str(self.name)+ "^{"+str(self.k)+"}_{"+str(self.q)+"}"
	
	def node_string(self):
		return str(self.name)+ "^{"+str(self.k)+"}_{"+str(self.q)+"}"
		
	def node_rank_string(self):
		return str(self.name)+"^{"+str(self.k)+"}"
	
	
# Here we need to define the Spherical Tensor class
# The implementation of the data structure will be a binary tree
class SphericalTensor:

    # This is the class constructor
    # k -> The rank of the tensor
    # q -> the index of the tensor
    # name -> The symbol that will represent the tensor of choice
	
	# The data structure of a tensor should be a binary tree
    # We should check that the |q| <= k
	def __init__(self, k, q, T):
	    
	    # This is the rank of the Tree
	    self.k = k
	    self.q = q
	    self.name = T
	    self.length=1
	    self.transformations = 0
	    
	    # We initialize the root of the Tree structure
	    self.root = Node(k,q,T)
	    
	def set_root_right(self,T):
		self.root.r = T.root
	
	def set_root_left(self,T):
		self.root.l = T.root
	
	def set_root_name(self,new_name):
		self.root.name = new_name
	
	def print_length(self):
		return self.length
	
	# This function gets the root of the binary tree
	def get_root(self):
		return self.root
	
	def print_root(self):
		return self.root.print_node()
		
	# This function couples two tensors together	
		
	# This function should add a node to the Binary Tree Data
	def add(self,k,q,T):
		self.length=self.length+1
		
		# If the root is null, then create a new Tensor as the root
		if self.root == None:
			node.r = Node(k,q,T) # Put the First Tensor on the Right of the Tree
		
		# otherwise, we add the new Tensor on the right
		else:
			self._add(k,q,T,self.root)
	
	# This is the second "add function" for the binary tree
	# We always want to add the Tensors as: [A^k1 (x) B^k2 ]^k
	def _add(self, k,q,T, node):
		
		# If the right side of the nodes are not null then
		if node.r != None:
			self._add(k,q,T,node.r)
		
		elif node.l==None and node.r==None:
			# Now we add a new node
			node.l = Node(self.k,self.q,'A')
			node.r = Node(k,q,T)
			self.k = k
			self.q = q
			
		# If the right is null, then
		else:
			node.r = Node(k,q,T)
	
	# This prints off the tensor
	def print_tensor(self):
		
		if(self.root != None):
			self._print_tensor(self.root)
			
	def _print_tensor(self,node):
		
		if(node != None):
			print node.node_string()
			self._print_tensor(node.l)
			self._print_tensor(node.r)

    # This function prints off the definition of a Spherical tensor
    # This only goes one layer deep so far
	def print_tensor_defintion(self):
		clebsch_symbol = '< ' + str(self.root.l.k) + ' mk1 ' + str(self.root.r.k)+ ' mk2' + ' | '
		clebsch_symbol = clebsch_symbol + str(self.root.k) + ','+ str(self.root.q) + ' > '
		definition = '\sum_{mk1,mk2} '+clebsch_symbol+self.root.l.node_rank_string()+"_{mk1} "+self.root.r.node_rank_string()+"_{mk2}"
		return definition

	
	# This function couples two tensors together	
	# This class function couples together two tensors into a new one  
	# It essentially couples two binary trees
	def couple(T1,T2,k12,q12):
		# Here we create a new tensor
		new_name = '[ '+T1.root.node_rank_string()+ ' (x) '+ T2.root.node_rank_string() + ' ]'
		T12 = SphericalTensor(k12,q12,new_name)
		T12.set_root_left(T1)
		T12.set_root_right(T2)
		return T12
		
		
	# Now we want to recouple tensors....
	# This requires a set of binary Tree Transformations
	# We will focus first on re-ordering the Tree slightly
	# [a x b]^f = (-1)^{a+b} [b x a]^f
	def recouple_lr(self):
		
		# Create a new Tensor object
		newName = '((-1)^{'+str(self.root.r.k)+' + '+str(self.root.l.k)+'})'
		newName = newName+'[ '+self.root.r.node_rank_string()+ ' (x) '+ self.root.l.node_rank_string() + ' ]'
		Trl = SphericalTensor(self.k,self.q,newName)
		
		# Increment the number of Transformations
		Trl.transformations = self.transformations + 1
		
		# Now we change the order of the nodes
		Trl.root.r = self.root.l
		Trl.root.l = self.root.r
		
		return Trl
	
	# Here we have a Binary tree reshuffle of three Coupled Elements
	# [A x [B x C] ] = Sum_{h} C1(A,B,C,h) [[A x B]^h x C] (1,2,3)
	# [A x [B x C] ] = Sum_{h} C2(A,B,C,h) [[A x C]^h x B] (1,3,2)
	def reshuffle(self,a,b,c):
		
		# Create a new Tree object
		
		# Left Node is [A C]
		# Right Node is B
		
		
		# Step one, locate teh
		
		return None





