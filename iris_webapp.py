import streamlit as st
import joblib
import numpy as np
st.set_page_config(page_title="Iris Flower Prediction", page_icon="🌸", layout="centered")
st.title("Iris Flower Prediction 🌸")
st.image("iris.jpg", caption="Iris Flower")
def get_model():
    model = joblib.load("iris.joblib")
    return model
spl=st.text_input("Sepal Length (cm)", "")
spw=st.text_input("Sepal Width (cm)", "")
pel=st.text_input("Petal Length (cm)", "")
pew=st.text_input("Petal Width (cm)", "")
if st.button("Classify"):
    values = np.array([[float(spl), float(spw), float(pel), float(pew)]])
    model = get_model()
    pred = model.predict(values)
    pred=int(pred[0])
    if pred == 0:
        st.success("The flower is classified as: Setosa")
    elif pred == 1:
        st.success("The flower is classified as: Versicolor")
    else:
        st.success("The flower is classified as: Virginica")
