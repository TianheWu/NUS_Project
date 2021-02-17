import matplotlib.pyplot as plt
import random


def random_color():
    color = ['royalblue', 'orange', 'darkred', 'gold', 'deeppink', 'firebrick',
             'indigo', 'mediumpurple', 'limegreen', 'darkmagenta', 'hotpink',
             'mediumblue', 'goldenrod', 'yellow', 'gold']

    i = random.randint(0, 14)
    return color[i]


def func_draw(new_x, new_y, name):
    plt.scatter(new_x, new_y, label=name, s=12, c=random_color())
