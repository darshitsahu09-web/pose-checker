import streamlit as st

st.set_page_config(
    page_title="Pose Value Checker",
    page_icon="⚔️",
    layout="centered"
)

def normalize(text):
    return text.lower().replace(" ", "")

poses = {

    # High Tier
    "authority": {
        "price": "2.5b+-",
        "status": "Rising 📈",
        "swords": ["Diamond Aegis"]
    },

    "laidback": {
        "price": "600m+-",
        "status": "Stable ⚖️",
        "swords": ["Divine Shadow"]
    },

    "soulstep": {
        "price": "160m+-",
        "status": "Stable",
        "swords": ["Soulblade"]
    },

    "gracebound": {
        "price": "300m-",
        "status": "Falling 📉",
        "swords": ["Crystal Dahlia"]
    },

    "stallsword": {
        "price": "200m-220m",
        "status": "Stable",
        "swords": ["Lotus Oblivion"]
    },

    "driftfall": {
        "price": "180m+",
        "status": "Rising",
        "swords": ["Fallen Aphelion"]
    },

    "reckless": {
        "price": "300m+",
        "status": "Rising",
        "swords": ["Colossal Blazehead", "Nutcracker"]
    },

    "overdrive": {
        "price": "140m+-",
        "status": "Stable",
        "swords": ["Inferno Blade"]
    },

    "backlash": {
        "price": "150m+-",
        "status": "Rising",
        "swords": ["Enigma", "Cyber Enigma", "Winter Scythe", "Eclipse X", "Protector"]
    },

    "overrule": {
        "price": "80m+-",
        "status": "Stable",
        "swords": ["Leviathan Judicator"]
    },

    "stillblade": {
        "price": "90m-",
        "status": "Stable",
        "swords": ["Amethyst Oblivion"]
    },

    "resolve": {
        "price": "100m+-",
        "status": "Stable",
        "swords": ["Pink Pearl Sword"]
    },

    "focus": {
        "price": "65m-70m",
        "status": "Stable",
        "swords": ["Dragonheart"]
    },

    "stable": {
        "price": "30m-",
        "status": "Stable",
        "swords": ["Gemblade"]
    },

    "vigor": {
        "price": "40m+-",
        "status": "Stable",
        "swords": ["Divine Slayer"]
    },

    "strikeform": {
        "price": "25m-30m",
        "status": "Stable",
        "swords": ["Tri Heat Scythe"]
    },

    "lastoath": {
        "price": "25m",
        "status": "Stable",
        "swords": ["Elf Enforcer", "Olimpus Sword"]
    },

    "cursed": {
        "price": "20m+-",
        "status": "Stable",
        "swords": ["Cursed Spirit Blade"]
    },

    "backstab": {
        "price": "20m+-",
        "status": "Stable",
        "swords": ["Wrath Blade"]
    },

    "steady": {
        "price": "15m+-",
        "status": "Stable",
        "swords": ["Spirit Scythe"]
    },

    "valor": {
        "price": "15m+-",
        "status": "Stable",
        "swords": ["Darkness"]
    },

    # Wheel Poses

    "primed": {"price": "10m-", "status": "Stable", "swords": ["Wheel"]},
    "gunslinger": {"price": "4m+-", "status": "Stable", "swords": ["Wheel"]},
    "resilient": {"price": "3m+-", "status": "Stable", "swords": ["Wheel"]},
    "razor": {"price": "2m+-", "status": "Stable", "swords": ["Wheel"]},
    "rogue": {"price": "5m+-", "status": "Stable", "swords": ["Wheel"]},
    "phantom": {"price": "2.5m-3m", "status": "Stable", "swords": ["Wheel"]},
    "resolute": {"price": "3m+-", "status": "Stable", "swords": ["Wheel"]},
    "nichi": {"price": "3m+", "status": "Stable", "swords": ["Wheel"]},
    "titan": {"price": "2m+-", "status": "Stable", "swords": ["Wheel"]},
    "battlefan": {"price": "2.5m+-", "status": "Stable", "swords": ["Wheel"]},
    "bow": {"price": "2m+-", "status": "Stable", "swords": ["Wheel"]},
    "triscythe": {"price": "2m+-", "status": "Stable", "swords": ["Wheel"]},

    # Newly Added

    "backdraw": {
        "price": "90m-100m",
        "status": "Stable",
        "swords": ["Soulpiercer"]
    },

    "resonance": {
        "price": "90m-100m",
        "status": "Stable",
        "swords": ["Lumina"]
    },

    "pendrath": {
        "price": "150m-",
        "status": "Stable",
        "swords": ["Cyber Hammer"]
    },

    "devoted": {
        "price": "300m+",
        "status": "Stable",
        "swords": ["Devotion"]
    }

}


st.title("⚔️ Pose Value Checker")
st.markdown("Check **price, status and obtain method** instantly")

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

            with col2:
                st.metric("📊 Status", data["status"])

            st.subheader("🗡️ Obtainable From")

            for sword in data["swords"]:
                st.markdown(f"- **{sword}**")

            found = True
            break

    if not found:
        st.error("Pose not found")
