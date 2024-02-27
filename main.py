from utils import logger
import sys
import logging
import bpy

# --------------------------------------------------------------------
# Enable Plugins
# --------------------------------------------------------------------

logger.configure_logger("true")
bpy.ops.wm.read_factory_settings(use_empty=True)

# --------------------------------------------------------------------
# Initing
# --------------------------------------------------------------------

PROGRAM_NAME, INPUT_PATH, OUTPUT_PATH = sys.argv
INPUT_FORMAT = INPUT_PATH.split(".")[-1]
OUTPUT_FORMAT = OUTPUT_PATH.split(".")[-1]
logging.info(f"Program \"{PROGRAM_NAME}\" started")

# --------------------------------------------------------------------
# Main
# --------------------------------------------------------------------

try:
    match INPUT_FORMAT:
        case "obj":
            bpy.ops.import_scene.obj(filepath=INPUT_PATH, axis_forward="-Z", axis_up="Y")

        case "dae":
            bpy.ops.wm.collada_import(filepath=INPUT_PATH)

        case "glb":
            bpy.ops.import_scene.gltf(filepath=INPUT_PATH, filter_glob=".glb")

        case "fbx":
            bpy.ops.import_scene.fbx(filepath=INPUT_PATH)

        case "ply":
            bpy.ops.wm.ply_import(filepath=INPUT_PATH, forward_axis="NEGATIVE_Z", up_axis="Y")

        case "stl":
            bpy.ops.import_mesh.stl(filepath=INPUT_PATH)
    logging.info("Successful importing!")

    try:
        match OUTPUT_FORMAT:
            case "obj":
                bpy.ops.export_scene.obj(filepath=OUTPUT_PATH, axis_forward="-Z", axis_up="Y")

            case "dae":
                bpy.ops.wm.collada_export(filepath=OUTPUT_PATH)

            case "glb":
                bpy.ops.export_scene.gltf(filepath=OUTPUT_PATH, export_format="GLB")

            case "fbx":
                bpy.ops.export_scene.fbx(filepath=OUTPUT_PATH, axis_forward="-Z", axis_up="Y")

            case "ply":
                bpy.ops.export_mesh.ply(filepath=OUTPUT_PATH, axis_forward="-Z", axis_up="Y")

            case "stl":
                bpy.ops.export_mesh.stl(filepath=OUTPUT_PATH)
        logging.info("Successful exporting!")
    except Exception as e:
        logging.error("Exporting error: {}", e)
except Exception as e:
    logging.error("Importing error: {}", e)

# --------------------------------------------------------------------
# Exiting
# --------------------------------------------------------------------

logging.info("Program stopped")
