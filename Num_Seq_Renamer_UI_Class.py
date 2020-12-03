import maya.cmds as cmds

class RenamerUI():
    def __init__(self):
        self.my_window = 'bsrenamerwindow'

    def createWindow(self):
        self.delete()

        self.my_window = cmds.window(self.my_window,
                                     title='Becky Snells Basic Window',
                                     widthHeight=(432, 432),
                                     backgroundColor=[0.019, 0.077, 0.214],
                                     s=True)


        self.basic_column = cmds.columnLayout(parent=self.my_window,
                                              columnAlign = "center",
                                              adjustableColumn=True)

        self.name_field = cmds.textField(parent=self.basic_column, placeholderText='Name of New Object...')

        cmds.button(parent = self.basic_column, label='Rename', command= lambda *x: self.renameobj())

        cmds.showWindow(self.my_window)

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

    def renameobj(self):
        my_string = cmds.textField(self.name_field, q=True, text=True)
        selected = cmds.ls(selection=True)

        num_of_cars = my_string.count('#')
        num_of_parts = my_string.partition('#' * num_of_cars)

        if num_of_parts[1]:
            obj_seq_num = 0
            for i in selected:
                obj_seq_num += 1
                obj_seq_str = str(obj_seq_num)
                z_filler_value = obj_seq_str.zfill(num_of_cars)
                cmds.rename(i, num_of_parts[0] + z_filler_value + num_of_parts[2])
            else:
                cmds.error("Please Enter Name in Format: Name_Name_#*_Name")
