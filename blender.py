import os
from PIL import Image
import argparse

tmp_frame_dir = "./tmp_frames"
frame_name_prefix =  tmp_frame_dir + "/frame-"

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg

def blend_two_frames(i, j):
    ifp = frame_name_prefix + str(i) + ".png"
    jfp = frame_name_prefix + str(j) + ".png"
    background = Image.open(ifp)
    overlay = Image.open(jfp)
    background = background.convert("RGBA")
    overlay = overlay.convert("RGBA")
    new_img = Image.blend(background, overlay, 0.5)
    return new_img

# parses arguments
parser = argparse.ArgumentParser(description='Extracts all frames from a GIF, blends all possible frame pair combinations, and outputs result to specified output directory.')
parser.add_argument('-g', '--gif', 
					dest='gif', 
					help='The path to the GIF', 
					metavar="FILE", 
					type=lambda x: is_valid_file(parser, x), required=True)
parser.add_argument('-o', '--output-dir', 
					dest='output_dir', 
					help='Path to the output directory', 
					type=str, required=True)
args = parser.parse_args()

path_to_gif = args.gif
output_dir = args.output_dir

# clears tmp and output directory
if os.path.exists(tmp_frame_dir) and os.path.isdir(tmp_frame_dir):
    os.system("rm -rf " + tmp_frame_dir)
if os.path.exists(output_dir) and os.path.isdir(output_dir):
    os.system("rm -rf " + output_dir)

# creates necessary directories
os.system("mkdir " + tmp_frame_dir)
os.system("mkdir " + output_dir)

# extracts all frames from the gif to frames/frame-n.png
os.system("convert -coalesce " + path_to_gif + " " + tmp_frame_dir + "/frame.png")
frame_count = len(next(os.walk(tmp_frame_dir))[2])

# blends all pair frames
for i in range(0, frame_count, 1):
    i_dir = output_dir + "/" + str(i)
    os.system("mkdir " + i_dir)
    for j in range(0, frame_count, 1):
        new_img = blend_two_frames(i, j)
        print("Blended frame " + str(i) + " with frame " + str(j))
        new_img.save(i_dir + "/" + str(j), "PNG")

# removes tmp directory
os.system("rm -rf " + tmp_frame_dir)

print("Finished!")
