#!/usr/bin/env python2.7

'''
The Challenge:
Given the following sentence output whether the given acronyms
can be made from the characters in the sentence.

Input:
sentence = 'All good boys love dogs, cats, mice, autos, and lions'
acronyms = ['aclu', 'mgm', 'mia', 'mlb', 'llm','uzi', 'vta']

Expected Output:
          ['aclu','mlb','mia','llm','vta']

Rules:
1.  No letter in the sentence may be used more than once
2.  Disregard case sensitivity
'''

import re
import sys

candidate_acronyms = ['aclu', 'mgm', 'mia', 'mlb', 'llm', 'uzi', 'vta']


def get_available_letters(str):
    ''' return a dictionary of the count of letters (lowercased)
        in the given string.
    '''
    available_letters = {}
    for char in re.findall('[A-Za-z]', str.lower()):
        if char not in available_letters:
            available_letters[char] = 0
        available_letters[char] += 1
    return available_letters


def generate_acronyms(available_letters, candidate_acronyms):
    ''' return the list of the candidate acronyms that can be constructed
        using the available letters given
    '''
    generated_acronyms = []

    for acronym in candidate_acronyms:
        acronym_generation_failed = False
        letters = available_letters.copy()
        for c in acronym:
            if c in letters and letters[c] > 0:
                letters[c] -= 1
            else:
                acronym_generation_failed = True
                break
        if not acronym_generation_failed:
            generated_acronyms.append(acronym)

    return generated_acronyms


def process_string(sentence):
    ''' print results of acronym generation attempts for given string
    '''
    available_letters = get_available_letters(sentence)
    generated_acronyms = generate_acronyms(available_letters,
                                           candidate_acronyms)
    print generated_acronyms


def main():
    sentence = 'All good boys love dogs, cats, mice, autos, and lions'
    process_string(sentence)


if __name__ == '__main__':
    sys.exit(main())
