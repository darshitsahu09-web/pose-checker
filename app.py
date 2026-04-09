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
    },

    "soulstep": {
        "price": "160m+-",
        "demand": "Medium",
        "status": "Stable",
        "swords": ["Soulblade"]
    },

    "gracebound": {
        "price": "300m-",
        "demand": "Medium",
        "status": "Falling 📉",
        "swords": ["Crystal Dahlia"]
    },

    "stallsword": {
        "price": "200m-220m",
        "demand": "Medium",
        "status": "Stable",
        "swords": ["Lotus Oblivion"]
    },

    "driftfall": {
        "price": "180m+",
        "demand": "High",
        "status": "Rising",
        "swords": ["Fallen Aphelion"]
    },

    "reckless": {
        "price": "300m+",
        "demand": "High",
        "status": "Rising",
        "swords": ["Colossal Blazehead", "Nutcracker"]
    },

    "overdrive": {
        "price": "140m+-",
        "demand": "Medium",
        "status": "Stable",
        "swords": ["Inferno Blade"]
    },

    "backlash": {
        "price": "150m+-",
        "demand": "High",
        "status": "Rising",
        "swords": ["Enigma", "Cyber Enigma", "Winter Scythe", "Eclipse X", "Protector"]
    },

    "overrule": {
        "price": "80m+-",
        "demand": "Medium",
        "status": "Stable",
        "swords": ["Leviathan Judicator"]
    },

    "stillblade": {
        "price": "90m-",
        "demand": "Low",
        "status": "Falling",
        "swords": ["Amethyst Oblivion"]
    },

    "resolve": {
        "price": "100m+-",
        "demand": "Medium",
        "status": "Stable",
        "swords": ["Pink Pearl Sword"]
    },

    "focus": {
        "price": "65m-70m",
        "demand": "Medium",
        "status": "Stable",
        "swords": ["Dragonheart"]
    },

    "stable": {
        "price": "30m-",
        "demand": "Low",
        "status": "Stable",
        "swords": ["Gemblade"]
    },

    "vigor": {
        "price": "40m+-",
        "demand": "Medium",
        "status": "Stable",
        "swords": ["Divine Slayer"]
    },

    "strikeform": {
        "price": "25m-30m",
        "demand": "Low",
        "status": "Stable",
        "swords": ["Tri Heat Scythe"]
    },

    "lastoath": {
        "price": "25m",
        "demand": "Low",
        "status": "Stable",
        "swords": ["Elf Enforcer", "Olimpus Sword"]
    },

    "cursed": {
        "price": "20m+-",
        "demand": "Low",
        "status": "Stable",
        "swords": ["Cursed Spirit Blade"]
    },

    "backstab": {
        "price": "20m+-",
        "demand": "Low",
        "status": "Stable",
        "swords": ["Wrath Blade"]
    },

    "steady": {
        "price": "15m+-",
        "demand": "Low",
        "status": "Stable",
        "swords": ["Spirit Scythe"]
    },

    "valor": {
        "price": "15m+-",
        "demand": "Low",
        "status": "Stable",
        "swords": ["Darkness"]
    }
}


st.title("⚔️ Pose Value Checker")
st.markdown("Check **price, demand, status and swords** instantly")

st.divider()

user_input = st.text_input(
    "🔍 Enter Pose Name",
    placeholder="Example: Authority"
)

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
