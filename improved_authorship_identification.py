import string
import os
import sys
import csv
import os
import csv



def clean_word(word):
    """
    Return a sentence with all letters converted to lowercase, all punctuation stripped from the ends,
    and inner punctuation left untouched.
    
    Args:
    word (str): The word to be cleaned.
    
    Returns:
    str: The cleaned word. 

    >>> clean_word('card-board')
    'card-board' 
    """
    return word.lower().strip(string.punctuation)   


def average_word_length(text):
    """
    Calculate the average word length of the words in the text.

    Args:
    text (str): The input text.

    Returns:
    float: The average word length.

    >>> average_word_length('A pearl! Pearl! Lustrous pearl! \
Rare. What a nice find.')
    4.1
    """
    words = text.split()
    cleaned_words = [clean_word(word) for word in words]
    word_lengths = [len(word) for word in cleaned_words]
    
    if len(word_lengths) == 0:
        return 0
    
    return sum(word_lengths) / len(word_lengths)



def different_to_total(text):
    """
    Calculate the ratio of unique words to the total number of words in the text.
    
    Args:
    text (str): The input text.
    
    Returns:
    float: The ratio of unique words to the total number of words.

    >>> different_to_total('A pearl! Pearl! Lustrous pearl! \
Rare. What a nice find.')
    0.7
    """
    words = text.split()
    cleaned_words = [clean_word(word) for word in words if word.strip(string.punctuation)]
    
    unique_words = set(cleaned_words)
    
    if len(cleaned_words) == 0:
        return 0
    
    return len(unique_words) / len(cleaned_words)


def exactly_once_to_total(text):
    """
    Calculate the ratio of words that appear exactly once to the total number of words in the text.
    
    Args:
    text (str): The input text.
    
    Returns:
    float: The ratio of words that appear exactly once to the total number of words.

    >>> exactly_once_to_total('A pearl! Pearl! Lustrous pearl! \
Rare. What a nice find.')
    0.5
    """
    words = text.split()
    cleaned_words = [clean_word(word) for word in words if word.strip(string.punctuation)]
    
    word_count = {}
    for word in cleaned_words:
        word_count[word] = word_count.get(word, 0) + 1
    
    once_words = sum(1 for count in word_count.values() if count == 1)
    
    if len(cleaned_words) == 0:
        return 0
    
    return once_words / len(cleaned_words)



def split_string(text, separators):
    """
    Split the text into a list using any of the one-character separators and return the result.
    Remove spaces from the beginning and end of a string before adding it to the list.
    Do not include empty strings in the list.
    
    Args:
    text (str): The input text.
    separators (str): String of separator characters.
    
    Returns:
    list: The list of split strings.

    >>> split_string('one*two[three', '*[')
    ['one', 'two', 'three']
    """
    words = []        
    word = ''                
    for char in text:
        if char in separators:    
            word = word.strip()      
            if word != '':          
                words.append(word)      
            word = ''                 
        else:
            word += char           
    word = word.strip()      
    if word != '':          
        words.append(word)   
    return words 


def get_sentences(text):
    """
    Split the text into a list of sentences using '.', '?' or '!' as separators and return the result.
    
    Args:
    text (str): The input text.
    
    Returns:
    list: The list of sentences.

    >>> get_sentences('A pearl! Pearl! Lustrous pearl! Rare. \
What a nice find.')
    ['A pearl', 'Pearl', 'Lustrous pearl', 'Rare', \
'What a nice find']
    """
    return split_string(text, '.?!')

def average_sentence_length(text):
    """
    Calculate the average number of words per sentence in the given text.
    
    Args:
    text (str): The input text.
    
    Returns:
    float: The average number of words per sentence.

    >>> average_sentence_length('A pearl! Pearl! Lustrous pearl! \
Rare. What a nice find.')
    2.0
    """
    sentences = get_sentences(text)
    total_words = sum(len(split_string(sentence, string.whitespace)) for sentence in sentences if sentence.strip())
    total_sentences = len(sentences)
    if total_sentences == 0:
        return 0
    return total_words / total_sentences if total_sentences > 0 else 0


def get_phrases(sentence):
    """
    Split the text into a list of phrases using ',', ';' or ':' as separators and return the result.
    
    Args:
    text (str): The input text.
    
    Returns:
    list: The list of phrases.

    >>> get_phrases('Lustrous pearl, Rare, What a nice find')
    ['Lustrous pearl', 'Rare', 'What a nice find']
    """
    return split_string(sentence, ',;:')


def average_sentence_complexity(text):
    """
    Calculate the average number of phrases per sentence in the given text.
    
    Args:
    text (str): The input text.
    
    Returns:
    float: The average number of phrases per sentence.

    >>> average_sentence_complexity('A pearl! Pearl! Lustrous \
pearl! Rare. What a nice find.')
    1.0
    """
    sentences = get_sentences(text)
    total_phrases = sum(len(get_phrases(sentence)) for sentence in sentences if sentence.strip())
    total_sentences = len(sentences)
    if total_sentences == 0:
        return 0
    return total_phrases / total_sentences if total_sentences > 0 else 0


