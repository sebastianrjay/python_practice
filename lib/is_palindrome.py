# Method returns whether or not the string is a palindrome

def is_palindrome(string):
  for i in range(int(len(string) / 2)):
    if(string[i] != string[len(string) - i - 1]):
      return False

  return True

# print(is_palindrome("banaadanab"))
