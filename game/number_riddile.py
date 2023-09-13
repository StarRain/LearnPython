# 导入随机数模块
import random

# 目标数字
target_numbder = 1
# 计数器，记录猜了几局
play_count = 0

# 开始游戏
def play():
    # 生命成全局变量
    global target_numbder
    global play_count

    # 重置猜的次数
    play_count = 0
    # 从1-100中随机一个数字出来
    target_numbder = random.randint(1, 100)
    # print("当前答案是：{}".format(target_numbder))
    # 获取用户输入的内容
    content = input("请输入100(含)以内的任意正整数:")
    # 判断输入内容
    judgement(content)

# 判断输入内容
def judgement(content):
    global play_count
    play_count = play_count + 1
    if content.isdigit():
        input_number = int(content)
        if input_number == target_numbder:
            print("\n太棒了，你猜对了！您一共猜了{}局！".format(play_count))
            again = input("\n再来一局？(Y/N)")
            if "Y" == again.upper():
                start_game()
            else:
                print("\n欢迎下次再玩~")
        elif input_number > target_numbder:
            if input_number - target_numbder <= 5:
                print("\n接近了，加油~")
            else:
                print("\n太大了！")

            content = input("\n请再次输100(含)以内的任意正整数:")
            judgement(content)
        elif input_number < target_numbder:
            if target_numbder - input_number <= 5:
                print("\n接近了，加油~")
            else:
                print("\n太小了！")

            content = input("\n请再次输100(含)以内的任意正整数:")
            judgement(content)
        else:
            print("程序出错了~")
    elif "退出" == content or "qw" == content.lower():
        print("\n欢迎下次再玩~")
    else:
        print("\n只能输入数字哦~")
        content = input("\n请再次输入100(含)以内的任意正整数:")
        judgement(content)

print("Tips: 游戏过程中输入qw/QW/退出，即可退出游戏~\n")