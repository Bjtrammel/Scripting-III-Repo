import maya.cmds as cmds

class MatchTransUI():
    def __init__(self):
        self.my_window = 'bsmtwindow'

    def createWindow(self):
        self.delete()

        self.my_window = cmds.window(self.my_window,
                                     title='Becky Snells Match Transforms Window',
                                     widthHeight=(432, 432),
                                     backgroundColor=[0.019, 0.077, 0.214],
                                     s=True)


        self.basic_column = cmds.columnLayout(parent=self.my_window,
                                              columnAlign = "center",
                                              adjustableColumn=True)

        self.name_field = cmds.text(parent=self.basic_column, label='On Channel Box')

        cmds.button(parent = self.basic_column, label='Match All Translation', command= lambda *x: self.matchall())
        cmds.button(parent = self.basic_column, label='Match Transform', command= lambda *x: self.matchtrans())
        cmds.button(parent=self.basic_column, label='Match Roatation', command=lambda *x: self.matchrot())
        cmds.button(parent=self.basic_column, label='Match Scale', command=lambda *x: self.matchscl())
        cmds.button(parent=self.basic_column, label='Match Pivots', command=lambda *x: self.matchpiv())

        cmds.showWindow(self.my_window)

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)


    def matchall(self):
        cmds.matchTransform()

    def matchtrans(self):
        cmds.matchTransform(position=True)

    def matchrot(self):
        cmds.matchTransform(rotation=True)

    def matchscl(self):
        cmds.matchTransform(scale=True)

    def matchpiv(self):
        cmds.matchTransform(pivots=True)