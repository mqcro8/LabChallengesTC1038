def calc_damage(attack, mult):
    return attack * mult

def apply_healing(health, healing):
    health += healing
    if health > 100:
        health = 100
    return health

def check_battle_status(player_hp, monster_hp):
    if player_hp <= 0 and monster_hp <= 0:
        return "MUTUAL DEFEAT"
    elif monster_hp <= 0:
        return "VICTORY"
    elif player_hp <= 0:
        return "DEFEAT"
    else:
        return "Battle continues"
    
def turn_resolution(player_hp, player_mana, player_atk, monster_hp, monster_atk, choice):
    if choice.lower() == "attack":
        damage = calc_damage(player_atk, 1)
        monster_hp -= damage
        player_hp -= monster_atk
        
        print("You decided to attack and delt", damage, "damage")
        print("Monster delt you", monster_atk, "damage")
    
    elif choice.lower() == "magic":
        if player_mana >= 15:
            player_mana -= 15
            damage = calc_damage(player_atk, 2.5)
            monster_hp -= damage
            monster_damage = monster_atk / 2
            player_hp -= monster_damage
            
            print("You decided to make a magic attack and delt", damage, "damage")
            print("Monster delt you", monster_damage, "damage")
        
        else:
            player_hp -= monster_atk
            
            print("Not enough mana, your spell failed!")
            print("Monster delt you", monster_atk, "damage")
    
    elif choice.lower() == "heal":
        player_hp = apply_healing(player_hp, 30)
        monster_damage = monster_atk / 2
        player_hp -= monster_damage
        
        print("You healed yourself, now you have", player_hp, "hp")
        print("Monster delt you", monster_damage, "damage")
        
    else:
        print("Invalid action")
        print("Choose: attack, magic, or heal")
        return player_hp, player_mana, monster_hp
    
    if player_hp <= 0:
        player_hp = 0
    
    if monster_hp <= 0:
        monster_hp = 0
        
    status = check_battle_status(player_hp, monster_hp)
    
    print("Player hp:", player_hp)
    print("Player mana:", player_mana)
    print("Monster hp:", monster_hp)
    print("Status:", status)
    
    return player_hp, player_mana, monster_hp
        
def main():
    player_hp = 100
    player_mana = 50
    player_atk = 10
    monster_hp = 100
    monster_atk = 10
    
    print("THE DUNGEON ENCOUNTER")
    print("You enounter a monster")
    print("Actions: attack, magic, heal")
    
    while (player_hp > 0) and (monster_hp > 0):
        choice = input("What do you want to do? ")
        player_hp, player_mana, monster_hp = turn_resolution(player_hp, player_mana, player_atk, monster_hp, monster_atk, choice)
main()
