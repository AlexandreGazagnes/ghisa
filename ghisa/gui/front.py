"""
Streamlit front-end for the Ghisa app.
"""

import streamlit as st

from ghisa.core.ghisa import Ghisa
from ghisa.core.helpers import asciize

# header image
img = "./docs/assets/img/image.png"
st.image(img)  # caption="Thanks to DALL-E for the image ;) "


# title
st.title("Welcome to Ghisa")
