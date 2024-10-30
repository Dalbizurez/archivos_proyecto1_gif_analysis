class Gif:
    def __init__(self, path:str, gifInfo:list[str]) -> None:
        self.path = path
        self.version = gifInfo[0]
        self.size = gifInfo[1]
        self.noOfColors = gifInfo[2]
        self.compressionType = gifInfo[3]
        self.numFormat = gifInfo[4]
        self.backgroundColor = gifInfo[5]
        self.noOfImages = gifInfo[6]
        self.dateCreation = gifInfo[7]
        self.dateModified = gifInfo[8]
        self.commnets = gifInfo[9]

    def __repr__(self) -> str:
        return f"{self.path} {self.version}"

    def __str__(self) -> str:
        return f"{self.path},{self.version},{self.size},{self.noOfColors},{self.compressionType},{self.numFormat},{self.backgroundColor},{self.noOfImages},{self.dateCreation},{self.dateModified},{self.commnets}"

    