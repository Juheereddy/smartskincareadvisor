import json
import os

def load_json(filename):
    with open(os.path.join("sample_data", filename)) as f:
        return json.load(f)

concern_data = load_json("concerns.json")
diy_data = load_json("diy_recipes.json")

def get_recommendations(concern):
    ingredients = concern_data.get(concern, [])
    diy = diy_data.get(concern, "No DIY available.")
    return {
        "ingredients": ingredients,
        "diy": diy
    }