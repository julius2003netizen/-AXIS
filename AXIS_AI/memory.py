import json

FILE = "memory.json"

def remember(key, value):
    data = json.load(open(FILE))
    data[key] = value
    json.dump(data, open(FILE, "w"))

def recall(key):
    data = json.load(open(FILE))
    return data.get(key)
