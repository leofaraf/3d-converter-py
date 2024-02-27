# 3d-converter-py

high-performance python 3d models convertor

## supported formats to convert:

- obj
- dae
- glb
- fbx
- ply
- stl

## requirements:

- python 3.10
- installed packages from requirements.txt `pip install -r requirements.txt`

## how to use:

- save your model which should be converted to data/
- `python main.py data/*input_filename.input_format* data/output_filename.output_foramt`. example: `python main.py data/example.obj data/example.stl`