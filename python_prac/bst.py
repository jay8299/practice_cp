
class BinarySearchTree():
    class _Node():
        __slots__ = ['_data','_left','_right']
        def __init__(self,element,left,right):
            self._data=element
            self._left = left
            self._right = right
    def __init__(self):
        self._root = None
        self._size = 0
    def insert(self, e):
        troot = self._root
        ttroot = None
        while troot:
            ttroot = troot
            if e < troot._data:
                troot = troot._left
            elif e> troot._data:
                troot = troot._right

        node = self._Node(e)
        if self._root:
            if e < ttroot:
                ttroot._left = node
            else:
                ttroot._right = node

    def search(self, k):


