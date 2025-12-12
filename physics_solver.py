import streamlit as st

st.title("Physics Problem Solver")
cols = st.columns(5)

with cols[0]:
  st.image("kinematics.png")
  if st.button("Kinematics"):
    go_to("kinematics")
