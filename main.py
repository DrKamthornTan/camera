import streamlit as st
import av
import numpy as np
import streamlit_webrtc as webrtc

st.title("Video Streaming")

# Request camera access
webrtc_ctx = webrtc.webrtc_streamer(
    key="camera",
    video_transformer_factory=webrtc.VideoTransformerBase,
    async_transform=True,
)

# Display the video stream
if webrtc_ctx.video_transformer:
    st.video(webrtc_ctx)
else:
    st.write("Camera not available.")