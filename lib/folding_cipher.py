# Encode a string with the folding_cipher, in O(n) time

def folding_cipher(string):
  ascii_indexes = range(ord('a'), ord('z') + 1)
  alphabet = list(map(lambda idx: chr(idx), ascii_indexes))
  reversed_alphabet = alphabet[:]
  reversed_alphabet.reverse()
  cipher = {}
  cipher[' '] = ' '

  for i in range(0, 26):
    cipher[alphabet[i]] = reversed_alphabet[i]

  return ''.join(map(lambda letter: cipher[letter], list(string)))

# print(folding_cipher('abcdef ghijklmnopqr stuvwxyz'))
