#1
# numbers = [1, 2, 3]
# numbers[6] = 5
#yes, index error

#2
# str1 = "Come over here!"  # True
# str2 = "What's up, Doc?"  # False

# print(str1.endswith('!'))
# print(str2.endswith('!'))

#3
# famous_words = "seven years ago..."
# print(f'Four score and {famous_words}')
# print('Four score and ' + famous_words)

#4
# munsters_description = "the Munsters are CREEPY and Spooky."
# # => 'The munsters are creepy and spooky.'

# print(munsters_description.capitalize())

#5
# munsters_description = "The Munsters are creepy and spooky."
# print(munsters_description.swapcase())

#6
# str1 = "Few things in life are as important as house training your pet dinosaur."
# str2 = "Fred and Wilma have a pet dinosaur named Dino."
# print('Dino' in str2)

#7
# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append('Dino')
# print(flintstones)

#8
# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.extend(['Dino', 'Hoppy'])
# print(flintstones)

#9
# advice = "Few things in life are as important as house training your pet dinosaur."
# # Expected output:
# # Few things in life are as important as
# print(advice.split('house')[0])

#10
advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.replace('important', 'urgent'))