import xmltodict

class ParseXML:
    def __init__(self, filename="config.xml"):
        self.filename = filename
        if not('.xml' in self.filename):
            raise Exception("Invalid file")
        
        with open(self.filename, 'r') as f:
            self.fileContents = f.read()
            f.close()

        self.contentsAsDict = xmltodict.parse(self.fileContents)
        
    
if __name__ == "__main__":
    classTest = ParseXML()
    print(classTest.contentsAsDict)

    try:
        classTest = ParseXML("config.xm")
        print(classTest.contentsAsDict)
    except:
        print("Error occured")    