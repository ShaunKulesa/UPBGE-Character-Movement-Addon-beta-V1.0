#Library
import bpy
import os
bl_info = {
     "name": "Test", 
     "category": "Object", 
     "author": "Shaun Kulesa and Shihab Al-Den", 
     "blender": (2,91,0), 
     "location": "View3D > UI toolbar (n)", 
     "description":"Charcter movement to object selected", "version":(1,2), 
     "wiki_url": "https://github.com/ShaunKulesa/UPBGE0.30.0-Character-Movement-Addon-beta-V1.05",
    "tracker_url": "https://github.com/ShaunKulesa/UPBGE0.30.0-Character-Movement-Addon-beta-V1.0/issues"
     }

#Location
class View3DPanel:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
#IDK
    @classmethod
    def poll(cls, context):
        return (context.object is not None)
class BasicMovementLogicBricks(bpy.types.Operator):
    bl_idname = ".basic_movement_logic_bricks"
    bl_label = "Minimal Operator"
    #Function
    def execute(self, context):
        play = bpy.context.object
        play.name = 'Character'
        
        #Keyboard_Sensors
        bpy.ops.logic.sensor_add(type="KEYBOARD",name='Forward',object=play.name)
        bpy.ops.logic.sensor_add(type="KEYBOARD",name='Backward',object=play.name)
        bpy.ops.logic.sensor_add(type="KEYBOARD",name='Left',object=play.name)
        bpy.ops.logic.sensor_add(type="KEYBOARD",name='Right',object=play.name)
        bpy.ops.logic.sensor_add(type="KEYBOARD",name='Jump',object=play.name)
        
        #Sensor_Keys
        play.game.sensors['Forward'].key = 'W'
        play.game.sensors['Backward'].key = 'S'
        play.game.sensors['Left'].key = 'A'
        play.game.sensors['Right'].key = 'D'
        play.game.sensors['Jump'].key = 'SPACE'
        
        



        #Show_Expanded_False

        
        #Sensor_Collision
        bpy.ops.logic.sensor_add(type="COLLISION",name='Collision',object=play.name)
        
        #Sensor_Property
        play.game.sensors['Collision'].property = ''
        
        #Mouse_Sensor
        bpy.ops.logic.sensor_add(type="MOUSE",name='Look',object=play.name)
        play.game.sensors['Look'].mouse_event = "MOVEMENT"
        
        #And_Controllers
        bpy.ops.logic.controller_add(type="LOGIC_AND", name="F-And", object=play.name)
        bpy.ops.logic.controller_add(type="LOGIC_AND", name="B-And", object=play.name)
        bpy.ops.logic.controller_add(type="LOGIC_AND", name="L-And", object=play.name)
        bpy.ops.logic.controller_add(type="LOGIC_AND", name="R-And", object=play.name)
        bpy.ops.logic.controller_add(type="LOGIC_AND", name="J-And", object=play.name)
        bpy.ops.logic.controller_add(type="LOGIC_AND", name="LO-And", object=play.name)
        
        #Motion_Actuators
        bpy.ops.logic.actuator_add(type="MOTION", name="F-Movement", object=play.name)
        bpy.ops.logic.actuator_add(type="MOTION", name="B-Movement", object=play.name)
        bpy.ops.logic.actuator_add(type="MOTION", name="L-Movement", object=play.name)
        bpy.ops.logic.actuator_add(type="MOTION", name="R-Movement", object=play.name)
        bpy.ops.logic.actuator_add(type="MOTION", name="J-Movement", object=play.name)
        
        #Mouse_Actuator
        bpy.ops.logic.actuator_add(type="MOUSE", name="LO-Look", object=play.name)
        play.game.actuators['LO-Look'].mode = "LOOK"
        play.game.actuators['LO-Look'].use_axis_y = False
        play.game.actuators['LO-Look'].sensitivity_x = 1.6
        
        #Motion_Location
        play.game.actuators['F-Movement'].offset_location = (0, 0.1, 0)
        play.game.actuators['B-Movement'].offset_location = (0, -0.1, 0)
        play.game.actuators['L-Movement'].offset_location = (-0.1, 0, 0)
        play.game.actuators['R-Movement'].offset_location = (0.1, 0, 0)
        
        #Motion_Force
        play.game.actuators['J-Movement'].force = (0, 0, 100)
        
        #Expand_False
        play.game.sensors['Backward'].show_expanded = False
        play.game.sensors['Left'].show_expanded = False
        play.game.sensors['Right'].show_expanded = False
        play.game.sensors['Jump'].show_expanded = False
        play.game.sensors['Collision'].show_expanded = False
        play.game.controllers['F-And'].show_expanded = False
        play.game.controllers['B-And'].show_expanded = False
        play.game.controllers['L-And'].show_expanded = False
        play.game.controllers['R-And'].show_expanded = False
        play.game.controllers['J-And'].show_expanded = False
        play.game.actuators['F-Movement'].show_expanded = False
        play.game.actuators['B-Movement'].show_expanded = False
        play.game.actuators['L-Movement'].show_expanded = False
        play.game.actuators['R-Movement'].show_expanded = False
        play.game.actuators['J-Movement'].show_expanded = False
        play.game.sensors['Look'].show_expanded = False
        play.game.controllers['LO-And'].show_expanded = False
        play.game.actuators['LO-Look'].show_expanded = False
        
        #Sensors_To_Controllers
        play.game.sensors['Forward'].link(play.game.controllers[0])
        play.game.sensors['Backward'].link(play.game.controllers[-5])
        play.game.sensors['Left'].link(play.game.controllers[-4])
        play.game.sensors['Right'].link(play.game.controllers[-3])
        play.game.sensors['Jump'].link(play.game.controllers[-2])
        play.game.sensors['Collision'].link(play.game.controllers[-2])
        play.game.sensors['Look'].link(play.game.controllers[-1])
        
        #Controllers_To_Actuators
        play.game.actuators["F-Movement"].link(play.game.controllers[0])
        play.game.actuators["B-Movement"].link(play.game.controllers[-5])
        play.game.actuators["L-Movement"].link(play.game.controllers[-4])
        play.game.actuators["R-Movement"].link(play.game.controllers[-3])
        play.game.actuators["J-Movement"].link(play.game.controllers[-2])
        play.game.actuators["LO-Look"].link(play.game.controllers[-1])

