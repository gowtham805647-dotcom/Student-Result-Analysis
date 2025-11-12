import time

class TreeNode:
    def __init__(self, marks, name):
        self.marks = marks
        self.name = name
        self.left = None
        self.right = None

class StudentBST:
    def __init__(self):
        self.root = None
    
    def insert(self, marks, name):
        if self.root is None:
            self.root = TreeNode(marks, name)
        else:
            self._insert_recursive(self.root, marks, name)
    
    def _insert_recursive(self, node, marks, name):
        if marks < node.marks:
            if node.left is None:
                node.left = TreeNode(marks, name)
            else:
                self._insert_recursive(node.left, marks, name)
        else:
            if node.right is None:
                node.right = TreeNode(marks, name)
            else:
                self._insert_recursive(node.right, marks, name)
    
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.name)
            self._inorder_recursive(node.right, result)
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.name)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.name)
    
    def to_dict(self):
        return self._to_dict_recursive(self.root)
    
    def _to_dict_recursive(self, node):
        if not node:
            return None
        return {
            'name': node.name,
            'marks': node.marks,
            'left': self._to_dict_recursive(node.left),
            'right': self._to_dict_recursive(node.right)
        }

class SortingAlgorithms:
    def sort(self, students, algorithm, sort_by):
        data = students.copy()
        
        if sort_by == 'name':
            key_func = lambda x: x['name']
        elif 'desc' in sort_by.lower():
            key_func = lambda x: x['maths'] + x['science'] + x['english']
            data.sort(key=key_func, reverse=True)
            return data, 0.0
        else:
            key_func = lambda x: x['maths'] + x['science'] + x['english']
        
        start = time.time()
        
        if algorithm == 'bubble':
            data = self._bubble_sort(data, key_func)
        elif algorithm == 'selection':
            data = self._selection_sort(data, key_func)
        elif algorithm == 'insertion':
            data = self._insertion_sort(data, key_func)
        
        elapsed = time.time() - start
        return data, elapsed
    
    def _bubble_sort(self, arr, key_func):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if key_func(arr[j]) > key_func(arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    def _selection_sort(self, arr, key_func):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if key_func(arr[j]) < key_func(arr[min_idx]):
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    
    def _insertion_sort(self, arr, key_func):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key_func(arr[j]) > key_func(key):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
