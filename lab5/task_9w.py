words = ["яблоко", "груша", "банан", "киви", "апельсин", "ананас"]

result = {}

for word in words:
   first_letter = word[0].lower()

   if first_letter not in result:
      result[first_letter] = []

   result[first_letter].append(word)

print(result)