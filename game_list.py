# 导入猜数字小游戏
from game import number_riddile
from module import game

game_dict = {"1": game.Game("猜数字", number_riddile), "2": game.Game("猜数字", number_riddile)}

game_dict_keys = list(game_dict.keys())

game_dict_values = list(game_dict.values())

game_list = ""

for index in range(0, len(game_dict)):
    game_list += ("\t{}、{}\n".format(game_dict_keys[index], game_dict_values[index].name))    

def find_game_name_order_number(order_number):
    game_obj = game_dict.get(order_number);
    if(None != game_obj):
        return game_obj.name
    else:
        return None

# 根据序号返回对应的游戏
def find_game_by_order_number(order_number):
    game_obj = game_dict.get(order_number);
    if(None != game_obj):
        return game_obj.game
    else:
        return None

