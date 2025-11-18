import json
import streamlit as st
from PIL import Image
from streamlit_timeline import timeline

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Joel Trulin",
    page_icon="assets/1000047742.jpg",
    layout="wide",
)


# st.markdown("---")

# ---------- HERO SECTION ----------
col1, col2 = st.columns([1, 3])

with col1:
    image = Image.open("assets/48336.jpg")
    st.image(image, width=180)

with col2:
    st.title("Joel Trulin")
    st.subheader("Machine Learning Engineer | AI Enthusiast | Computer Vision | Gen AI")
    st.write("""
    Passionate about designing intelligent systems and deploying edge device data-driven solutions.  
    I specialize in **Computer Vision, Gen AI** and **Deep Learning** using TensorFlow and PyTorch.
    """)

st.markdown("---")

# ---------- ABOUT ----------
st.header("About Me")
st.write("""
 Results-driven Machine Learning and Computer Vision Engineer over 4+ years of experience in Data
 Exploration, Image Processing, Object Detection, Segmentation, Classification & Regression,
 Anomaly Detection, GAN, VAE, Speech to Text, Multimodel, Statistical modeling, DVC, MLflow.
 Proficient in developing scalable solutions using AWS S3, TensorFlow, PyTorch, OpenCV, Pandas,
 Sklearn and Matplotlib. Proven success in optimizing models for mobile deployment and improving
 production efficiency using TFLite.
""")

st.markdown("---")

# ---------- Career Timeline ----------
st.header("Career Timeline")
with open("Career Timeline/timeline.json") as f:
    timeline_data = json.load(f)
# Render the timeline
timeline(timeline_data)
st.markdown("---")
# ---------- SKILLS ----------
st.header("Technical Skills")

with st.container():
    col1, col2 = st.columns([2, 3.5])
    color = ['red', 'orange', 'yellow', 'blue', 'green', 'violet', 'gray', 'grey', 'primary']
    with col1:
        st.subheader("Tools", divider='rainbow')
        
        col1_1, col1_2 = st.columns([1, 1], border=True)

        with col1_1:
          tool1 = ['Python', 'Numpy', 'Pandas', 'Matplotlib', 'Tensorflow', 'PyTorch', 'Sklearn', 'PIL','OpenCV']
          for t1 in tool1:
            st.badge(t1, color='primary')

        with col1_2:
          tool2 = ['Data Version Control (DVC)', 'MLflow 3', 'ClearML', 'Git/Github', 'AWS', 'AZURE',
                 'GCP', 'Docker', 'Streamlit']
          for t2 in tool2:
            st.badge(t2, color='primary')
    with col2:
        st.subheader("Techniques", divider='rainbow')

        col2_1, col2_2, col2_3 = st.columns([1, 1, 1], border=True)

        with col2_1:
          tool2_1 = ['Data Preprocessing', 'Feature Engineering', 'Cloud computing', 'Cloud storage services',
                   'MLOps', 'Elastic search', 'Prompting', 'Chatbot', 'Algebra']
          for t2_1 in tool2_1:
            st.badge(t2_1, color='primary')

        with col2_2:
          tool3 = ['GAN', 'Image Captioning', 'Neural Style Transfer', 'Face Recognition', 'OCR', 'PCA',
                 'Semantic segmentation', 'Instance segmentation', 'Pose Estimation']
          for t3 in tool3:
            st.badge(t3, color='primary')

        with col2_3:        
          tool4 = ['PEFT', 'Quantization', 'Pruning', 'Knowledge Distillation', 'Hyper-Parameter Tuning',
                 'Graph Neural Networks', 'Transformers', 'Quantum Neural Networks', 'Reinforcement Learning']
          for t4 in tool4:
            st.badge(t4, color='primary')

        
st.markdown("---")

_, middle, _ = st.columns([1.4, 1, 1])

middle.markdown("""
<style>
.icon-button {
    text-decoration: none;
    color: inherit;
    margin-right: 20px;
}
.icon-button svg {
    width: 30px;
    height: 30px;
    transition: transform 0.2s ease-in-out;
}
.icon-button:hover svg {
    transform: scale(1.2);
}
</style>

<div style="display:flex; align-items:center; gap:20px;">

  <!-- GitHub -->
  <a class="icon-button" href="http://github.com/JoelTrulin/Machine-Learning-Joel-Trulin-" target="_blank">
    <svg xmlns="http://www.w3.org/2000/svg" fill="black" viewBox="0 0 24 24">
      <path d="M12 .297a12 12 0 00-3.797 23.4c.6.113.82-.262.82-.582v-2.236
      c-3.338.726-4.042-1.416-4.042-1.416a3.18 3.18 0 00-1.34-1.76c-1.096-.75.084-.734.084-.734
      a2.52 2.52 0 011.844 1.236 2.56 2.56 0 003.504 1 2.59 2.59 0 01.764-1.616
      c-2.666-.3-5.466-1.332-5.466-5.93a4.64 4.64 0 011.236-3.22 4.3 4.3 0 01.116-3.176
      s1-.32 3.3 1.23a11.4 11.4 0 016 0c2.3-1.55 3.3-1.23 3.3-1.23a4.3 4.3 0 01.116 3.176
      4.64 4.64 0 011.236 3.22c0 4.61-2.8 5.63-5.47 5.93a2.88 2.88 0 01.82 2.24v3.32
      c0 .32.22.7.82.58A12 12 0 0012 .297z"/>
    </svg>
  </a>

  <!-- LinkedIn -->
  <a class="icon-button" href="https://linkedin.com/in/joel-trulin-25611018b" target="_blank">
    <svg xmlns="http://www.w3.org/2000/svg" fill="#0A66C2" viewBox="0 0 24 24">
      <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.036-1.852-3.036
      -1.853 0-2.136 1.446-2.136 2.939v5.666H9.351V9h3.414v1.561h.049
      c.477-.9 1.637-1.852 3.371-1.852 3.603 0 4.269 2.372 4.269 5.456v6.287z
      M5.337 7.433a2.062 2.062 0 1 1 0-4.124 2.062 2.062 0 0 1 0 4.124z
      M6.997 20.452H3.676V9h3.321v11.452z"/>
    </svg>
  </a>

  <!-- Email -->
  <a class="icon-button" href="joel98trulin@gmail.com">
    <svg xmlns="http://www.w3.org/2000/svg" fill="#D44638" viewBox="0 0 24 24">
      <path d="M12 12.713l11.985-7.713v13.362c0 .621-.504 1.125-1.125 1.125H1.14
      A1.125 1.125 0 010 18.362V5l12 7.713zM12 1.5l12 7.5H0l12-7.5z"/>
    </svg>
  </a>

  <!-- Mobile -->
  <a class="icon-button" href="+91 8682934366" title="+91 8682934366">
    <svg xmlns="http://www.w3.org/2000/svg" fill="#25D366" viewBox="0 0 24 24">
      <path d="M21.707 16.95l-4.62-1.98a1.004 1.004 0 0 0-1.1.23l-2.19 2.19
      a15.053 15.053 0 0 1-6.59-6.59l2.19-2.19a1.004 1.004 0 0 0 .23-1.1L7.05 2.293
      A1.003 1.003 0 0 0 6.05 1.71C4.44 1.87 3 3.36 3 5c0 8.28 6.72 15 15 15
      1.64 0 3.13-1.44 3.29-3.05a1.004 1.004 0 0 0-.58-.94z"/>
    </svg>
  </a>


</div>
""", unsafe_allow_html=True)

middle.write('')
middle.caption("© 2025 Joel Trulin — Built with ❤️ using Streamlit")
