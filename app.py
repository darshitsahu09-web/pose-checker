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
        "swords": ["Diamond Aegis"]
    },

     "Laidback": {
        "aliases": ["laidback", "laid"],
        "price": "600m+-",
        "status": "Stable",
        "swords": ["Divine Shadow"]
    },

    "soulstep": {
        "aliases": ["step", "soul"],
        "price": "170m+-",
        "status": "Stable",
        "swords": ["Soulblade"]
    },

    "gracebound": {
        "aliases": ["bound", "grace"],
        "price": "300m-",
        "status": "Stable",
        "swords": ["Crystal Dahlia"]
    },

    "stallsword": {
        "aliases": ["sword", "stall"],
        "price": "200m-220m",
        "status": "Stable",
        "swords": ["Lotus Oblivion"]
    },

    "driftfall": {
        "aliases": ["drift", "drft","fall"],
        "price": "190m+",
        "status": "Rising",
        "swords": ["Fallen Aphelion"]
    },

    "reckless": {
        "aliases": ["less", "reck"],
        "price": "345m+",
        "status": "Rising",
        "swords": ["Colossal Blazehead", "Nutcracker"]
    },

    "overdrive": {
        "aliases": ["over", "drive","od"],
        "price": "140m+-",
        "status": "Stable",
        "swords": ["Inferno Blade"]
    },

    "backlash": {
        "aliases": ["back", "lash","bl"],
        "price": "140m+-",
        "status": "Stable",
        "swords": ["Enigma", "Cyber Enigma", "Winter Scythe", "Eclipse X", "Protector"]
    },

    "overrule": {
        "aliases": ["or", "rule"],
        "price": "80m+-",
        "status": "Stable",
        "swords": ["Leviathan Judicator"]
    },

    "stillblade": {
        "aliases": ["still", "blade"],
        "price": "90m-",
        "status": "Stable",
        "swords": ["Amethyst Oblivion"]
    },

    "resolve": {
        "aliases": ["rslv", "solve"],
        "price": "100m+-",
        "status": "Stable",
        "swords": ["Pink Pearl Sword"]
    },

    "focus": {
        "aliases": ["cus", "fo"],
        "price": "65m-70m",
        "status": "Stable",
        "swords": ["Dragonheart"]
    },

    "stable": {
        "aliases": ["stbl"],
        "price": "30m-",
        "status": "Stable",
        "swords": ["Gemblade"]
    },

    "vigor": {
        "aliases": ["vgr"],
        "price": "40m+-",
        "status": "Stable",
        "swords": ["Divine Slayer"]
    },

    "strikeform": {
        "aliases": ["strike"],
        "price": "25m-30m",
        "status": "Stable",
        "swords": ["Tri Heat Scythe"]
    },

    "lastoath": {
        "aliases": ["oath", "last"],
        "price": "25m",
        "status": "Stable",
        "swords": ["Elf Enforcer", "Olimpus Sword"]
    },

    "cursed": {
        "aliases": ["curse"],
        "price": "20m+-",
        "status": "Stable",
        "swords": ["Cursed Spirit Blade"]
    },

    "backstab": {
        "aliases": ["stab"],
        "price": "20m+-",
        "status": "Stable",
        "swords": ["Wrath Blade"]
    },

    "steady": {
        "aliases": ["stdy"],
        "price": "15m+-",
        "status": "Stable",
        "swords": ["Spirit Scythe"]
    },

    "valor": {
        "aliases": ["lor"],
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
    
    #Pack Poses
    
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
     "crowned": {"price": "500k+-", "status": "Stable", "swords": ["Pose Pack"]},
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
    "swords": ["Pose Pack"]
},
    
    

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
        "price": "100m+-",
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
    "swords": ["Limited Pack"],
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
    "swords": ["Limited Pack"],
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
    "swords": ["Limited Pack"],
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
    "swords": ["Limited Pack"],
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
    "swords": ["Limited Pack"],
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
    "swords": ["Limited Pack"],
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
    "swords": ["Limited Pack"],
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
    "swords": ["Limited Pack"],
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
    "swords": ["Finisher Pack"],
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
    "swords": ["Finisher Pack"],
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
    "swords": ["Finisher Pack"],
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
    "swords": ["Finisher Pack"],
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
    "swords": ["Finisher Pack"],
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
    "swords": ["Finisher Pack"],
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
    "swords": ["Finisher Pack"],
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
        "swords": ["Limited Store"]
    },

    "shadowbooks": {
        "aliases": ["shadow", "shadowbook"],
        "price": "5m+-",
        "status": "Stable",
        "swords": ["Limited Store"]
    },

    "dragonbooks": {
        "aliases": ["dragon", "dragonbook"],
        "price": "1.5m+",
        "status": "Stable",
        "swords": ["Limited Store"]
    },

    "cosmicbooks": {
        "aliases": ["cosmic", "cosmicbook"],
        "price": "3.5m+-",
        "status": "Stable",
        "swords": ["Limited Store"]
    },

    "skybooks": {
        "aliases": ["sky", "skybook"],
        "price": "2m",
        "status": "Stable",
        "swords": ["----"]
    },

    "rosebooks": {
        "aliases": ["rose", "rosebook"],
        "price": "600k",
        "status": "Stable",
        "swords": ["----"]
    }

}


# ---------------- SKINS ---------------- #

skins = {

    "bloodblue": {
        "aliases": ["blood blue", "bloodblue skin", "blue blood"],
        "price": "10m-",
        "status": "Stable",
        "swords": ["Limited Pack"]
    },

    "bloodpink": {
        "aliases": ["blood pink", "bloodpink skin", "pink blood"],
        "price": "10m-",
        "status": "Stable",
        "swords": ["Limited Pack"]
    },

    "radiantwing": {
        "aliases": ["radiant wing", "radiant wings", "radiant"],
        "price": "15m+",
        "status": "Stable",
        "swords": ["Limited Pack"]
    },

    "voidwing": {
        "aliases": ["void wing", "void wings", "void"],
        "price": "15m+",
        "status": "Stable",
        "swords": ["Limited Pack"]
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
        "swords": ["Limited Pack"]
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
        "swords": ["Limited Pack"]
    },

    "crypticvision": {
        "aliases": [
            "cryptic vision",
            "cryptic",
            "vision cryptic"
        ],
        "price": "5m+-",
        "status": "Stable",
        "swords": ["Limited Pack"]
    },

    "player654": {
        "aliases": [
            "player 654",
            "654",
            "player654 skin"
        ],
        "price": "1m+-",
        "status": "Stable",
        "swords": ["Limited Pack"]
    },

    "plagueskin": {
        "aliases": [
            "plague skin",
            "plague",
            "plague skin pack"
        ],
        "price": "1.5m+-",
        "status": "Stable",
        "swords": ["Limited Pack"]
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
        "swords": ["Limited Pack"]
    },

    "marblecloak": {
        "aliases": [
            "marble cloak",
            "marble",
            "marble skin"
        ],
        "price": "120m+",
        "status": "Stable",
        "swords": ["Limited Pack"]
    },

    "royalecloak": {
        "aliases": [
            "royale cloak",
            "royale",
            "royal cloak"
        ],
        "price": "2m+-",
        "status": "Stable",
        "swords": ["Limited Pack"]
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

category = st.selectbox(
    "Select Category",
    ["Poses", "Finishers", "Books","Skins","Explosions"]
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

    if category == "Books":
        search(books)

    if category == "Skins":
        search(skins)

    if category == "Explosions":
        search(explosions)

    
