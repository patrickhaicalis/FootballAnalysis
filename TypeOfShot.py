import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from UnderstatPitch import CreatePitch
import json

def TypeOfShot(name):

    with open(f'jsonfiles/{name}.json') as data_file:
        data = json.load(data_file)

    df = pd.read_json(data)

    (fig, ax) = CreatePitch()


    for i, shot in df.iterrows():
        x = shot['X']
        y = shot['Y']

        right = shot['shotType'] == 'RightFoot'
        left = shot['shotType'] == 'LeftFoot'
        head = shot['shotType'] == 'Head'
        goal = shot['result'] == 'Goal'

        size = shot.xG*1200
        alpha = 0.9

        if right:
            if goal:
                plt.scatter(1 - y, x, s=size, alpha=alpha, c='green', label='Goal', edgecolors='white', linewidths=3)
            else:
                plt.scatter(1 - y, x, s=size, alpha=alpha, c='green')
        elif left:
            if goal:
                plt.scatter(1 - y, x, s=size, alpha=alpha, c='blue', label='Goal', edgecolors='white', linewidths=3)
            else:
                plt.scatter(1 - y, x, s=size, alpha=alpha, c='blue')
        elif head:
            if goal:
                    plt.scatter(1 - y, x, s=size, alpha=alpha, c='purple', label='Goal', edgecolors='white', linewidths=3)
            else:
                plt.scatter(1 - y, x, s=size, alpha=alpha, c='purple')
        else:
            plt.scatter(1 - y, x, s=size, alpha=alpha, c='yellow')

        righty = plt.Circle((4, 4), 5, label='Right', color='green')
        lefty = plt.Circle((4, 4), 5, label='Left', color='blue')
        heady = plt.Circle((4, 4), 5, label='Head', color='purple')

        plt.legend((righty, lefty, heady), ('Right', 'Left', 'Head'), loc='upper right', prop={'size': 15})

    plt.title(f'{name} Shots 2019/20 Season Body Parts')
    plt.savefig(f'Images/{name}TypeOfShot.png')
    plt.show()
