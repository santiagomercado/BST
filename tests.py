import unittest

from bst import BST


class TestBST(unittest.TestCase):

    def test_insert(self):
        tree = BST()
        for val in [5, 2, 9, 3, 4, 1, 6, 10, 8, 7]:
            tree.insert(val)
        self.assertEqual(tree.root.value,5)
        self.assertEqual(tree.root.left.value,2)
        self.assertEqual(tree.root.right.value,9)
        self.assertEqual(tree.root.left.left.value,1)
        self.assertEqual(tree.root.left.right.value,3)
        self.assertEqual(tree.root.right.left.value,6)
        self.assertEqual(tree.root.right.right.value,10)
        self.assertEqual(tree.root.left.right.right.value,4)
        self.assertEqual(tree.root.right.left.right.value,8)
        self.assertEqual(tree.root.right.left.right.left.value,7)


    def test_search(self):
        tree = BST()
        for val in [5, 2, 9, 3, 4, 1, 6, 10, 8, 7]:
            tree.insert(val)
        for val in [5, 2, 9, 3, 4, 1, 6, 10, 8, 7]:
            self.assertTrue(tree.search(val))
        self.assertFalse(tree.search(-10))
        self.assertFalse(tree.search(25))
        self.assertFalse(tree.search(19))

    def test_delete(self):
        tree = BST()
        for val in [5, 2, 9, 3, 4, 1, 6, 10, 8, 7]:
            tree.insert(val)

        tree.delete(6)
        self.assertEqual(tree.root.value,5)
        self.assertEqual(tree.root.left.value,2)
        self.assertEqual(tree.root.right.value,9)
        self.assertEqual(tree.root.left.left.value,1)
        self.assertEqual(tree.root.left.right.value,3)
        self.assertEqual(tree.root.right.left.value,8)
        self.assertEqual(tree.root.right.right.value,10)
        self.assertEqual(tree.root.left.right.right.value,4)
        self.assertEqual(tree.root.right.left.left.value,7)


        tree.delete(9)
        self.assertEqual(tree.root.value,5)
        self.assertEqual(tree.root.left.value,2)
        self.assertEqual(tree.root.right.value,10)
        self.assertEqual(tree.root.left.left.value,1)
        self.assertEqual(tree.root.left.right.value,3)
        self.assertEqual(tree.root.right.left.value,8)
        self.assertEqual(tree.root.left.right.right.value,4)
        self.assertEqual(tree.root.right.left.left.value,7)

        tree.delete(1)
        self.assertEqual(tree.root.value,5)
        self.assertEqual(tree.root.left.value,2)
        self.assertEqual(tree.root.right.value,10)
        self.assertEqual(tree.root.left.right.value,3)
        self.assertEqual(tree.root.right.left.value,8)
        self.assertEqual(tree.root.left.right.right.value,4)
        self.assertEqual(tree.root.right.left.left.value,7)

        tree.delete(3)
        self.assertEqual(tree.root.value,5)
        self.assertEqual(tree.root.left.value,2)
        self.assertEqual(tree.root.right.value,10)
        self.assertEqual(tree.root.left.right.value,4)
        self.assertEqual(tree.root.right.left.value,8)
        self.assertEqual(tree.root.right.left.left.value,7)

        tree.delete(7)
        self.assertEqual(tree.root.value,5)
        self.assertEqual(tree.root.left.value,2)
        self.assertEqual(tree.root.right.value,10)
        self.assertEqual(tree.root.left.right.value,4)
        self.assertEqual(tree.root.right.left.value,8)

        tree.delete(2)
        self.assertEqual(tree.root.value,5)
        self.assertEqual(tree.root.left.value,4)
        self.assertEqual(tree.root.right.value,10)
        self.assertEqual(tree.root.right.left.value,8)

        tree.delete(10)
        self.assertEqual(tree.root.value,5)
        self.assertEqual(tree.root.left.value,4)
        self.assertEqual(tree.root.right.value,8)

        tree.delete(5)
        self.assertEqual(tree.root.value,8)
        self.assertEqual(tree.root.left.value,4)

        tree.delete(4)
        self.assertEqual(tree.root.value,8)
        tree.delete(8)
        self.assertIsNone(tree.root)

if __name__ == '__main__':
    unittest.main()