class BasicMovementPython(bpy.types.Operator):
    bl_idname = ".basic_movement_python"
    bl_label = "Minimal Operator"
    def execute(self, context):
        play = bpy.context.object
        play.name = 'Character'
        
        #Movement_Script
        bpy.ops.text.open(filepath=os.path.join(os.path.dirname(__file__), "Movement_script.py"))
        path = os.path.join(os.path.dirname(__file__), "Movement_script_BGE.txt") #filepath to your file
        file = open(path, 'rt')
        mytext = bpy.data.texts.new('Movement_script_BGE')
        line = file.readline()
        while line:
            mytext.write(line)
            line = file.readline()
        file.close()
        
        #Always_Sensor
        bpy.ops.logic.sensor_add(type="ALWAYS",name='Always',object=play.name)
        play.game.sensors['Always'].use_pulse_true_level = True
        
        #Keyboard_Sensors
        bpy.ops.logic.sensor_add(type="KEYBOARD",name='Forward',object=play.name)
        bpy.ops.logic.sensor_add(type="KEYBOARD",name='Backward',object=play.name)
        bpy.ops.logic.sensor_add(type="KEYBOARD",name='Left',object=play.name)
        bpy.ops.logic.sensor_add(type="KEYBOARD",name='Right',object=play.name)
        bpy.ops.logic.sensor_add(type="KEYBOARD",name='Jump',object=play.name)
        
        #Python_Controller
        bpy.ops.logic.controller_add(type="PYTHON",name='Python',object=play.name)
        play.game.controllers['Python'].text = bpy.data.texts["Movement_script_BGE"]
        
        #Sensor_Collision
        bpy.ops.logic.sensor_add(type="COLLISION",name='Collision',object=play.name)
        
        #Sensor_Property
        play.game.sensors['Collision'].property = ''
        
        #Sensor_Keys
        play.game.sensors['Forward'].key = 'W'
        play.game.sensors['Backward'].key = 'S'
        play.game.sensors['Left'].key = 'A'
        play.game.sensors['Right'].key = 'D'
        play.game.sensors['Jump'].key = 'SPACE'
        
        #Expand_False
        play.game.sensors['Forward'].show_expanded = False
        play.game.sensors['Backward'].show_expanded = False
        play.game.sensors['Left'].show_expanded = False
        play.game.sensors['Right'].show_expanded = False
        play.game.sensors['Jump'].show_expanded = False
        play.game.sensors['Always'].show_expanded = False
        play.game.sensors['Collision'].show_expanded = False
        play.game.controllers['Python'].show_expanded = False
        
        #Sensor_Link_Controller
        play.game.sensors['Always'].link(play.game.controllers[-1])
        play.game.sensors['Forward'].link(play.game.controllers[-1])
        play.game.sensors['Backward'].link(play.game.controllers[-1])
        play.game.sensors['Left'].link(play.game.controllers[-1])
        play.game.sensors['Right'].link(play.game.controllers[-1])
        play.game.sensors['Jump'].link(play.game.controllers[-1])
        play.game.sensors['Collision'].link(play.game.controllers[-1])
        return {'FINISHED'}

