"""
Chain Of Responsibility - A chain of components who all get a chance to process a command or a query, optionally having default processing implementation and an ability to terminate the processing chain
"""
from abc import ABC
from enum import Enum

class Creature:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self) -> str:
        return f'{self.name} ({self.attack}/{self.defense})'

class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        self.next_modifier = None

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier=modifier)
        else:
            self.next_modifier=modifier

class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f"Doubling {self.creature.name}'s attack ")
        self.creature.attack *= 2
        super().handle()

goblin = Creature('Goblin', 1, 1)
print(goblin)
root = CreatureModifier(goblin)
root.add_modifier(DoubleAttackModifier(goblin))
root.handle()
print(goblin)
