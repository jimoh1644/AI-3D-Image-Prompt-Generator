import streamlit as st

st.set_page_config(page_title="Pixar-Style AI Prompt Builder", page_icon="🎨", layout="centered")

st.title("🎬 Pixar-Style 3D Cartoon Scene Prompt Builder")
st.write("Generate beautiful Pixar-style prompts for DALL·E, Midjourney, or Leonardo AI with consistent characters and cinematic style.")

# --- Sidebar Configuration ---
st.sidebar.header("🎨 Character Settings")
character = st.sidebar.text_input(
    "Main Character Description:",
    "A cheerful curly-haired little boy with rosy cheeks and big expressive eyes, wearing blue overalls and a striped shirt"
)

style = st.sidebar.selectbox(
    "Art Style:",
    ["Pixar-style 3D animation", "DreamWorks-style", "Disney-style", "Cartoon 3D illustration"]
)

lighting = st.sidebar.text_input(
    "Lighting Description:",
    "soft warm sunlight, cinematic lighting, bright color palette"
)

mood = st.sidebar.text_input(
    "Mood / Atmosphere:",
    "happy, cozy, family-friendly, vibrant"
)

detail_level = st.sidebar.selectbox(
    "Detail Level:",
    ["high detail", "ultra-realistic 3D textures", "cinematic composition", "illustration quality"]
)

# --- Main Scene Input ---
scene = st.text_area(
    "🖼️ Describe your scene or action:",
    placeholder="Example: walking in a sunny park with his mother, surrounded by green trees and birds flying."
)

# --- Generate Prompt ---
if st.button("✨ Generate Pixar-Style Prompt"):
    if scene.strip():
        prompt = f"""
{character}, {scene}, rendered in {style}, with {lighting}.
Maintain consistent character design: same curly-haired boy across all scenes.
Scene atmosphere: {mood}. Rendered with {detail_level}, smooth shading, natural expressions,
soft focus, and cinematic depth of field. Wholesome animated movie tone.
"""
        st.subheader("🎨 Your AI Prompt:")
        st.code(prompt.strip(), language="text")
        st.success("✅ Copy and paste this prompt into DALL·E, Midjourney, or Leonardo AI.")
    else:
        st.warning("Please describe your scene before generating the prompt.")

# --- Footer ---
st.markdown("---")
st.caption("Created by BRAINTECH • Pixar-style AI prompt generator for creative storytelling.")
