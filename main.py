# 导入游戏列表
import game_list
# 导入常量模块
from constants import constants

# 提示
print(constants.quit_tip)
print(game_list.game_list)

def get_order_number(tip):
    return input(tip)

game_order_number = get_order_number("请选择想玩的游戏，输入序号：")

while True:
    game = game_list.find_game_by_order_number(game_order_number)
    if None != game:
        game.play()
        break
    elif "退出" == game_order_number or "quit" == game_order_number.lower() or "exit" == game_order_number.lower():
        print("\n欢迎下次再玩~")
        break
    else:
        game_name = game_list.find_game_name_order_number(game_order_number)
        if None != game:
            game_order_number = get_order_number("当前选择的游戏【{}】还未开发，请重新选择：".format(game_name))
        else:
            game_order_number = get_order_number("当前选择序号为【{}】的游戏不存在，请重新选择：".format(game_order_number))