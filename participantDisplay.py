from tkinter import *
from tkinter import ttk
from character import Character


class ParticipantDisplay(ttk.Frame):
    def __init__(self, parent, entity, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        self.entity = entity
        self.parent = parent

        armor = "AC: " + str(self.entity.armorClass)
        hp = "HP: " + str(self.entity.maxHP)

        ttk.Label(self, text=entity.characterName).grid(column=0, row=0, sticky=W)
        ttk.Label(self, text=armor).grid(column=0, row=1, sticky=W)
        ttk.Label(self, text=hp).grid(column=1, row=1)
        ttk.Label(self, text=entity.initiative).grid(column=2, row=0,
                                                     rowspan=2, sticky=E)
