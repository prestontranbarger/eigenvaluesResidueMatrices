class rwEvs:
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

    def readEvs(self, n):
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

    def writeEvs(self, evs):
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
