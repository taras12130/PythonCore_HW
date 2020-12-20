# Will there be enough space?

def enough(cap, on, wait):
    if on + wait > cap:
        return (on + wait) - cap
    else:
        return 0
print(enough(100, 60, 50))