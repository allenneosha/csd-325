def city_country(city, country, population=None, language=None):
    """Return a single string, formatted like 'City, Country'."""
    result = f"{city.title()}, {country.title()}"
    
    if population:
        result += f" - population: {population}"
    if language:
        result += f", {language.title()}" if population else f" {language.title()}"

    return result

print(city_country('egypt', 'africa'))
print(city_country('paris', 'france'))
print(city_country('tokyo', 'japan'))

print(city_country('egypt', 'africa', population=12000000))
print(city_country('paris', 'france', population=2148000))
print(city_country('tokyo', 'japan', population=13929286))

print(city_country('egypt', 'africa', population=12000000, language='arabic'))
print(city_country('paris', 'france', population=2148000, language='french'))
print(city_country('tokyo', 'japan', population=13929286, language='japanese'))