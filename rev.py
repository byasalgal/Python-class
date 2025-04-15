class reverse:
 def __init__(self, s):
  self.s = s

 def rev(self):
  word = ""
  words = []
  for c in self.s:
   if c != " ":
    word = word + c
   else:
    words.append(word)
    word = ""
  words.append(word)
  result = ""
  i = len(words) - 1
  
  while i >= 0:
   result = result + words[i] + " "
   i = i - 1
  return result[:-1]

sentence = input("say: ")
r = reverse(sentence)
print(r.rev())