import streamlit as st

import sea_level_predictor

st.title('Sea Level Predictor')

# Sidebar settings
with st.sidebar:
    st.write("Settings")
    year_range = st.slider("Select Year Range", 1880, 2050, (2000, 2050))
    custom_title = st.text_input("Enter a custom title", "Rise in Sea Level")
    show_best_fit = st.checkbox("Show Best Fit Line", True)
    if st.button('Recalculate'):
        st.rerun()

# Main content
st.write("This application displays the rise in sea level over time.")
fig = sea_level_predictor.draw_plot(year_range[0], year_range[1], custom_title, show_best_fit)
st.pyplot(fig)

