import streamlit as st
import numpy as np
from custom_knn_recommender import knnRecommendation

names = np.load(r"C:\Users\Angel\Downloads\MLHackathon\demo\names.npy", allow_pickle=True)
st.title('Slider Demo')

dataset_name = st.sidebar.selectbox(
    'Select Dataset',
    ('Iris', 'Ecoli', 'Wine')
)

st.write(f"## {dataset_name} Dataset Recommendation")
k = st.sidebar.slider('Number of Datasets', min_value=1, max_value=10, value=3)
weights = st.sidebar.slider('Preferences', min_value=0, max_value=100, value=[33, 67])
pop_weight, char_weight, con_weight = weights[0]-0, weights[1]-weights[0], 100-weights[1]

st.sidebar.write(f"### Recommend Datasets Similar In:")
st.sidebar.write(f"Popularity: {pop_weight}%")
st.sidebar.write(f"Characteristics: {char_weight}%")
st.sidebar.write(f"\n Area/Background: {con_weight}%")

rec = st.sidebar.button(f"Recommend Me {k} Datasets")
if rec:
    ids = knnRecommendation(dataset_name, k=k, weights=[con_weight/100, pop_weight/100, char_weight/100])
    for i in range(len(ids)):
                   st.write(f"{i+1}: {names[ids[i]]}")