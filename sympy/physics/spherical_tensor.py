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
	
	
# Here we need to define the Spherical Tensor class
# The implementation of the data structure will be a binary tree
class SphericalTensor:

    # This is the class constructor
    # k -> The rank of the tensor
    # q -> the index of the tensor
    # name -> The symbol that will represent the tensor of choice
	
	# These are variables accessible to the whole class
	k =0
	q =0
	name = 'T'
	
	# The data structure of a tensor should be a binary tree
    # We should check that the |q| <= k
	def __init__(self, k, q, T):
	    self.k = k
	    self.q = q
	    self.name = T
	    
	    self.root = None
	    
	# This function gets the root of the binary tree
	def get_root(self):
		return self.root
		
	# This function should add a node to the Binary Tree Data
	def add(self,k,q,T):
		if self.root == None:
			self.root = Node(k,q,T)
		else:
			self._add(k,q,T,self.root)
	
	# This is the second "add function" for the binary tree
	def _add(self, val, node):
		if(val < node.v):
			if(node.l != None):
				self._add(val, node.l)
			else:
				node.l = Node(val)
		else:
			if(node.r != None):
				self._add(val, node.r)
			else:
				node.r = Node(val)
	
	# This prints off the tensor
	def print_tensor(self):
		#print str(SphericalTensor.name)+ "^{"+str(SphericalTensor.k)+"}_{"+str(SphericalTensor.q)+"}"
		print str(self.name)+ "^{"+str(self.k)+"}_{"+str(self.q)+"}"
	
	# This function returns the Tensor name 
	def print_tensor_2(self):
		s = str(self.name)+"^{"+str(self.k)+"}"
		return s
	
	# This class function couples together two tensors into a new one  
	# It essentially couples two binary trees
	def couple(T1,T2,k12,q12,T12):
		# Here we create a new tensor
		new_name = "[ "+SphericalTensor.print_tensor_2(T1) + " (x) "+ SphericalTensor.print_tensor_2(T2)  +" ]"+"^{"+str(k12)+"}"+"_{"+str(q12)+"}"
		T12 = SphericalTensor(k12,q12,new_name)
		
		return T12





