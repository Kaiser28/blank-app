# 🎈 Blank app template

A simple Streamlit app template for you to modify!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Configure your Qdrant connection by creating a `.streamlit/secrets.toml` file.
   Start from the provided `sample_secrets.toml`:

   ```bash
   cp .streamlit/sample_secrets.toml .streamlit/secrets.toml
   ```

   Edit `secrets.toml` with your `qdrant_api_key` and optional `qdrant_url`.

3. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
