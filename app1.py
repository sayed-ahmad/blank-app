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
    font-size: 90px;
    text-align: center;
    margin-top: 150px;
    letter-spacing: 4px;
}

/* EACH LETTER DIFFERENT COLOR */
.g { color: red; }
.a { color: orange; }
.m { color: yellow; }
.e { color: lime; }
.space { width: 20px; display: inline-block; }
.o { color: cyan; }
.v { color: blue; }
.e2 { color: violet; }
.r { color: pink; }

.text {
    color: white;
    text-align: center;
    font-size: 24px;
    margin-top: 40px;
    font-family: Arial;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="game-over">
    <span class="g">G</span>
    <span class="a">A</span>
    <span class="m">M</span>
    <span class="e">E</span>
    <span class="space"></span>
    <span class="o">O</span>
    <span class="v">V</span>
    <span class="e2">E</span>
    <span class="r">R</span>
</div>

<div class="text">
    🙏🙏🙏🙏 Vielen Dank, Insa! 🙏🙏🙏🙏 <br><br>
    🕹️🕹️🕹️Das ist der Tattoo, den ich gesagt habe, dass ich codieren werde.🕹️🕹️🕹️
</div>

""", unsafe_allow_html=True)
