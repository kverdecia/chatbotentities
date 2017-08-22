import unittest
from chatbotentities.extractor import EntityOr
from dummy import DummyEntity


class EntityOrTest(unittest.TestCase):
    def test_constructor(self):
        self.assertRaises(TypeError, lambda: EntityOr())
        self.assertRaises(TypeError, lambda: EntityOr(DummyEntity(None)))
        self.assertRaises(TypeError, lambda: EntityOr(DummyEntity(None), None))
        left = DummyEntity(1)
        right = DummyEntity(2)
        entity = EntityOr(left, right)
        self.assertIs(entity.left, left)
        self.assertIs(entity.right, right)

    def test_none_none(self):
        left = DummyEntity(None)
        right = DummyEntity(None)
        entity = EntityOr(left, right)
        self.assertIsNone(entity(''))
        self.assertListEqual(entity('', 'abc'), ['abc'])

    def test_value_none(self):
        left = DummyEntity(1)
        right = DummyEntity(None)
        entity = EntityOr(left, right)
        self.assertListEqual(entity(''), [1])
        self.assertListEqual(entity('', 'abc'), [1])

    def test_none_value(self):
        left = DummyEntity(None)
        right = DummyEntity(1)
        entity = EntityOr(left, right)
        self.assertListEqual(entity(''), [1])
        self.assertListEqual(entity('', 'abc'), ['abc'])
        
    def test_value_value(self):
        left = DummyEntity(1)
        right = DummyEntity(2)
        entity = EntityOr(left, right)
        self.assertListEqual(entity(''), [1])
        self.assertListEqual(entity('', 'abc'), [1])
        
    def test_list_none(self):
        left = DummyEntity([1, 2])
        right = DummyEntity(None)
        entity = EntityOr(left, right)
        self.assertListEqual(entity(''), [1, 2])
        self.assertListEqual(entity('', 'abc'), [1, 2])
        
    def test_none_list(self):
        left = DummyEntity(None)
        right = DummyEntity([1, 2])
        entity = EntityOr(left, right)
        self.assertListEqual(entity(''), [1, 2])
        self.assertListEqual(entity('', 'abc'), ['abc'])

    def test_list_list(self):
        left = DummyEntity([1, 2])
        right = DummyEntity([3, 4])
        entity = EntityOr(left, right)
        self.assertListEqual(entity(''), [1, 2])
        self.assertListEqual(entity('', 'abc'), [1, 2])


if __name__ == '__main__':
    unittest.main()
