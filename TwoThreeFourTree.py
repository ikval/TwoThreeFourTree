def createTreeItem(key, val):
    return TreeItem(key, val)


class TreeItem:
    def __init__(self, key, val):
        self.key = key
        self.value = val


class TwoNode:
    def __init__(self):
        self.type = "TwoNode"
        self.parent = None
        self.item = None  # 1 item
        self.left_child = None
        self.right_child = None


class ThreeNode:
    def __init__(self):
        self.type = "ThreeNode"
        self.parent = None
        self.items = []  # 2 items
        self.left_child = None
        self.middle_child = None
        self.right_child = None


class FourNode:
    def __init__(self):
        self.type = "FourNode"
        self.parent = None
        self.items = []  # 3 items
        self.leftest_child = None
        self.left_child = None
        self.right_child = None
        self.rightest_child = None


def isLeaf(node):
    if node.type == "TwoNode" and node.left_child is None and node.right_child is None:
        return True
    elif node.type == "ThreeNode" and node.left_child is None and node.middle_child is None and node.right_child is None:
        return True
    elif node.type == "FourNode" and node.leftest_child is None and node.left_child is None and node.right_child is None and node.rightest_child is None:
        return True
    else:
        return False


class TwoThreeFourTree:
    def __init__(self):
        self.root = TwoNode()

    def isEmpty(self):
        if self.root.type == "TwoNode" and self.root.item is None:
            return True
        elif self.root.type == "ThreeNode" and self.root.items.__len__() == 0:
            return True
        elif self.root.type == "FourNode" and self.root.items.__len__() == 0:
            return True
        else:
            return False

    def split(self, node):
        node.items.sort()
        left_item = node.items[0]
        middle_item = node.items[1]
        right_item = node.items[2]

        if node.parent is None:
            new_left_node = TwoNode()
            new_left_node.item = left_item
            new_left_node.left_child = node.leftest_child
            if node.leftest_child is not None:
                node.leftest_child.parent = new_left_node
            new_left_node.right_child = node.left_child
            if node.left_child is not None:
                node.left_child.parent = new_left_node

            new_right_node = TwoNode()
            new_right_node.item = right_item
            new_right_node.left_child = node.right_child
            if node.right_child is not None:
                node.right_child.parent = new_right_node
            new_right_node.right_child = node.rightest_child
            if node.rightest_child is not None:
                node.rightest_child.parent = new_right_node

            new_root_node = TwoNode()
            new_root_node.item = middle_item
            new_root_node.left_child = new_left_node
            new_left_node.parent = new_root_node
            new_root_node.right_child = new_right_node
            new_right_node.parent = new_root_node

            self.root = new_root_node
        elif node.parent.type == "TwoNode":
            if middle_item < node.parent.item:
                child_type = "Left"
            else:
                child_type = "Right"

            node.parent.__class__ = ThreeNode
            node.parent.type = "ThreeNode"
            node.parent.__setattr__('items', list())
            node.parent.__setattr__('middle_child', None)
            node.parent.items.append(node.parent.item)
            node.parent.items.append(middle_item)
            node.parent.items.sort()
            node.parent.__delattr__('item')

            new_left_node = TwoNode()
            new_left_node.item = left_item
            new_left_node.left_child = node.leftest_child
            if node.leftest_child is not None:
                node.leftest_child.parent = new_left_node
            new_left_node.right_child = node.left_child
            if node.left_child is not None:
                node.left_child.parent = new_left_node

            new_right_node = TwoNode()
            new_right_node.item = right_item
            new_right_node.left_child = node.right_child
            if node.right_child is not None:
                node.right_child.parent = new_right_node
            new_right_node.right_child = node.rightest_child
            if node.rightest_child is not None:
                node.rightest_child.parent = new_right_node

            if child_type == "Left":
                node.parent.left_child = new_left_node
                new_left_node.parent = node.parent
                node.parent.middle_child = new_right_node
                new_right_node.parent = node.parent
            elif child_type == "Right":
                node.parent.middle_child = new_left_node
                new_left_node.parent = node.parent
                node.parent.right_child = new_right_node
                new_right_node.parent = node.parent
        elif node.parent.type == "ThreeNode":
            left_item = node.items[0]
            middle_item = node.items[1]
            right_item = node.items[2]

            if middle_item < node.parent.items[0]:
                child_type = "Left"
            elif node.parent.items[0] < middle_item < node.parent.items[1]:
                child_type = "Middle"
            elif node.parent.items[1] < middle_item:
                child_type = "Right"

            node.parent.__class__ = FourNode
            node.parent.type = "FourNode"
            node.parent.__setattr__('leftest_child', None)
            node.parent.__setattr__('rightest_child', None)
            node.parent.items.append(middle_item)
            node.parent.items.sort()

            if child_type == "Left":
                node.parent.rightest_child = node.parent.right_child
                node.parent.right_child = node.parent.middle_child
            elif child_type == "Middle":
                node.parent.leftest_child = node.parent.left_child
                node.parent.rightest_child = node.parent.right_child
            elif child_type == "Right":
                node.parent.leftest_child = node.parent.left_child
                node.parent.left_child = node.parent.middle_child

            node.parent.__delattr__('middle_child')

            new_left_node = TwoNode()
            new_left_node.item = left_item
            new_left_node.left_child = node.leftest_child
            if node.leftest_child is not None:
                node.leftest_child.parent = new_left_node
            new_left_node.right_child = node.left_child
            if node.left_child is not None:
                node.left_child.parent = new_left_node

            new_right_node = TwoNode()
            new_right_node.item = right_item
            new_right_node.left_child = node.right_child
            if node.right_child is not None:
                node.right_child.parent = new_right_node
            new_right_node.right_child = node.rightest_child
            if node.rightest_child is not None:
                node.rightest_child.parent = new_right_node

            if child_type == "Left":
                node.parent.leftest_child = new_left_node
                new_left_node.parent = node.parent
                node.parent.left_child = new_right_node
                new_right_node.parent = node.parent
            elif child_type == "Middle":
                node.parent.left_child = new_left_node
                new_left_node.parent = node.parent
                node.parent.right_child = new_right_node
                new_right_node.parent = node.parent
            elif child_type == "Right":
                node.parent.right_child = new_left_node
                new_left_node.parent = node.parent
                node.parent.rightest_child = new_right_node
                new_right_node.parent = node.parent

    def insertItem(self, item):
        value = item.value

        if self.isEmpty():
            self.root.item = value
        else:
            self._insert(value, self.root)

        return True

    def _insert(self, value, current):
        type = current.type

        if type == "FourNode":
            self.split(current)
            self._insert(value, self.root)

        if isLeaf(current) is True:
            if type == "TwoNode":
                current.__class__ = ThreeNode
                current.type = "ThreeNode"
                current.__setattr__('items', list())
                current.__setattr__('middle_child', None)
                current.items.append(current.item)
                current.items.append(value)
                current.items.sort()
                current.__delattr__('item')
                return True
            elif type == "ThreeNode":
                current.__class__ = FourNode
                current.type = "FourNode"
                current.__setattr__('leftest_child', None)
                current.__setattr__('rightest_child', None)
                current.items.append(value)
                current.items.sort()
                current.__delattr__('middle_child')
                return True
        elif type == "TwoNode":
            if value < current.item:
                self._insert(value, current.left_child)
            elif value > current.item:
                self._insert(value, current.right_child)
        elif type == "ThreeNode":
            if value < current.items[0]:
                self._insert(value, current.left_child)
            elif current.items[0] < value < current.items[1]:
                self._insert(value, current.middle_child)
            elif value > current.items[1]:
                self._insert(value, current.right_child)

    def retrieveItem(self, key):
        if self.isEmpty():
            return False, False
        else:
            return self._retrieve(key, self.root)

    def _retrieve(self, key, current):
        if current is None:
            return None, False
        else:
            if current.type == "TwoNode":
                if key == current.item:
                    return current.item, True
                elif key < current.item:
                    return self._retrieve(key, current.left_child)
                elif key > current.item:
                    return self._retrieve(key, current.right_child)
            if current.type == "ThreeNode":
                if key == current.items[0]:
                    return current.items[0], True
                elif key == current.items[1]:
                    return current.items[1], True

                elif key < current.items[0]:
                    return self._retrieve(key, current.left_child)
                elif current.items[0] < key < current.items[1]:
                    return self._retrieve(key, current.middle_child)
                elif key > current.items[1]:
                    return self._retrieve(key, current.right_child)

    def inorderTraverse(self, func):
        self._inorder(self.root, func)

    def _inorder(self, current, func):
        if current is not None:
            if current.type == "TwoNode":
                self._inorder(current.left_child, func)
                func(current.item)
                self._inorder(current.right_child, func)
            elif current.type == "ThreeNode":
                self._inorder(current.left_child, func)
                func(current.items[0])
                self._inorder(current.middle_child, func)
                func(current.items[1])
                self._inorder(current.right_child, func)
            elif current.type == "FourNode":
                self._inorder(current.leftest_child, func)
                func(current.items[0])
                self._inorder(current.left_child, func)
                func(current.items[1])
                self._inorder(current.right_child, func)
                func(current.items[2])
                self._inorder(current.rightest_child, func)


# Testcode
if __name__ == "__main__":
    t = TwoThreeFourTree()
    print(t.insertItem(createTreeItem(7, 7)))
    print(t.insertItem(createTreeItem(8, 8)))
    print(t.insertItem(createTreeItem(9, 9)))
    print(t.insertItem(createTreeItem(10, 10)))
    print(t.insertItem(createTreeItem(11, 11)))
    print(t.insertItem(createTreeItem(12, 12)))
    print(t.insertItem(createTreeItem(6, 6)))
    print(t.insertItem(createTreeItem(5, 5)))
    print(t.insertItem(createTreeItem(4, 4)))
    print(t.insertItem(createTreeItem(3, 3)))
    print(t.insertItem(createTreeItem(2, 2)))
    print(t.insertItem(createTreeItem(1, 1)))
    print(t.insertItem(createTreeItem(0, 0)))
    print(t.insertItem(createTreeItem(14, 14)))
    print(t.insertItem(createTreeItem(13, 13)))
    print(t.insertItem(createTreeItem(15, 15)))
    print(t.insertItem(createTreeItem(16, 16)))
    t.inorderTraverse(print)
