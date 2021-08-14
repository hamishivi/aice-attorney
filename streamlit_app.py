import streamlit as st
from aigen import random_gen
import gdown
import os

def gen_and_display():
    if not os.path.exists('smaller_trained_model'):
        os.mkdir('smaller_trained_model')
    if not os.path.exists("smaller_trained_model/config.json"):
        gdown.download(
            "https://drive.google.com/uc?id=1JkPZqaAuoX7eh4IuDQMVYpyu2IciQ-73", "smaller_trained_model/config.json", quiet=False
        )
    if not os.path.exists("smaller_trained_model/pytorch_model.bin"):
        gdown.download(
            "https://drive.google.com/uc?id=1OfAAfPNxorF-_hy7k1fysLBc6JJc7X41", "smaller_trained_model/pytorch_model.bin", quiet=False
        )
    # generate file
    random_gen('thing.mp4')
    st.video('thing.mp4')

st.title('Endl-Ace Attorney')
st.button('Generate!', on_click=gen_and_display)