def contraction_density(text):
    """
    Calculate the contraction density in the given text.
    
    Contraction density is the ratio of contractions to total words in the text.
    
    Args:
    text (str): The input text.
    
    Returns:
    float: The contraction density.
    
    >>> get_contraction_density("I'm not sure if I'd like it.")
    2/7
    """
    contractions = ["'s", "'re", "'m", "'ll", "'d", "'ve", "n't"]
    raw_words = text.split()
    words = [clean_word(word) for word in raw_words if word.strip(string.punctuation)]
    total_words = len(words)
    contractions_count = sum(1 for word in words if any(contraction in word for contraction in contractions))
    
    return contractions_count / total_words if total_words > 0 else 0


def make_signature(text):
    '''
    The signature for text is a list of five elements:
    average word length, different words divided by total words, 
    words used exactly once divided by total words,
    average sentence length, and average sentence complexity.
    
    Return the signature for text.    

    >>> make_signature('A pearl! Pearl! Lustrous pearl! \
Rare, what a nice find.')
    [4.1, 0.7, 0.5, 2.5, 1.25]
    '''
    return [average_word_length(text),            
            different_to_total(text),             
            exactly_once_to_total(text),          
            average_sentence_length(text),        
            average_sentence_complexity(text),
            contraction_density(text)]    

def get_all_signatures(known_dir):
    """
    Get the signature for each file in the specified directory.

    Args:
    known_dir (str): The directory containing the books.

    Returns:
    dict: A dictionary where each key is the file name and the value is its signature.
    """
    signatures = {}
    for file_name in os.listdir(known_dir):
        with open(os.path.join(known_dir, file_name), encoding='utf-8') as file:
            text = file.read()
            signatures[file_name] = make_signature(text)
    return signatures




def get_score(signature1, signature2, weights):
    '''
    signature1 and signature2 are signatures.
    weights is a list of five weights.
        
    Return the score for signature1 and signature2.
        
    >>> get_score([4.6, 0.1, 0.05, 10, 2],\
                  [4.3, 0.1, 0.04, 16, 4],\
                  [11, 33, 50, 0.4, 4])       
    14.2
    '''
    return sum(abs(s1 - s2) * w for s1, s2, w in zip(signature1, signature2, weights))


def lowest_score(signatures_dict, unknown_signature, weights):
    '''
    signatures_dict is a dictionary mapping keys to signatures.
    unknown_signature is a signature.
    weights is a list of five weights.
    Return the key whose signature value has the lowest 
    score with unknown_signature.
    
    >>> d = {'Dan': [1, 1, 1, 1, 1], 'Leo': [3, 3, 3, 3, 3]}       
    >>> unknown = [1, 0.8, 0.9, 1.3, 1.4]
    >>> weights = [11, 33, 50, 0.4, 4]
    >>> lowest_score(d, unknown, weights)     
    'Dan'
    '''
    lowest = None
    for key in signatures_dict:                         
        score = get_score(signatures_dict[key],           
                          unknown_signature, weights)    
        if lowest is None or score < lowest[1]:      
            lowest = (key, score)       
    return lowest[0]   



def process_data(mystery_filenames, known_dir, save_signatures=False):
    '''
    mystery_filenames is a list of filenames of mystery books whose 
                     authors we want to know.
    known_dir is the name of a directory of books.
    save_signatures is a boolean indicating whether to save signatures to a CSV file.
    
    Return a dictionary with the name of each mystery file as key and the name of the signature closest to 
    the signature of the text of that mystery file as value.
    '''
    results = {}
    
    if save_signatures:
        signatures_file = '/data/signatures.csv'
        if not os.path.exists(signatures_file):
            signatures = get_all_signatures(known_dir)
            with open(signatures_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                for key, value in signatures.items():
                    writer.writerow([key] + value)
        else:
            with open(signatures_file, mode='r') as file:
                reader = csv.reader(file)
                signatures = {rows[0]: list(map(float, rows[1:])) for rows in reader}
    else:
        signatures = get_all_signatures(known_dir)
    
    for mystery_filename in mystery_filenames:
        with open(mystery_filename, encoding='utf-8') as f:    
            text = f.read()                                
            unknown_signature = make_signature(text)         
        results[mystery_filename] = lowest_score(signatures, unknown_signature, [11, 33, 50, 0.4, 4, 1])
    
    return results

        
def make_guess(known_dir, file_list, save_signatures=True):
    '''
    Guess author for a list of files.
    '''
    results = process_data(file_list, known_dir, save_signatures)
    print(results)

if __name__ == '__main__':
    # Run from terminal with 
    # python improved_authorship_identification.py  'data/known_authors' "True" 'data/unknown3.txt' 'data/unknown2.txt'
    make_guess(sys.argv[1], sys.argv[3:], sys.argv[2]=='True')

