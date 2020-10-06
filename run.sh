#!/bin/bash
#Please download the checkpoint before running
input_dir="./data/wood/"
jpg_dir="./data/wood_out/jpgs/"
output_dir="./data/wood_out/"
checkpoint_dir="./checkpoint/"

python3 image_converter.py --input_dir $input_dir --output_dir $jpg_dir
python3 material_net.py --input_dir $jpg_dir --mode eval --output_dir $output_dir --checkpoint $checkpoint_dir --imageFormat jpg --scale_size 256 --batch_size 1
