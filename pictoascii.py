from skimage import io
from skimage.color import rgb2gray
from skimage.transform import resize
from sys import argv

def main():
    image = rgb2gray(resize(io.imread(str(argv[1])), (int(argv[4]), int(argv[3])), anti_aliasing=False))
    output = ['']
    string = ""
    whitespaces = False

    if argv[6] == 'true'          : whitespaces = True

    if int(argv[5]) == 14         : symbols = [' ', '.', ',', ':', '*', '/', '+', 'o', 'O', '#', '$', '&', '%', '@']
    if int(argv[5]) == 13         : symbols = [' ', '.', ',', ':', '*', '/', '+', 'o', 'O', '#', '$', '%', '@']
    if int(argv[5]) == 12         : symbols = [' ', '.', ',', ':', '*', '/', '+', 'o', 'O', '#', '$', '@']
    if int(argv[5]) == 11         : symbols = [' ', '.', ',', ':', '*', '/', '+', 'o', 'O', '$', '@']
    if int(argv[5]) == 10         : symbols = [' ', '.', ',', ':', '*', '/', '+', 'o', 'O', '@']
    if int(argv[5]) == 9          : symbols = [' ', '.', ':', '*', '/', '+', 'o', 'O', '@']
    if int(argv[5]) == 8          : symbols = [' ', '.', ':', '*', '/', '+', 'o', '@']
    if int(argv[5]) == 7          : symbols = [' ', '.', ':', '*', '+', 'o', '@']
    if int(argv[5]) == 6          : symbols = [' ', '.', ':', '*', 'o', '@']

    kef = 1 / len(symbols)

    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            for k in range(0, len(symbols)):
                if image[i][j] <= kef * (k + 1):
                    string += symbols[len(symbols) - 1 - k]
                    if whitespaces : string += ' '
                    break
        output.append(string + '\n')
        string = ""

    file = open(str(argv[2]) + '.txt', "w")
    for i in range(0, len(output)):
        file.write(output[i])
    file.close()

if (len(argv) == 1):
    print("Not all args provided! Use [python3 pictoascii.py ?].")
elif (argv[1] == '?'):
    print("Usage: [python3 pictoascii.py {path-to-file} {name-of-created-file} {width} {height} {shades-of-gray (6 - 14)} {whitespaces (true or false)}")
elif (len(argv) != 7):
    print("Not all args provided! Use [python3 pictoascii.py ?].")
else:
    main()