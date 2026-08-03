class FM:
    def __init__(self,ec,hc):
        self.ec=ec
        self.hc=hc

    def st(self):
        print("Eye color: ",self.ec)
        print("Height (cm): ",self.hc)    

class kid(FM):
    def __init__(self, ec, hc,n,a):
        self.n=n
        self.a=a
        super().__init__(ec, hc)

    def st(self):
        print("Name:",self.n)
        print("Age:",self.a)
        super().st()

    def fh(self,hobby):
        print(self.n,"loves", hobby)

ch=kid("Brown", 165, "Hermione", 11)
ch.st()
ch.fh("painting")

print ("Is child a subclass of Family Member?",issubclass(kid,FM))


