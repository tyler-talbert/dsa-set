class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root

        def dfs(index, node):
            if index == len(word):
                return node.end

            ch = word[index]
        
            if word[index] == ".":
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
            elif ch not in node.children:
                return False
            else:
                return dfs(index + 1, node.children[ch])

            return False
        
        return dfs(0, cur)


        
