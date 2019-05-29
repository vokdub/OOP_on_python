class Person:

    nameOfPerson = ""

    def __init__(self, name):
        self.nameOfPerson = name

    def name(self, value=0):
        if value:
            self.nameOfPerson = value
        else:
            print (self.nameOfPerson)

    def marry(self):
        pass

    def divorce(self):
        pass

class Man(Person):

    hisWoman = None

    def marry(self, woman):
        if isinstance(woman, Woman):
            if self.hisWoman is None and woman.herMan is None:
                self.hisWoman = woman
                woman.herMan = self
            else:
                print("one of the marriage mates must first divorce the previous spouse")
        else:
            print("Only heterosexual marriages are allowed")

    def wife(self, woman=0):
        if woman:
            if isinstance(woman, Woman):
                if self.hisWoman is None and woman.herMan is None:
                    self.hisWoman = woman
                    woman.herMan = self
                else:
                    print("one of the marriage mates must first divorce the previous spouse")
            else:
                print("Only heterosexual marriages are allowed")
        else:
            try:
                print (self.hisWoman.nameOfPerson)
            except AttributeError:
                print ("No spouse")

    def divorce(self):
        self.hisWoman = None
        self.hisWoman.herMan = None

class Woman(Person):

    herMan = None

    def marry(self, man):
        if isinstance(man, Man):
            if self.herMan is None and man.hisWoman is None:
                self.herMan = man
                man.hisWoman = self
            else:
                print("one of the marriage mates must first divorce the previous spouse")
        else:
            print("Only heterosexual marriages are allowed")

    def husband(self, man=0):
        if man:
            if isinstance(man, Man):
                if self.herMan is None and man.hisWoman is None:
                    self.herMan = man
                    man.hisWoman = self
                else:
                    print("one of the marriage mates must first divorce the previous spouse")
            else:
                print("Only heterosexual marriages are allowed")
        else:
            try:
                print (self.herMan.nameOfPerson)
            except AttributeError:
                print ("No spouse")

    def divorce(self):
        self.herMan = None
        self.herMan.hisWoman = None
