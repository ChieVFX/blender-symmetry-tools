# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "SymmetryTools",
    "author" : "ChieVFX",
    "description" : "",
    "blender" : (2, 80, 0),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy
import bmesh

# class OpCylindricalSidesChange(bpy.types.Operator):
#     bl_idname = "sym.cylindrical_sides_change"
#     bl_label = "Cylindrical Steps Op"
#     def execute(self, context):
        
#         return {'FINISHED'}

#     def modal(self, context, event):
#         if event in ['ESC', 'RIGHTMOUSE']:
#             return {'CANCELLED'}

#         if event in ['ENTER', 'LEFTMOUSE']:
#             return self.execute(context)

#         #insert you code here
#         return {'RUNNING_MODAL'}

#     def invoke(self, context, event):
#         #insert you code here
#         context.window_manager.modal_handler_add(self)
#         return {'RUNNING_MODAL'}

class OpCylindricalSidesChange(bpy.types.Operator):
    bl_idname = "sym.cylindrical_sides_change"
    bl_label = "Cylindrical Steps Op"
    bl_description = "Changes the mesh to be a closed edge loop with screw modifier"
    bl_options = {'REGISTER', 'UNDO'}

    steps : bpy.props.IntProperty(name="Edges", default=3, min=3, soft_max=100)

    def execute(self, context:bpy.types.Context):
        obj:bpy.types.Object = context.active_object
        obj.show_wire = True

        mods:bpy.types.ObjectModifiers = obj.modifiers
        mods.new("Cylindrical Sides", 'SCREW')
        screw:bpy.types.ScrewModifier = obj.modifiers[-1]
        screw.steps = self.steps
        # print(context.)
        return {'FINISHED'}

    # @classmethod
    # def poll(self, context):
    #     return self

    def invoke(self, context:bpy.types.Context, event):
        print("test")
        # self.initialized = False
        # # bpy.ops.ed.undo_push(message=self.bl_label)

        # obj:bpy.types.Object = context.edit_object
        # mesh:bpy.types.Mesh = obj.data

        # #make sure that loop is selected  and not anything else
        # #cache selected loop vertex positions
        # #calculate and cache amount of rings
        # #switch to object mode
        # #create bmesh and fill with edges
        # #add vertices and edges to cap holes
        # #change mesh to edges
        # #add screw with cached num_of_rings

        # #ALTERNATIVE:
        # bpy.ops.mesh.select_mode(type='EDGE')
        # obj.update_from_editmode()
        # #make sure only 1 edge or edge loop is selected
        # selection = [e for e in mesh.edges if e.select]
        # if mesh.total_edge_sel == 0:
        #     self.report('ERROR_INVALID_INPUT', "No active edge found!")
        #     return {'CANCELLED'}
        # else:
        #     active_edge = None
        #     active_vertices = [v for v in mesh.vertices]

        #     for edge in selection:
        #         vertexIndices = edge.vertices
        #         for vertex in mesh.vertices

        # if len_selection == 1:
        #     bpy.ops.mesh.loop_select()
        #     #select  edge loop
        #     pass 
        # elif len_selection > 1:
        #     #make sure edge loop is selected
        #     pass
        # else:
        # #if 1 edge was selected, select an edge loop
        # #calculate and cache amount of rings
        # self.steps = 3
        # #invert selection
        # bpy.ops.mesh.select_all(action='INVERT')
        # #delete selection
        # bpy.ops.mesh.delete(type='EDGE')
        # #add 'screw' modifier with cached amount of rings
        # # bpy.ops.ed.undo_push("HEY")
        # # mods:bpy.types.ObjectModifiers = obj.modifiers
        # # mods.new("Cylindrical Sides", 'SCREW')
        # # bpy.ops.object.modifier_add(type='SCREW')
        # #go to object mode
        # bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

        # # self.execute(context)

        

        # # mesh = context.active_object.data
        # # bm:bmesh.types.BMesh = bmesh.new()
        # # # bm.from_mesh(mesh)
        # # bm.

        return context.window_manager.invoke_props_popup(self, event)

classes = [
    OpCylindricalSidesChange
]

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)