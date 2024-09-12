import json
import os
import random
import time
from pathlib import Path

import streamlit as st
from PIL import Image, ImageDraw
from streamlit_shortcuts import add_keyboard_shortcuts, button
from typing import Union, Optional

st.set_page_config(layout="wide")


shortcut2label = {'1': 'Convertible',
 '2': 'Coupe',
 '3': 'Hatchback',
 '4': 'Minivan',
 '5': 'Pickup',
 '6': 'SUV',
 '7': 'Sedan',
 '8': 'Sportscar',
 '9': 'Truck',
 '10': 'Wagon'}

add_keyboard_shortcuts(shortcut2label)

if 'image_files' not in st.session_state:
    img_root = Path('data')
    st.session_state.image_files =  [ p for p in img_root.rglob('*') if any(
        [
            p.suffix.lower() == ".png",
            p.suffix.lower() == ".jpg",
            p.suffix.lower() == ".jpeg",
        ]
    )
    ]

out_dir = Path("artifact")
out_dir.mkdir(exist_ok=True, parents=True)


# Function to save the label and remove the image from the list
def save_label_and_remove_image(filename: Optional[Path], label: str) -> None:
    if not filename:
        return

    dest = out_dir / filename.name
    dest = dest.with_suffix('.json')
    gt = {}    
    
    gt["filename"] = str(filename)
    gt["label"] = label

    dest.write_text(json.dumps(gt, indent=4))
    
    st.session_state.image_files.remove(filename)

    if True: 
        # for debugging. if not set, it immediately showing the next image after 0.001 second  
        st.json(
            gt,
            expanded=2,
        )               
        time.sleep(1)
    

# Streamlit app layout
st.title("Image Labeling Tool")


if st.session_state.image_files:
    image_file =  random.choice(st.session_state.image_files)
    image = Image.open(image_file)
else:
    image_file = None
    image = Image.new("RGB", (300, 300), "red")


if False:
    # you can set it true to use full width
    st.image(image, 
            use_column_width=True
            )    

st.image(image, 
        width=500,
        use_column_width=False
        )


for _, label in shortcut2label.items():
    if st.button(label):
        save_label_and_remove_image(image_file, label)
        st.rerun()