class FirstPersonCameraLogicBricks(bpy.types.Operator):
    bl_idname = ".first_person_camera_logic_bricks"
    bl_label = "Minimal Operator"
    def execute(self, context):
        bpy.ops.object.camera_add()
        cam = bpy.context.object
        cam.rotation_euler = (7.84, 0, 0)
        cam.name = 'Camera_First_Person'
        cam.data.lens = (20)
        bpy.context.scene.camera = cam
        
        #Mouse_Sensor
        bpy.ops.logic.sensor_add(type="MOUSE",name='Look',object=cam.name)
        cam.game.sensors['Look'].mouse_event = "MOVEMENT"

        #Mouse_And
        bpy.ops.logic.controller_add(type="LOGIC_AND", name="LO-And", object=cam.name)

        #Mouse_Actuator
        bpy.ops.logic.actuator_add(type="MOUSE", name="LO-Look", object=cam.name)
        cam.game.actuators['LO-Look'].mode = "LOOK"
        cam.game.actuators['LO-Look'].use_axis_x = False
        cam.game.actuators['LO-Look'].sensitivity_y = 1.6

        #Show_Expanded_False
        cam.game.sensors['Look'].show_expanded = False
        cam.game.controllers['LO-And'].show_expanded = False
        cam.game.actuators['LO-Look'].show_expanded = False

        #Link
        cam.game.sensors['Look'].link(cam.game.controllers[0])
        cam.game.actuators["LO-Look"].link(cam.game.controllers[0])
        
        
class PanelOne(View3DPanel, bpy.types.Panel):
    bl_idname = "VIEW3D_PT_test_1"
    bl_label = "Character Movement"
    #All_of_the_stuff 
    def draw(self, context):
        layout = self.layout
        #First_Person_Label
        layout.label(text="Character Movement:")
        row = layout.row()
        row.scale_y = 1.0
        #Basic_Movement_Button_Logic_Bricks
        row.operator(".basic_movement_logic_bricks", text="Basic Movement Logic Bricks")
        row = layout.row()
        row.scale_y = 1.0
        #Basic_Movement_Button_Python
        row.operator(".basic_movement_python", text="Basic Movement Python")
        row = layout.row()
        row.scale_y = 1.0
        #camera
        row.operator(".first_person_camera_logic_bricks", text="Basic Movement Python")
        row = layout.row()
        row.scale_y = 1.0
#Register_Panel
bpy.utils.register_class(PanelOne)

def register():
    bpy.utils.register_class(BasicMovementLogicBricks)
    bpy.utils.register_class(BasicMovementPython)
    bpy.utils.register_class(FirstPersonCameraLogicBricks)


def unregister():
    bpy.utils.unregister_class(BasicMovementLogicBricks)
    bpy.utils.unregister_class(BasicMovementPython)
    bpy.utils.unregister_class(FirstPersonCameraLogicBricks)
    
if __name__ == "__main__":
    register()