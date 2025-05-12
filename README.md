
# 🤖 Arghya Robo – Gemini Chatbot Web App

This is a Streamlit-powered chatbot app that integrates with Google's Gemini API to create a conversational assistant. You can change the background color or image, choose emojis, and chat interactively with Gemini 2.0 Flash model.

---

## 🌐 Live Demo

You can deploy this app on [Streamlit Community Cloud](https://streamlit.io/cloud) for free and access it globally.

---

## 📁 Files

- `app2_streamlit_ready.py` – Main Streamlit chatbot script (secure API key handling)
- `requirements.txt` – Python dependencies for deployment

---

## 🚀 How to Deploy on Streamlit Cloud

1. **Upload these files to a GitHub repository**
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and sign in with GitHub
3. Click **“New App”**
4. Choose your repo and select `app2_streamlit_ready.py` as the main file
5. Under **Advanced settings → Secrets**, add the following:
    ```toml
    GOOGLE_API_KEY = "your_gemini_api_key_here"
    ```
6. Click **Deploy**

---

## 📸 Features

- 🌈 Customize background with colors or uploaded images
- 😎 Pick an emoji to represent yourself
- 💬 Chat powered by Gemini 2.0 Flash
- 🎉 Fun emojis and styled message bubbles

---

## 🔐 Important

Don't share your Gemini API key publicly. Use Streamlit [Secrets Management](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management) to keep it secure.

---

Enjoy chatting with your AI Robo assistant! 🤖
