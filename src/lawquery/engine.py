import re
import json
import gzip
import os


class Node:
    def __init__(self, name, content, node_type, node_id, parent=None):
        self.name = name
        self.content = content
        self.node_id = node_id
        self.node_type = node_type
        self.children = []
        self.parent = parent

    def add_child(self, obj: 'Node'):
        obj.parent = self
        self.children.append(obj)

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'--node--\nName: {self.name}\nNode type: {self.node_type}\nNode id: {self.node_id}\nChildren: {len(self.children)}\nContent: {len(self.content)} characters\n--node--\n'

    def print_path(self):
        s = ''
        node = self
        while node is not None:
            s = node.name + ' > ' + s
            node = node.parent
        return s[:-3]

    def asdict(self):
        return {
            'name': self.name,
            'node_id': self.node_id,
            'node_type': self.node_type,
            'children': [i.asdict() for i in self.children],
        }


class ITree:
    def __init__(self, data: dict):
        self.raw_text = data['raw_text']
        self.root = self._import(data['tree'])

    def _import(self, data: dict) -> Node:
        content = self.raw_text[data['content']
                                ['start']:data['content']['end']]
        root = Node(data['name'], content, data['node_type'],
                    data['node_id'])
        for child in data['children']:
            root.add_child(self._import(child))
        return root

    def __repr__(self):
        return self._print_tree(self.root)

    def __str__(self):
        return self._print_tree(self.root)

    def _print_tree(self, node: 'Node', level=0):
        s = ''
        s += '  '*level + node.name + '\n'
        if len(node.children) == 0 and len(node.content) > 0 and node.content != node.name:
            content = node.content
            content = re.sub(r'\n', '\n'+'  '*(level+1)+'📄', content)
            s += '  '*(level+1)+'📄' + content + '\n'
        else:
            for child in node.children:
                s += self._print_tree(child, level+1)
        return s


class Engine:
    tree: ITree

    def __init__(self, filepath: str):
        with gzip.open(filepath, 'rb') as f:
            data = json.loads(f.read())
        self.metadata = data['metadata']
        self.tree = ITree(data)
        self.__nodes = []
        self._traverse(self.tree.root)

    def _traverse(self, node: Node):
        """Traverse tree and add node to self.nodes

        Parameters
        ----------
        node : Node
            node of tree

        Returns
        -------
        None
        """

        self.__nodes.append(node)
        for child in node.children:
            self._traverse(child)

    def query_by_path(self, node_path: list[dict]) -> Node:
        nodes = []
        for path in node_path:
            node_type = path['node_type'] if 'node_type' in path else None
            node_id = path['node_id'] if 'node_id' in path else None
            name = path['name'] if 'name' in path else None
            new_nodes = []
            for node in nodes:
                new_nodes += self.query(node_type=node_type,
                                        node_id=node_id, name=name, parent=node)
            if len(nodes) == 0:
                new_nodes += self.query(node_type=node_type,
                                        node_id=node_id, name=name)
            nodes = new_nodes
        return nodes

    def query(self, name: str = None, node_type: str = None, node_id: str = None,  parent: Node = None) -> list[Node]:
        results = []
        for node in self.__nodes:
            if node_type is not None and node.node_type != node_type:
                continue
            if node_id is not None and node.node_id != node_id:
                continue
            if name is not None and name.lower() not in node.name.lower():
                continue
            if parent is not None and node.parent != parent:
                continue
            results.append(node)
        return results

    def print_tree(self):
        print(self.tree)

    def __repr__(self):
        # metadata
        s = ''
        for key, value in self.metadata.items():
            s += f'{key}: {value}\n'
        return s

    def __str__(self):
        # metadata
        s = ''
        for key, value in self.metadata.items():
            s += f'{key}: {value}\n'
        return s


def list_documents():
    # path only in this package
    root_path = os.path.dirname(os.path.abspath(__file__))
    return [os.path.join(root_path, 'documents', i) for i in os.listdir(os.path.join(root_path, 'documents'))]
