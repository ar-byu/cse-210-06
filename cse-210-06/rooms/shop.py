#Imports classes from other files
from casting.weapon import Weapon
from casting.shield import Shield

class Shop:
    def __init__(self, player):
        #Initializes the player, three weapons, and three shields
        self._player = player
        self.weapon_1 = Weapon()
        self.weapon_2 = Weapon()
        self.weapon_3 = Weapon()
        self.shield_1 = Shield()
        self.shield_2 = Shield()
        self.shield_3 = Shield()

    def enter_shop(self):
        #Displays the shop and asks for input
        print("""The shop is manned by a disinterested-looking goblin. There are several things on display by the counter. 
        There are weapons to the left, and shields to the right. You may only buy one item, so choose wisely.""")
        print()
        shop_choice = input("Do you buy a [w]eapon, a [s]hield, or go [b]ack to the hallway? ")
        print()
        if shop_choice.lower() == "w" or shop_choice.lower() == "weapon":
            self.buy_weapon()
        elif shop_choice.lower() == "s" or shop_choice.lower() == "shield":
            self.buy_defense()
        elif shop_choice.lower() == "b" or shop_choice.lower() == "back":
            return
        else:
            print("Please choose a valid option.")
        

    def buy_weapon(self):
        #Asks for weapon choice and adds to player's max attack
        print(f"[1] Weapon Type: {self.weapon_1.name} | Attack Bonus: {self.weapon_1.attack} | Price: {self.weapon_1.price}")
        print(f"[2] Weapon Type: {self.weapon_2.name} | Attack Bonus: {self.weapon_2.attack} | Price: {self.weapon_2.price}")
        print(f"[3] Weapon Type: {self.weapon_3.name} | Attack Bonus: {self.weapon_3.attack} | Price: {self.weapon_3.price}")
        print("[B]ack to shop menu")
        print()
        weapon_choice = input("Which weapon do you choose? ")
        print()
        if weapon_choice == "1":
            if self._player._gold <= self.weapon_1.price:
                print("You don't have enough money for that.")
                self.buy_weapon()
            else:
                self._player.equip_new_weapon(self.weapon_1)
                self._player.pay(self.weapon_1.price)
        elif weapon_choice == "2":
            if self._player._gold <= self.weapon_2.price:
                print("You don't have enough money for that.")
                self.buy_weapon()
            else:
                self._player.equip_new_weapon(self.weapon_2)
                self._player.pay(self.weapon_2.price)
        elif weapon_choice == "3":
            if self._player._gold <= self.weapon_3.price:
                print("You don't have enough money for that.")
                self.buy_weapon()
            else:
                self._player.equip_new_weapon(self.weapon_3)
                self._player.pay(self.weapon_3.price)
        elif weapon_choice.lower() == "b" or weapon_choice.lower() == "back":
            self.enter_shop()
        else:
            print("Please choose a valid option.")
        print(f"You pay the goblin for your purchase. Your attack is now {self._player._attack}, and your gold is now {self._player._gold}.")
        print()
        return self._player._attack, self._player._max_attack, self._player._gold

    def buy_defense(self):
        #Asks for defense choice and adds to player's defense
        print(f"[1] Shield Type: {self.shield_1.name} | Defense: {self.shield_1.defense} | Price: {self.shield_1.price}")
        print(f"[2] Shield Type: {self.shield_2.name} | Defense: {self.shield_2.defense} | Price: {self.shield_2.price}")
        print(f"[3] Shield Type: {self.shield_3.name} | Defense: {self.shield_3.defense} | Price: {self.shield_3.price}")
        print("[B]ack to shop menu")
        print()
        shield_choice = input("Which shield do you choose? ")
        print()
        if shield_choice == "1":
            if self._player._gold < self.shield_1.price:
                print("You don't have enough gold for this.")
                self.buy_defense()
            else:
                self._player.equip_new_shield(self.shield_1)
                self._player.pay(self.shield_1.price)
        elif shield_choice == "2":
            if self._player._gold < self.shield_2.price:
                print("You don't have enough gold for this.")
                self.buy_defense()
            else:
                self._player.equip_new_shield(self.shield_2)
                self._player.pay(self.shield_2.price)
        elif shield_choice == "3":
            if self._player._gold < self.shield_3.price:
                print("You don't have enough gold for this.")
                self.buy_defense()
            else:
                self._player.equip_new_shield(self.shield_3)
                self._player.pay(self.shield_3.price)
        elif shield_choice.lower() == "b" or shield_choice.lower() == "back":
            self.enter_shop()
        else:
            print("Please choose a valid option.")
        print(f"You pay the goblin for your purchase. Your defense is now {self._player._defense}, and your gold is now {self._player._gold}.")
        print()
        return self._player._defense, self._player._gold