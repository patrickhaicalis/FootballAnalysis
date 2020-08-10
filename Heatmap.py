import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from UnderstatPitch import CreatePitch
from PIL import Image
from matplotlib.colors import LinearSegmentedColormap
import json
import cv2
import numpy as np


def Heatmapshots(name):

    im = Image.open(f'Images/Shots/{name}Shots.png')

    with open(f'jsonfiles/{name}.json') as data_file:
        data = json.load(data_file)

    df = pd.read_json(data)

    f, ax = CreatePitch()
    cmap = LinearSegmentedColormap.from_list("", ['black', "blue","green","yellow","red"])
    sns.kdeplot(1-df.Y, df.X, cmap=cmap, n_levels=50, shade=True, shade_lowest=False)
    plt.savefig(f'Images/ShotHeatmap/{name}ShotHeatmap.png')

    m =  plt.imread(f"Images/ShotHeatmap/{name}ShotHeatmap.png")

    h,w,bpp = np.shape(m)

    for py in range(0,h):
        for px in range(0,w):

            if(m[py][px][0] > 15) and (m[py][px][1] < 150):
                m[py][px][0]=0
                m[py][px][1]=0
                m[py][px][2]=0
            if (170 > m[py][px][1]) and (200> m[py][px][2]):
                m[py][px][0] = 0
                m[py][px][1] = 0
                m[py][px][2] = 0

    plt.title(f'{name} Shot Heatmap 2019/20 Season')
    plt.savefig(f'Images/ShotHeatmap/{name}ShotHeatmapTEST.png')
    plt.show()
