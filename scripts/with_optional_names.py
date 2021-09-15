import json

JSON_READ_FILE = "../cities.json"
JSON_READ_FILE_EN = "../cities_en.json"
JSON_WRITE_FILE = "../cities_with_optional.json"
JSON_WRITE_FILE_EN = "../cities_with_optional_en.json"

optional_city_names = {
    "mersin": "icel",
    "sakarya": "adapazari",
    "kocaeli": "izmit",
    "hatay": "antakya",
}

attributes = ["name", "plate", "latitude", "longitude", "counties"]

def optional_name(city_name):
    for key, val in optional_city_names.items():
        if key == city_name.lower():
            return val


def has_optional_name(city_name):
    return True if city_name.lower() in optional_city_names else False


def get_json(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
        return data


def create_json(file_name, json_data):
    cities = []

    with open(file_name, "w") as file:
        for city in json_data:
            new_city = {}
            for attr in attributes:
                new_city[attr] = city[attr]
                if attr == "name" and has_optional_name(city[attr]):
                    new_city["optional_name"] = optional_name(city[attr])
                
            cities.append(new_city)

        cities = json.dumps(cities, indent=4)
        file.write(cities)


def create_with_turkish():
    data = get_json(JSON_READ_FILE)
    create_json(JSON_WRITE_FILE, data)


def create_without_turkish():
    data = get_json(JSON_READ_FILE_EN)
    create_json(JSON_WRITE_FILE_EN, data)


create_with_turkish()
create_without_turkish()