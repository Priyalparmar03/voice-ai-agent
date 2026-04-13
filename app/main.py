import streamlit as st
import requests

st.title("🎤 Multilingual Voice AI Agent")

audio = st.file_uploader("Upload Audio", type=["wav", "mp3"])

if audio:
    files = {"file": (audio.name, audio, audio.type)}

    try:
        res = requests.post("http://127.0.0.1:8000/process", files=files)

        st.write("STATUS CODE:", res.status_code)   # 👈 ADD THIS

        data = res.json()

        st.write("FULL RESPONSE:", data)   # 👈 ADD THIS

        st.subheader("📝 Transcription")
        st.write(data.get("text"))

        st.subheader("🌐 Language")
        st.write(data.get("language"))

        st.subheader("🧠 Planned Tasks")
        st.json(data.get("tasks"))

        if data.get("confirm"):
            st.warning("⚠️ Confirm execution")

            if st.button("Execute Tasks"):
                res = requests.post("http://127.0.0.1:8000/execute", json=data)
                st.success(res.json().get("output"))

        if "timing" in data:
            st.subheader("⏱ Performance")
            st.write(data["timing"])

    except Exception as e:
        st.error(f"ERROR: {e}")