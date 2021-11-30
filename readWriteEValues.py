from tqdm import tqdm

class rwEValues:
    def __init__(self, readPath = None, writePath = None):
        self.readPath = readPath
        if((readPath is not None) and (writePath is None)):
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

    def readEvsOld(self, n):
        file = open(self.readPath, 'r')
        lines = file.readlines()
        file.close()

        i = 0
        if lines:
            while int(lines[i].strip()) != n:
                i += int(lines[i].strip()) + 1
                if(i >= len(lines)):
                    return -1
            return [float(lines[i].strip()) for i in range(i + 1, i + int(lines[i].strip()) + 1)]
        else:
            return -1

    def writeEvsOld(self, evs):
        temp = self.readPath
        self.readPath = self.writePath
        file = open(self.readPath, 'r')
        lines = file.readlines()
        file.close()
        self.readPath = temp

        file = open(self.writePath, 'a')
        evs.insert(0, len(evs))
        if(len(lines) != 0):
            file.writelines(("\n" + str(evs[i])) for i in range(len(evs)))
        else:
            file.writelines((("\n" if i != 0 else "") + str(evs[i])) for i in range(len(evs)))
        file.close()
        return 0

    def readEValuesGuide(self):
        with open(self.readPath) as file:
            guide = file.readline()[1:-2].replace("\'", "").split(", ")
        return guide

    def guideToDict(self, guide):
        guideDict = {"": -1}
        for i in range(len(guide)):
            guideDict[guide[i]] = i
        return guideDict

    def readEValues(self, rows):
        out = []
        with open(self.readPath) as file:
            i = 0
            for line in tqdm(file):
                if (i - 1) in rows:
                    eValues = line[1:-2].replace("\'", "").split(", ")
                    out.append(eValues)
                elif (i - 1) > rows[-1]:
                    break
                i += 1
        return out

    def writeEValues(self, eValues):
        storReadPath, self.readPath = self.readPath, self.writePath
        guide = self.readEValuesGuide()
        dict = self.guideToDict(guide)
        self.readPath = storReadPath

        if len(dict) == 1:
            file = open(self.writePath, 'w')
            file.write(str([str(len(eValues))]) + "\n" + str(eValues))
            file.close()
        else:
            try:
                dict[str(len(eValues))]
            except KeyError:
                file = open(self.writePath, 'r')
                lines = file.readlines()
                file.close()
                guide.append(str(len(eValues)))
                lines[0] = str(guide) + "\n"
                lines.append("\n" + str(eValues))
                file = open(self.writePath, 'w')
                file.writelines(lines)
                file.close()
        return 0