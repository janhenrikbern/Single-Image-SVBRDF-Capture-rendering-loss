#!/bin/bash
#Please download the checkpoint before running
input_dir="../data/captured_data/rectified/positive"
jpg_dir="../data/captured_data/cropped/positive"
output_dir="../data/captured_data/results/positive"
checkpoint_dir="./checkpoint/"

# python3 image_converter.py --input_dir $input_dir --output_dir $jpg_dir
python3 material_net.py --input_dir $jpg_dir --mode eval --output_dir $output_dir --checkpoint $checkpoint_dir --imageFormat jpg --scale_size 256 --batch_size 1

input_dir2="../data/captured_data/rectified/negative"
jpg_dir2="../data/captured_data/cropped/negative"
output_dir2="../data/captured_data/results/negative"


# python3 image_converter.py --input_dir $input_dir2 --output_dir $jpg_dir2
python3 material_net.py --input_dir $jpg_dir2 --mode eval --output_dir $output_dir2 --checkpoint $checkpoint_dir --imageFormat jpg --scale_size 256 --batch_size 1