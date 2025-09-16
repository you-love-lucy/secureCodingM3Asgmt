startText = input('Enter text: ')
shiftNum = int(input('Enter number to shift text: '))
endText = ''

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for letter in startText:
    try:
        position = alphabet.index(letter)
        newPos = position + shiftNum
        final = alphabet[newPos]
    except:
        final = letter
    endText += final

print(endText)