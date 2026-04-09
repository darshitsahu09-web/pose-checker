import streamlit as st

def normalize(text):
    return text.lower().replace(" ", "")

poses = {
    "authority": {
        "price": "2.5b+-",
        "demand": "Extremely High",
        "status": "Rising",
        "swords": ["Diamond Aegis"]
    },

    "laidback": {
        "price": "600m+-",
        "demand": "High",
        "status": "Stable",
        "swords": ["Divine Shadow"]
    }
}

st.title("Pose Value Checker")

user_input = st.text_input("Enter Pose Name")

if user_input:
    normalized_input = normalize(user_input)

    for pose in poses:
        if normalize(pose) == normalized_input:
            data = poses[pose]

            st.header(pose.title())
            st.write("Price:", data["price"])
            st.write("Demand:", data["demand"])
            st.write("Status:", data["status"])

            st.write("Swords:")
            for sword in data["swords"]:
                st.write("-", sword)

            break
    else:
        st.write("Pose not found")
