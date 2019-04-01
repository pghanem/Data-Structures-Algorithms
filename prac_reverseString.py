def rip(string):
    start = 0
    end = len(string) - 1
    temp = ''

    while start < end:
        temp = string[start]
        string = string.replace(string[start], string[end])
        string = string.replace(string[end], temp)
        end -= 1
        start += 1

    print(string)

def rev(string):
    for x in range(len(string)):
        return string[::-1]
        break

def revl(s):
    word = []
    for x in s:
        word.append(x)

    start = 0
    end = len(word) - 1
    temp = ''

    while start < end:
        temp = word[start]
        word[start] = word[end]
        word[end] = temp
        end -= 1
        start += 1

    print(word)
