import skimage.io as io
from skimage import measure
from skimage.color import rgb2gray

import cv2
import numpy as np
import pandas as pd

import pathlib
import argparse


parser = argparse.ArgumentParser(description='Cell size detector')
parser.add_argument('--input', '-i', type=str, default='input', help='input directory')
parser.add_argument('--output', '-o', type=str, default='output', help='output directory')
parser.add_argument('--width', '-w', type=float, default=2.71, help='width of pixel')
parser.add_argument('--height', '-h', type=float, default=2.86, help='height of pixel')

WIDTH_PIXEL = parser.width
HEIGHT_PIXEL = parser.height
AREA_PIXEL = WIDTH_PIXEL * HEIGHT_PIXEL

BASE_DIR = pathlib.Path(parser.input)
IMAGES = BASE_DIR.glob('*.tif')

def main():
    print(f'Start load_img {BASE_DIR.absolute()}')
    imgs = [io.imread(path) for path in IMAGES] #load images
    imgs = [rgb2gray(img) for img in imgs] #convert to grayscale
    result = []
    id_ims = []
    print(f'Start detecting cell size. number of imgs: {len(imgs)}')
    for id_im, img in enumerate(imgs):
        contours = measure.find_contours(img, 0.1)
        areas = []
        wids = []
        heis = []
        id_cells = []
        
        for cell_id, contour in enumerate(contours:
            c = np.expand_dims(contour.astype(np.float32), 1)
            # Convert it to UMat object
            c = cv2.UMat(c)
            area = cv2.contourArea(c)
            wid = contour[:,0].max() - contour[:,0].min()
            hei = contour[:,1].max() - contour[:,1].min()

            areas.append(area)
            wids.append(wid)
            heis.append(hei)
            id_ims.append(id_im)
            id_cells.append(cell_id)

        result.append([id_ims, id_cells, areas, wids, heis])

    result_df = pd.DataFrame()
    result_df['id_im'] = [i[0] for i in result]
    result_df['id_cell'] = [i[1] for i in result]
    result_df['area'] = [i[2] for i in result]
    result_df['wid'] = [i[3] for i in result]
    result_df['hei'] = [i[4] for i in result]

    print(f'Mean cell size: {result_df["area"].mean()}')
    print(f'Sd cell size: {result_df["area"].std()}')
    
    result_df.to_csv(parser.output+'result.csv'., index=False)
    print(f'Done saving result to {parser.output}')

if __name__ == '__main__':
    main()