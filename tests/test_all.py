import unittest
from test_dummy_entity import DummyEntityTest
from test_entity_and import EntityAndTest
from test_entity_or import EntityOrTest
from test_entity_first import EntityFirstTest
from test_entity_concat import EntityConcatTest
from test_entity_sum import EntitySumTest
from test_entity_mult import EntityMultTest
from test_es_email_patterns import EmailPatternsTest
from test_es_phone_patterns import PhonePatternsTest


if __name__ == '__main__':
    suites = [
        unittest.TestLoader().loadTestsFromTestCase(DummyEntityTest),
        unittest.TestLoader().loadTestsFromTestCase(EntityAndTest),
        unittest.TestLoader().loadTestsFromTestCase(EntityOrTest),
        unittest.TestLoader().loadTestsFromTestCase(EntityFirstTest),
        unittest.TestLoader().loadTestsFromTestCase(EntityConcatTest),
        unittest.TestLoader().loadTestsFromTestCase(EntitySumTest),
        unittest.TestLoader().loadTestsFromTestCase(EntityMultTest),
        unittest.TestLoader().loadTestsFromTestCase(EmailPatternsTest),
        unittest.TestLoader().loadTestsFromTestCase(PhonePatternsTest),
    ]
    suite = unittest.TestSuite(suites)
    unittest.TextTestRunner(verbosity=2).run(suite)
