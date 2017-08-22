import unittest
from dummy import DummyEntity


class DummyEntityTest(unittest.TestCase):
    def test_constructor(self):
        self.assertRaises(TypeError, lambda: DummyEntity())

    def test_entity_none(self):
        entity = DummyEntity(None)
        self.assertIsNone(entity(''))
        
    def test_entity_value(self):
        entity = DummyEntity(5)
        self.assertListEqual(entity(''), [5])
        
    def test_entity_list(self):
        entity = DummyEntity([1, 2, 3])
        self.assertListEqual(entity(''), [1, 2, 3])
        
    def test_entity_default(self):
        entity = DummyEntity(None)
        self.assertListEqual(entity('', 'abc'), ['abc'])
        entity = DummyEntity(5)
        self.assertListEqual(entity('', 'abc'), [5])


if __name__ == '__main__':
    unittest.main()
