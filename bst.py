from __future__ import print_function

class Node:

    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

    # Insert a new node
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)
        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)
        else:
            pass

    # Returns True if it finds the node for a given value.
    # Otherwise, returns False
    def search(self, value):
        if self.value == value:
            return True
        elif value < self.value:
            return self.left.search(value) if self.left else False
        else:
            return self.right.search(value) if self.right else False


    # Returns the node (and its parent) for a given value
    def __find(self, value,parent=None):
        if self.value == value:
            return self,parent
        elif value < self.value:
            return self.left.__find(value,self)
        else:
            return self.right.__find(value,self)

    # Returns the leftmost node (and its parent)
    def __leftistElem(self, parent=None):
        if not self.left:
            return self,parent
        else:
            return self.left.__leftistElem(self)

    # Check if a node has a left branch
    def __hasLeftBranch(self):
        return True if self.left else False

    # Check if a node has a right branch
    def __hasRightBranch(self):
        return True if self.right else False

    # Delete the r(oot) element
    def __deleteRoot(self):
        r = self

        # Case: root element has both left and right branches
        #
        #        r(oot)                    z = min(b)
        #        /    \                  /   \
        #      a       b                a     b_
        #     . .     . .    =>       . .     . .
        #    .   .   .   .           .   .   .   .
        #   .     . .     .         .     . .     .
        if r.__hasLeftBranch() and r.__hasRightBranch():
            a,b = r.left,r.right

            # Get the leftmost element in the subtree b
            leftist, leftistP = b.__leftistElem()
            y = leftist.right
            if b == leftist:
                b_ = b.right
            else:
                b_ = b
                leftistP.left = y

            z = Node(leftist.value, a, b_)
            del leftist
            return z

        # Case: root element has only a left branch
        #
        #        r(oot)               a
        #        /                   . .
        #      a                    .   .
        #     . .         =>       .     .
        #    .   .
        #   .     .
        elif r.__hasLeftBranch():
            return r.left

        # Case: root element has only a right branch
        #
        #   r(oot)                      b
        #       \                      . .
        #        b                    .   .
        #       . .         =>       .     .
        #      .   .
        #     .     .
        elif r.__hasRightBranch():
            return r.right

        # Case: root is leaf
        #
        #   r(oot)         =>      < >
        else:
            return None

    def delete(self, value):
        if self.search(value):
            delElem, parent = self.__find(value)
            updated = delElem.__deleteRoot()
            del delElem
            if parent:
                if value < parent.value:
                    parent.left = updated
                else:
                    parent.right = updated
                return self
            else:
                return updated
        return self


    def show(self,cs=0):
        print("  "*cs,self.value)
        if self.left:
            self.left.show(cs+1)
        if self.right:
            self.right.show(cs+1)


class BST:

    def __init__(self):
        """Initialize an empty Binary Tree"""
        self.root = None

    def insert(self,value):
        """Insert a node into the Binary Tree"""
        if self.root:
            self.root.insert(value)
        else:
            self.root = Node(value)

    def search(self,value):
        """Search for a node (Predicate)"""
        if self.root:
            return self.root.search(value)
        else:
            return False

    def delete(self,value):
        """Delete a node"""
        if self.root:
            self.root = self.root.delete(value)

    def show(self):
        """Show the Tree"""
        if self.root:
            self.root.show()
        else:
            print(self.root)
