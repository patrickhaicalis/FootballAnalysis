import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from UnderstatPitch import CreatePitch
import json


def ShotResult(name):

    with open(f'jsonfiles/{name}.json') as data_file:
        data = json.load(data_file)

    df = pd.read_json(data)

    (fig, ax) = CreatePitch()


    for i, shot in df.iterrows():
        x = shot['X']
        y = shot['Y']

        goal = shot['result'] == 'Goal'
        missed = shot['result'] == 'MissedShots'
        blocked = shot['result'] == 'BlockedShot'
        saved = shot['result'] == 'SavedShot'

        size = shot.xG*1200
        alpha = 0.9

        if goal:
            plt.scatter(1 - y, x, s=size, alpha=alpha, c='green', label='Goal', edgecolors='white', linewidths=3)
        elif missed:
            plt.scatter(1 - y, x, s=size, alpha=alpha, c='red', label='Miss')
        elif blocked:
            plt.scatter(1 - y, x, s=size, alpha=alpha, c='purple')
        elif saved:
            plt.scatter(1 - y, x, s=size, alpha=alpha, c='blue')
        else:
            plt.scatter(1 - y, x, s=size, alpha=alpha, c='yellow')

        Goal = plt.Circle((4, 4), 5, color='green')
        Miss = plt.Circle((4, 4), 5, color='red')
        Block = plt.Circle((4, 4), 5, color='purple')
        Save = plt.Circle((4, 4), 5, color='blue')
        Other = plt.Circle((4, 4), 5, color='yellow')

        plt.legend((Goal, Miss, Block, Save, Other), ('Goal', 'Miss', 'Block', 'Save', 'Other'),
                   loc='upper right', prop={'size': 15})

    plt.title(f'{name} Shots 2019/20 Season')
    plt.savefig(f'Images/{name}Shots.png')
    plt.show()
