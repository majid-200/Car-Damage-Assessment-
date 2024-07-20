import streamlit as st
import pandas as pd
import pickle
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import os


def app():
    st.header('Cars Damage level classification')
    st.subheader('Powered by YOLOv8')
    st.write('Welcome!')
    model = YOLO('best.pt')

    def load_image(img):
        im = Image.open(img)
        image = np.array(im)
        return image
    
    def file_selector(folder_path='./data'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox('Select a file', filenames)
        return os.path.join(folder_path, selected_filename)

    filename = file_selector()
    st.write('You selected `%s`' % filename)

    # Uploading the File to the Page
    

    if st.button('Run Classification'):
        cmd = f"yolo classify predict model=best.pt source='{filename}'"
        os.system(cmd)

    uploadFile = st.file_uploader(label="Upload image", type=['jpg', 'png'],  accept_multiple_files=True)
    # Checking the Format of the page
    if uploadFile is not None:
        for file in uploadFile:
            # Perform your Manupilations (In my Case applying Filters)
            img = load_image(file)
            st.image(img)
            st.write("Image Uploaded Successfully")
        
    
if __name__ == "__main__":
    app()

