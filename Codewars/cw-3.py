# Hello, Name or World!

def hello(name='World'):
    sentence = 'Hello, '

    if not name:
        sentence += 'World!'
    else:
        chars = list(name)

        for i in range(len(chars)):
            if i == 0:
                chars[i] = chars[i].upper()
            else:
                chars[i] = chars[i].lower()

        name = ''.join(chars)

        sentence += name + '!'

    return sentence

name = 'aliCE'
print(hello(name))