import maya.cmds as cmds

class ToggleAxisUI():
    def __init__(self):
        self.my_window = 'bstlrawindow'

    def createWindow(self):
        self.delete()

        self.my_window = cmds.window(self.my_window,
                                     title='Becky Snells Toggle Local Rotation Axis Window',
                                     widthHeight=(432, 432),
                                     backgroundColor=[0.019, 0.077, 0.214],
                                     s=True)


        self.basic_column = cmds.columnLayout(parent=self.my_window,
                                              columnAlign = "center",
                                              adjustableColumn=True)

        self.name_field = cmds.text(parent=self.basic_column, label='On Channel Box')

        cmds.button(parent = self.basic_column, label='Toggle All', command= lambda *x: self.toggleall())
        cmds.button(parent = self.basic_column, label='Toggle Display Local Axis', command= lambda *x: self.toggledla())
        cmds.button(parent=self.basic_column, label='Toggle Joint Orient X', command=lambda *x: self.togglexjnt())
        cmds.button(parent=self.basic_column, label='Toggle Joint Orient Y', command=lambda *x: self.toggleyjnt())
        cmds.button(parent=self.basic_column, label='Toggle Joint Orient Z', command=lambda *x: self.togglezjnt())

        cmds.showWindow(self.my_window)

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)


    def toggleall(self):
        obj = cmds.ls(sl=True)
        for i in obj:
            cmds.setAttr(i + '.jointOrientX', channelBox=True)
            cmds.setAttr(i + '.jointOrientY', channelBox=True)
            cmds.setAttr(i + '.jointOrientZ', channelBox=True)
            cmds.setAttr(i + '.displayLocalAxis', channelBox=True)
            cmds.setAttr(i + '.displayLocalAxis', 1)

    def togglexjnt(self):
        obj = cmds.ls(sl=True)
        for i in obj:
            cmds.setAttr(i + '.jointOrientX', channelBox=True)

    def toggleyjnt(self):
        obj = cmds.ls(sl=True)
        for i in obj:
            cmds.setAttr(i + '.jointOrientY', channelBox=True)

    def togglezjnt(self):
        obj = cmds.ls(sl=True)
        for i in obj:
            cmds.setAttr(i + '.jointOrientY', channelBox=True)

    def toggledla(self):
        obj = cmds.ls(sl=True)
        for i in obj:
            cmds.setAttr(i + '.displayLocalAxis', channelBox=True)
            cmds.setAttr(i + '.displayLocalAxis', 1)
