from tqdm import tqdm

class rwBFM:
    def __init__(self, readPath = None ,writePath = None):
        self.readPath = readPath
        if ((readPath is not None) and (writePath is None)):
            self.writePath = readPath
        else:
            self.writePath = writePath

    def getReadPath(self):
        return self.readPath

    def setReadPath(self, readPath):
        self.readPath = readPath
        return 0

    def getWritePath(self):
        return self.writePath

    def setWritePath(self, writePath):
        self.writePath = writePath
        return 0

    def readBFMGuide(self):
        with open(self.readPath) as file:
            rowGuide = file.readline()[1:-2].replace("\'", "").split(", ")
            colGuide = file.readline()[1:-2].replace("\'", "").split(", ")
        return rowGuide, colGuide

    def guideToDict(self, guide):
        guideDict = {"": -1}
        for i in range(len(guide)):
            guideDict[guide[i]] = i
        return guideDict

    def readBFM(self, rows, cols):
        m = []
        with open(self.readPath) as file:
            i = 0
            for line in tqdm(file):
                if (i - 2) in rows:
                    rowEntries = line[1:-2].replace("\'", "").split(", ")
                    rowAppend = [rowEntries[col] for col in cols]
                    m.append(rowAppend)
                elif (i - 2) > rows[-1]:
                    break
                i += 1
        return m

    def writeBFM(self, matrix, rowGuide, colGuide):
        file = open(self.writePath, 'a')
        file.writelines(str(rowGuide)+"\n")
        file.writelines(str(colGuide)+"\n")
        file.writelines([str(row)+"\n" for row in tqdm(matrix)])
        file.close()