# Gif Frame Pair Blender

```
python3 blender.py -h
usage: blender.py [-h] -g FILE -o OUTPUT_DIR

Extracts all frames from a GIF, blends all possible frame pair combinations, and outputs result to specified output directory.

optional arguments:
  -h, --help            show this help message and exit
  -g FILE, --gif FILE   The path to the GIF
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Path to the output directory
```

### Example

`python3 blender.py -g example.gif -o ./output`
