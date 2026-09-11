words = ['sky', 'apple', 'rhythm', 'fly', 'orange']
for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f'The word "{word}" contains the vowel "{letter}".')
            break
    else:
        print(f'The word "{word}" has no vowels.')