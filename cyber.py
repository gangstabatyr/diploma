import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image
import time


st.subheader('Analysis of network threat')

pickle_in = open("cyber_LogisticRegression.pkl","rb")
classifier=pickle.load(pickle_in)



def predict_note_authentication(packet_length, num_packets, protocol):
    prediction = classifier.predict([[packet_length, num_packets, protocol]])
    icmp = 1 if protocol == 'ICMP' else 0
    tcp = 1 if protocol == 'TCP' else 0
    udp = 1 if protocol == 'UDP' else 0
    prediction = classifier.predict([[packet_length, num_packets, icmp, tcp, udp]])
    print(prediction)
    return prediction

def main():
    st.title("Analysis of network threat")
    packet_length = st.number_input('how long is length packet', step=0.1, value=0.0)
    num_packets = st.number_input('how many packets you have?', step=0.1, value=0.0)
    protocol = st.radio('Select your packet protocol', ('ICMP', 'TCP', 'UDP'))

    result = ""
    if st.button("Predict"):
        result = int(predict_note_authentication(packet_length, num_packets, protocol))
        if result == 0:
            with st.spinner('Wait for it...'):
                time.sleep(2)
            st.error('You have risk of network threat')
        elif result == 1:
            with st.spinner('Wait for it...'):
                time.sleep(2)
            st.success("You don't have risk of network threat")
        else:
            st.warning("WARNING!!! CODE RED!")

if __name__ == '__main__':
    main()
