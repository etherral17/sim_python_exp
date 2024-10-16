import streamlit as st
import numpy as np 
import pandas as pd
import os 
import sys

try :
    st.set_page_config(layout = "wide")
    st.title("JAI BHOLENATH EV - AUTOMOBILE")
    # image1 = 'pros.jpg'
    # image2 = 'pik_solo.jpg'
    #st.logo(image1, link=None, icon_image=image1)
    #st.logo(image2, link=None, icon_image=image2)
    st.image(['pros.jpg','pik1.jpg', 'pik3.jpg','pik_solo.jpg'], width=300, caption=['PROS','First image', 'Second image','EV Bike'])
    #st.image('pik3.jpg')
    #st.image('pik1.jpg')
    # st.write("Sample demo")
    st.write("this is a primary motivation for the buyers to know what a dashboard can do ")
    st.write("content can be written and showed here and can be deployed on on-premise or cloud")
    df =  pd.DataFrame([[1,2,3],[6,6,8]])
    st.table(df)

except Exception as e :
    raise e
    print(e)