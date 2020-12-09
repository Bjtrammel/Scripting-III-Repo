import maya.cmds as cmds

from bs_3670_Toolbox import RNG_Object_Duplication_UI_Class, Num_Seq_Renamer_UI_Class


class ToolboxUI():
    def __init__(self):
        self.my_window = 'bstoolboxuiwindow'

    def createWindow(self):
        self.delete()

        self.my_window = cmds.window(self.my_window,
                                     title='Becky Snells Toolbox UI',
                                     widthHeight=(432, 432),
                                     backgroundColor=[0.019, 0.077, 0.214],
                                     s=True)


        self.basic_column = cmds.columnLayout(parent=self.my_window,
                                              columnAlign = "center",
                                              adjustableColumn=True)

        cmds.text(parent=self.basic_column, label='Choose which tool you would like to use.')

        cmds.button(parent = self.basic_column, label='Rename Object Tool', command= lambda *x: self.call_renamerUI())
        cmds.button(parent=self.basic_column, label='Duplicate Object', command=lambda *x: self.call_objduplicatorUI())

        cmds.showWindow(self.my_window)

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

    def call_renamerUI(self):
        import Num_Seq_Renamer_UI_Class as renamer
        reload(Num_Seq_Renamer_UI_Class)
        renamerUI_inst = renamer.RenamerUI()
        renamerUI_inst.createWindow()

    def call_objduplicatorUI(self):
        import RNG_Object_Duplication_UI_Class as dupobj
        reload(RNG_Object_Duplication_UI_Class)
        dupobjUI_inst = dupobj.RngUI()
        dupobjUI_inst.createWindow()

