import streamlit as st

st.set_page_config(
    page_title="Death Ball Values",
    page_icon="⚔️",
    layout="centered"
)



def normalize(text):
    return text.lower().replace(" ", "").replace("'", "")

# ---------------- POSES ---------------- #

poses = {

    # High Tier
    "authority": {
        "aliases": ["author", "auth"],
        "price": "2.5b+-",
        "status": "Stable",
        "swords": ["Diamond Aegis","Trading"]
    },

     "Laidback": {
        "aliases": ["laidback", "laid"],
        "price": "600m+-",
        "status": "Stable",
        "swords": ["Divine Shadow","Trading"]
    },

    "soulstep": {
        "aliases": ["step", "soul"],
        "price": "170m+-",
        "status": "Stable",
        "swords": ["Soulblade","Trading"]
    },

    "gracebound": {
        "aliases": ["bound", "grace"],
        "price": "300m-",
        "status": "Stable",
        "swords": ["Crystal Dahlia","Trading"]
    },

    "stallsword": {
        "aliases": ["sword", "stall"],
        "price": "200m-220m",
        "status": "Stable",
        "swords": ["Lotus Oblivion","Trading"]
    },

    "driftfall": {
        "aliases": ["drift", "drft","fall"],
        "price": "190m+",
        "status": "Rising",
        "swords": ["Fallen Aphelion","Trading"]
    },

    "reckless": {
        "aliases": ["less", "reck"],
        "price": "345m+",
        "status": "Rising",
        "swords": ["Colossal Blazehead", "Nutcracker","Trading"]
    },

    "overdrive": {
        "aliases": ["over", "drive","od"],
        "price": "140m+-",
        "status": "Stable",
        "swords": ["Inferno Blade","Trading"]
    },

    "backlash": {
        "aliases": ["back", "lash","bl"],
        "price": "140m+-",
        "status": "Stable",
        "swords": ["Enigma", "Cyber Enigma", "Winter Scythe", "Eclipse X", "Protector","Trading"]
    },

    "overrule": {
        "aliases": ["or", "rule"],
        "price": "80m+-",
        "status": "Stable",
        "swords": ["Leviathan Judicator","Trading"]
    },

    "stillblade": {
        "aliases": ["still", "blade"],
        "price": "90m-",
        "status": "Stable",
        "swords": ["Amethyst Oblivion","Trading"]
    },

    "resolve": {
        "aliases": ["rslv", "solve"],
        "price": "100m+-",
        "status": "Stable",
        "swords": ["Pink Pearl Sword","Trading"
    },

    "focus": {
        "aliases": ["cus", "fo"],
        "price": "65m-70m",
        "status": "Stable",
        "swords": ["Dragonheart","Trading"]
    },

    "stable": {
        "aliases": ["stbl"],
        "price": "30m-",
        "status": "Stable",
        "swords": ["Gemblade","Trading"]
    },

    "vigor": {
        "aliases": ["vgr"],
        "price": "40m+-",
        "status": "Stable",
        "swords": ["Divine Slayer","Trading"]
    },

    "strikeform": {
        "aliases": ["strike"],
        "price": "25m-30m",
        "status": "Stable",
        "swords": ["Tri Heat Scythe","Trading"]
    },

    "lastoath": {
        "aliases": ["oath", "last"],
        "price": "25m",
        "status": "Stable",
        "swords": ["Elf Enforcer", "Olimpus Sword","Trading"]
    },

    "cursed": {
        "aliases": ["curse"],
        "price": "20m+-",
        "status": "Stable",
        "swords": ["Cursed Spirit Blade","Trading"]
    },

    "backstab": {
        "aliases": ["stab"],
        "price": "20m+-",
        "status": "Stable",
        "swords": ["Wrath Blade","Trading"]
    },

    "steady": {
        "aliases": ["stdy"],
        "price": "15m+-",
        "status": "Stable",
        "swords": ["Spirit Scythe","Trading"]
    },

    "valor": {
        "aliases": ["lor"],
        "price": "15m+-",
        "status": "Stable",
        "swords": ["Darkness","Trading"]
    },

    # Wheel Poses

    "primed": {"price": "10m-", "status": "Stable", "swords": ["Wheel","Trading"]},
    "gunslinger": {"price": "4m+-", "status": "Stable", "swords": ["Wheel","Trading"]},
    "resilient": {"price": "3m+-", "status": "Stable", "swords": ["Wheel","Trading"]},
    "razor": {"price": "2m+-", "status": "Stable", "swords": ["Wheel","Trading"]},
    "rogue": {"price": "5m+-", "status": "Stable", "swords": ["Wheel","Trading"]},
    "phantom": {"price": "2.5m-3m", "status": "Stable", "swords": ["Wheel","Trading"]},
    "resolute": {"price": "3m+-", "status": "Stable", "swords": ["Wheel","Trading"]},
    "nichi": {"price": "3m+", "status": "Stable", "swords": ["Wheel","Trading"]},
    "titan": {"price": "2m+-", "status": "Stable", "swords": ["Wheel","Trading"]},
    "battlefan": {"price": "2.5m+-", "status": "Stable", "swords": ["Wheel","Trading"]},
    "bow": {"price": "2m+-", "status": "Stable", "swords": ["Wheel","Trading"]},
    "triscythe": {"price": "2m+-", "status": "Stable", "swords": ["Wheel","Trading"]},
    
    #Pack Poses
    
    "skyrest": {"price": "1m-", "status": "Stable", "swords": ["Pose Pack","Trading"]},
    "jitter": {"price": "1m-", "status": "Stable", "swords": ["Pose Pack","Trading"]},
    "stand": {"price": "20k+-", "status": "Stable", "swords": ["Pose Pack","Trading"]},
    "balance": {"price": "20k+-", "status": "Stable", "swords": ["Pose Pack","Trading"]},
    "protector": {"price": "20k+-", "status": "Stable", "swords": ["Pose Pack","Trading"]},
    "watchpoint": {"price": "20k+-", "status": "Stable", "swords": ["Pose Pack","Trading"]},
    "prepared": {"price": "20k+-", "status": "Stable", "swords": ["Pose Pack","Trading"]},
    "headoff": {"price": "200k+-", "status": "Stable", "swords": ["Pose Pack","Trading"]},
    "serenity": {"price": "200k+-", "status": "Stable", "swords": ["Pose Pack","Trading"]},
    "glory": {"price": "200k+-", "status": "Stable", "swords": ["Pose Pack","Trading"]},
    "override": {"price": "200k+-", "status": "Stable", "swords": ["Pose Pack","Trading"]},
    "overclock": {"price": "200k+-", "status": "Stable", "swords": ["Pose Pack","Trading"]},
    "whirlcut": {"price": "20k+-", "status": "Stable", "swords": ["Pose Pack","Trading"]},
     "ready": {"price": "500k+-", "status": "Stable", "swords": ["Pose Pack","Trading"]},
     "airsurf": {"price": "500k+-", "status": "Stable", "swords": ["Pose Pack","Trading"]},
     "cyclone": {"price": "500k+-", "status": "Stable", "swords": ["Pose Pack","Trading"]},
     "crowned": {"price": "500k+-", "status": "Stable", "swords": ["Pose Pack","Trading"]},
    "i'mfine": {
    "aliases": [
        "i'm fine",
        "im fine",
        "i am fine",
        "fine pose",
        "fine"
    ],
    "price": "500k+-",
    "status": "Stable",
    "swords": ["Pose Pack","Trading"]
},
    
    

    # Newly Added

    "backdraw": {
        "price": "90m-100m",
        "status": "Stable",
        "swords": ["Soulpiercer","Trading"]
    },

    "resonance": {
        "price": "80-90m",
        "status": "Stable",
        "swords": ["Lumina","Trading"]
    },

    "pendrath": {
        "price": "100m+-",
        "status": "Stable",
        "swords": ["Cyber Hammer","Trading"]
    },

      "devoted": {
        "price": "300m+",
        "status": "Stable",
        "swords": ["Devotion","Trading"]
    },

    "kunai": {
        "price": "3-4m",
        "status": "Stable",
        "swords": ["Wheel","Trading"]
    }
}



# ---------------- FINISHERS ---------------- #

finishers = {

"thousanddeaths": {
    "price": "40m",
    "status": "Stable",
    "swords": ["Limited Pack","Trading"],
    "aliases": [
        "thousand",
        "1000 deaths",
        "1000deaths",
        "td",
        "thousand death"
    ]
},

"hanabatake": {
    "price": "10m-",
    "status": "Stable",
    "swords": ["Limited Pack","Trading"],
    "aliases": [
        "hana",
        "hanab",
        "flower",
        "hanabat"
    ]
},

"gamblertoss": {
    "price": "6m+-",
    "status": "Stable",
    "swords": ["Limited Pack","Trading"],
    "aliases": [
        "gambler",
        "gamble",
        "gt",
        "toss"
    ]
},

"jinglebarrage": {
    "price": "1m+-",
    "status": "Stable",
    "swords": ["Limited Pack","Trading"],
    "aliases": [
        "jingle",
        "jb",
        "bells",
        "jingle barrage"
    ]
},

"soulreaper": {
    "price": "15m+-",
    "status": "Stable",
    "swords": ["Limited Pack","Trading"],
    "aliases": [
        "soul",
        "reaper",
        "sr",
        "soul reap"
    ]
},

"cupidstrap": {
    "price": "20m+-",
    "status": "Stable",
    "swords": ["Limited Pack","Trading"],
    "aliases": [
        "cupid",
        "cupid trap",
        "cupids trap",
        "ct",
        "heart trap"
    ]
},

"hairslick": {
    "price": "25m-30m",
    "status": "Stable",
    "swords": ["Limited Pack","Trading"],
    "aliases": [
        "hair",
        "slick",
        "hs",
        "hairs"
    ]
},

"colossaldrill": {
    "price": "10m-15m",
    "status": "Stable",
    "swords": ["Limited Pack","Trading"],
    "aliases": [
        "colossal",
        "drill",
        "cd",
        "big drill"
    ]
},

"axecutor": {
    "price": "200k",
    "status": "Stable",
    "swords": ["Finisher Pack","Trading"],
    "aliases": [
        "axe",
        "axecution",
        "axec",
        "ax"
    ]
},

"hollowbreaker": {
    "price": "200k",
    "status": "Stable",
    "swords": ["Finisher Pack","Trading"],
    "aliases": [
        "hollow",
        "hollow break",
        "hb",
        "breaker"
    ]
},

"oneshot": {
    "price": "200k",
    "status": "Stable",
    "swords": ["Finisher Pack","Trading"],
    "aliases": [
        "one",
        "1shot",
        "one shot",
        "os"
    ]
},

"flashkill": {
    "price": "200k",
    "status": "Stable",
    "swords": ["Finisher Pack","Trading"],
    "aliases": [
        "flash",
        "flash kill",
        "fk",
        "flashk"
    ]
},

"monarchscall": {
    "price": "500k - 1m",
    "status": "Stable",
    "swords": ["Finisher Pack","Trading"],
    "aliases": [
        "monarch",
        "monarch call",
        "mc",
        "monarchs"
    ]
},

"finaltrick": {
    "price": "500k - 1m",
    "status": "Stable",
    "swords": ["Finisher Pack","Trading"],
    "aliases": [
        "final",
        "trick",
        "ft",
        "final trick"
    ]
},

"flushout": {
    "price": "500k - 1m",
    "status": "Stable",
    "swords": ["Finisher Pack","Trading"],
    "aliases": [
        "flush",
        "flush out",
        "fo",
        "flushout"
    ]
}

}


# ---------------- BOOKS ---------------- #
books = {

    "cyberbooks": {
        "aliases": ["cyber", "cyberbook", "cyber books"],
        "price": "20m",
        "status": "Stable",
        "swords": ["Limited Store","Trading"]
    },

    "shadowbooks": {
        "aliases": ["shadow", "shadowbook"],
        "price": "5m+-",
        "status": "Stable",
        "swords": ["Limited Store","Trading"]
    },

    "dragonbooks": {
        "aliases": ["dragon", "dragonbook"],
        "price": "1.5m+",
        "status": "Stable",
        "swords": ["Limited Store","Trading"]
    },

    "cosmicbooks": {
        "aliases": ["cosmic", "cosmicbook"],
        "price": "3.5m+-",
        "status": "Stable",
        "swords": ["Limited Store","Trading"]
    },

    "skybooks": {
        "aliases": ["sky", "skybook"],
        "price": "2m",
        "status": "Stable",
        "swords": ["----","Trading"]
    },

    "rosebooks": {
        "aliases": ["rose", "rosebook"],
        "price": "600k",
        "status": "Stable",
        "swords": ["----","Trading"]
    }

}


# ---------------- SKINS ---------------- #

skins = {

    "bloodblue": {
        "aliases": ["blood blue", "bloodblue skin", "blue blood"],
        "price": "10m-",
        "status": "Stable",
        "swords": ["Limited Pack","Trading"]
    },

    "bloodpink": {
        "aliases": ["blood pink", "bloodpink skin", "pink blood"],
        "price": "10m-",
        "status": "Stable",
        "swords": ["Limited Pack","Trading"]
    },

    "radiantwing": {
        "aliases": ["radiant wing", "radiant wings", "radiant"],
        "price": "15m+",
        "status": "Stable",
        "swords": ["Limited Pack","Trading"]
    },

    "voidwing": {
        "aliases": ["void wing", "void wings", "void"],
        "price": "15m+",
        "status": "Stable",
        "swords": ["Limited Pack","Trading"]
    },

    "blazingarmour": {
        "aliases": [
            "blazing armour",
            "blazing armor",
            "blazing",
            "blaze armour",
            "blaze armor"
        ],
        "price": "6m+-",
        "status": "Stable",
        "swords": ["Limited Pack","Trading"]
    },

    "flaringarmour": {
        "aliases": [
            "flaring armour",
            "flaring armor",
            "flaring",
            "flare armour",
            "flare armor"
        ],
        "price": "6m+-",
        "status": "Stable",
        "swords": ["Limited Pack","Trading"]
    },

    "crypticvision": {
        "aliases": [
            "cryptic vision",
            "cryptic",
            "vision cryptic"
        ],
        "price": "5m+-",
        "status": "Stable",
        "swords": ["Limited Pack","Trading"]
    },

    "player654": {
        "aliases": [
            "player 654",
            "654",
            "player654 skin"
        ],
        "price": "1m+-",
        "status": "Stable",
        "swords": ["Limited Pack","Trading"]
    },

    "plagueskin": {
        "aliases": [
            "plague skin",
            "plague",
            "plague skin pack"
        ],
        "price": "1.5m+-",
        "status": "Stable",
        "swords": ["Limited Pack","Trading"]
    },

    "visarawings": {
        "aliases": [
            "visara wings",
            "visara wing",
            "visara",
            "visara skin"
        ],
        "price": "2m+-",
        "status": "Stable",
        "swords": ["Limited Pack","Trading"]
    },

    "marblecloak": {
        "aliases": [
            "marble cloak",
            "marble",
            "marble skin"
        ],
        "price": "120m+",
        "status": "Stable",
        "swords": ["Limited Pack","Trading"]
    },

    "royalecloak": {
        "aliases": [
            "royale cloak",
            "royale",
            "royal cloak"
        ],
        "price": "2m+-",
        "status": "Stable",
        "swords": ["Limited Pack","Trading"]
    }

}


# ---------------- EXPLOSIONS ---------------- #

explosions = {


"voltburst": {
    "price": "6m+-",
    "status": "Stable",
    "swords": ["Limited Pack", "Trading"],
    "aliases": [
        "volt",
        "burst",
        "volt burst",
        "vb"
    ]
},

"fallfire": {
    "price": "3m+-",
    "status": "Stable",
    "swords": ["Limited Pack", "Trading"],
    "aliases": [
        "fall",
        "fire fall",
        "fall fire",
        "ff"
    ]
},

"jingleblast": {
    "price": "1m-1.5m",
    "status": "Stable",
    "swords": ["Limited Pack", "Trading"],
    "aliases": [
        "jingle",
        "blast",
        "jingle blast",
        "jb"
    ]
},

"nightpop": {
    "price": "4m-5m",
    "status": "Stable",
    "swords": ["Limited Pack", "Trading"],
    "aliases": [
        "night",
        "pop",
        "night pop",
        "np"
    ]
},

"blackhalo": {
    "price": "3m-4m",
    "status": "Stable",
    "swords": ["Limited Pack", "Trading"],
    "aliases": [
        "black",
        "halo",
        "black halo",
        "bh"
    ]
},

"heartbreak": {
    "price": "4m+-",
    "status": "Stable",
    "swords": ["Limited Pack", "Trading"],
    "aliases": [
        "heart",
        "break",
        "heart break",
        "hb"
    ]
},

"novashock": {
    "price": "1.5m-2m",
    "status": "Stable",
    "swords": ["Limited Pack", "Trading"],
    "aliases": [
        "nova",
        "shock",
        "nova shock",
        "ns"
    ]
},
    "meteorstrike": {
    "price": "50k - 200k",
    "status": "Stable",
    "swords": ["Explosion Pack", "Trading"],
    "aliases": [
        "meteor strike",
        "meteor",
        "ms",
        "meteorstrike explosion"
    ]
},

"abyssburn": {
    "price": "50k - 200k",
    "status": "Stable",
    "swords": ["Explosion Pack", "Trading"],
    "aliases": [
        "abyss burn",
        "abyss",
        "ab",
        "abyssburn explosion"
    ]
},

"dragonsroar": {
    "price": "50k - 200k",
    "status": "Stable",
    "swords": ["Explosion Pack", "Trading"],
    "aliases": [
        "dragon roar",
        "dragons roar",
        "dragon",
        "dr",
        "dragonsroar explosion"
    ]
},

"shadowpunch": {
    "price": "500k",
    "status": "Stable",
    "swords": ["Explosion Pack", "Trading"],
    "aliases": [
        "shadow punch",
        "shadow",
        "sp",
        "shadowpunch explosion"
    ]
},

"rollerdrop": {
    "price": "500k",
    "status": "Stable",
    "swords": ["Explosion Pack", "Trading"],
    "aliases": [
        "roller drop",
        "roller",
        "rd",
        "rollerdrop explosion"
    ]
},

"heavenpiercer": {
    "price": "500k",
    "status": "Stable",
    "swords": ["Explosion Pack", "Trading"],
    "aliases": [
        "haven piercer",
        "heaven",
        "hp",
        "heavenpiercer explosion"
    ]
},

"divinejudgement": {
    "price": "500k",
    "status": "Stable",
    "swords": ["Explosion Pack", "Trading"],
    "aliases": [
        "divine judgement",
        "divine judgment",
        "divine",
        "dj",
        "divinejudgement explosion"
    ]
},

}

# ---------------- UI ---------------- #

st.title("⚔️ Death Ball Values")

st.markdown("""
### 📊 Value List & Trading Guide

Search for:
- ⚔️ Poses  
- 💥 Explosions  
- 🎯 Finishers  
- 📚 Books  
- 🎨 Skins  

Type any name to see value instantly.
""")

st.divider()

category = st.radio(
    "📂 Select Category",
    ["Poses", "Finishers", "Books", "Skins", "Explosions"],
    horizontal=True
)

st.divider()

user_input = st.text_input("🔍 Enter Name")


def search(data):

    normalized_input = normalize(user_input)

    for item in data:

        aliases = data[item].get("aliases", [])

        if normalize(item) == normalized_input or any(
            normalize(alias) == normalized_input for alias in aliases
        ):

            info = data[item]

            st.success(f"Found: {item.title()}")

            st.markdown("---")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("💰 Price", info["price"])

            with col2:
                st.write("")

            # Status Colors
            if info["status"].lower() == "stable":
                st.success(f"📊 Status: {info['status']}")

            elif info["status"].lower() == "rising":
                st.warning(f"📈 Status: {info['status']}")

            elif info["status"].lower() == "dropping":
                st.error(f"📉 Status: {info['status']}")

            st.markdown("### 🗡️ Obtainable From")

            for sword in info["swords"]:
                st.markdown(f"• **{sword}**")

            return

    st.error("Not Found")


if user_input:

    if category == "Poses":
        search(poses)

    if category == "Finishers":
        search(finishers)

    if category == "Books":
        search(books)

    if category == "Skins":
        search(skins)

    if category == "Explosions":
        search(explosions)


st.divider()

st.caption("⚔️ Death Ball Values • Community Value List")
