# No yelling!

def filter_words(st):
    return ' '.join(st.split()).lower().capitalize()
print(filter_words('HELLO world!'))