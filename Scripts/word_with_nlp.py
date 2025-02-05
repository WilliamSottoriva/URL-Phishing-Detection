import re

class nlp_class:
    def __init__(self):
        # Initialize any resources you might need (e.g., dictionaries, language models, etc.)
        pass

    def check_word_random(self, domain):
        """
        This function checks if a domain name is random by using some heuristic methods:
        1. Checks for sequences of characters that are unlikely in real words (e.g., long consonant sequences).
        2. Checks if the domain name consists mostly of letters or numbers.
        3. Checks for uncommon patterns such as a high ratio of digits to letters.
        """

        # Step 1: Check for excessive consonant sequences (heuristic)
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        domain_lower = domain.lower()
        
        # Find sequences of consonants of length >= 4 (unlikely to be a valid word)
        consonant_seq = re.findall(f'[{consonants}]{{4,}}', domain_lower)
        if consonant_seq:
            return True  # Likely random

        # Step 2: Check if there are very few vowels (e.g., mostly consonants)
        vowel_count = sum(1 for char in domain_lower if char in vowels)
        consonant_count = sum(1 for char in domain_lower if char in consonants)
        if vowel_count < 2 and consonant_count > 3:  # Few vowels and many consonants
            return True  # Likely random

        # Step 3: Check if the domain contains mostly digits
        digit_count = sum(1 for char in domain if char.isdigit())
        letter_count = sum(1 for char in domain if char.isalpha())
        if digit_count > letter_count:  # More digits than letters
            return True  # Likely random

        # Step 4: Check for a high number of special characters
        special_chars_count = sum(1 for char in domain if not char.isalnum())
        if special_chars_count > 3:  # Arbitrary threshold for special characters
            return True  # Likely random

        # If none of the checks detect randomness, consider the domain legitimate
        return False  # Not random
