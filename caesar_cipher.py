# Encode a string using the caesar cipher

def caesar_cipher(message, offset):
  return_string = ""
  a_ord = ord("a")
  for char in message:
    if char == " ":
      return_string += " "
    else:
      return_string += chr(a_ord + ((ord(char) - a_ord + offset) % 26))

  return return_string

# print(caesar_cipher("hello", 4))
