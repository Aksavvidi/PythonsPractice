vowels = "aeiouy"
given_word = "Coding Factory"

vowel_count = [[vowel, given_word.count(vowel)] for vowel in vowels]

for vowel, count in vowel_count:
    print(vowel, ":", count)