# 产品经理：提需求  /  改需求
# 开放封闭原则，已经写好的代码能不要改就不要改
# 装饰器的高级使用：在不采编原有函数的基础上，为函数增添函数，增加功能

def can_play(fn):
    def inner(name, game, *args, **kwargs):
        if args[0] <= 22:
            fn(name, game)
        else:
            print('太晚了')

    return inner


@can_play
def play_game(name, game):
    print("{}正在玩{}".format(name, game))


play_game("张三", "王者荣耀", 18)
play_game("李四", "绝地求生", 24)
