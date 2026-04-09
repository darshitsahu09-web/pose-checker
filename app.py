import streamlit as st

st.set_page_config(
    page_title="Death Ball Values",
    page_icon="⚔️",
    layout="centered"
)

def normalize(text):
    return text.lower().replace(" ", "")


# ---------------- POSES ---------------- #

poses = {

    # High Tier
    "authority": {
        "price": "2.5b+-",
        "status": "Stable",
        "swords": ["Diamond Aegis"]
    },

    "laidback": {
        "price": "600m+-",
        "status": "Stable",
        "swords": ["Divine Shadow"]
    },

    "soulstep": {
        "price": "160m+-",
        "status": "Stable",
        "swords": ["Soulblade"]
    },

    "gracebound": {
        "price": "300m-",
        "status": "Stable",
        "swords": ["Crystal Dahlia"]
    },

    "stallsword": {
        "price": "200m-220m",
        "status": "Stable",
        "swords": ["Lotus Oblivion"]
    },

    "driftfall": {
        "price": "190m+",
        "status": "Rising",
        "swords": ["Fallen Aphelion"]
    },

    "reckless": {
        "price": "345m+",
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
        "status": "Stable",
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
    "skyrest": {"price": "1m-", "status": "Stable", "swords": ["Pose Pack"]},
    "jitter": {"price": "1m-", "status": "Stable", "swords": ["Pose Pack"]},
    "stand": {"price": "20k+-", "status": "Stable", "swords": ["Pose Pack"]},
    "balance": {"price": "20k+-", "status": "Stable", "swords": ["Pose Pack"]},
    "protector": {"price": "20k+-", "status": "Stable", "swords": ["Pose Pack"]},
    "watchpoint": {"price": "20k+-", "status": "Stable", "swords": ["Pose Pack"]},
    "prepared": {"price": "20k+-", "status": "Stable", "swords": ["Pose Pack"]},
    "headoff": {"price": "200k+-", "status": "Stable", "swords": ["Pose Pack"]},
    "serenity": {"price": "200k+-", "status": "Stable", "swords": ["Pose Pack"]},
    "glory": {"price": "200k+-", "status": "Stable", "swords": ["Pose Pack"]},
    "override": {"price": "200k+-", "status": "Stable", "swords": ["Pose Pack"]},
    "overclock": {"price": "200k+-", "status": "Stable", "swords": ["Pose Pack"]},
    "whirlcut": {"price": "20k+-", "status": "Stable", "swords": ["Pose Pack"]},
     "ready": {"price": "500k+-", "status": "Stable", "swords": ["Pose Pack"]},
     "airsurf": {"price": "500k+-", "status": "Stable", "swords": ["Pose Pack"]},
     "cyclone": {"price": "500k+-", "status": "Stable", "swords": ["Pose Pack"]},
     "I'm fine": {"price": "500k+-", "status": "Stable", "swords": ["Pose Pack"]},
     "crowned": {"price": "500k+-", "status": "Stable", "swords": ["Pose Pack"]},
    
    

    # Newly Added

    "backdraw": {
        "price": "90m-100m",
        "status": "Stable",
        "swords": ["Soulpiercer"]
    },

    "resonance": {
        "price": "80-90m",
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


# ---------------- FINISHERS ---------------- #

finishers = {

    "thousanddeaths": {
        "price": "40m",
        "status": "Stable",
        "swords": ["Limited Pack"]
    },

    "hanabatake": {
        "price": "10m-",
        "status": "Stable",
        "swords": ["Limited Pack"]
    },

    "gamblertoss": {
        "price": "6m+-",
        "status": "Stable",
        "swords": ["Limited Pack"]
    },

    "jinglebarrage": {
        "price": "1m+-",
        "status": "Stable",
        "swords": ["Limited Pack"]
    },

    "soulreaper": {
        "price": "15m+-",
        "status": "Stable",
        "swords": ["Limited Pack"]
    },

    "cupidstrap": {
        "price": "20m+-",
        "status": "Stable",
        "swords": ["Limited Pack"]
    },

    "hairslick": {
        "price": "25m-30m",
        "status": "Stable",
        "swords": ["Limited Pack"]
    },

    "colossaldrill": {
        "price": "10m-15m",
        "status": "Stable",
        "swords": ["Limited Pack"]
    }

}


# ---------------- UI ---------------- #

st.title("⚔️ Death Ball Values")

category = st.selectbox(
    "Select Category",
    ["Poses", "Finishers"]
)

st.divider()

user_input = st.text_input(
    "🔍 Enter Name",
    placeholder="Example: Authority"
)


def search(data):

    normalized_input = normalize(user_input)

    for item in data:

        if normalize(item) == normalized_input:

            info = data[item]

            st.success(f"Found: {item.title()}")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("💰 Price", info["price"])

            with col2:
                st.metric("📊 Status", info["status"])

            st.subheader("🗡️ Obtainable From")

            for sword in info["swords"]:
                st.markdown(f"- **{sword}**")

            return

    st.error("Not Found")


if user_input:

    if category == "Poses":
        search(poses)

    if category == "Finishers":
        search(finishers)
