#He's upside down on purpose

import maya.cmds as cmds

cmds.polySphere(name="big_ball_geo",
                radius=1,
                subdivisionsX=20,
                subdivisionsY=20,
                axis=[0,1,0],
                createUVs=2,
                constructionHistory=1)
cmds.scale( 2.5, 2.5, 2.5, 'big_ball_geo')
cmds.move( 0, 6, 0, 'big_ball_geo' )

cmds.polySphere(name="medium_ball_geo",
                radius=1,
                subdivisionsX=20,
                subdivisionsY=20,
                axis=[0,1,0],
                createUVs=2,
                constructionHistory=1)
cmds.scale( 2, 2, 2, 'medium_ball_geo')
cmds.move( 0, 2.5, 0, 'medium_ball_geo' )

cmds.polySphere(name="small_ball_geo",
                radius=1,
                subdivisionsX=20,
                subdivisionsY=20,
                axis=[0,1,0],
                createUVs=2,
                constructionHistory=1)
cmds.scale( 1.25, 1.25, 1.25, 'small_ball_geo')


cmds.polyCylinder(name="L_Arm_geo",
                  radius=0.2,
                  height=4,
                  subdivisionsX=20,
                  subdivisionsY=1,
                  subdivisionsZ=5,
                  axis=[0,1,0],
                  roundCap=1,
                  createUVs=3,
                  constructionHistory=1)
cmds.move( 0, 1.5, -3.5, 'L_Arm_geo' )
cmds.rotate( 63, 0, 0, 'L_Arm_geo' )

cmds.polyCylinder(name="L_Finger_One_geo",
                  radius=0.15,
                  height=1,
                  subdivisionsX=20,
                  subdivisionsY=1,
                  subdivisionsZ=5,
                  axis=[0,1,0],
                  roundCap=1,
                  createUVs=3,
                  constructionHistory=1)
cmds.move( 0, 0.75, -4, 'L_Finger_One_geo' )
cmds.rotate( 15, 0, 0, 'L_Finger_One_geo' )

cmds.polyCylinder(name="L_Finger_Two_geo",
                  radius=0.1,
                  height=1,
                  subdivisionsX=20,
                  subdivisionsY=1,
                  subdivisionsZ=5,
                  axis=[0,1,0],
                  roundCap=1,
                  createUVs=3,
                  constructionHistory=1)
cmds.move( 0, 2, -4, 'L_Finger_Two_geo' )
cmds.rotate( -55, 0, 0, 'L_Finger_Two_geo' )

cmds.polyCylinder(name="R_Arm_geo",
                  radius=0.2,
                  height=4,
                  subdivisionsX=20,
                  subdivisionsY=1,
                  subdivisionsZ=5,
                  axis=[0,1,0],
                  roundCap=1,
                  createUVs=3,
                  constructionHistory=1)
cmds.move( 0, 1.5, 3.5, 'R_Arm_geo' )
cmds.rotate( -63, 0, 0, 'R_Arm_geo' )

cmds.polyCylinder(name="R_Finger_One_geo",
                  radius=0.15 ,
                  height=1,
                  subdivisionsX=20,
                  subdivisionsY=1,
                  subdivisionsZ=5,
                  axis=[0,1,0],
                  roundCap=1,
                  createUVs=3,
                  constructionHistory=1)
cmds.move( 0, 0.75, 4, 'R_Finger_One_geo' )
cmds.rotate( -15, 0, 0, 'R_Finger_One_geo' )

cmds.polyCylinder(name="R_Finger_Two_geo",
                  radius=0.1,
                  height=1,
                  subdivisionsX=20,
                  subdivisionsY=1,
                  subdivisionsZ=5,
                  axis=[0,1,0],
                  roundCap=1,
                  createUVs=3,
                  constructionHistory=1)
cmds.move( 0, 2, 4, 'R_Finger_Two_geo' )
cmds.rotate( 55, 0, 0, 'R_Finger_Two_geo' )

