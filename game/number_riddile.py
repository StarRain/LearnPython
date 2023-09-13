# 导入随机数模块
import random

# 开始游戏
def play():
    # 声明成全局变量
    global target_numbder
    global play_count

    # 重置猜的次数
    play_count = 0
    # 从1-100中随机一个数字出来
    target_numbder = random.randint(1, 100)
    # TODO debug code
    print("当前答案是：****{}***".format(target_numbder))
    # 获取用户输入的内容
    content = input("请输入100(含)以内的任意正整数: ")
    # 判断输入内容
    judgement(content)

# 判断输入内容


def judgement(content):
    global play_count
    play_count = play_count + 1
    if content.isdigit():
        input_number = int(content)
        if input_number == target_numbder:
            print("太棒了，你猜对了！您一共猜了{}局！".format(play_count))
            play_once_again = input("\n再来一局？(Y/N) ")
            if "Y" == play_once_again.upper():
                play()
            else:
                print("\n欢迎下次再玩~")
        elif input_number > target_numbder:
            if input_number - target_numbder <= 5:
                again_input("接近了，加油~")
            else:
                again_input("太大了！")
        elif input_number < target_numbder:
            if target_numbder - input_number <= 5:
                again_input("接近了，加油~")
            else:
                again_input("太小了！")
        else:
            print("程序出错了~")
    elif "退出" == content or "quit" == content.lower() or "exit" == content.lower():
        print("\n欢迎下次再玩~")
    else:
        again_input("只能输入数字哦~")

# 提示用户再次输入


def again_input(tip):
    print(tip)
    content = input("\n请再次输入100(含)以内的任意正整数: ")
    judgement(content)
