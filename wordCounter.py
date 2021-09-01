import sys
import argparse

class WordCounter(object):
    def __init__(self, text: str, delimiter: str=" ") -> None:
        """
        Intialises the WordCounter object.
        
        Args:
            text (str): A word sequence or a single word.
            delimiter (str, optional): Character or string that seoarates
             a sequence of characters or strings. Defaults to None.
        """
        self._text = text.split(delimiter)

    def __compare__(self, other_object) -> str:
        """
        Compare the number of words in two WordCounter objects.

        Args:
            other_object (object): The other WordCounter object.

        Returns:
            str: [description]
        """
        if not isinstance(other_object, type(self)):
            return f'The {other_object} should be of type WordCounter and not {type(other_object)}'
        l1, l2 = len(self._text), len(other_object._text)
        return "equal" if l1 == l2 else ("less words" if l1<l2 else "more words")

    def get_word_count(self) -> int:
        """
        Count the number of words in the text.

        Returns:
            int: total count of words in the text.
        """
        return len(self._text)

    def get_count(self, word: str, ignore_case: bool=True) -> int:
        """
        Calculate the frequency of a given word in the text.

        Args:
            word (str): Word whose occurance(frequency) is to calculated
            ignore_case (bool, optional): if the case is to be ignored or not. Defaults to True.

        Returns:
            int: frequency of the word in the text.
        """
        if ignore_case:
            all_lower_words = [word.lower() for word in self._text]
            return all_lower_words.count(word)
        return self._text.count(word)

    def get_word_frequencies(self, ignore_case: bool=True) -> dict:
        """
        Calculate the frequency of each word in the text.

        Args:
            ignore_case (bool, optional): if the case is to be ignored or not. Defaults to True.

        Returns:
            dict: dictionary having key as words and value as their count.
        """
        counter = {}
        if ignore_case:
            for char in self._text:
                counter[char.lower()] = counter.get(char.lower(), 0) + 1
        else:
            for char in self._text:
                counter[char] = counter.get(char, 0) + 1
        return counter

    def get_most_common_word(self, ignore_case: bool=True) -> list:
        """Get the most common word in the text.

        Args:
            ignore_case (bool, optional): if the case is to be ignored or not. Defaults to True.

        Returns:
            str: the most common word.
        """
        counter = self.get_word_frequencies(ignore_case)
        count = max(counter.values())
        list_ = []
        for key, value in counter.items():
            if value == count:
                list_.append(key)
        return list_
        # return max(counter.keys(), key=counter.get) #returns a single comman word
        
    def get_word_by_freq(self, freq: int, ignore_case: bool=True) -> list:
        """
        Get the word with a given number of occurance in the text.

        Args:
            count (int): the number of occurances.
            ignore_case (bool, optional): if the case is to be ignored or not. Defaults to True.

        Returns:
            list(str): a list of words with the given frequency.
        """
        counter = self.get_word_frequencies(ignore_case)
        list_ = []
        for key, value in counter.items():
            if value == freq:
                list_.append(key)
        if list_:
            return list_
        else:
            return f"No word exists with count = {freq}"

def main():
    parser = argparse.ArgumentParser(prog='wordCounter', usage='%(prog)s [options] path', description='Process some text')
    parser.add_argument("-f", "--file", help="count number of words in specified file", type=str)
    args = parser.parse_args()
    if args.file:
        text = ''
        try:
            with open(args.file, 'r') as file:
                text = file.read().replace('\n', ' ')
        except Exception as e:
            print(f"Exception {str(e)}: Please try again!!!")
            sys.exit(0)
        word_counter = WordCounter(text)

        # # Test from file.txt
        # print(word_counter.get_word_count())
        # print(word_counter.get_count('the'))
        # print(word_counter.get_count('the', ignore_case=False))
        # print(word_counter.get_word_frequencies())
        # print(word_counter.get_word_frequencies(ignore_case=False))
        # print(word_counter.get_most_common_word())
        # print(word_counter.get_most_common_word(ignore_case=False))
        # print(word_counter.get_word_by_freq(2))
        # print(word_counter.get_word_by_freq(2, ignore_case=False))

if __name__ == '__main__':
    main()