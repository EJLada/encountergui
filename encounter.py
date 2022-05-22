from tkinter import *
from tkinter import ttk
from character import Character
from participantDisplay import ParticipantDisplay


class Encounter(ttk.Frame):

    def __init__(self, parent, creatures=None, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        if creatures is None:
            creatures = []
        self.parent = parent
        self.title = "Encounter"
        self.creatures = creatures

        for index in range(len(self.creatures)):
            participant = ParticipantDisplay(self,
                               self.creatures[index],
                               borderwidth=5,
                               relief="ridge",
                               padding=(5, 10))
            participant.grid(column=0, row=index+1, sticky=(E, W))

    def rollInitiative(self):
        for creature in self.creatures:
            creature.rollInitiative()
        self.creatures.sort(key=lambda x: x.initiative, reverse=True)
        self.refresh()

    def refresh(self):
        creatures = self.creatures
        parent = self.parent
        self.destroy()
        self.__init__(parent, creatures)

