from random import sample

bathroom: dict[str, str] = {
    "secret_name": "bathroom",

    "toilet": "On top of this, you sit and... do some other stuff.",
    "sink": "used to clean your hands after using that nasty toilet. eugh.",
    "shower": "for when you want the ultimate clean. feels like rebirth.",
    "towels": "instruments used in the drying of a wet surface. handy."
}

bedroom: dict[str, str] = {
    "secret_name": "bedroom",

    "bed": "this is where you sleep at night. Pretty soft like a cloud.",
    "tv": "Moving images appear on here. oh wow.",
    "lamp": "for when you want to read something before going to bed.",
    "pillow": "a soft bag of foam for your head. full of hopes and dreams."
}

closet: dict[str, str] = {
    "secret_name": "closet",

    "shirt": "clothing for your upper half.",
    "pants": "clothes your lower half.",
    "shorts": "Eventually, it gets warm out. shorts are good for that.",
    "overalls": "for when you want to cosplay as a pudgy, italian man. yahoo."
}

empty_room: dict[str, str] = {
    "secret_name": "empty room",

    "...": "Nothing.",
    "???": "null.",
    "---": "none.",
    "   ": "uppercase."
}

garage: dict[str, str] = {
    "secret_name": "garage",

    "car": "alright, we're here, just sittin' in the car. i want you to show me if you can get far.",
    "guitar": "here are some bands that started in a garage: weezer, nirvana, the ramones, and the kinks.",
    "gasoline": "Smells very nice. i know it's bad, but i like it.",
    "scooter": "Exciting entity emitting engagement."
}

kitchen: dict[str, str] = {
    "secret_name": "kitchen",

    "stove": "prepare the food on here.",
    "fridge": "put the food in here.",
    "table": "Eat the food on here.",
    "bowl": "crack-crack-crack the egg into the bowl."
}

laundry_room: dict[str, str] = {
    "secret_name": "laundry room",

    "washer": "makes clothes really wet with a stir.",
    "dryer": "be careful not to start a fire.",
    "detergent": "Should use on clothes. that's urgent.",
    "bleach": "very powerful cleaner that's in reach."
}

living_room: dict[str, str] = {
    "secret_name": "living room",

    "couch": "for when you want to relax, but you don't want to fall asleep. sit on it.",
    "rug": "A room decoration covered with a grid of einstein tiles.",
    "painting": "a landscape of subdued green and a setting sun in the back.",
    "fan": "cooler than fondue, but not as cool as the fonz."
}

# Opens up a huge file containing 6,775 nouns.
# Source: https://www.desiquintans.com/nounlist
with open("nouns.txt") as file:
    treasure_room: dict[str, str] = {
        # Picks 4 random nouns / things and puts them into the room.
        word[:-1]: "(None)." for word in sample(file.readlines(), 4)
    }

    treasure_room["secret_name"] = "treasure room"