import streamlit as st
import google.generativeai as genai 
import base64

# ---------------------- API Setup ----------------------
import os
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

# ------------------ Session Initialization ------------------
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "bg_color" not in st.session_state:
    st.session_state.bg_color = "#000000"
if "temp_color" not in st.session_state:
    st.session_state.temp_color = "#000000"
if "bg_image" not in st.session_state:
    st.session_state.bg_image = None
if "user_emoji" not in st.session_state:
    st.session_state.user_emoji = "👤"
if "msg_emoji" not in st.session_state:
    st.session_state.msg_emoji = ""

# --------------------- Page Setup ---------------------
st.set_page_config(page_title="Arghya Robo", layout="centered")
st.title("🤖 Arghya Robo")

# ------------------- Sidebar Settings -------------------
st.sidebar.header("🛠 Settings")

# Background color
st.sidebar.subheader("🎨 Background Color")
st.session_state.temp_color = st.sidebar.color_picker("Choose a color:", st.session_state.bg_color)
if st.sidebar.button("Apply Background Color"):
    st.session_state.bg_color = st.session_state.temp_color
    st.session_state.bg_image = None  # Reset image

# Background image
st.sidebar.subheader("🖼 Upload Background Image")
uploaded_img = st.sidebar.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
if uploaded_img:
    img_data = uploaded_img.read()
    b64_img = base64.b64encode(img_data).decode()
    st.session_state.bg_image = f"data:image/jpeg;base64,{b64_img}"

# Emoji selector
st.sidebar.subheader("😊 Choose your profile emoji")
emoji_options = ["👤", "😎", "👩‍💻", "🧑‍🚀", "🧙‍♂️", "🧠", "👽", "🤓"]
st.session_state.user_emoji = st.sidebar.selectbox("Pick an emoji to represent you:", emoji_options)

# ------------------ Background Styling ------------------
if st.session_state.bg_image:
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{st.session_state.bg_image}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {st.session_state.bg_color};
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# ------------------- Chat History -------------------
with st.container():
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(
                f"<div style='text-align: right; background-color: #000000; padding: 8px; border-radius: 10px; margin: 5px; color: white;'>"
                f"{st.session_state.user_emoji} {msg['content']}</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"<div style='text-align: left; background-color: #D0E6FF; color: #000000; padding: 8px; border-radius: 10px; margin: 5px;'>"
                f"🤖 {msg['content']}</div>",
                unsafe_allow_html=True,
            )

# ------------------- Input Section -------------------
with st.form(key="chat_form", clear_on_submit=True):
    st.markdown(
        """
        <style>
        .chat-row-container {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-top: 10px;
        }
        .chat-row-container .text-box {
            flex: 1;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="chat-row-container">', unsafe_allow_html=True)

    # Text input
    user_input = st.text_input("Type your message:", key="user_input", label_visibility="collapsed")

    # Emoji dropdown (with simulated placeholder)
    emoji_list = ["🎭 Use the emojis", "😂", "👍", "🙏", "🔥", "❤️", "🎉", "🤔"]
    selected = st.selectbox("", emoji_list, key="emoji_select")
    st.session_state.msg_emoji = "" if selected == "🎭 Use the emojis" else selected

    # Send button
    send = st.form_submit_button("Send")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------- Handle Message -------------------
if send and user_input.strip() != "":
    full_input = f"{user_input} {st.session_state.msg_emoji}".strip()
    st.session_state.messages.append({"role": "user", "content": full_input})
    response = st.session_state.chat.send_message(full_input)
    st.session_state.messages.append({"role": "bot", "content": response.text})
    st.rerun()



