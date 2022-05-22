from tkinter import *
from tkinter import ttk
from encounter import Encounter
from character import Character

# Temp data definitions
character1 = Character(characterName="Omin Dran",
                       level=7,
                       charClass="Paladin",
                       subclass=None,
                       armorClass=18,
                       maxHP=65)
character2 = Character(characterName="Jim Darkmagic",
                       level=7,
                       charClass="Wizard",
                       subclass=None,
                       armorClass=12,
                       maxHP=40)
character3 = Character(characterName="Viari",
                       level=7,
                       charClass="Rogue",
                       subclass=None,
                       armorClass=18,
                       maxHP=65)
character4 = Character(characterName="Morgaen",
                       level=7,
                       charClass="Ranger",
                       subclass=None,
                       armorClass=16,
                       maxHP=66)
kobold1 = Character(characterName="kobold",
                    level=None,
                    charClass=None,
                    subclass=None,
                    armorClass=12,
                    maxHP=5)
kobold2 = Character(characterName="kobold",
                    level=None,
                    charClass=None,
                    subclass=None,
                    armorClass=12,
                    maxHP=5)
kobold3 = Character(characterName="kobold",
                    level=None,
                    charClass=None,
                    subclass=None,
                    armorClass=12,
                    maxHP=5)
kobold4 = Character(characterName="kobold",
                    level=None,
                    charClass=None,
                    subclass=None,
                    armorClass=12,
                    maxHP=5)
creatures = [character1,
             character2,
             character3,
             character4,
             kobold1,
             kobold2,
             kobold3,
             kobold4]


class EncounterBuilder(Frame):

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("5e Encounter Builder")
        button = ttk.Button(self,
                            text="Roll Initiative!",
                            command=self.rollInitiative)
        button.pack()
        self.display = Encounter(self, creatures)
        self.display.pack()

    def rollInitiative(self):
        for creature in creatures:
            creature.rollInitiative()
        creatures.sort(key=lambda x: x.initiative, reverse=True)
        self.display.destroy()
        self.display = Encounter(self, creatures)
        self.display.pack()


if __name__ == "__main__":
    root = Tk()

    windowWidth = 600
    windowHeight = 400

    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    centerX = int(screenWidth / 2 - windowWidth / 2)
    centerY = int(screenHeight / 2 - windowHeight / 2)

    root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')

    EncounterBuilder(root).pack(side='top', fill='both', expand=True)

    root.mainloop()