import unittest
from chatbotentities.extractor import EntityConcat
from dummy import DummyEntity


class EntityConcatTest(unittest.TestCase):
    def test_constructor(self):
        dummy1 = DummyEntity(None)
        dummy2 = DummyEntity(None)
        dummy3 = DummyEntity(None)
        self.assertRaises(TypeError, lambda: EntityConcat())
        self.assertRaises(TypeError, lambda: EntityConcat(None))
        self.assertRaises(TypeError, lambda: EntityConcat(dummy1, None, dummy2, dummy3))
        EntityConcat(dummy1, dummy2, dummy3)

    def test_none_none_none(self):
        dummy1 = DummyEntity(None)
        dummy2 = DummyEntity(None)
        dummy3 = DummyEntity(None)
        entity = EntityConcat(dummy1, dummy2, dummy3)
        self.assertIsNone(entity(''))
        self.assertListEqual(entity('', 'abc'), ['abc', 'abc', 'abc'])

    def test_value_none_none(self):
        dummy1 = DummyEntity(1)
        dummy2 = DummyEntity(None)
        dummy3 = DummyEntity(None)
        entity = EntityConcat(dummy1, dummy2, dummy3)
        self.assertListEqual(entity(''), [1])
        self.assertListEqual(entity('', 'abc'), [1, 'abc', 'abc'])

    def test_value_value_none(self):
        dummy1 = DummyEntity(1)
        dummy2 = DummyEntity(2)
        dummy3 = DummyEntity(None)
        entity = EntityConcat(dummy1, dummy2, dummy3)
        self.assertListEqual(entity(''), [1, 2])
        self.assertListEqual(entity('', 'abc'), [1, 2, 'abc'])

    def test_value_none_value(self):
        dummy1 = DummyEntity(1)
        dummy2 = DummyEntity(None)
        dummy3 = DummyEntity(3)
        entity = EntityConcat(dummy1, dummy2, dummy3)
        self.assertListEqual(entity(''), [1, 3])
        self.assertListEqual(entity('', 'abc'), [1, 'abc', 3])

    def test_value_value_value(self):
        dummy1 = DummyEntity(1)
        dummy2 = DummyEntity(2)
        dummy3 = DummyEntity(3)
        entity = EntityConcat(dummy1, dummy2, dummy3)
        self.assertListEqual(entity(''), [1, 2, 3])
        self.assertListEqual(entity('', 'abc'), [1, 2, 3])

    def test_none_value_value(self):
        dummy1 = DummyEntity(None)
        dummy2 = DummyEntity(2)
        dummy3 = DummyEntity(3)
        entity = EntityConcat(dummy1, dummy2, dummy3)
        self.assertListEqual(entity(''), [2, 3])
        self.assertListEqual(entity('', 'abc'), ['abc', 2, 3])

    def test_none_list_value(self):
        dummy1 = DummyEntity(None)
        dummy2 = DummyEntity([2, 3, 4])
        dummy3 = DummyEntity(5)
        entity = EntityConcat(dummy1, dummy2, dummy3)
        self.assertListEqual(entity(''), [2, 3, 4, 5])
        self.assertListEqual(entity('', 'abc'), ['abc', 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
