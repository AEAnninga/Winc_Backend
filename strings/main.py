# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
nl_player_10 = 'Ruud Gullit'
nl_player_12 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = nl_player_10 + ' ' + str(goal_0) + ', ' + nl_player_12 + ' ' + str(goal_1)

report = f'{nl_player_10} scored in the {goal_0}nd minute\n{nl_player_12} scored in the {goal_1}th minute'

print(report)

# part 2

player = 'Frank de Boer'
first_name = player[:player.find(" ")]
last_name_len = len(player[player.find(" ")+1:])
name_short = f'{player[0]}. {player[player.find(" ")+1:]}'
chant = (f'{first_name}! ' * len(first_name)).strip()
good_chant = chant[-1:] != ' ' 
# good_chant = chant[-1:].isspace() == False

print(first_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)
# print(good_chant_2)
