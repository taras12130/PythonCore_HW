# Reversing Words in a String

def reverse(st):
    st = st.split()
    return ' '.join(st[::-1])
print(reverse('Hello World'))