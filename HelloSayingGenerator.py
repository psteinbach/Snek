class HelloSayingGenerator(object):
    """docstring forHelloSayingGenerator."""
    def __init__(self, name):
        self.name = name

    def sayHelloToName(self):
        print("Hello, " + self.name + ".")

    def sayHelloToNameLoudly(self):
        print("HELLO, " + self.name.upper() + "!")

    def neverWriteThisFunction(self):
        pass
