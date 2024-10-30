import fileHandler
import gifProcessor
from gif import Gif


def setDir(path):
    fileHandler.addPath(path)

def saveGifs(gifs):
    fileHandler.writeAppFile(gifs)

def getGifs():
    gifs = fileHandler.readAppFile()
    if not gifs:
        try:
            gifs = []
            for path in fileHandler.readAppPath():
                gifPaths = fileHandler.getGifs(path)
                byteArray = fileHandler.getBytes(gifPaths)
                for array in byteArray:
                    info = gifProcessor.decodeGif(array)
                    gifs.append(getGifObject(gifPaths[byteArray.index(array)], info))
        except Exception as e:
            print(e)
    return gifs
    

def getGifObject(path:str, meta:list[str]):
    info = [] # Ruta con el nombre del archivo
    info.append(meta[0]) # Version
    info.append(meta[1]) # Tamaño
    info.append(meta[2]) # Numero de colores
    info.append(meta[3]) # Tipo de compresion
    info.append(meta[4]) # Formato numerico
    info.append(meta[5]) # Fondo
    info.append(meta[6]) # Numero de imagenes
    times = fileHandler.getTimes(path)
    info.append(times[0]) # Fecha de creacion
    info.append(times[1]) # Fecha de ultima modificacion
    info.append(meta[7])

    return Gif(path, info)