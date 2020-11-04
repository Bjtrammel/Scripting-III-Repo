import maya.cmds as cmds
import random

def rngObjs(dupeNum, maxX, maxY, maxZ):
    selected = cmds.ls(selection=True)
    allDupedObjects = []
    for s in range(0 , dupeNum):
        dupeObjs = cmds.duplicate(selected)
        allDupedObjects.extend(dupeObjs)

    for i in allDupedObjects:
        cmds.move( random.uniform(0, maxX), random.uniform(0, maxY), random.uniform(0, maxZ), i)

print rngObjs(5, 10, 10, 10)