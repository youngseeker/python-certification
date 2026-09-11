languages = ['Spanish', 'English', 'Swahili', 'French']
for index, language in enumerate(languages, start=1):
    print(f'Index {index}: language {language}')
# This code uses enumerate to loop through the list of languages,
# providing both the index (starting from 1) and the language name.
# It prints each language along with its corresponding index.

#zip() function example
countries = ['Spain', 'USA', 'Kenya', 'France']
capitals = ['Madrid', 'Washington, D.C.', 'Nairobi', 'Paris']
for country, capital in zip(countries, capitals):
    print(f'The capital of {country} is {capital}.')
# This code uses the zip() function to pair each country with its capital
# and prints them in a formatted string.