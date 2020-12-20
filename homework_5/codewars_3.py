# Are You Playing Banjo?

def areYouPlayingBanjo(name):
    if name.lower()[0] == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
print(areYouPlayingBanjo("Rikke"))