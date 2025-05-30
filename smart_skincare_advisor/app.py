import streamlit as st
from PIL import Image
from skin_analysis import analyze_skin
from recommendations import get_recommendations

st.set_page_config(page_title="Smart Skincare Advisor")

st.title("🧴 Smart Skincare Advisor")
st.write("Upload a face image and get personalized skincare advice!")

uploaded_file = st.file_uploader("Upload your face image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Analyze Skin"):
        concerns = analyze_skin(image)
        st.subheader("Detected Skin Concerns:")
        st.write(concerns)

        st.subheader("Recommended Ingredients & DIY Remedies:")
        for concern in concerns:
            recs = get_recommendations(concern)
            st.markdown(f"**{concern.capitalize()}**")
            st.markdown(f"- **Ingredients:** {', '.join(recs['ingredients'])}")
            st.markdown(f"- **DIY Remedy:** {recs['diy']}")