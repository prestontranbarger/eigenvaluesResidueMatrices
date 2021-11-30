from tqdm import tqdm

class rwEVectors:
    def __init__(self, readPath = None, writePath = None):
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

    def readEVectorsGuide(self):
        with open(self.readPath) as file:
            guide = file.readline()[1:-2].replace("\'", "").split(", ")
        return guide

    def guideToDict(self, guide):
        guideDict = {"": -1}
        for i in range(len(guide)):
            guideDict[guide[i]] = i
        return guideDict

    def readEVectors(self, rows):
        out = []
        with open(self.readPath) as file:
            i = 0
            for line in tqdm(file):
                if (i - 1) in rows:
                    for element in line.replace("[", "").split("], "):
                        out.append(element.replace("]", "").replace("\'", "").split(", "))
                elif (i - 1) > rows[-1]:
                    break
                i += 1
        return out

    def writeEVectors(self, eVectors):
        storReadPath, self.readPath = self.readPath, self.writePath
        guide = self.readEVectorsGuide()
        dict = self.guideToDict(guide)
        self.readPath = storReadPath

        if len(dict) == 1:
            file = open(self.writePath, 'w')
            file.write(str([str(len(eVectors))]) + "\n" + str(eVectors))
            file.close()
        else:
            try:
                dict[str(len(eVectors))]
            except KeyError:
                file = open(self.writePath, 'r')
                lines = file.readlines()
                file.close()
                guide.append(str(len(eVectors)))
                lines[0] = str(guide) + "\n"
                lines.append("\n" + str(eVectors))
                file = open(self.writePath, 'w')
                file.writelines(lines)
                file.close()
        return 0