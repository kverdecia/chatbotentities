# -*- coding: utf-8 -*-
import unittest
from pattern.es import parsetree
from pattern.search import Pattern
from chatbotentities.es import PhonePatterns


def sentence(text):
    return parsetree(text)[0]


class PhonePatternsTest(unittest.TestCase):
    def setUp(self):
        self.patterns = PhonePatterns.patterns()
        self.get_entities = lambda text: self.patterns(sentence(text))

    def tearDown(self):
        self.patterns = None
        self.get_entities = None

    def test_parent(self):
        parent = PhonePatterns.parent
        self.assertIsNone(parent('2323'))
        self.assertIsNone(parent('asdf'))
        self.assertListEqual(parent('787878346'), ['phone'])
        self.assertListEqual(parent(u'numero'), ['numero'])
        self.assertListEqual(parent(u'número'), ['numero'])
        self.assertListEqual(parent(u'telefono'), ['telefono'])
        self.assertListEqual(parent(u'teléfono'), ['telefono'])
        self.assertListEqual(parent(u'celular'), ['telefono'])
        self.assertListEqual(parent(u'mobil'), ['telefono'])
        self.assertListEqual(parent(u'móbil'), ['telefono'])
        self.assertListEqual(parent(u'mobile'), ['telefono'])
        self.assertListEqual(parent(u'cel'), ['telefono'])
        self.assertListEqual(parent(u'telefonico'), ['telefono'])
        self.assertListEqual(parent(u'telefónico'), ['telefono'])

    def test_taxonomy(self):
        taxonomy = PhonePatterns.taxonomy()
        self.assertListEqual(taxonomy.parents('2342'), [])
        self.assertListEqual(taxonomy.parents('234343432'), ['phone'])
        self.assertListEqual(taxonomy.parents(u'numero'), ['numero'])
        self.assertListEqual(taxonomy.parents(u'número'), ['numero'])
        self.assertListEqual(taxonomy.parents(u'telefono'), ['telefono'])
        self.assertListEqual(taxonomy.parents(u'teléfono'), ['telefono'])
        self.assertListEqual(taxonomy.parents(u'celular'), ['telefono'])
        self.assertListEqual(taxonomy.parents(u'mobil'), ['telefono'])
        self.assertListEqual(taxonomy.parents(u'móbil'), ['telefono'])
        self.assertListEqual(taxonomy.parents(u'mobile'), ['telefono'])
        self.assertListEqual(taxonomy.parents(u'cel'), ['telefono'])
        self.assertListEqual(taxonomy.parents(u'telefonico'), ['telefono'])
        self.assertListEqual(taxonomy.parents(u'telefónico'), ['telefono'])

    def test_no_match_pattern(self):
        extract = self.get_entities
        self.assertIsNone(extract(u"mi telefono"))
        self.assertIsNone(extract(u"ese es mi telefono"))
        self.assertIsNone(extract(u"llámame"))
        self.assertIsNone(extract(u"mi nombre es juan"))

    def test_match_mal_el_numero(self):
        taxonomy = PhonePatterns.taxonomy()
        pattern = Pattern.fromstring(u'mal el|en TELEFONO|NUMERO', taxonomy=taxonomy)
        self.assertIsNotNone(pattern.match(u"mal el número"))
        self.assertIsNotNone(pattern.match(u"mal el telefono"))
        self.assertIsNotNone(pattern.match(u"te dije mal el número"))
        self.assertIsNotNone(pattern.match(u"te dije mal el teléfono"))
        self.assertIsNotNone(pattern.match(u"disculpa, está mal el número"))
        self.assertIsNotNone(pattern.match(u"disculpa, escribí mal el número"))
        pattern = Pattern.fromstring(u'mal el NUMERO de? TELEFONO', taxonomy=taxonomy)
        self.assertIsNotNone(pattern.match(u"mal el número de telefono"))
        self.assertIsNotNone(pattern.match(u"mal el número telefono"))
        self.assertIsNotNone(pattern.match(u"mal el número telefónico"))
        self.assertIsNotNone(pattern.match(u"mal el número de celular"))
        self.assertIsNotNone(pattern.match(u"escribí mal el número de celular"))

    def test_match_telefono_esta_mal(self):
        taxonomy = PhonePatterns.taxonomy()
        pattern = Pattern.fromstring(u'TELEFONO|NUMERO esta|está mal', taxonomy=taxonomy)
        self.assertIsNotNone(pattern.match(u"el telefono esta mal"))
        self.assertIsNotNone(pattern.match(u"mi número telefónico está mal"))
        self.assertIsNotNone(pattern.match(u"mi numero está mal"))
        pattern = Pattern.fromstring(u'NUMERO de? TELEFONO esta|está mal', taxonomy=taxonomy)
        self.assertIsNotNone(pattern.match(u"mi número telefónico está mal"))

    def test_match_no_es_mi_numero(self):
        taxonomy = PhonePatterns.taxonomy()
        pattern = Pattern.fromstring(u'no es mi TELEFONO|NUMERO', taxonomy=taxonomy)
        self.assertIsNotNone(pattern.match(u"Ese no es mi número"))
        self.assertIsNotNone(pattern.match(u"Ese no es mi telefono"))
        pattern = Pattern.fromstring(u'no es mi NUMERO de? TELEFONO', taxonomy=taxonomy)
        self.assertIsNotNone(pattern.match(u"Ese no es mi número de teléfono"))
        self.assertIsNotNone(pattern.match(u"Ese no es mi número telefónico"))

    def test_match_numero_no_es_mi_phone(self):
        taxonomy = PhonePatterns.taxonomy()
        pattern = Pattern.fromstring(u'NUMERO|TELEFONO no es {PHONE}', taxonomy=taxonomy)
        pattern = Pattern.fromstring(u'NUMERO de TELEFONO no es {PHONE}', taxonomy=taxonomy)
        self.fail("Implement this test.")

    def test_match_numero_es_phone(self):
        taxonomy = PhonePatterns.taxonomy()
        pattern = Pattern.fromstring(u'TELEFONO|NUMERO es? {PHONE}', taxonomy=taxonomy)
        pattern = Pattern.fromstring(u'NUMERO de? TELEFONO es? {PHONE}', taxonomy=taxonomy)
        self.fail("Implement this test.")
        
    def test_match_phone(self):
        taxonomy = PhonePatterns.taxonomy()
        pattern = Pattern.fromstring(u'{PHONE}', taxonomy=taxonomy)
        self.assertIsNone(pattern.match(u"sdfsd"))
        self.assertIsNone(pattern.match(u"3333"))
        self.assertIsNotNone(pattern.match(u"3333454544"))

    def test_match_patterns(self):
        patterns = PhonePatterns.patterns()
        self.assertIsNone(patterns(sentence('aldfjasldf')))
        #############################
        entities = patterns(sentence('mi telefono es 484848483'))
        self.assertIsNotNone(entities)
        self.assertEquals(len(entities), 1)
        self.assertEquals(entities[0]['value'], '484848483')
        self.assertEquals(entities[0]['entity_type'], 'phone')
        self.assertEquals(entities[0]['negation'], False)
        #############################
        entities = patterns(sentence('disculpa, está mal el número'))
        self.assertIsNotNone(entities)
        self.assertEquals(len(entities), 1)
        self.assertEquals('value' in entities[0], False)
        self.assertEquals(entities[0]['entity_type'], 'phone')
        self.assertEquals(entities[0]['negation'], True)


if __name__ == '__main__':
    unittest.main()
