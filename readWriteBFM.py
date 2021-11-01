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

    def readBFM(self, rows, cols):
        file = open(self.readPath, 'r')
        lines = file.readlines()
        file.close()

        m = []
        for row in rows[:-2]:
            rowEntries = lines[row][1:-2].replace("\'","").split(", ")
            rowAppend = [rowEntries[col] for col in cols]
            m.append(rowAppend)
        rowGuide = lines[-2][1:-2].replace("\'","").split(", ")
        colGuide = lines[-1][1:-2].replace("\'","").split(", ")
        return m, rowGuide, colGuide

        # add row/col dictionaries

    def writeBFM(self, matrix, rowGuide, colGuide):
        file = open(self.writePath, 'a')
        file.writelines([str(row)+"\n" for row in matrix])
        file.writelines(str(rowGuide)+"\n")
        file.writelines(str(colGuide)+"\n")
        file.close()

        # add row/col dictionaries