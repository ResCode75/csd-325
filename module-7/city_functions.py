#Rachel Shaw - 7.1 Assignment - 11/26/2024

def city_country(city, country, population= None, language= None ):
   
   #changes returned string based on arguments sent
   if population == None and language == None:
      city_and_country = f"{city}, {country}."
   elif population == None:
      city_and_country = f'{city}, {country}, {language}'
   elif language == None:
      city_and_country = f'{city}, {country} -population {population}'
   else:
      city_and_country = f'{city}, {country} -population {population}, {language}'
   

   return city_and_country


# city, state
print(city_country( city = "Tokyo", country = "Japan"))

#city, state, population
print(city_country(city = "Berlin", country = "Germany", population = "3,576,870"))

#city, state, population, language
print(city_country(city = "Paris", country = "France", population = "2,138,551", language = "French"))
