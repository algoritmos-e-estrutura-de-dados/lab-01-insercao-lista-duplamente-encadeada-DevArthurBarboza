
class Node:

    def __init__(self, x):
        self.x = x
        self.next = None
        self.prev = None


class Lista:

    def __init__(self):
        self.init = None
        self.tail = None


    def append(self, node):
        """
        Método para inserir um elemento no final

        :param node:
        :return:
        """
        if self.init is None:
            self.init = node
            self.tail = node
            return

        node_aux = self.init
        while (node_aux.next is not None):
            node_aux = node_aux.next
        node.prev = self.tail
        node_aux.next = node
        self.tail = node 


    def add(self, node):
        """
        Inserir um elemento sempre no inicio da lista

        :param node:
        :return:
        """
        if self.init is None:
            self.init = node
            self.tail = node
            return

        node_aux = self.init
        while (node_aux.next is not None):
            node_aux = node_aux.next
        node_aux = node

        node.next = self.init
        self.init.prev = node
        self.init = node
        
    def __str__(self):
        str_aux = '['
        node_aux = self.init
        while(node_aux is not None):
            str_aux += str(node_aux.x) + ','
            node_aux = node_aux.next
        str_aux += ']'
        str_aux = str_aux.replace(",]","]")
        return str_aux

    def insertBetween(self,node,prev,next):
        """
        Método para inserir um elemento entre dois nós

        """
        node.next = next
        node.prev = prev
        auxNode = self.init 
        while (auxNode.x != node.prev.x):
            auxNode = auxNode.next
        auxNode.next = node 
        auxNode.next.next = node.next 
        

if __name__ == '__main__':
    lista = Lista()
    lista.add(Node(x=27))
    lista.add(Node(x=1))
    print(lista)
    lista.append(Node(x=5))
    lista.append(Node(x=19))
    lista.insertBetween(Node(x=100),Node(x=5),Node(x=19))
    print(lista)
