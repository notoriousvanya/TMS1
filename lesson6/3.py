import json

n = {
    123456: ("Sansha", 45),
    654321: ("Vanya", 13),
    109876: ("Vera", 25),
    246810: ("Katya", 83),
    456372: ("Danik", 26)
}

with open("d_file.json", "w") as file:
    json.dump(n, file)