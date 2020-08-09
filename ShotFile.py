from Test import understat_json
from PulisicShots import ShotResult
from TypeOfShot import TypeOfShot
from Heatmap import Heatmapshots
from HeatmapGoal import Heatmapgoals

name = 'Salah'
id = 1250

understat_json(name, id)
ShotResult(name)
TypeOfShot(name)
Heatmapshots(name)
Heatmapgoals(name)
print('All done!')
