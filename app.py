import streamlit as st
import pandas as pd
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer

st.set_page_config(
    page_title="Analisis Topik Ulasan Cek Bansos",
    page_icon="📊",
    layout="wide"
)

@st.cache_resource
def load_model():

    embedding_model = SentenceTransformer(
         "LazarusNLP/all-indo-e5-small-v4"
    )

    topic_model = BERTopic.load(
        "models",
        embedding_model=embedding_model
    )

    return topic_model

topic_model = load_model()


def predict_topic(text, topic_model):
    topic, prob = topic_model.transform([text])

    topic_id = int(topic[0])

    topic_words = topic_model.get_topic(topic_id)

    if topic_words:
        keywords = [word for word, _ in topic_words[:10]]
    else:
        keywords = []

    confidence = (
        float(prob[0].max())
        if prob is not None
        else 0.0
    )

    return {
        "text": text,
        "topic_id": topic_id,
        "keywords": keywords,
        "confidence": confidence
    }


st.title("📊 Analisis Topik Ulasan Aplikasi Cek Bansos")

st.markdown("""
Sistem ini menggunakan **BERTopic** untuk mengidentifikasi topik
dari ulasan pengguna aplikasi Cek Bansos.
""")

text = st.text_area(
    "Masukkan Ulasan",
    height=150,
    placeholder="Contoh: Aplikasi sering error saat login dan loading sangat lama..."
)

if st.button("🔍 Prediksi Topik", use_container_width=True):

    if text.strip():

        result = predict_topic(
            text=text,
            topic_model=topic_model
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Topic ID",
                result["topic_id"]
            )

        with col2:
            st.metric(
                "Confidence",
                f"{result['confidence']:.2%}"
            )

        st.subheader("🏷️ Kata Kunci Topik")

        keyword_html = ""

        for word in result["keywords"]:
            keyword_html += f"""
            <span style="
                background-color:#e3f2fd;
                padding:8px;
                border-radius:10px;
                margin-right:5px;
                display:inline-block;
                margin-bottom:5px;
            ">
                {word}
            </span>
            """

        st.markdown(keyword_html, unsafe_allow_html=True)

        st.subheader("📄 Hasil Prediksi")

        df_result = pd.DataFrame([{
            "Text": result["text"],
            "Topic ID": result["topic_id"],
            "Confidence": round(result["confidence"], 4),
            "Keywords": ", ".join(result["keywords"])
        }])

        st.dataframe(
            df_result,
            use_container_width=True
        )

        with st.expander("Lihat Detail"):
            st.json(result)

    else:
        st.warning("Masukkan teks ulasan terlebih dahulu.")