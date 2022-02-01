# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
nl_player_10 = 'Ruud Gullit'
nl_player_12 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = nl_player_10 + ' ' + str(goal_0) + ', ' + nl_player_12 + ' ' + str(goal_1)

report = f'{nl_player_10} scored in the {str(goal_0)}nd minute\n{nl_player_12} scored in the {str(goal_1)}th minute'

print(report)

# part 2

player = 'Ronald Koeman'
# index_first_name = nl_player_4.find("Ronald")
# index_last_name = nl_player_4.find("Koeman")
# index_first_name_end = index_last_name - 2
# nl_player_4_first_name = nl_player_4[index_first_name:index_first_name_end]
# nl_player_4_last_name = nl_player_4[index_last_name:]
# But exercises must be single lines:
first_name = player[player.find("Ronald"):6]
last_name_len = len(player[player.find("Koeman"):])
name_short = f'{first_name[:1]}. {player[player.find("Koeman"):]}'
chant = (f'{first_name}! ' * len(first_name)).strip()
good_chant = chant[-1:] != '' 
# good_chant = chant[-1:].isspace() == False

print(first_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)
print(good_chant_2)