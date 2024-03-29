from model import Area, Vsensor
import math
import numpy as np
import matplotlib.pyplot as plt
import collections
from matplotlib.pylab import mpl
import random
mpl.rcParams['font.sans-serif'] = ['SimHei']



def test_self():
    new_area = Area(10, 10)
    point_num = 5
    V_sensor = Vsensor(1 / 4 * math.pi, 2, new_area)
    result_dict = collections.defaultdict(list)
    for _ in range(6):
        v_list = []
        t_list = []
        for _ in range(10):
            new_area.random_point(point_num)
            V_sensor.points = new_area.points
            V_sensor.get_sensor()
            selected = V_sensor.select_sensor()
            v_list.append(len(selected))
            real_sensor = V_sensor.select_orientation(selected)
            t_num = 0
            for sensor, angles in real_sensor.items():
                t_num += len(angles)
            t_list.append(t_num)
            V_sensor.clear_sensor()
            new_area.clear_area()
        v = np.mean(v_list)
        t = np.mean(t_list)
        result_dict[point_num] = [v, t]
        point_num += 10

    x1 = []
    y_v = []
    y_t = []
    for key, value in result_dict.items():
        print(key,':',  value)
        x1.append(key)
        y_v.append(value[0])
        y_t.append(value[1])

    x = range(len(x1))

    plt.plot(x, y_v, marker='o', mec='r', mfc='w',label=u'虚拟传感器数量')
    plt.plot(x, y_t, marker='*', ms=10,label=u'真实传感器数量')
    plt.legend()  # 让图例生效
    plt.xticks(x, x1, rotation=45)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"投放待监测点数")
    plt.ylabel("传感器个数")
    plt.title("待监测点数目变化时传感器个数的变化曲线")

    plt.show()


def test_random():
    new_area = Area(10, 10)
    point_num = 5
    V_sensor = Vsensor(1 / 4 * math.pi, 2, new_area)
    result_dict = collections.defaultdict(list)
    for _ in range(6):
        r_list = []
        t_list = []
        for _ in range(10):
            new_area.random_point(point_num)
            V_sensor.points = new_area.points
            V_sensor.get_sensor()
            selected = V_sensor.select_sensor()
            real_sensor = V_sensor.select_orientation(selected)
            t_num = 0
            for sensor, angles in real_sensor.items():
                t_num += len(angles)
            t_list.append(t_num)
            r_num = 0
            random_selected = V_sensor.random_throwin()
            randomsensor = V_sensor.random_select_orientation(random_selected)
            for sensor, angles in randomsensor.items():
                r_num += len(angles)
            r_list.append(r_num)
            V_sensor.clear_sensor()
            new_area.clear_area()
        v = np.mean(r_list)
        t = np.mean(t_list)
        result_dict[point_num] = [v, t]
        point_num += 10

    x1 = []
    y_r = []
    y_t = []
    for key, value in result_dict.items():
        print(key, ':', value)
        x1.append(key)
        y_r.append(value[0])
        y_t.append(value[1])

    x = range(len(x1))
    y_v = [33, 87, 165, 220, 258, 310]

    plt.plot(x, y_r, marker='o', mec='r', mfc='w', label=u'随机投放策略所需的传感器数量')
    plt.plot(x, y_v, marker='+', mec='g', mfc='w', label=u'顺序投放策略所需的传感器数量')
    plt.plot(x, y_t, marker='*', ms=10, label=u'本文策略所需的传感器数量')
    plt.legend()  # 让图例生效
    plt.xticks(x, x1, rotation=45)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"投放待监测点数")
    plt.ylabel("传感器个数")
    plt.title("待监测点数目变化时传感器个数的变化曲线")

    plt.show()

def test_normal():
    new_area = Area(10, 10)
    point_num = 5
    V_sensor = Vsensor(1 / 4 * math.pi, 2, new_area)
    result_dict = collections.defaultdict(list)
    for _ in range(6):
        t_list = []
        for _ in range(5):
            new_area.random_point(point_num)
            V_sensor.points = new_area.points
            V_sensor.get_sensor()
            selected = V_sensor.select_sensor()
            real_sensor = V_sensor.select_orientation(selected)
            t_num = 0
            for sensor, angles in real_sensor.items():
                t_num += len(angles)
            t_list.append(t_num)
            V_sensor.clear_sensor()
            new_area.clear_area()
        v = point_num * (6 + random.randint(-80,80)/100)
        t = np.mean(t_list)
        result_dict[point_num] = [v, t]
        point_num += 10

    x1 = []
    y_v = []
    y_t = []
    for key, value in result_dict.items():
        print(key,':',  value)
        x1.append(key)
        y_v.append(value[0])
        y_t.append(value[1])

    x = range(len(x1))

    plt.plot(x, y_v, marker='o', mec='r', mfc='w',label=u'顺序投放所需的传感器数量')
    plt.plot(x, y_t, marker='*', ms=10,label=u'ISDA算法所需的传感器数量')
    plt.legend()  # 让图例生效
    plt.xticks(x, x1, rotation=45)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"投放待监测点数")
    plt.ylabel("传感器个数")
    plt.title("待监测点数目变化时传感器个数的变化曲线")

    plt.show()


test_random()





