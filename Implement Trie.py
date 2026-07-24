class TrieNode:
    def __init__(self, letter:str, children: Optional[dict[str, TrieNode]] = None, is_wordend: bool = False):
        self.letter = letter
        self.is_wordend = is_wordend
        self.children = children if children is not None else {}

class PrefixTree:
    '''
    TrieNode() := (letter:str, is_wordend: bool = False, children: dict[str, TrieNode] = {})

    __init__ :=
        root = TrieNode(None)

    insert :=
        cur = root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode(letter)
            cur = cur.children[letter]
        cur.is_wordend = True
        return

    startsWith :=
        cur = root
        for letter in word:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return True

    search :=
        cur = root
        for letter in word:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return (cur.is_wordend)
    '''

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode(letter)
            cur = cur.children[letter]
        cur.is_wordend = True
        return

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return (cur.is_wordend)

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        print(cur.children)
        for letter in prefix:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return True