import streamlit as st

st.set_page_config(
    page_icon='👋',
    page_title='Home',
    layout='wide'

)


st.title(":blue[Welcome] to the Home page! 👋")
st.subheader('This is an interactive experince, aimed at giving a :blue[demonstration] of our model at work')
st.markdown(
    """
    ### The source of the used Data
    - Check out [Car Damage dataset](https://www.kaggle.com/datasets/prajwalbhamere/car-damage-severity-dataset/data)
"""
)
st.markdown(
    """
### Please choose the :orange[Demonstration Page] in the sidebar to start
"""
)