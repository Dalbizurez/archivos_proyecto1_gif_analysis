from gif import Gif

# Funcion que transforma los bytes de un archivo en 
# la informacion correspondiente
def decodeGif(gifBytes:list[bytes]):
    version = gifBytes[0:6]
    width = int.from_bytes(gifBytes[7:5:-1])
    height = int.from_bytes(gifBytes[9:7:-1])
    noOfColors = getNoOfColors(bin(gifBytes[10]))
    compressionType = "LZW"
    format = "Little-endian"
    background = gifBytes[11]
    noOfImages = 0

    index = 13 + noOfColors*3
    cont = 0

    noOfImages = gifBytes.count(44)

    index = len(gifBytes)

    while (index < len(gifBytes)):
        if gifBytes[index] == 33:
            index += 2 # Block size
            index += gifBytes[index] + 1
            while gifBytes[index] != 0:
                index += gifBytes[index+1] + 1
        elif gifBytes[index] == 44:
            noOfImages += 1
            index += 10 +1
#            localColors = getNoOfColors(bin(gifBytes[index]))
#            index += 1 + localColors*3
            index += gifBytes[index]
            while gifBytes[index] != 0:
                index += gifBytes[index+1] + 1
        elif gifBytes[index] == 0:
            index +=1
        elif index >= len(gifBytes)-1:
            break            
        else:
            cont += 1
        if cont == 2:
            print("cont")
            break

    comments = "Not supported"
#    print(index, len(gifBytes), gifBytes[index])


    return version, f"{width}x{height}", noOfColors, compressionType, format, background, noOfImages, comments


def getNoOfColors(colorTable:str):
    flag = colorTable[2]
    if flag == "0":
        return 0
    return 2**(int(colorTable[-3::+1],2)+1)

def getGifs(data:list[any]):
    gifs = []
    for entry in data:
        gifs.append(entry)
    return gifs
    