import unittest
from chatbotentities.extractor import EntityOr
from dummy import DummyEntity


class EntityMultTest(unittest.TestCase):
    def test_entity_mult_2(self):
        dummy1 = DummyEntity(1)
        dummy2 = DummyEntity(2)
        entity = dummy1 * dummy2
        self.assertIsInstance(entity, EntityOr)
        self.assertIs(entity.left, dummy1)
        self.assertIs(entity.right, dummy2)

    def test_entity_mult_3(self):
        dummy1 = DummyEntity(1)
        dummy2 = DummyEntity(2)
        dummy3 = DummyEntity(3)
        entity = dummy1 * dummy2 * dummy3
        self.assertIsInstance(entity, EntityOr)
        self.assertIsInstance(entity.left, EntityOr)
        self.assertIs(entity.left.left, dummy1)
        self.assertIs(entity.left.right, dummy2)
        self.assertIs(entity.right, dummy3)


if __name__ == '__main__':
    unittest.main()
