import string
 
### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    Returns: a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list
 
### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation
 
    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    Returns: True if word is in word_list, False otherwise
 
    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list
 
### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story
 
WORDLIST_FILENAME = 'words.txt'
 
class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
        text (string): the message's text
 
        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
 
    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        Returns: self.message_text
        '''
        return self.message_text
 
    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26
 
        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # pass #delete this line and replace with your code here
 
        # self.dict = {}
 
 
        # len_l = len(string.ascii_lowercase)
        # len_u = len(string.ascii_uppercase)
        # lower = (string.ascii_lowercase)
        # upper = (string.ascii_uppercase)
 
        # for i in range(lower) : #0..25
        #     dict[lower[i]] = lower[i + shift]  #ToDo: wrap around
        # #print(dict)
 
 
        # print(string.ascii_lowercase)
        # print(string.ascii_uppercase)
 
        self.shift_dict = {}
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
 
        for char in lower:
            shifted_char = lower[(lower.index(char) + shift) % 26]
            self.shift_dict[char] = shifted_char
 
        for char in upper:
            shifted_char = upper[(upper.index(char) + shift) % 26]
            self.shift_dict[char] = shifted_char
 
        return self.shift_dict
 
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26
 
        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        pass #delete this line and replace with your code here
 
        # s = ''
        # for every letter in self.message_text
        #     if letter is lower or upper
        #         then shift letter 
        #         1) you need self.build_shift_dict
        #         2) look up the letter
        #         3) replace letter with the shifted from dict[letter]
 
 
        #         s += letter
 
        # otherwise the letter must be punctuation
        #     so dont shift it, just keep
        #         s += letter
        #     check for punctuation
        #     if letter in string.punctuation
        #     or letter in string.digits
        #     or letter in string.whitespace
        #     then dont shift it
        #     otherwise it must be a letter
        #         so shift it
 
        #return s
        shifted_text = ''
        shift_dict = self.build_shift_dict(shift)
 
        for char in self.message_text:
            if char.isalpha():
                shifted_text += shift_dict[char]
            else:
                shifted_text += char
 
        return shifted_text
 
m = Message('happy')
d = m.build_shift_dict(3) 
m.build_shift_dict(3)
print(d)  
 
shifted_text = m.apply_shift(3)
print(shifted_text) #kdSSb !!!!
 
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        text (string): the message's text
        shift (integer): the shift associated with this message
 
        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)
 
        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        #pass #delete this line and replace with your code here
 
        super().__init__(text)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
 
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        Returns: self.shift
        '''
        #pass #delete this line and replace with your code here
 
        return self.shift
 
    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        Returns: a COPY of self.encrypting_dict
        '''
        #pass #delete this line and replace with your code here
        #just use .copy()
        return self.encrypting_dict.copy()
 
    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        Returns: self.message_text_encrypted
        '''
        #pass #delete this line and replace with your code here
        return self.message_text_encrypted
 
    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26
 
        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
# test case for p2
p = PlaintextMessage('Happy ???', 3)
p.change_shift(3)
print(p.get_message_text())
p.change_shift(4)
print(p.get_message_text())
 
 
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
        text (string): the message's text
        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        #pass #delete this line and replace with your code here
        super().__init__(text)

def decrypt_message(self):

        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.
        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return
        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        #brute-force method = trying every possible combination
        # PIN 4-digit: try all combination from 0000 up to 9999
        '''
        # common_words = ["I", "you", "we", "and", "but", "the"]
 
        # try apply_shift(1)
        #     count how many english words you found
        # try apply_shift(2)
        #     count how many english words you found
        # try apply_shift(3)
        #     count how many english words you found
        # the highest word count is the correct shift
        # return(best_shift, message)

        max_word_count = 0
        best_shift = 0
        decrypted_message = ''
 
        for shift in range(26):
            decrypted_text = self.apply_shift(shift)
            word_count = sum(is_word(self.valid_words, word) for word in decrypted_text.split())

            if word_count > max_word_count:
                max_word_count = word_count
                best_shift = shift
                decrypted_message = decrypted_text
        return best_shift, decrypted_message

       # pass #delete this line and replace with your code here
 
 
if __name__ == '__main__':

    s = get_story_string()

    ciphertext = CiphertextMessage(s)

    print(ciphertext.decrypt_message())