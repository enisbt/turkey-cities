import json


def replace_turkish_letters(string):
    letter_dict = {
        "ç": "c",
        "ğ": "g",
        "ı": "i",
        "ö": "o",
        "ş": "s",
        "ü": "u",
    }

    for key, val in letter_dict.items():
        if key in string:
            string = string.replace(key, val)

    return string


def replace_turkish_letters_list(counties):
    new_counties = []

    for county in counties:        
        new_counties.append(replace_turkish_letters(county))

    return new_counties


with open("cities.json", "r") as file:
    data = json.load(file)
    for city in data:
        city["name"] = replace_turkish_letters(city["name"])
        city["counties"] = replace_turkish_letters_list(city["counties"])



with open("cities_en.json", "w") as file:
    data = json.dumps(data, indent=4)
    file.write(data)