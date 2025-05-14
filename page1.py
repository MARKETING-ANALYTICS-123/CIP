import streamlit as st

# Page config
st.set_page_config(
    page_title="Snowtrack Cards ",
    page_icon="❄️",
    layout="centered",
    initial_sidebar_state="collapsed",
    # background_color="#29B5E8"
)

# Custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #29B5E8;
        font-family: 'Segoe UI', sans-serif;
    }

    .main {
        background-color: black;
        padding: 0 !important;
    }

    .card-container {
        display: flex;
        flex-direction: row;
        justify-content: center;
        gap: 2rem;
        margin-top: 4rem;
        flex-wrap: wrap;
    }

    .card-link {
        text-decoration:question; ;
    }

    .card {
        background-color: #29B5E8;
        border-radius: 16px;
        padding: 2rem;
        width: 320px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        text-align: center;
    }

    .card:hover {
        transform: translateY(-6px);
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.12);
        color: #ffffff;
    }

    .card h3 {
        font-size: 1.6rem;
        color: white;
        margin-bottom: 0.8rem;
    }

    .card p {
        font-size: 1rem;
        color: #white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML card layout with clickable links
st.markdown(
    """
    <div class="card-container">
        <a href="Logic" class="card-link">
            <div class="card">
                <h3>🧠 Logic</h3>
                <p>This card can contain backend logic explanation or interactive toggles for logic processing.</p>
            </div>
        </a>
        <a href="Graph" class="card-link">
            <div class="card">
                <h3>📈 Graph</h3>
                <p>This card can host a graph or visualization (like matplotlib, plotly, or Altair charts).</p>
            </div>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
