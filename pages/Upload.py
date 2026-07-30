import os
import shutil
import streamlit as st

st.title("📄 Upload Agriculture PDF")

uploaded_file = st.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    save_dir = "data/agriculture"
    os.makedirs(save_dir, exist_ok=True)

    save_path = os.path.join(save_dir, uploaded_file.name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"{uploaded_file.name} uploaded successfully!")

    st.info("Now click the button below to rebuild the knowledge base.")

    if st.button("Create Knowledge Base"):

        shutil.rmtree("database/faiss_index", ignore_errors=True)

        os.system("python -m src.vector_store")

        st.success("Knowledge Base Updated Successfully!")