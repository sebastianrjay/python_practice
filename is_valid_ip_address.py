# Returns whether or not the input string is a valid IP address

def is_valid_ip_address(string):
  nums = list(map(lambda num: int(num), string.split(".")))
  if(len(nums) != 4):
    return False
  else:
    return all(map(lambda num: (num >= 0 and num < 256), nums))

# print(is_valid_ip_address("255.255.255.0.1"))
