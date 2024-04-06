#lista_encadeada.py

class Node:
	data = None
	next = None
	
	def __init__(self, data):
		self.data = data

class linkedList:

	head = None		# O primeiro nó da lista
	length = 0		# Total de elementos da lista
	
	
	# Adiciona elemento ao início da lista
	def push(self, data):
	
		new_node = Node(data)
		
		# Insere o elemento no início caso a lista esteja vazia
		if not self.head:
			self.head = new_node
		
		# Insere antes do primeiro elemento
		else:
			new_node.next = self.head
			self.head = new_node
			
		self.length += 1
			
	
	# Adiciona elemento ao final da lista
	def append(self, data):
	
		new_node = Node(data)
	
		if not self.head:
			self.head = new_node
		else:
			# Percorre os nós procurando por aquele que não aponta pra ninguém (ou seja o último nó)
			last_node = self.head
			
			while last_node.next:
				last_node = last_node.next
				
			# Encontrado o último nó insere o novo nó após esse
			last_node.next = new_node
			
		self.length += 1
			
			
	def dump(self):
		finalstr = ''
		
		print ()
		print ('===================')
		
		last_node = self.head
		
		while last_node:
			finalstr += (str(last_node.data))
			last_node = last_node.next
			
			if last_node:
				finalstr += ' -> '
		
		
		print ('	LISTA: ' + finalstr)
		print ('===================')
		
if __name__ == '__main__':
	l = linkedList()
	
	while True:
		print()
		print('Escolha uma opção:')
		print('1 - Adicionar elemento ao início da lista(push)')
		print('2 - Adicionar elemento ao final da lista(append)')
		print('3 - Sair')
		print()
		
		opt = input()
		
		if opt == '3':
			break
		
		elif opt == '1':
			print('Digite o valor a ser inserido ao início da lista:')
			val = input()
			l.push(val)
			
		elif opt == '2':
			print('Digite o valor a ser inserido ao final da lista:')
			val = input()
			l.append(val)
		
		else:
			print('Opção inválida!')
			continue
			
		l.dump()