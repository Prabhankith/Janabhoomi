import streamlit as st
from prompts.prompt_generator import get_daily_prompt
from handlers.db_handler import save_entry, get_entries
from corpus.corpus_logger import log_to_corpus

st.set_page_config(page_title="Janabhoomi", layout="centered")
st.title("📔 జనభూమి - Telugu Public Diary")

prompt = get_daily_prompt()
st.markdown(f"🗒️ **ఈరోజు ప్రేరణ:** *{prompt}*")

entry = st.text_area("మీ భావాలను తెలుగులో రాయండి", height=200)

if entry:
    privacy = st.radio("ప్రైవసీ ఎంపిక:", ["ప్రైవేట్", "పబ్లిక్"])
    if st.button("సేవ్ చేయండి"):
        save_entry(entry, privacy)
        log_to_corpus(entry, privacy)
        st.success("ఎంట్రీ సేవ్ అయ్యింది!")

st.subheader("🔓 పబ్లిక్ డైరీ ఎంట్రీలు")
for item in get_entries(public_only=True):
    st.markdown(f"📝 *{item['text']}*")
