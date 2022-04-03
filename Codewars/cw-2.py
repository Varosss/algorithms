# V A P O R C O D E

def vaporcode(string):
    chars = list(string)
    vaporsent = ''

    for i in range(len(chars)):
        if not chars[i].isspace():
            vaporsent += chars[i].upper() + '  '

    vaporsent = vaporsent.strip()

    return vaporsent

string = "_UvQDxjvW?ImpZ,;t ;F  F "
print(vaporcode(string))