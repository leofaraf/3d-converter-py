from utils import logger, blender
import sys
import logging
import bpy

# --------------------------------------------------------------------
# Enable Plugins
# --------------------------------------------------------------------

logger.configure_logger("true")

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

blender.convert(INPUT_PATH, INPUT_FORMAT, OUTPUT_PATH, OUTPUT_FORMAT)

# --------------------------------------------------------------------
# Exiting
# --------------------------------------------------------------------

logging.info("Program stopped")
