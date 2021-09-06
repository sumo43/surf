
class Node:
    
    def __init__(self, url: str):
        self.url = url

    def get_url(self):
        return self.url
        
class Store:

    def __init__(self):
        self.urls = []

    def push_url(self, url: str):
        node = Node(url)
        self.urls.append(node)

    def get_urls(self):
        return self.urls

    def pop_node(self):
        return self.urls.pop()        

    def pop_node_url(self):
        return self.urls.pop().url


