import maya.cmds as cmds
from bs_3670_Toolbox import RNG_Object_Duplication_UI_Class, Num_Seq_Renamer_UI_Class, Freeze_and_Delete_UI, \
    Parent_Scale_Constraint_UI, Parent_Group_UI, Toggle_Local_Axis_UI, Match_Transforms_UI


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
        cmds.button(parent=self.basic_column, label='Duplicate Object', command= lambda *x: self.call_objduplicatorUI())
        cmds.button(parent=self.basic_column, label='Freeze Transforms and Delete History', command= lambda *x: self.call_freezeanddeleteUI())
        cmds.button(parent=self.basic_column, label='Parent Group Object', command= lambda *x: self.call_parentgroupUI())
        cmds.button(parent=self.basic_column, label='Parent Scale Constrain', command= lambda *x: self.call_parentscaleUI())
        cmds.button(parent=self.basic_column, label='Toggle Local Rotation Axis', command= lambda *x: self.call_toggleaxisUI())
        cmds.button(parent=self.basic_column, label='Match Translation', command=lambda *x: self.call_matchtransUI())

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

    def call_freezeanddeleteUI(self):
        import Freeze_and_Delete_UI as fad
        reload(Freeze_and_Delete_UI)
        fadUI_inst = fad.FreezeandDeleteUI()
        fadUI_inst.createWindow()

    def call_parentgroupUI(self):
        import Parent_Group_UI as pg
        reload(Parent_Group_UI)
        pgUI_inst = pg.ParentGroupUI()
        pgUI_inst.createWindow()

    def call_parentscaleUI(self):
        import Parent_Scale_Constraint_UI as psc
        reload(Parent_Scale_Constraint_UI)
        pscUI_inst = psc.ParentScaleUI()
        pscUI_inst.createWindow()

    def call_toggleaxisUI(self):
        import Toggle_Local_Axis_UI as tla
        reload(Toggle_Local_Axis_UI)
        tla_inst = tla.ToggleAxisUI()
        tla_inst.createWindow()

    def call_matchtransUI(self):
        import Match_Transforms_UI as mt
        reload(Match_Transforms_UI)
        mt_inst = mt.MatchTransUI
        mt_inst.createWindow()