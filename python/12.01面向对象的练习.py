# 房子(House)有户型、总面积，剩余面积（等于总面积的60%） 和 家具名称列表 属性，
# 新房子没有任何家具，
# 将 家具的名称追加 到 家具名称列表 中，
# 判断 家具的面积 是否 超过剩余面积。如果超过 提示不能添加家具，
class House(object):
    # 缺省参数
    def __init__(self, house_type, total_area, fru_list=None):
        if fru_list is None:  # 如果这个值为空，将他设置为一个空列表
            fru_list = []
        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area * 0.6
        self.fru_list = fru_list

    def add_fru(self, x):
        if self.free_area < x.area:
            print('剩余面积不足')
        else:
            self.fru_list.append(x.name)
            self.free_area = self.free_area - x.area

    def __str__(self):
        return '户型={}，总面积={}，剩余面积={}，家具列表={}'.format(self.house_type, self.total_area, self.free_area, self.fru_list)

    # 家具（Furniture），家具有 名字 和 占地属性，其中


# 席梦思（bed）占地4㎡，
# 衣柜（chest）占地2㎡。
# 餐桌(table)占地1.5㎡，
# 将以上三件家具添加到房子中，
# 打印房子时要求输出 户型、 总面积，剩余面积，家具名称列表。

class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area


# 创建房间对象时候，传入户型和总面积
house = House('一室一厅', 20)
sofa = Furniture('沙发', 10)
bed = Furniture('席梦思', 4)
chest = Furniture('衣柜', 2)
table = Furniture('餐桌', 1.5)

# 把家具添加到房间里（面向对象关注点：让谁做），
house.add_fru(sofa)
house.add_fru(bed)
house.add_fru(chest)
house.add_fru(table)
# 调用对象的__str__ ,__repr__方法
print(house)
