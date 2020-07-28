import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import pandas as pd
import numpy as np
plt.style.use('dark_background')


def CreatePitch():

    #df = pd.read_csv('PulisicShots.csv')
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(16, 10))
    #plt.scatter(1 - df.Y, df.X, s=df.xG*1500, alpha=0.75)
    ax = fig.add_subplot(1, 1, 1)
    # Outer Pitch
    plt.plot([0, 0], [0.5, 1], color="white")
    plt.plot([0, 1], [1, 1], color="white")
    plt.plot([1, 1], [1, 0.5], color="white")
    plt.plot([1, 0], [0.5, 0.5], color="white")
    # 18 Yard Box
    plt.plot([0.22, 0.78], [0.83, 0.83], color="white")
    plt.plot([0.22, 0.22], [1, 0.83], color="white")
    plt.plot([0.78, 0.78], [1, 0.83], color="white")
    penArc = Arc((0.5, 0.9575), height=0.34, width=0.34, angle=0, theta1=229, theta2=311, color="white")
    ax.add_patch(penArc)
    plt.scatter(0.5, 0.885, c='white')

    # 6 Yard Box
    plt.plot([0.355, 0.645], [0.943, 0.943], color="white")
    plt.plot([0.355, 0.355], [1, 0.943], color="white")
    plt.plot([0.645, 0.645], [1, 0.943], color="white")
    # Goal
    plt.plot([0.44, 0.56], [1.01, 1.01], color="white")
    plt.plot([0.44, 0.44], [1, 1.01], color="white")
    plt.plot([0.56, 0.56], [1, 1.01], color="white")
    # Corner Arc
    leftcornerArc = Arc((0, 1), height=0.03, width=0.03, angle=0, theta1=270, theta2=0, color="white")
    ax.add_patch(leftcornerArc)
    rightcornerArc = Arc((1, 1), height=0.03, width=0.03, angle=0, theta1=180, theta2=270, color="white")
    ax.add_patch(rightcornerArc)

    plt.axis('off')
    plt.xlim(-0.01, 1.01)
    plt.ylim(0.49, 1.03)
    return fig, ax
