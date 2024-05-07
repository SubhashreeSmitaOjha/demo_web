import streamlit as st
# import pandas as pd

name=st.text_input("Enter your name:")
fname=st.text_input("Enter your Ftaher's name:")
addr=st.text_area("Enter your Address:")
classdata=st.selectbox("Enter your class:",(1,2,3,4,5))
button=st.button("Done")
if button:
    st.markdown(f"""
        Name:{name}
        Father's Name:{fname}
        Address:{addr}
        Class:{classdata}
    """)

# dataset = pd.read_csv("SourceFile.csv")
# st.dataframe(dataset)

# st.title("Welcome to Python Tutorial")
# st.header("Python")
# st.subheader("java")
# st.markdown("I love python")
# st.code("""for i in range(1,5,1)
#                 print("Hello")
#             """)