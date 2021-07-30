'''
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.

There are no characters in this string that do not repeat.

'''


def firstNotRepeatingCharacter(s):
    
    dict = {}
    for i in range(0, len(s)):
        char = s[i]
        dict[char] = dict.get(char, 0) + 1
        
    for i in range(0, len(s)):
        char = s[i]
        if dict[char] == 1:
            return char
        
            
    return "_"

