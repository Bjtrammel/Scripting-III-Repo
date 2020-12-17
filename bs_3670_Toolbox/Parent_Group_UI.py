import maya.cmds as cmds

class ParentGroupUI():
    def __init__(self):
        self.my_window = 'bspargrpwindow'

    def createWindow(self):
        self.delete()

        self.my_window = cmds.window(self.my_window,
                                     title='Becky Snells Parent Group Window',
                                     widthHeight=(432, 432),
                                     backgroundColor=[0.019, 0.077, 0.214],
                                     s=True)


        self.basic_column = cmds.columnLayout(parent=self.my_window,
                                              columnAlign = "center",
                                              adjustableColumn=True)

        self.name_field = cmds.text(parent=self.basic_column, label='Create Parent Group')

        cmds.button(parent = self.basic_column, label='Single Object', command= lambda *x: self.singleobjpg())
        cmds.button(parent = self.basic_column, label='Multiple Objects', command= lambda *x: self.multiobjpg())

        cmds.showWindow(self.my_window)

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

    def singleobjpg(self):
        obj = cmds.ls(selection=True)[0]
        cmds.duplicate(obj)
        nullgrp = cmds.ls(selection=True)
        selection = cmds.select(obj, nullgrp)
        cmds.parent()
        cmds.select(nullgrp)
        cmds.pickWalk(direction='down')
        cmds.delete()
        cmds.select(nullgrp)
        cmds.rename(nullgrp, obj + '_grp')

    def multiobjpg(self):
        obj = cmds.ls(selection=True)
        obj_num = len(obj)
        cmds.duplicate(obj)
        nullgrp = cmds.ls(selection=True)
        for i in range(0, obj_num):
            cmds.parent(obj[i], nullgrp[i])
        selection = cmds.select(nullgrp)
        cmds.pickWalk(direction='down')
        cmds.delete()
        selection = cmds.select(nullgrp)
        for r in range(obj_num):
            cmds.rename(nullgrp[r], obj[r] + '_grp')
