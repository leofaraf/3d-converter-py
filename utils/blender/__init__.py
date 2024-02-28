import bpy, logging

bpy.ops.wm.read_factory_settings(use_empty=True)

def convert(input_path, input_format, output_path, output_format):
    try:
        match input_format:
            case "obj":
                bpy.ops.import_scene.obj(filepath=input_path, axis_forward="-Z", axis_up="Y")

            case "dae":
                bpy.ops.wm.collada_import(filepath=input_path)

            case "glb":
                bpy.ops.import_scene.gltf(filepath=input_path, filter_glob=".glb")

            case "fbx":
                bpy.ops.import_scene.fbx(filepath=input_path)

            case "ply":
                bpy.ops.wm.ply_import(filepath=input_path, forward_axis="NEGATIVE_Z", up_axis="Y")

            case "stl":
                bpy.ops.import_mesh.stl(filepath=input_path)
        logging.info("Successful importing!")

        try:
            match output_format:
                case "obj":
                    bpy.ops.export_scene.obj(filepath=output_path, axis_forward="-Z", axis_up="Y")

                case "dae":
                    bpy.ops.wm.collada_export(filepath=output_path)

                case "glb":
                    bpy.ops.export_scene.gltf(filepath=output_path, export_format="GLB")

                case "fbx":
                    bpy.ops.export_scene.fbx(filepath=output_path, axis_forward="-Z", axis_up="Y")

                case "ply":
                    bpy.ops.export_mesh.ply(filepath=output_path, axis_forward="-Z", axis_up="Y")

                case "stl":
                    bpy.ops.export_mesh.stl(filepath=output_path)
            logging.info("Successful exporting!")
        except Exception as e:
            logging.error(f"Exporting error: {e}")
    except Exception as e:
        logging.error(f"Importing error: {e}")