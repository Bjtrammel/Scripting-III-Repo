import maya.cmds as cmds

class FreezeandDeleteUI():
    def __init__(self):
        self.my_window = 'bsfrezanddelwindow'

    def createWindow(self):
        self.delete()

        self.my_window = cmds.window(self.my_window,
                                     title='Becky Snells Freeze and Delete Window',
                                     widthHeight=(432, 432),
                                     backgroundColor=[0.019, 0.077, 0.214],
                                     s=True)


        self.basic_column = cmds.columnLayout(parent=self.my_window,
                                              columnAlign = "center",
                                              adjustableColumn=True)

        self.name_field = cmds.text(parent=self.basic_column, label='Freeze Transforms & Delete History')

        cmds.button(parent = self.basic_column, label='Freeze Transforms', command= lambda *x: self.freezeTransforms())
        cmds.button(parent = self.basic_column, label='Delete History', command= lambda *x: self.deleteHistory())
        cmds.button(parent = self.basic_column, label='Freeze Transforms & Delete History', command= lambda *x: self.freezeDelete())


        cmds.showWindow(self.my_window)

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)


    def freezeTransforms(self):
        selected = cmds.ls(selection=True)
        for s in selected:
            cmds.makeIdentity(apply=True)

    def deleteHistory(self):
        selected = cmds.ls(selection=True)
        for s in selected:
            cmds.delete(ch=True)

    def freezeDelete(self):
        selected = cmds.ls(selection=True)
        for s in selected:
            cmds.makeIdentity(apply=True)
            cmds.delete(ch=True)