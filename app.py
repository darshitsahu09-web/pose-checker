import streamlit as st

st.set_page_config(
    page_title="Pose Value Checker",
    page_icon="⚔️",
    layout="centered"
)

def normalize(text):
    return text.lower().replace(" ", "")

poses = {
    "authority": {
        "price": "2.5b+-",
        "demand": "Extremely High 🔥",
        "status": "Rising 📈",
        "swords": ["Diamond Aegis"]
    },

    "laidback": {
        "price": "600m+-",
        "demand": "High",
        "status": "Stable ⚖️",
        "swords": ["Divine Shadow"]
    }
}

# Title
st.title("⚔️ Pose Value Checker")
st.markdown("Check pose **price, demand, status, and swords** instantly")

st.divider()

# Input Box
user_input = st.text_input("🔍 Enter Pose Name", placeholder="Example: Authority")

if user_input:
    normalized_input = normalize(user_input)

    found = False

    for pose in poses:
        if normalize(pose) == normalized_input:
            data = poses[pose]

            st.success(f"Found: {pose.title()}")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("💰 Price", data["price"])
                st.metric("📈 Demand", data["demand"])

            with col2:
                st.metric("📊 Status", data["status"])

            st.subheader("🗡️ Obtainable From")

            for sword in data["swords"]:
                st.markdown(f"- **{sword}**")

            found = True
            break

    if not found:
        st.error("Pose not found")
