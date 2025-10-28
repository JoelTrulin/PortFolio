import streamlit as st

st.set_page_config(
    page_title="Joel Trulin",
    page_icon="assets/1000047742.jpg",
    layout="wide",
)

project_data = [
    {
        "title": "My Byte",
        "desc": "Designed a custom frame picker model with 95% of accuracy that selects the optimal frame via camera.  \n"
                "Compressed the Vision model to 60K from 24M parameter.  \n"
                "Achieved memory reduction by 86.6%, from 1.5 GB to 200 KB in Edge-Device deployment.  \n"
                "Increased inference upto 200 fps which decreased production time by 400%.  \n"
                "Selected frame is further segmented, across the teeth aligner and its adaptivness with respect to the teeth is predicted.",
        "img" : "Projects/byte_seg.jpg",
        "more_detail" : "Projects/Joel Trulin project details.pdf",
        "url" : "https://patient.byte.com/welcome"
    },
    {
        "title": "Systematic Literature Review",
        "desc": "Innovative Artificial Intelligence/Machine Learning Solution for Healthcare in Life Science Content Synthesis.  \n"
                "The MadeAi Platform and AI-Powered Expert Services help life sciences companies with scalable, compliant AI solutions for data synthesis, summarization, content creation, and more.  \n"
                "GenAI platform that seamlessly integrates with systems and supports custom LLMs and models  \n"
                "Achieved 90% Accuracy, 60% Time-save, 1~2secs/Article screened.  \n",
        "img" : "Projects/madeai.png",
        "more_detail" : "Projects/madeai architecture.png",
        "url" : "https://madeai.com/"
    },
    {
        "title": "Cattle Crossing Detection System",
        "desc": "Developed a CNN-based video analysis model using TensorFlow to detect cattle crossing roads in real-time footage.  \n"
                "Deployed in cctv cameras.",
        "img": "Projects/cattle crossing.jpg"
    },
    {
        "title": "Art Creation",
        "desc": "Implemented Neural Style Transfer to blend the artistic style of one image with the content of another using convolutional neural networks. The model optimizes a loss function combining content and style representations extracted from pretrained CNN layers (e.g., VGG19) to generate visually appealing, art-inspired images.",
        "img": "Projects/neural style transfer.png"
    },
    {
        "title": "Video Caption Generator",
        "desc": "Created a transformer-based model that converts short video clips into natural language captions by integrating visual features (CNN/ViT) with temporal encoding (Transformer encoder-decoder).  \n"
                "Tech Stack:  \n"
                "   PyTorch · CLIP / ViT · Transformer encoder-decoder · Tokenizer (BERT or GPT2) · Streamlit for demo U.",
        "img": "Projects/video caption gen.png"
    },
    {
        "title": "Music Mood Visualizer (GenAI Fusion Project)",
        "desc": "Built an AI that listens to a song, detects mood/emotion using audio embeddings, and generates matching AI-art visuals using a diffusion model or style-transfer network.  \n"
                "Tech Stack:  \n"
                "librosa · PyTorch · Diffusion / Stable Diffusion · CLIP embeddings · Streamlit UI",
        "img": "Projects\music mood.png"
    }
]

for project in project_data:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(project["img"], width='stretch')
    with col2:
        st.subheader(project["title"])
        st.write(project["desc"])

        if "url" in project.keys():
            st.page_link(project["url"], label='Visit')
        if "more_detail" in project.keys():
            with st.expander("More Details"):
                if project["more_detail"].split('.')[-1] == "pdf":
                  st.pdf(project["more_detail"])
                elif project["more_detail"].split('.')[-1] == "png":
                    st.image(project["more_detail"])
        
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
