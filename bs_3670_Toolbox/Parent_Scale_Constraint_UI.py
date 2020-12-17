import maya.cmds as cmds

class ParentGroupUI():
    def __init__(self):
        self.my_window = 'bsparsclwindow'

    def createWindow(self):
        self.delete()

        self.my_window = cmds.window(self.my_window,
                                     title='Becky Snells Parent Scale Window',
                                     widthHeight=(432, 432),
                                     backgroundColor=[0.019, 0.077, 0.214],
                                     s=True)


        self.basic_column = cmds.columnLayout(parent=self.my_window,
                                              columnAlign = "center",
                                              adjustableColumn=True)

        self.name_field = cmds.text(parent=self.basic_column, label='Create Parent Group')

        cmds.button(parent = self.basic_column, label='Group Test', command= lambda *x: self.groupconstraint())

        cmds.showWindow(self.my_window)

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

    def groupconstraint(self):
        sl_list = cmds.ls(sl=True)
        sl_num = len(sl_list) /2
        ctrls = sl_list[0:len(sl_list)/2]
        jnts = sl_list[len(sl_list)/2:]
        if len(sl_list) % 2 == 1:
            cmds.error('Please select an even number of objects')
        for r in range(0, sl_num):
            cmds.parentConstraint(ctrls[r], jnts[r])
            cmds.scaleConstraint(ctrls[r], jnts[r])