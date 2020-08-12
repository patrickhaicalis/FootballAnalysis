import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import rcParams

def CombinedReport(name):
    # figure size in inches optional
    rcParams['figure.figsize'] = 33 ,24
    rcParams['figure.facecolor'] = 'black'

    # read images
    shots = mpimg.imread(f'Images/Shots/{name}Shots.png')
    toshots = mpimg.imread(f'Images/TypeOfShot/{name}TypeOfShot.png')
    heatmap = mpimg.imread(f'Images/ShotHeatmap/{name}ShotHeatmap.png')
    heatmapgoal = mpimg.imread(f'Images/GoalHeatmap/{name}GoalHeatmap.png')

    # display images
    fig, ax = plt.subplots(2,2)
    ax[0, 0].imshow(shots)
    ax[0, 0].axis('off')

    ax[0, 1].imshow(toshots)
    ax[0, 1].axis('off')

    ax[1, 0].imshow(heatmap)
    ax[1, 0].axis('off')

    ax[1, 1].imshow(heatmapgoal)
    ax[1, 1].axis('off')
    fig.patch.set_facecolor('black')
    plt.savefig(f'Images/Combined Report/{name}Report.png')
