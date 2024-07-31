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
        self.items = []  # 1 item
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


class TwoThreeFourTree:
    def __init__(self):
        self.root = TwoNode()

    def isEmpty(self):
        if self.root.type == "TwoNode" and self.root.items.__len__() == 0:
            return True
        elif self.root.type == "ThreeNode" and self.root.items.__len__() == 0:
            return True
        elif self.root.type == "FourNode" and self.root.items.__len__() == 0:
            return True
        else:
            return False

    def isLeaf(self, node):
        if node.type == "TwoNode" and node.left_child is None and node.right_child is None:
            return True
        elif node.type == "ThreeNode" and node.left_child is None and node.middle_child is None and node.right_child is None:
            return True
        elif node.type == "FourNode" and node.leftest_child is None and node.left_child is None and node.right_child is None and node.rightest_child is None:
            return True
        else:
            return False

    def split(self, node):
        left_item = node.items[0]
        middle_item = node.items[1]
        right_item = node.items[2]

        if node.parent is None:
            new_left_node = TwoNode()
            new_left_node.items.append(left_item)
            new_left_node.left_child = node.leftest_child
            if node.leftest_child is not None:
                node.leftest_child.parent = new_left_node
            new_left_node.right_child = node.left_child
            if node.left_child is not None:
                node.left_child.parent = new_left_node

            new_right_node = TwoNode()
            new_right_node.items.append(right_item)
            new_right_node.left_child = node.right_child
            if node.right_child is not None:
                node.right_child.parent = new_right_node
            new_right_node.right_child = node.rightest_child
            if node.rightest_child is not None:
                node.rightest_child.parent = new_right_node

            new_root_node = TwoNode()
            new_root_node.items.append(middle_item)
            new_root_node.left_child = new_left_node
            new_left_node.parent = new_root_node
            new_root_node.right_child = new_right_node
            new_right_node.parent = new_root_node

            self.root = new_root_node

        elif node.parent.type == "TwoNode":
            if middle_item < node.parent.items[0]:
                child_type = "Left"
            else:
                child_type = "Right"

            node.parent.__class__ = ThreeNode
            node.parent.type = "ThreeNode"
            node.parent.__setattr__('middle_child', None)
            node.parent.items.append(middle_item)
            node.parent.items.sort()

            new_left_node = TwoNode()
            new_left_node.items.append(left_item)
            new_left_node.left_child = node.leftest_child
            if node.leftest_child is not None:
                node.leftest_child.parent = new_left_node
            new_left_node.right_child = node.left_child
            if node.left_child is not None:
                node.left_child.parent = new_left_node

            new_right_node = TwoNode()
            new_right_node.items.append(right_item)
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
            new_left_node.items.append(left_item)
            new_left_node.left_child = node.leftest_child
            if node.leftest_child is not None:
                node.leftest_child.parent = new_left_node
            new_left_node.right_child = node.left_child
            if node.left_child is not None:
                node.left_child.parent = new_left_node

            new_right_node = TwoNode()
            new_right_node.items.append(right_item)
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
        if self.isEmpty():
            self.root.items.append(item.value)
        else:
            self._insert(item.value, self.root)

        return True

    def _insert(self, value, current):
        if current.type == "FourNode":
            self.split(current)
            self._insert(value, self.root)

        if self.isLeaf(current) is True:

            if current.type == "TwoNode":
                current.__class__ = ThreeNode
                current.type = "ThreeNode"
                current.__setattr__('middle_child', None)
                current.items.append(value)
                current.items.sort()
                return True

            elif current.type == "ThreeNode":
                current.__class__ = FourNode
                current.type = "FourNode"
                current.__setattr__('leftest_child', None)
                current.__setattr__('rightest_child', None)
                current.items.append(value)
                current.items.sort()
                current.__delattr__('middle_child')
                return True

        elif current.type == "TwoNode":

            if value < current.items[0]:
                self._insert(value, current.left_child)
            elif value > current.items[0]:
                self._insert(value, current.right_child)

        elif current.type == "ThreeNode":

            if value < current.items[0]:
                self._insert(value, current.left_child)
            elif current.items[0] < value < current.items[1]:
                self._insert(value, current.middle_child)
            elif value > current.items[1]:
                self._insert(value, current.right_child)

    def findSiblingToDonate(self, node):
        if node.parent.type == "TwoNode":

            if node.parent.left_child.items == node.items:
                if node.parent.right_child.type == "TwoNode":  # Sibling cannot donate an item
                    return None
                else:  # Sibling can donate an item
                    return node.parent.right_child

            elif node.parent.right_child.items == node.items:
                if node.parent.left_child.type == "TwoNode":  # Sibling cannot donate an item
                    return None
                else:  # Sibling can donate an item
                    return node.parent.left_child

        elif node.parent.type == "ThreeNode":

            if node.parent.left_child.items == node.items:
                if node.parent.middle_child.type == "TwoNode":  # Sibling cannot donate an item
                    return None
                else:  # Sibling can donate an item
                    return node.parent.middle_child

            elif node.parent.middle_child.items == node.items:
                if node.parent.left_child.type == "TwoNode" and node.parent.right_child.type == "TwoNode":  # Neither siblings can donate an item
                    return None
                elif node.parent.left_child.type != "TwoNode":  # Left sibling can donate
                    return node.parent.left_child
                elif node.parent.right_child.type != "TwoNode":  # Right sibling can donate
                    return node.parent.right_child

            elif node.parent.right_child.items == node.items:
                if node.parent.middle_child.type == "TwoNode":  # Sibling cannot donate an item
                    return None
                else:  # Sibling can donate an item
                    return node.parent.middle_child

        elif node.parent.type == "FourNode":

            if node.parent.leftest_child.items == node.items:
                if node.parent.left_child.type == "TwoNode":  # Sibling cannot donate an item
                    return None
                else:  # Sibling can donate an item
                    return node.parent.left_child

            elif node.parent.left_child.items == node.items:
                if node.parent.leftest_child.type == "TwoNode" and node.parent.right_child.type == "TwoNode":  # Neither siblings can donate an item
                    return None
                elif node.parent.leftest_child.type != "TwoNode":  # Left sibling can donate
                    return node.parent.leftest_child
                elif node.parent.right_child.type != "TwoNode":  # Right sibling can donate
                    return node.parent.right_child

            elif node.parent.right_child.items == node.items:
                if node.parent.left_child.type == "TwoNode" and node.parent.rightest_child.type == "TwoNode":  # Neither siblings can donate an item
                    return None
                elif node.parent.left_child.type != "TwoNode":  # Left sibling can donate
                    return node.parent.left_child
                elif node.parent.rightest_child.type != "TwoNode":  # Right sibling can donate
                    return node.parent.rightest_child

            elif node.parent.rightest_child.items == node.items:
                if node.parent.right_child.type == "TwoNode":  # Sibling cannot donate an item
                    return None
                else:  # Sibling can donate an item
                    return node.parent.right_child

    def mergeTwoNode(self, node):
        node.__class__ = FourNode
        node.type = "FourNode"
        node.items.append(node.left_child.items[0])
        node.items.append(node.right_child.items[0])
        node.items.sort()

        node.__setattr__('leftest_child', node.left_child.left_child)
        if node.leftest_child is not None:
            node.leftest_child.parent = node
        node.left_child = node.left_child.right_child
        if node.left_child is not None:
            node.left_child.parent = node
        node.__setattr__('rightest_child', node.right_child.right_child)
        if node.rightest_child is not None:
            node.rightest_child.parent = node
        node.right_child = node.right_child.left_child
        if node.right_child is not None:
            node.right_child.parent = node

        return node

    def mergeThreeNode(self, node, merge_direction):
        if merge_direction == "left":
            new_node = FourNode()
            new_node.items.append(node.left_child.items[0])
            new_node.items.append(node.items[0])
            new_node.items.append(node.middle_child.items[0])
            new_node.parent = node

            new_node.leftest_child = node.left_child.left_child
            if new_node.leftest_child is not None:
                new_node.leftest_child.parent = new_node
            new_node.left_child = node.left_child.right_child
            if new_node.left_child is not None:
                new_node.left_child.parent = new_node
            new_node.right_child = node.middle_child.left_child
            if new_node.right_child is not None:
                new_node.right_child.parent = new_node
            new_node.rightest_child = node.middle_child.right_child
            if new_node.rightest_child is not None:
                new_node.rightest_child.parent = new_node

            node.__class__ = TwoNode
            node.type = "TwoNode"
            node.left_child = new_node
            node.items.remove(node.items[0])
            node.__delattr__('middle_child')

        elif merge_direction == "right":
            new_node = FourNode()
            new_node.items.append(node.middle_child.items[0])
            new_node.items.append(node.items[1])
            new_node.items.append(node.right_child.items[0])
            new_node.parent = node

            new_node.leftest_child = node.middle_child.left_child
            if new_node.leftest_child is not None:
                new_node.leftest_child.parent = new_node
            new_node.left_child = node.middle_child.right_child
            if new_node.left_child is not None:
                new_node.left_child.parent = new_node
            new_node.right_child = node.right_child.left_child
            if new_node.right_child is not None:
                new_node.right_child.parent = new_node
            new_node.rightest_child = node.right_child.right_child
            if new_node.rightest_child is not None:
                new_node.rightest_child.parent = new_node

            node.__class__ = TwoNode
            node.type = "TwoNode"
            node.right_child = new_node
            node.items.remove(node.items[1])
            node.__delattr__('middle_child')

        return node

    def mergeFourNode(self, node, merge_direction):
        if merge_direction == "left":
            new_node = FourNode()
            new_node.items.append(node.leftest_child.items[0])
            new_node.items.append(node.items[0])
            new_node.items.append(node.left_child.items[0])
            new_node.parent = node

            new_node.leftest_child = node.leftest_child.left_child
            if new_node.leftest_child is not None:
                new_node.leftest_child.parent = new_node
            new_node.left_child = node.leftest_child.right_child
            if new_node.left_child is not None:
                new_node.left_child.parent = new_node
            new_node.right_child = node.left_child.left_child
            if new_node.right_child is not None:
                new_node.right_child.parent = new_node
            new_node.rightest_child = node.left_child.right_child
            if new_node.rightest_child is not None:
                new_node.rightest_child.parent = new_node

            node.__class__ = ThreeNode
            node.type = "ThreeNode"
            node.items.remove(node.items[0])
            node.left_child = new_node
            node.__setattr__('middle_child', node.right_child)
            node.right_child = node.rightest_child
            node.__delattr__('leftest_child')
            node.__delattr__('rightest_child')

        elif merge_direction == "middle":
            new_node = FourNode()
            new_node.items.append(node.left_child.items[0])
            new_node.items.append(node.items[1])
            new_node.items.append(node.right_child.items[0])
            new_node.parent = node

            new_node.leftest_child = node.left_child.left_child
            if new_node.leftest_child is not None:
                new_node.leftest_child.parent = new_node
            new_node.left_child = node.left_child.right_child
            if new_node.left_child is not None:
                new_node.left_child.parent = new_node
            new_node.right_child = node.right_child.left_child
            if new_node.right_child is not None:
                new_node.right_child.parent = new_node
            new_node.rightest_child = node.right_child.right_child
            if new_node.rightest_child is not None:
                new_node.rightest_child.parent = new_node

            node.__class__ = ThreeNode
            node.type = "ThreeNode"
            node.items.remove(node.items[1])
            node.left_child = node.leftest_child
            node.__setattr__('middle_child', new_node)
            node.right_child = node.rightest_child
            node.__delattr__('leftest_child')
            node.__delattr__('rightest_child')

        elif merge_direction == "right":
            new_node = FourNode()
            new_node.items.append(node.right_child.items[0])
            new_node.items.append(node.items[2])
            new_node.items.append(node.rightest_child.items[0])
            new_node.parent = node

            new_node.leftest_child = node.right_child.left_child
            if new_node.leftest_child is not None:
                new_node.leftest_child.parent = new_node
            new_node.left_child = node.right_child.right_child
            if new_node.left_child is not None:
                new_node.left_child.parent = new_node
            new_node.right_child = node.rightest_child.left_child
            if new_node.right_child is not None:
                new_node.right_child.parent = new_node
            new_node.rightest_child = node.rightest_child.right_child
            if new_node.rightest_child is not None:
                new_node.rightest_child.parent = new_node

            node.__class__ = ThreeNode
            node.type = "ThreeNode"
            node.items.remove(node.items[2])
            node.__setattr__('middle_child', node.left_child)
            node.left_child = node.leftest_child
            node.right_child = new_node
            node.__delattr__('leftest_child')
            node.__delattr__('rightest_child')

        return node

    def merge(self, node):
        if node.parent.type == "TwoNode":
            self.mergeTwoNode(node.parent)
            return

        elif node.parent.type == "ThreeNode":
            if node == node.parent.left_child or node == node.parent.middle_child:
                return self.mergeThreeNode(node.parent, "left")
            else:
                return self.mergeThreeNode(node.parent, "right")

        elif node.parent.type == "FourNode":
            if node == node.parent.leftest_child or node == node.parent.left_child:
                return self.mergeFourNode(node.parent, "left")
            elif node == node.parent.right_child:
                return self.mergeFourNode(node.parent, "middle")
            elif node == node.parent.rightest_child:
                return self.mergeFourNode(node.parent, "right")

    def _twoNodeRedistribute(self, node, node_to_donate):
        if node_to_donate.type == "ThreeNode":
            if node == node.parent.right_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[0])
                node.items.sort()
                node.__setattr__('middle_child', node.left_child)
                node.left_child = node_to_donate.right_child
                if node.left_child is not None:
                    node.left_child.parent = node

                node.parent.items[0] = node_to_donate.items[1]

                node_to_donate.__class__ = TwoNode
                node_to_donate.type = "TwoNode"
                node_to_donate.right_child = node_to_donate.middle_child
                node_to_donate.items.remove(node_to_donate.items[1])
                node_to_donate.__delattr__('middle_child')

            elif node == node.parent.left_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[0])
                node.items.sort()
                node.__setattr__('middle_child', node.right_child)
                node.right_child = node_to_donate.left_child
                if node.right_child is not None:
                    node.right_child.parent = node

                node.parent.items[0] = node_to_donate.items[0]

                node_to_donate.__class__ = TwoNode
                node_to_donate.type = "TwoNode"
                node_to_donate.left_child = node_to_donate.middle_child
                node_to_donate.items.remove(node_to_donate.items[0])
                node_to_donate.__delattr__('middle_child')

        elif node_to_donate.type == "FourNode":
            if node == node.parent.right_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[0])
                node.items.sort()
                node.__setattr__('middle_child', node.left_child)
                node.left_child = node_to_donate.rightest_child
                if node.left_child is not None:
                    node.left_child.parent = node

                node.parent.items[0] = node_to_donate.items[2]

                node_to_donate.__class__ = ThreeNode
                node_to_donate.type = "ThreeNode"
                node_to_donate.items.remove(node_to_donate.items[2])
                node_to_donate.__setattr__('middle_child', node_to_donate.left_child)
                node_to_donate.left_child = node_to_donate.leftest_child
                node_to_donate.__delattr__('rightest_child')
                node_to_donate.__delattr__('leftest_child')

            elif node == node.parent.left_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[0])
                node.items.sort()
                node.__setattr__('middle_child', node.right_child)
                node.right_child = node_to_donate.leftest_child
                if node.right_child is not None:
                    node.right_child.parent = node

                node.parent.items[0] = node_to_donate.items[0]

                node_to_donate.__class__ = ThreeNode
                node_to_donate.type = "ThreeNode"
                node_to_donate.items.remove(node_to_donate.items[0])
                node_to_donate.__setattr__('middle_child', node_to_donate.right_child)
                node_to_donate.right_child = node_to_donate.rightest_child
                node_to_donate.__delattr__('rightest_child')
                node_to_donate.__delattr__('leftest_child')

        return node

    def _threeNodeRedistribute(self, node, node_to_donate):
        if node_to_donate.type == "ThreeNode":
            if node == node.parent.middle_child and node_to_donate == node.parent.left_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[0])
                node.items.sort()
                node.__setattr__('middle_child', node.left_child)
                node.left_child = node_to_donate.right_child
                if node.left_child is not None:
                    node.left_child.parent = node

                node.parent.items[0] = node_to_donate.items[1]

                node_to_donate.__class__ = TwoNode
                node_to_donate.type = "TwoNode"
                node_to_donate.right_child = node_to_donate.middle_child
                node_to_donate.items.remove(node_to_donate.items[1])
                node_to_donate.__delattr__('middle_child')

            elif node == node.parent.middle_child and node_to_donate == node.parent.right_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[1])
                node.items.sort()
                node.__setattr__('middle_child', node.right_child)
                node.right_child = node_to_donate.left_child
                if node.right_child is not None:
                    node.right_child.parent = node

                node.parent.items[1] = node_to_donate.items[0]

                node_to_donate.__class__ = TwoNode
                node_to_donate.type = "TwoNode"
                node_to_donate.left_child = node_to_donate.middle_child
                node_to_donate.items.remove(node_to_donate.items[0])
                node_to_donate.__delattr__('middle_child')

            elif node == node.parent.left_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[0])
                node.items.sort()
                node.__setattr__('middle_child', node.right_child)
                node.right_child = node_to_donate.left_child
                if node.right_child is not None:
                    node.right_child.parent = node

                node.parent.items[0] = node_to_donate.items[0]

                node_to_donate.__class__ = TwoNode
                node_to_donate.type = "TwoNode"
                node_to_donate.left_child = node_to_donate.middle_child
                node_to_donate.items.remove(node_to_donate.items[0])
                node_to_donate.__delattr__('middle_child')

            elif node == node.parent.right_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[1])
                node.items.sort()
                node.__setattr__('middle_child', node.left_child)
                node.left_child = node_to_donate.right_child
                if node.left_child is not None:
                    node.left_child.parent = node

                node.parent.items[1] = node_to_donate.items[1]

                node_to_donate.__class__ = TwoNode
                node_to_donate.type = "TwoNode"
                node_to_donate.right_child = node_to_donate.middle_child
                node_to_donate.items.remove(node_to_donate.items[1])
                node_to_donate.__delattr__('middle_child')

        elif node_to_donate.type == "FourNode":
            if node == node.parent.middle_child and node_to_donate == node.parent.left_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[0])
                node.items.sort()
                node.__setattr__('middle_child', node.left_child)
                node.left_child = node_to_donate.rightest_child
                if node.left_child is not None:
                    node.left_child.parent = node

                node.parent.items[0] = node_to_donate.items[2]

                node_to_donate.__class__ = ThreeNode
                node_to_donate.type = "ThreeNode"
                node_to_donate.items.remove(node_to_donate.items[2])
                node_to_donate.__setattr__('middle_child', node_to_donate.left_child)
                node_to_donate.left_child = node_to_donate.leftest_child
                node_to_donate.__delattr__('rightest_child')
                node_to_donate.__delattr__('leftest_child')

            elif node == node.parent.middle_child and node_to_donate == node.parent.right_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[1])
                node.items.sort()
                node.__setattr__('middle_child', node.right_child)
                node.right_child = node_to_donate.leftest_child
                if node.right_child is not None:
                    node.right_child.parent = node

                node.parent.items[1] = node_to_donate.items[0]

                node_to_donate.__class__ = ThreeNode
                node_to_donate.type = "ThreeNode"
                node_to_donate.items.remove(node_to_donate.items[0])
                node_to_donate.__setattr__('middle_child', node_to_donate.right_child)
                node_to_donate.right_child = node_to_donate.rightest_child
                node_to_donate.__delattr__('rightest_child')
                node_to_donate.__delattr__('leftest_child')

            elif node == node.parent.left_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[0])
                node.items.sort()
                node.__setattr__('middle_child', node.right_child)
                node.right_child = node_to_donate.leftest_child
                if node.right_child is not None:
                    node.right_child.parent = node

                node.parent.items[0] = node_to_donate.items[0]

                node_to_donate.__class__ = ThreeNode
                node_to_donate.type = "ThreeNode"
                node_to_donate.items.remove(node_to_donate.items[0])
                node_to_donate.__setattr__('middle_child', node_to_donate.right_child)
                node_to_donate.right_child = node_to_donate.rightest_child
                node_to_donate.__delattr__('rightest_child')
                node_to_donate.__delattr__('leftest_child')

            elif node == node.parent.right_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[1])
                node.items.sort()
                node.__setattr__('middle_child', node.left_child)
                node.left_child = node_to_donate.rightest_child
                if node.left_child is not None:
                    node.left_child.parent = node

                node.parent.items[1] = node_to_donate.items[2]

                node_to_donate.__class__ = ThreeNode
                node_to_donate.type = "ThreeNode"
                node_to_donate.items.remove(node_to_donate.items[2])
                node_to_donate.__setattr__('middle_child', node_to_donate.left_child)
                node_to_donate.left_child = node_to_donate.leftest_child
                node_to_donate.__delattr__('rightest_child')
                node_to_donate.__delattr__('leftest_child')

        return node

    def _fourNodeRedistribute(self, node, node_to_donate):
        if node_to_donate.type == "ThreeNode":
            if node == node.parent.leftest_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[0])
                node.items.sort()
                node.__setattr__('middle_child', node.right_child)
                node.right_child = node_to_donate.left_child
                if node.right_child is not None:
                    node.right_child.parent = node

                node.parent.items[0] = node_to_donate.items[0]

                node_to_donate.__class__ = TwoNode
                node_to_donate.type = "TwoNode"
                node_to_donate.left_child = node_to_donate.middle_child
                node_to_donate.items.remove(node_to_donate.items[0])
                node_to_donate.__delattr__('middle_child')

            elif node == node.parent.left_child and node_to_donate == node.parent.leftest_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[0])
                node.items.sort()
                node.__setattr__('middle_child', node.left_child)
                node.left_child = node_to_donate.right_child
                if node.left_child is not None:
                    node.left_child.parent = node

                node.parent.items[0] = node_to_donate.items[1]

                node_to_donate.__class__ = TwoNode
                node_to_donate.type = "TwoNode"
                node_to_donate.right_child = node_to_donate.middle_child
                node_to_donate.items.remove(node_to_donate.items[1])
                node_to_donate.__delattr__('middle_child')

            elif node == node.parent.left_child and node_to_donate == node.parent.right_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[1])
                node.items.sort()
                node.__setattr__('middle_child', node.right_child)
                node.right_child = node_to_donate.left_child
                if node.right_child is not None:
                    node.right_child.parent = node

                node.parent.items[1] = node_to_donate.items[0]

                node_to_donate.__class__ = TwoNode
                node_to_donate.type = "TwoNode"
                node_to_donate.left_child = node_to_donate.middle_child
                node_to_donate.items.remove(node_to_donate.items[0])
                node_to_donate.__delattr__('middle_child')

            elif node == node.parent.right_child and node_to_donate == node.parent.left_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[1])
                node.items.sort()
                node.__setattr__('middle_child', node.left_child)
                node.left_child = node_to_donate.right_child
                if node.left_child is not None:
                    node.left_child.parent = node

                node.parent.items[1] = node_to_donate.items[1]

                node_to_donate.__class__ = TwoNode
                node_to_donate.type = "TwoNode"
                node_to_donate.right_child = node_to_donate.middle_child
                node_to_donate.items.remove(node_to_donate.items[1])
                node_to_donate.__delattr__('middle_child')

            elif node == node.parent.right_child and node_to_donate == node.parent.rightest_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[2])
                node.items.sort()
                node.__setattr__('middle_child', node.right_child)
                node.right_child = node_to_donate.left_child
                if node.right_child is not None:
                    node.right_child.parent = node

                node.parent.items[2] = node_to_donate.items[0]

                node_to_donate.__class__ = TwoNode
                node_to_donate.type = "TwoNode"
                node_to_donate.left_child = node_to_donate.middle_child
                node_to_donate.items.remove(node_to_donate.items[0])
                node_to_donate.__delattr__('middle_child')

            elif node == node.parent.rightest_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[2])
                node.items.sort()
                node.__setattr__('middle_child', node.left_child)
                node.left_child = node_to_donate.right_child
                if node.left_child is not None:
                    node.left_child.parent = node

                node.parent.items[2] = node_to_donate.items[1]

                node_to_donate.__class__ = TwoNode
                node_to_donate.type = "TwoNode"
                node_to_donate.right_child = node_to_donate.middle_child
                node_to_donate.items.remove(node_to_donate.items[1])
                node_to_donate.__delattr__('middle_child')

        elif node_to_donate.type == "FourNode":
            if node == node.parent.leftest_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[0])
                node.items.sort()
                node.__setattr__('middle_child', node.right_child)
                node.right_child = node_to_donate.leftest_child
                if node.right_child is not None:
                    node.right_child.parent = node

                node.parent.items[0] = node_to_donate.items[0]

                node_to_donate.__class__ = ThreeNode
                node_to_donate.type = "ThreeNode"
                node_to_donate.items.remove(node_to_donate.items[0])
                node_to_donate.__setattr__('middle_child', node_to_donate.right_child)
                node_to_donate.right_child = node_to_donate.rightest_child
                node_to_donate.__delattr__('rightest_child')
                node_to_donate.__delattr__('leftest_child')

            elif node == node.parent.left_child and node_to_donate == node.parent.leftest_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[0])
                node.items.sort()
                node.__setattr__('middle_child', node.left_child)
                node.left_child = node_to_donate.rightest_child
                if node.left_child is not None:
                    node.left_child.parent = node

                node.parent.items[0] = node_to_donate.items[2]

                node_to_donate.__class__ = ThreeNode
                node_to_donate.type = "ThreeNode"
                node_to_donate.items.remove(node_to_donate.items[2])
                node_to_donate.__setattr__('middle_child', node_to_donate.left_child)
                node_to_donate.left_child = node_to_donate.leftest_child
                node_to_donate.__delattr__('rightest_child')
                node_to_donate.__delattr__('leftest_child')

            elif node == node.parent.left_child and node_to_donate == node.parent.right_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[1])
                node.items.sort()
                node.__setattr__('middle_child', node.right_child)
                node.right_child = node_to_donate.leftest_child
                if node.right_child is not None:
                    node.right_child.parent = node

                node.parent.items[1] = node_to_donate.items[0]

                node_to_donate.__class__ = ThreeNode
                node_to_donate.type = "ThreeNode"
                node_to_donate.items.remove(node_to_donate.items[0])
                node_to_donate.__setattr__('middle_child', node_to_donate.right_child)
                node_to_donate.right_child = node_to_donate.rightest_child
                node_to_donate.__delattr__('rightest_child')
                node_to_donate.__delattr__('leftest_child')

            elif node == node.parent.right_child and node_to_donate == node.parent.left_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[1])
                node.items.sort()
                node.__setattr__('middle_child', node.left_child)
                node.left_child = node_to_donate.rightest_child
                if node.left_child is not None:
                    node.left_child.parent = node

                node.parent.items[1] = node_to_donate.items[2]

                node_to_donate.__class__ = ThreeNode
                node_to_donate.type = "ThreeNode"
                node_to_donate.items.remove(node_to_donate.items[2])
                node_to_donate.__setattr__('middle_child', node_to_donate.left_child)
                node_to_donate.left_child = node_to_donate.leftest_child
                node_to_donate.__delattr__('rightest_child')
                node_to_donate.__delattr__('leftest_child')

            elif node == node.parent.right_child and node_to_donate == node.parent.rightest_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[2])
                node.items.sort()
                node.__setattr__('middle_child', node.right_child)
                node.right_child = node_to_donate.leftest_child
                if node.right_child is not None:
                    node.right_child.parent = node

                node.parent.items[2] = node_to_donate.items[0]

                node_to_donate.__class__ = ThreeNode
                node_to_donate.type = "ThreeNode"
                node_to_donate.items.remove(node_to_donate.items[0])
                node_to_donate.__setattr__('middle_child', node_to_donate.right_child)
                node_to_donate.right_child = node_to_donate.rightest_child
                node_to_donate.__delattr__('rightest_child')
                node_to_donate.__delattr__('leftest_child')

            elif node == node.parent.rightest_child:
                node.__class__ = ThreeNode
                node.type = "ThreeNode"
                node.items.append(node.parent.items[2])
                node.items.sort()
                node.__setattr__('middle_child', node.left_child)
                node.left_child = node_to_donate.rightest_child
                if node.left_child is not None:
                    node.left_child.parent = node

                node.parent.items[2] = node_to_donate.items[2]

                node_to_donate.__class__ = ThreeNode
                node_to_donate.type = "ThreeNode"
                node_to_donate.items.remove(node_to_donate.items[2])
                node_to_donate.__setattr__('middle_child', node_to_donate.left_child)
                node_to_donate.left_child = node_to_donate.leftest_child
                node_to_donate.__delattr__('rightest_child')
                node_to_donate.__delattr__('leftest_child')

        return node

    def redistribute(self, node):
        node_to_donate = self.findSiblingToDonate(node)

        if node.parent.type == "TwoNode":
            return self._twoNodeRedistribute(node, node_to_donate)
        elif node.parent.type == "ThreeNode":
            return self._threeNodeRedistribute(node, node_to_donate)
        elif node.parent.type == "FourNode":
            return self._fourNodeRedistribute(node, node_to_donate)

    def transformTwoNode(self, current):
        if current == self.root:
            return
        else:
            if self.findSiblingToDonate(current) is not None:
                return self.redistribute(current)
            else:
                return self.merge(current)

    def deleteItem(self, key):
        if not self.retrieveItem(key)[1]:
            return False
        else:
            self.transformNodesOnPath(key, self.root)
            self.transformNodesOnPath(self.findSuccessor(key), self.root)

            node_with_key = self.retrieveNode(key)
            node_with_successor = self.retrieveNode(self.findSuccessor(key))
            self.swapAndDelete(node_with_key, node_with_successor, key, self.findSuccessor(key))
            return True

    def swapAndDelete(self, node_with_key, node_with_successor, key, successor_key):
        if node_with_key == node_with_successor or node_with_successor == self.root or successor_key is None:
            node_with_key.items.remove(key)
            node_with_key.items.sort()

            if node_with_key.type == "ThreeNode":
                node_with_key.__class__ = TwoNode
                node_with_key.type = "TwoNode"
                node_with_key.__delattr__('middle_child')
            elif node_with_key.type == "FourNode":
                node_with_key.__class__ = ThreeNode
                node_with_key.type = "ThreeNode"
                node_with_key.__setattr__('middle_child', None)
                node_with_key.__delattr__('leftest_child')
                node_with_key.__delattr__('rightest_child')
        else:
            node_with_successor.items.append(key)
            node_with_key.items.append(successor_key)
            node_with_successor.items.remove(successor_key)
            node_with_key.items.remove(key)
            node_with_successor.items.remove(key)
            node_with_successor.items.sort()
            node_with_key.items.sort()

            if node_with_successor.type == "ThreeNode":
                node_with_successor.__class__ = TwoNode
                node_with_successor.type = "TwoNode"
                node_with_successor.__delattr__('middle_child')
            elif node_with_successor.type == "FourNode":
                node_with_successor.__class__ = ThreeNode
                node_with_successor.type = "ThreeNode"
                node_with_successor.__setattr__('middle_child', None)
                node_with_successor.__delattr__('leftest_child')
                node_with_successor.__delattr__('rightest_child')

    def transformNodesOnPath(self, key, current):
        if key is None:
            return None

        if key in current.items:
            if current.type == "TwoNode":
                return self.transformTwoNode(current)
            else:
                return current

        if current == self.root:
            if current.type == "TwoNode":
                if key < current.items[0]:
                    return self.transformNodesOnPath(key, current.left_child)
                elif key > current.items[0]:
                    return self.transformNodesOnPath(key, current.right_child)
            if current.type == "ThreeNode":
                if key < current.items[0]:
                    return self.transformNodesOnPath(key, current.left_child)
                elif current.items[0] < key < current.items[1]:
                    return self.transformNodesOnPath(key, current.middle_child)
                elif key > current.items[1]:
                    return self.transformNodesOnPath(key, current.right_child)
            if current.type == "FourNode":
                if key < current.items[0]:
                    return self.transformNodesOnPath(key, current.leftest_child)
                elif current.items[0] < key < current.items[1]:
                    return self.transformNodesOnPath(key, current.left_child)
                elif current.items[1] < key < current.items[2]:
                    return self.transformNodesOnPath(key, current.right_child)
                elif key > current.items[2]:
                    return self.transformNodesOnPath(key, current.rightest_child)
        else:
            if current.type == "TwoNode":
                self.transformTwoNode(current)
            elif current.type == "ThreeNode":
                if key < current.items[0]:
                    self.transformNodesOnPath(key, current.left_child)
                elif current.items[0] < key < current.items[1]:
                    self.transformNodesOnPath(key, current.middle_child)
                elif key > current.items[1]:
                    self.transformNodesOnPath(key, current.right_child)
            elif current.type == "FourNode":
                if key < current.items[0]:
                    self.transformNodesOnPath(key, current.leftest_child)
                elif current.items[0] < key < current.items[1]:
                    self.transformNodesOnPath(key, current.left_child)
                elif current.items[1] < key < current.items[2]:
                    self.transformNodesOnPath(key, current.right_child)
                elif key > current.items[2]:
                    self.transformNodesOnPath(key, current.rightest_child)

    def retrieveNode(self, key):
        if self.isEmpty() or key is None:
            return None
        else:
            return self._retrieveNode(key, self.root)

    def _retrieveNode(self, key, current):
        if current is None:
            return None
        else:
            if key in current.items:
                return current

            if current.type == "TwoNode":
                if key < current.items[0]:
                    return self._retrieveNode(key, current.left_child)
                elif key > current.items[0]:
                    return self._retrieveNode(key, current.right_child)
            if current.type == "ThreeNode":
                if key < current.items[0]:
                    return self._retrieveNode(key, current.left_child)
                elif current.items[0] < key < current.items[1]:
                    return self._retrieveNode(key, current.middle_child)
                elif key > current.items[1]:
                    return self._retrieveNode(key, current.right_child)
            if current.type == "FourNode":
                if key < current.items[0]:
                    return self._retrieveNode(key, current.leftest_child)
                elif current.items[0] < key < current.items[1]:
                    return self._retrieveNode(key, current.left_child)
                elif current.items[1] < key < current.items[2]:
                    return self._retrieveNode(key, current.right_child)
                elif key > current.items[2]:
                    return self._retrieveNode(key, current.rightest_child)

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
                if key == current.items[0]:
                    return current.items[0], True
                elif key < current.items[0]:
                    return self._retrieve(key, current.left_child)
                elif key > current.items[0]:
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
            if current.type == "FourNode":
                if key == current.items[0]:
                    return current.items[0], True
                elif key == current.items[1]:
                    return current.items[1], True
                elif key == current.items[2]:
                    return current.items[2], True

                elif key < current.items[0]:
                    return self._retrieve(key, current.leftest_child)
                elif current.items[0] < key < current.items[1]:
                    return self._retrieve(key, current.left_child)
                elif current.items[1] < key < current.items[2]:
                    return self._retrieve(key, current.right_child)
                elif key > current.items[2]:
                    return self._retrieve(key, current.rightest_child)

    def inorderTraverse(self, func):
        self._inorder(self.root, func)

    def _inorder(self, current, func):
        if current is not None:
            if current.type == "TwoNode":
                self._inorder(current.left_child, func)
                func(current.items[0])
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

    def findSuccessor(self, key):
        keys = list()
        self._inorder(self.root, keys.append)
        key_index = keys.index(key)

        if key == keys[-1]:  # Key doesn't have an inorder successor
            return None
        else:
            return keys[key_index + 1]

    def save(self):
        return self._save(self.root)

    def _save(self, current):
        if current is None:
            return "None"

        if current.type == "TwoNode":
            result = "{'root': " + str(current.items)
            left_child = self._save(current.left_child)
            right_child = self._save(current.right_child)

            if left_child != "None" or right_child != "None":
                result += ", 'children': [" + left_child + ", " + right_child + "]"

        elif current.type == "ThreeNode":
            result = "{'root': " + str(current.items)
            left_child = self._save(current.left_child)
            middle_child = self._save(current.middle_child)
            right_child = self._save(current.right_child)

            if left_child != "None" or right_child != "None" or middle_child != "None":
                result += ", 'children': [" + left_child + ", " + middle_child + ", " + right_child + "]"

        elif current.type == "FourNode":
            result = "{'root': " + str(current.items)
            leftest_child = self._save(current.leftest_child)
            left_child = self._save(current.left_child)
            right_child = self._save(current.right_child)
            rightest_child = self._save(current.rightest_child)

            if leftest_child != "None" or left_child != "None" or right_child != "None" or rightest_child != "None":
                result += ", 'children': [" + leftest_child + ", " + left_child + ", " + right_child + ", " + rightest_child + "]"

        result += "}"
        return result

    def load(self, tree):
        self.root = self._load(tree)

    def _load(self, tree):
        if tree is None:
            return None

        root_list = tree['root']
        nr_of_root_items = root_list.__len__()

        if nr_of_root_items == 1:
            root = TwoNode()
            root.items = root_list
        elif nr_of_root_items == 2:
            root = ThreeNode()
            root.items = root_list
        elif nr_of_root_items == 3:
            root = FourNode()
            root.items = root_list

        if 'children' in tree and tree['children'] is not None:

            if nr_of_root_items == 1:
                left_child = self._load(tree['children'][0])
                right_child = self._load(tree['children'][1])

                root.left_child = left_child
                root.left_child.parent = root

                root.right_child = right_child
                root.right_child.parent = root

            elif nr_of_root_items == 2:
                left_child = self._load(tree['children'][0])
                middle_child = self._load(tree['children'][1])
                right_child = self._load(tree['children'][2])

                root.left_child = left_child
                root.left_child.parent = root

                root.middle_child = middle_child
                root.middle_child.parent = root

                root.right_child = right_child
                root.right_child.parent = root

            elif nr_of_root_items == 3:
                leftest_child = self._load(tree['children'][0])
                left_child = self._load(tree['children'][1])
                right_child = self._load(tree['children'][2])
                rightest_child = self._load(tree['children'][3])

                root.leftest_child = leftest_child
                root.leftest_child.parent = root

                root.left_child = left_child
                root.left_child.parent = root

                root.right_child = right_child
                root.right_child.parent = root

                root.rightest_child = rightest_child
                root.rightest_child.parent = root

        return root

