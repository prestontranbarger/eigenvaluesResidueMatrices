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
        #not optimal for large files
        file = open(self.readPath, 'r')
        lines = file.readlines()
        file.close()

        rowGuide = lines[-2][1:-2].replace("\'","").split(", ")
        colGuide = lines[-1][1:-2].replace("\'","").split(", ")

        return rowGuide, colGuide

    def guideToDict(self, guide):
        guideDict = {"": -1}
        for i in range(len(guide)):
            guideDict[guide[i]] = i
        return guideDict

    def readBFM(self, getGuide = False, rows = None, cols = None):
        m = []
        rowGuide = []
        colGuide = []
        with open(self.readPath) as file:
            for line in tqdm(file):
                if not getGuide:
                    rowEntries = line[1:-2].replace("\'", "").split(", ")
                    rowAppend = [rowEntries[col] for col in range(len(rowEntries))]
                    m.append(rowAppend)
                rowGuide = colGuide
                colGuide = line[1:-2].replace("\'", "").split(", ")
        if getGuide:
            return rowGuide, colGuide
        else:
            return m[:-2], rowGuide, colGuide

    def writeBFM(self, matrix, rowGuide, colGuide):
        file = open(self.writePath, 'a')
        file.writelines([str(row)+"\n" for row in tqdm(matrix)])
        file.writelines(str(rowGuide)+"\n")
        file.writelines(str(colGuide)+"\n")
        file.close()
