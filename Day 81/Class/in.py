class Lomi:
    simba = "mefe lomi 2"
    mufasa = "mefe lomi 1"


print(Lomi.simba, Lomi.simba)





class Sname:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def quest(self):
        if self.role:
            return f"{self.name} is the {self.role}."
        return f"{self.name} has no role specified."

        print("rom davwert lamzadad gamogigdos chveni propertiebi <3")

        davwert = Sname("Davwert", "Developer")
        lamad = Sname("Lamad", None)

        print(davwert.quest())
        print(lamad.quest())