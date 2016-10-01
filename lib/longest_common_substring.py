# Longest common substring of two strings, calculated in O(m * n) time

def longest_common_substring(str1, str2):
  current_sub, longest_sub = "", ""
  str1_start, str1_idx, str2_idx = 0, 0, 0

  while(str1_idx < len(str1) - len(longest_sub)):
    current_sub, str2_idx = "", 0

    while(str1_idx < len(str1) and str2_idx < len(str2)):

      if(str1[str1_idx] == str2[str2_idx]):
        current_sub += str2[str2_idx]
        if(len(current_sub) > len(longest_sub)):
          longest_sub = current_sub

        str1_idx += 1
      else:
        str1_idx, current_sub = str1_start, ""

      str2_idx += 1

    str1_start += 1


  return longest_sub
