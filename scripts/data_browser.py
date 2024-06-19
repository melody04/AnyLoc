# This script is to browse image retrieval dataset, and viz true match or predicted match.

import argparse
import sys
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

matplotlib.use("TkAgg")

def plot_images(image_paths, fig):
    for i in range(len(image_paths)):
        fig.add_subplot(1, len(image_paths), i+1)
        if os.path.exists(image_paths[i]):
            img = cv2.imread(image_paths[i])
            plt.imshow(img)
            plt.axis('off')
        else:
            print('image path not exists', iamge_paths[i])

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

# return query image id
def get_match(ref_img_id):
    return []

def create_window(args):
    input_column = [
        [
            sg.Text("Query Image"),
            sg.In(size=(25,1),enable_events=True, key='-QUERY_IMG_ID-'),
            sg.Button("Enter")
        ],
    ]
    image_viewer_column = [
        [sg.Canvas(key="-CANVAS-")]   
    ]
    layout = [
        [
            sg.Column(input_column),
            sg.Column(image_viewer_column),
        ]
    ]
    window = sg.Window(title="Demo",
        layout=layout,
        location=(0, 0),
        finalize=True,
        element_justification="center",
        font="Helvetica 18")

    fig = plt.figure(figsize=(5, 4), dpi=100)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Enter":
            image_id = values["-QUERY_IMG_ID-"]
            print('image_id', image_id)
            image_paths = [os.path.join(args.reference_image_dir, image_id+'.jpg')]
            print('image_paths', image_paths)
            plot_images(image_paths, fig)
            draw_figure(window["-CANVAS-"].TKCanvas, fig)

            
    window.close()

def main(args):
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--reference_image_dir", type=str, default="../data/baidu_datasets/training_images_undistort/", required=False)
    arg_parser.add_argument("--query_image_dir", type=str, default="../data/baidu_datasets/query_images_undistort/", reuiqred=False)
    # arg_parser.add_argument("--true_labels", type=str, required=True)
    # arg_parser.add_argument("--predicted_labels", type=str, required=True)
    args = arg_parser.parse_args()

    create_window(args)

if __name__ == "__main__":
    main(sys.argv[1:])