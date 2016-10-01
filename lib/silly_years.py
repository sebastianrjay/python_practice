# Return all years after 'year' wherein the first two digits and the last two 
# digits sum to the middle two digits

def silly_years(year):
  years, year_copy = [], year
  
  while(len(years) < 10):
    year_copy += 1
    string_year = str(year_copy)

    if(int(string_year[0:2]) + int(string_year[2:]) == int(string_year[1:3])):
      years.append(year_copy)

  return years

# print(silly_years(1978))
