import unittest
from chatbotentities.extractor import EntityAnd
from dummy import DummyEntity


class EntitySumTest(unittest.TestCase):
    def test_sum_2(self):
        dummy1 = DummyEntity(1)
        dummy2 = DummyEntity(2)
        entity = dummy1 + dummy2
        self.assertIsInstance(entity, EntityAnd)
        self.assertIs(entity.left, dummy1)
        self.assertIs(entity.right, dummy2)

    def test_sum_3(self):
        dummy1 = DummyEntity(1)
        dummy2 = DummyEntity(2)
        dummy3 = DummyEntity(3)
        entity = dummy1 + dummy2 + dummy3
        self.assertIsInstance(entity, EntityAnd)
        self.assertIsInstance(entity.left, EntityAnd)
        self.assertIs(entity.left.left, dummy1)
        self.assertIs(entity.left.right, dummy2)
        self.assertIs(entity.right, dummy3)
        
    def test_eval_3(self):
        dummy1 = DummyEntity(1)
        dummy2 = DummyEntity(2)
        dummy3 = DummyEntity(3)
        dummy_none = DummyEntity(None)
        entity = dummy1 + dummy2 + dummy3
        self.assertListEqual(entity(''), [1, 2, 3])
        self.assertListEqual(entity('', 'abc'), [1, 2, 3])
        entity2 = dummy1 + dummy_none + dummy3
        self.assertListEqual(entity2(''), [1, 3])
        self.assertListEqual(entity2('', 'abc'), [1, 'abc', 3])


if __name__ == '__main__':
    unittest.main()
