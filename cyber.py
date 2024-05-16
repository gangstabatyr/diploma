import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image


st.subheader('Analysis of network threat')

pickle_in = open("cyber_LogisticRegression.pkl","rb")
classifier=pickle.load(pickle_in)



def predict_note_authentication(packet_length, num_packets, icmp,
                                tcp, udp):
    prediction = classifier.predict([[packet_length, num_packets, icmp,
                                      tcp, udp]])
    print(prediction)
    return prediction

def main():
    st.title("Analysis of network threat")
    packet_length = st.number_input('how long is length packet', step=0.1, value=0.0)
    num_packets = st.number_input('how many packets you have?', step=0.1, value=0.0)
    icmp = st.radio('does your packet has icmp (0 - no, 1 - yes ', (0, 1))
    tcp = st.radio('does your packet has tcp (0 - no, 1 - yes ', (0, 1))
    udp = st.radio('does your packet has udp (0 - no, 1 - yes ', (0, 1))

    result = ""
    if st.button("Predict"):
        result = int(predict_note_authentication(packet_length, num_packets, icmp,
                                                 tcp, udp))
        if result == 0:
            st.success('You have risk of network threat')
        else:
            st.success('You dont have risk of network threat')

if __name__ == '__main__':
    main()