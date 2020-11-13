import maya.cmds as cmds

# for my reference
# selected = cmds.ls(selection=True)
# obj_seq_num = 0
# for i in selected:
#     aint += 1
#     bint = "b" + str(aint)
#     cmds.rename(i, bint)



def Replacement(my_string):

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
            cmds.error("Don't fat finger the #")


Replacement("L_Leg_###_Geo")