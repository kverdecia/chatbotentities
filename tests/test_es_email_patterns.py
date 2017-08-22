# -*- coding: utf-8 -*-
import unittest
from pattern.es import parsetree
from pattern.search import Pattern
from chatbotentities.es import EmailPatterns


def sentence(text):
    return parsetree(text)[0]


class EmailPatternsTest(unittest.TestCase):
    def setUp(self):
        self.patterns = EmailPatterns.patterns()
        self.get_entities = lambda text: self.patterns(sentence(text))

    def tearDown(self):
        self.patterns = None
        self.get_entities = None
        
    def test_parent(self):
        parent = EmailPatterns.parent
        self.assertIsNone(parent('adsfa'))
        self.assertIsNone(parent('abc@ass.sss.'))
        self.assertIsNotNone(parent('usuario@prueba.com'))
        self.assertListEqual(parent('usuario@prueba.com'), ['email'])
        self.assertListEqual(parent(u'electronico'), ['electronico'])
        self.assertListEqual(parent(u'electrónico'), ['electronico'])
        self.assertListEqual(parent(u'escribir'), ['escribir'])
        self.assertListEqual(parent(u'escribeme'), ['escribir'])
        self.assertListEqual(parent(u'escribime'), ['escribir'])
        self.assertListEqual(parent(u'escribirme'), ['escribir'])
        self.assertListEqual(parent(u'contactame'), ['escribir'])
        self.assertListEqual(parent(u'contáctame'), ['escribir'])
        self.assertListEqual(parent(u'contactar'), ['escribir'])
        self.assertListEqual(parent(u'contactarme'), ['escribir'])
        
    def test_taxonomy(self):
        taxonomy = EmailPatterns.taxonomy()
        self.assertListEqual(taxonomy.parents('asdfkasdfasdf'), [])
        self.assertListEqual(taxonomy.parents('usuario@prueba.com.'), [])
        self.assertListEqual(taxonomy.parents('usuario@prueba.com'), ['email'])
        self.assertListEqual(taxonomy.parents(u'electronico'), ['electronico'])
        self.assertListEqual(taxonomy.parents(u'electrónico'), ['electronico'])
        self.assertListEqual(taxonomy.parents(u'escribir'), ['escribir'])
        self.assertListEqual(taxonomy.parents(u'escribeme'), ['escribir'])
        self.assertListEqual(taxonomy.parents(u'escribime'), ['escribir'])
        self.assertListEqual(taxonomy.parents(u'escribirme'), ['escribir'])
        self.assertListEqual(taxonomy.parents(u'contactame'), ['escribir'])
        self.assertListEqual(taxonomy.parents(u'contáctame'), ['escribir'])
        self.assertListEqual(taxonomy.parents(u'contactar'), ['escribir'])
        self.assertListEqual(taxonomy.parents(u'contactarme'), ['escribir'])

    def test_no_match_pattern(self):
        self.fail("Implement this test")
        
    def test_match_mal_correo_electronico(self):
        taxonomy = EmailPatterns.taxonomy()
        pattern = Pattern.fromstring(u'mal el|mi correo ELECTRONICO?', taxonomy=taxonomy)
        self.assertIsNotNone(pattern.match(parsetree(u"está mal mi correo")))
        self.assertIsNotNone(pattern.match(parsetree(u"escribi mal mi correo electronico")))
        self.assertIsNotNone(pattern.match(parsetree(u"te dije mal el correo")))

    def test_match_correo_electronico_esta_mal(self):
        taxonomy = EmailPatterns.taxonomy()
        pattern = Pattern.fromstring(u'correo ELECTRONICO? es|esta|está mal|incorrecto', taxonomy=taxonomy)
        self.assertIsNotNone(parsetree(u"el correo es incorrecto"))
        self.assertIsNotNone(parsetree(u"mi correo electrónico está mal"))
        self.assertIsNotNone(parsetree(u"disculpa pero mi correo está incorrecto"))
        
    def test_match_correo_electronico_no_esta_bien(self):
        taxonomy = EmailPatterns.taxonomy()
        pattern = Pattern.fromstring(u'correo ELECTRONICO? no es|esta|está bien|correcto', taxonomy=taxonomy)
        self.assertIsNotNone(parsetree(u"ese correo no es correcto"))
        self.assertIsNotNone(parsetree(u"ese correo no esta correcto"))
        self.assertIsNotNone(parsetree(u"ese correo no está bien"))
        self.assertIsNotNone(parsetree(u"mi correo electrónico no está bien"))
    
    def test_match_no_es_mi_correo(self):
        taxonomy = EmailPatterns.taxonomy()
        pattern = Pattern.fromstring(u'no es mi correo ELECTRONICO?', taxonomy=taxonomy)
        self.assertIsNotNone(pattern.match(parsetree(u"ese no es mi correo")))
        self.assertIsNotNone(pattern.match(parsetree(u"ese no es mi correo electronico")))
    
    def test_match_correo_no_es_email(self):
        taxonomy = EmailPatterns.taxonomy()
        pattern = Pattern.fromstring(u'correo ELECTRONICO? no es {EMAIL}', taxonomy=taxonomy)
        self.assertIsNotNone(pattern.match(parsetree(u"mi correo no es usuario@prueba.com")))
        self.assertIsNotNone(pattern.match(parsetree(u"el correo electrónico no es usuario@prueba.com")))
        
    def test_match_correo_es_email(self):
        taxonomy = EmailPatterns.taxonomy()
        pattern = Pattern.fromstring(u'correo ELECTRONICO? es? {EMAIL}', taxonomy=taxonomy)
        self.assertIsNotNone(pattern.match(parsetree(u"correo usuario@prueba.com")))
        self.assertIsNotNone(pattern.match(parsetree(u"el correo electrónico es usuario@prueba.com")))
        tree = parsetree(u"el correo es abc")
        print repr(tree)
        print repr(pattern.match(parsetree("esto es una prueba")))
        self.assertIsNotNone(pattern.match(parsetree(u"el correo es abc")))
        self.assertIsNotNone(pattern.match(parsetree(u"el correo es usuario@prueba.")))


if __name__ == '__main__':
    unittest.main()
