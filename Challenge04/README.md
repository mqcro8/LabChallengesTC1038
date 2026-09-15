🔴 Challenge 4 Choice-Based Text Adventure Game Engine
Build a text-driven interactive story or mini RPG combat calculator that processes a player's choices and combat stats through a series of chained functions!

Scenario: The Dungeon Encounter
A player encounters a monster. The player can choose an action: "attack", "magic", or "heal".

Game Rules
Player Stats: health (0–100), mana (0–50), attack_power.
Monster Stats: monster_health (0–100), monster_attack.
Actions:
"attack": Deals player's attack_power to monster. Monster counter-attacks for full monster_attack.
"magic": Costs 15 mana. Deals 
2.5
×
 attack_power to the monster. Monster counter-attacks for half monster_attack. (If player has 
<
15
 mana, the spell fails, player loses turn, and monster hits for full attack!).
"heal": Restores 30 health (max cap 100). Monster counter-attacks for half monster_attack.
Objective
Write a function turn_resolution(player_hp, player_mana, player_atk, monster_hp, monster_atk, choice) that calculates and prints the resulting state after one round of combat.

Requirements
Break down the logic into clear helper functions (e.g., calculate_damage(), apply_healing(), check_battle_status()).
Ensure player health cannot exceed 100 or fall below 0.
Handle invalid action strings gracefully.
Determine the battle outcome status at the end of the round: "VICTORY", "DEFEAT", "MUTUAL DEFEAT", or "Battle Continues".