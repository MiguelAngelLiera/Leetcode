class Trie:

    def __init__(self):
        self.root = Node("", children = {})
        

    def insert(self, word: str) -> None:
        if self.search(word):
            return
        curr = self.root
        for l in word:
            if l not in curr.children.keys():
                curr.children[l] = Node(val= l, children={})
            curr = curr.children[l]  
            
        curr.terminal = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for l in word:
            if l not in curr.children.keys():
                return False
            curr = curr.children[l]
            
        return curr.terminal
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for l in prefix:
            if l not in curr.children.keys():
                return False
            curr = curr.children[l]
            
        return True
        

class Node:
    def __init__(self, val= None, children = {}):
        self.val = val
        self.children = children
        self.terminal = False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)