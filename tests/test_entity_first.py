import unittest
from chatbotentities.extractor import AbstractEntity, EntityFirst
from dummy import DummyEntity


class EntityFirstTest(unittest.TestCase):
    def test_constructor(self):
        dummy1 = DummyEntity(None)
        dummy2 = DummyEntity(None)
        dummy3 = DummyEntity(None)        
        self.assertRaises(TypeError, lambda: EntityFirst())
        self.assertRaises(TypeError, lambda: EntityFirst(dummy1, None, dummy2))
        self.assertRaises(TypeError, lambda: EntityFirst([dummy1, dummy2, dummy3]))
        entity_none = EntityFirst(dummy1, dummy2, dummy3)
        
    def test_none_none_none(self):
        dummy1 = DummyEntity(None)
        dummy2 = DummyEntity(None)
        dummy3 = DummyEntity(None)
        entity = EntityFirst(dummy1, dummy2, dummy3)
        self.assertIsNone(entity(''))
        self.assertListEqual(entity('', 'abc'), ['abc'])
        
    def test_none_value_none(self):
        dummy1 = DummyEntity(None)
        dummy2 = DummyEntity(2)
        dummy3 = DummyEntity(None)
        entity = EntityFirst(dummy1, dummy2, dummy3)
        self.assertListEqual(entity(''), [2])
        self.assertListEqual(entity('', 'abc'), ['abc'])
        
    def test_none_value_value(self):
        dummy1 = DummyEntity(None)
        dummy2 = DummyEntity(2)
        dummy3 = DummyEntity(3)
        entity = EntityFirst(dummy1, dummy2, dummy3)
        self.assertListEqual(entity(''), [2])
        self.assertListEqual(entity('', 'abc'), ['abc'])
        
    def test_none_list_value(self):
        dummy1 = DummyEntity(None)
        dummy2 = DummyEntity([1, 2, 3])
        dummy3 = DummyEntity(5)
        entity = EntityFirst(dummy1, dummy2, dummy3)
        self.assertListEqual(entity(''), [1])
        self.assertListEqual(entity('', 'abc'), ['abc'])


if __name__ == '__main__':
    unittest.main()
