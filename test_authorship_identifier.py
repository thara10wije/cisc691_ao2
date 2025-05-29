import unittest
import improved_authorship_identification as auth

class TestAuthorshipIdentifier(unittest.TestCase):

    def test_clean_word(self):
        '''
        Test teh clean_word function.
        '''
        self.assertEqual(auth.clean_word("Hello!"), "hello")
        self.assertEqual(auth.clean_word("Pearl!"), "pearl")
        self.assertEqual(auth.clean_word('card-board'), 'card-board')

    def test_average_word_length(self):
        '''
        test the avearage word length function
        '''
        self.assertEqual(auth.average_word_length("Hello!"), 5)
        self.assertEqual(auth.average_word_length("To be, or not   to be"), 13/6)
        self.assertEqual(auth.average_word_length('A pearl! Pearl! Lustrous pearl! \
Rare. What a nice find.'), 4.1)
        
    def test_different_to_total(self):
        self.assertEqual( auth.different_to_total('A pearl! Pearl! Lustrous pearl! \
Rare. What a nice find.'), 0.7)
        
    def test_exactly_once_to_total(self):
        self.assertEqual(auth.exactly_once_to_total('A pearl! Pearl! Lustrous pearl! \
Rare. What a nice find.'), 0.5)
    
    def test_split_string(self):
        self.assertEqual(auth.split_string('one*two[three', '*['), ['one', 'two', 'three'])

    def test_get_sentences(self):
        self.assertEqual(auth.get_sentences('A pearl! Pearl! Lustrous pearl! Rare. \
What a nice find.'),['A pearl', 'Pearl', 'Lustrous pearl', 'Rare', \
'What a nice find'])
        
    def test_average_sentence_length(self):
        self.assertEqual(auth.average_sentence_length('A pearl! Pearl! Lustrous pearl! \
Rare. What a nice find.'), 2.0)
        
    def test_get_phrases(self):
        self.assertEqual(auth.get_phrases('Lustrous pearl, Rare, What a nice find'), 
                         ['Lustrous pearl', 'Rare', 'What a nice find'])
        
    def test_average_sentence_complexity(self):
        self.assertEqual(auth.average_sentence_complexity('A pearl! Pearl! Lustrous \
pearl! Rare. What a nice find.'), 1.0)
        
    def test_make_signature(self):
        self.assertEqual(auth.make_signature('A pearl! Pearl! Lustrous pearl! \
Rare, what a nice find.'), [4.1, 0.7, 0.5, 2.5, 1.25])
        

    def test_get_score(self):
        self.assertEqual(auth.get_score([4.6, 0.1, 0.05, 10, 2],\
                  [4.3, 0.1, 0.04, 16, 4],\
                  [11, 33, 50, 0.4, 4]), 14.2)
        
    def test_get_contraction_density(self):
        self.assertEqual(auth.contraction_density("I'm not sure if I'd like it."), 2/7)

if __name__ == '__main__':
    unittest.main()