cmds.polyCylinder(name="topHat_geo",
                  radius=1,
                  height=2,
                  subdivisionsX=20,
                  subdivisionsY=2,
                  subdivisionsZ=1,
                  axis=[0,1,0],
                  roundCap=0,
                  createUVs=3,
                  constructionHistory=1)
cmds.move( 0, -1.5, 0, 'topHat_geo' )
cmds.select( 'topHat_geo.e[20:39]' )
cmds.polyMoveEdge( localTranslateY=0.64 )
cmds.select( 'topHat_geo.f[20:39]' )
cmds.polyExtrudeFacet( keepFacesTogether=1,
                        scaleX=2,
                        scaleZ=2,
                       constructionHistory=1)

cmds.polySphere(name="L_Eye_geo",
                radius=1,
                subdivisionsX=20,
                subdivisionsY=20,
                axis=[0,1,0],
                createUVs=2,
                constructionHistory=1)
cmds.scale( 0.11, 0.3, 0.3, 'L_Eye_geo')
cmds.move( -1.25, 0, -0.32, 'L_Eye_geo' )

cmds.polySphere(name="R_Eye_geo",
                radius=1,
                subdivisionsX=20,
                subdivisionsY=20,
                axis=[0,1,0],
                createUVs=2,
                constructionHistory=1)
cmds.scale( 0.14, 0.3, 0.3, 'R_Eye_geo')
cmds.move( -1.25, 0, 0.32, 'R_Eye_geo' )

cmds.polyCylinder(name="pipe_Stem_geo",
                  radius=0.05,
                  height=2,
                  subdivisionsX=20,
                  subdivisionsY=2,
                  subdivisionsZ=1,
                  axis=[0,1,0],
                  roundCap=0,
                  createUVs=3,
                  constructionHistory=1)
cmds.move( -1.67, 0.59, -0.61, 'pipe_Stem_geo' )
cmds.rotate( -27.8, 0, 90, 'pipe_Stem_geo' )

cmds.polyCylinder(name="pipe_geo",
                  radius=0.25,
                  height=0.5,
                  subdivisionsX=20,
                  subdivisionsY=1,
                  subdivisionsZ=2,
                  axis=[0,1,0],
                  roundCap=0,
                  createUVs=3,
                  constructionHistory=1)
cmds.move( -2.359, 0.432, -1.032, 'pipe_geo' )
cmds.select( 'pipe_geo.f[60:79]' )
cmds.polyExtrudeFacet( keepFacesTogether=1,
                       localTranslateZ=-0.2,
                       constructionHistory=1)

cmds.polyCylinder(name="L_Leg_geo",
                  radius=0.2,
                  height=3,
                  subdivisionsX=20,
                  subdivisionsY=1,
                  subdivisionsZ=5,
                  axis=[0,1,0],
                  roundCap=1,
                  createUVs=3,
                  constructionHistory=1)
cmds.move( 0, 8.745, -2.709, 'L_Leg_geo' )
cmds.rotate( 140.389, 0, 0, 'L_Leg_geo' )

cmds.polyCylinder(name="R_Leg_geo",
                  radius=0.2,
                  height=3,
                  subdivisionsX=20,
                  subdivisionsY=1,
                  subdivisionsZ=5,
                  axis=[0,1,0],
                  roundCap=1,
                  createUVs=3,
                  constructionHistory=1)
cmds.move( 0, 8.745, 2.709, 'R_Leg_geo' )
cmds.rotate( -140.389, 0, 0, 'R_Leg_geo' )

cmds.polyCone(name="nose_geo",
                  radius=1,
                  height=2,
                  subdivisionsX=20,
                  subdivisionsY=1,
                  subdivisionsZ=5,
                  axis=[0,1,0],
                  roundCap=0,
                  createUVs=3,
                  constructionHistory=1)
cmds.move( -1.977, 0.459, 0, 'nose_geo' )
cmds.rotate( 0, 0, 86.499, 'nose_geo' )
cmds.scale( 0.228,  0.928,  0.228,  'nose_geo')