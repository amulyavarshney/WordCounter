import wordCounter
import unittest

class Test(unittest.TestCase):
    word_counter = wordCounter.WordCounter('The quick brown fox jumps over the lazy dog')

    def test_word_count(self):
        self.assertEqual(self.word_counter.get_word_count(), 9)

    def test_count_insensitive(self):
        self.assertEqual(self.word_counter.get_count('the'), 2)

    def test_count_sensitive(self):
        self.assertEqual(self.word_counter.get_count('the', ignore_case=False), 1)

    def test_word_frequencies_insensitive(self):
        self.assertEqual(self.word_counter.get_word_frequencies(), {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1})
    
    def test_word_frequencies_sensitive(self):
        self.assertEqual(self.word_counter.get_word_frequencies(ignore_case=False), {'The': 1, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'the': 1, 'lazy': 1, 'dog': 1})

    def test_most_common_word_insensitive(self):
        self.assertEqual(self.word_counter.get_most_common_word(), ['the'])

    def test_most_common_word_sensitive(self):
        self.assertEqual(self.word_counter.get_most_common_word(ignore_case=False), ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'])

    def test_get_word_by_freq(self):
        self.assertEqual(self.word_counter.get_word_by_freq(2), ['the'])

    def test_get_word_by_freq(self):
        self.assertEqual(self.word_counter.get_word_by_freq(2, ignore_case=False), 'No word exists with count = 2')

if __name__ == '__main__':
    unittest.main()