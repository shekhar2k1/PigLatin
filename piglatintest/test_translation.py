import unittest

from piglatin import piglatin


class Testpiglatin(unittest.TestCase):

    def test_sanity_word(self):
        test_words = [
            ('banana', 'ananabay'),
            ('trash', 'ashtray'),
            ('happy', 'appyhay'),
            ('duck', 'uckday'),
            ('glove', 'oveglay'),
            ('eat', 'eatyay'),
            ('omelet', 'omeletyay'),
            ('are', 'areyay'),
        ]
        for word, expected in test_words:
            actual = piglatin.piglatin_word(word)
            self.assertEqual(
                actual,
                expected,
                msg='"{}" should translate to {}'.format(word, expected)
            )

    def test_para(self):
        text = (
            "Enter the English text here that you want translated into "
            "Pig Latin. This is accomplished via this  document and "
            "accompanying JavaScript program. Note that hyphenated words "
            "are treated as two words. Words may consist of alphabetic"
            )
        expected = (
            "enteryay ethay englishyay exttay erehay atthay ouyay antway anslatedtray intoyay "
            "igpay atinlay. isthay isyay accomplishedyay iavay isthay ocumentday andyay "
            "accompanyingyay avascriptjay ogrampray. otenay atthay enatedhyphay ordsway "
            "areyay eatedtray asyay otway ordsway. ordsway aymay onsistcay ofyay alphabeticyay"

        )
        self.maxDiff = None
        actual = piglatin.translate(text)
        self.assertEqual(actual.lower(), expected.lower())

    def test_vowel_sound(self):
        test_words = [
            ('hello', False),
            ('yay', False),
            ('an', True),
        ]
        for word, expected in test_words:
            actual = piglatin.check_if_starts_with_vowel(word)
            self.assertEqual(
                actual,
                expected,
                msg='"{}" should be {}'.format(word, expected)
            )


    def test_basic(self):
        text = "This is a test."
        expected = ('Isthay', 'isyay', 'ayay', 'esttay.')
        actual = piglatin.piglatin_para(text)
        self.assertEqual(tuple(actual), expected)


