import streamlit as st

st.set_page_config(
    page_title="GAME OVER",
    page_icon="🎮",
    layout="centered"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

html, body, [class*="css"] {
    background: black;
    overflow: hidden;
}

.main {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* Animated background */
body::before {
    content: "";
    position: fixed;
    width: 200%;
    height: 200%;
    background:
        radial-gradient(circle, rgba(255,0,0,0.2) 10%, transparent 10%),
        radial-gradient(circle, rgba(0,255,255,0.2) 10%, transparent 10%);
    background-size: 100px 100px;
    animation: moveBg 10s linear infinite;
}

@keyframes moveBg {
    from { transform: translate(0,0); }
    to { transform: translate(-100px,-100px); }
}

.game-over {
    font-family: 'Press Start 2P', cursive;
    font-size: 80px;
    text-align: center;
    margin-top: 150px;

    background: linear-gradient(
        90deg,
        red,
        orange,
        yellow,
        lime,
        cyan,
        blue,
        violet,
        red
    );

    background-size: 400%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation:
         glow 1.5s ease-in-out infinite alternate,
         rainbow 6s linear infinite;
}

@keyframes glow {
    from {
        text-shadow:
            0 0 10px red,
            0 0 20px red,
            0 0 40px red;
    }

    to {
        text-shadow:
            0 0 20px cyan,
            0 0 40px cyan,
            0 0 80px cyan;
    }
}

@keyframes rainbow {
    0% { background-position: 0%; }
    100% { background-position: 400%; }
}

.text {
    color: white;
    text-align: center;
    font-size: 28px;
    margin-top: 40px;
    font-family: Arial;
}

.blink {
    animation: blink 1s infinite;
}

@keyframes blink {
    50% { opacity: 0; }
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="game-over">
    GAME OVER
</div>
<div class="text">
    🙏 Hallo, Insa! 🙏 <br><br>
    🕹️🕹️🕹️Das ist der Tattoo, den ich gesagt habe, dass ich codieren werde.🕹️🕹️🕹️
</div>

""", unsafe_allow_html=True)
