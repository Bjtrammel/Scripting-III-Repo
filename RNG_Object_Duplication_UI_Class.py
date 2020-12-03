import maya.cmds as cmds
import random

class RNGUI():
    def __init__(self):
        self.my_window = 'bsrngwindow'

    def createWindow(self):
        self.delete()

        self.my_window = cmds.window(self.my_window,
                                     title='Becky Snells RNG Window',
                                     widthHeight=(432, 432),
                                     #backgroundColor=[0.019, 0.077, 0.214],
                                     s=True)


        self.basic_column = cmds.columnLayout(parent=self.my_window,
                                              columnAlign = "center",
                                              adjustableColumn=True)

        cmds.text(parent=self.basic_column, label='Please input: ')
        cmds.text(parent=self.basic_column, label='Number of Times to Duplicate Object:')
        self.dupeNum_input = cmds.intField(parent=self.basic_column)
        cmds.text(parent=self.basic_column, label='Max X Value')
        self.maxX_input = cmds.floatField(parent=self.basic_column)
        cmds.text(parent=self.basic_column, label='Max Y Value')
        self.maxY_input = cmds.floatField(parent=self.basic_column)
        cmds.text(parent=self.basic_column, label='Max Z Value')
        self.maxZ_input = cmds.floatField(parent=self.basic_column)

        cmds.button(parent = self.basic_column, label='Randomize', command= lambda *x: self.rngObjs())

        cmds.showWindow(self.my_window)

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

    def rngObjs(self):
        dupeNum = cmds.intField(self.dupeNum_input, q=True, value=True)
        maxX = cmds.floatField(self.maxX_input, q=True, value=True)
        maxY = cmds.floatField(self.maxY_input, q=True, value=True)
        maxZ = cmds.floatField(self.maxZ_input, q=True, value=True)
        selected = cmds.ls(selection=True)
        allDupedObjects = []
        for s in range(0, dupeNum):
            dupeObjs = cmds.duplicate(selected)
            allDupedObjects.extend(dupeObjs)

        for i in allDupedObjects:
            cmds.move(random.uniform(0, maxX), random.uniform(0, maxY), random.uniform(0, maxZ), i)
