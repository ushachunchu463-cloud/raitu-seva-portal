import streamlit as st
import base64
import os
import random

# ================= PAGE CONFIG =================
st.set_page_config(page_title="రైతు సేవా పోర్టల్ / किसान सेवा पोर्टल", layout="wide")

# ================= BACKGROUND FUNCTION =================
def set_background(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# ================= STATES & DISTRICTS =================
INDIA = {
    "Telangana": ["Adilabad","Bhadradri Kothagudem","Hyderabad","Jagtial","Jangaon","Jayashankar Bhupalpally",
                  "Jogulamba Gadwal","Kamareddy","Karimnagar","Khammam","Komaram Bheem Asifabad","Mahabubabad",
                  "Mahabubnagar","Mancherial","Medchal–Malkajgiri","Mulugu","Nagarkurnool","Nalgonda","Nirmal",
                  "Nizamabad","Peddapalli","Rangareddy","Sangareddy","Siddipet","Suryapet","Vikarabad",
                  "Wanaparthy","Warangal Urban","Warangal Rural","Yadadri Bhuvanagiri"],
    "Andhra Pradesh": ["Anantapur","Chittoor","East Godavari","Guntur","Krishna","Kurnool","Prakasam","SPS Nellore",
                       "Srikakulam","Visakhapatnam","Vizianagaram","West Godavari","YSR Kadapa"],
}

# ================= RAINFALL DATA =================
rainfall_info_states = {"Telangana":"Medium","Andhra Pradesh":"Medium"}
rainfall_info_districts = {
    "Adilabad":"High","Bhadradri Kothagudem":"High","Hyderabad":"Medium","Jagtial":"Medium","Jangaon":"Medium",
    "Jayashankar Bhupalpally":"High","Jogulamba Gadwal":"Medium","Kamareddy":"Medium","Karimnagar":"Medium",
    "Khammam":"High","Komaram Bheem Asifabad":"High","Mahabubabad":"High","Mahabubnagar":"Medium","Mancherial":"High",
    "Medchal–Malkajgiri":"Medium","Mulugu":"High","Nagarkurnool":"Medium","Nalgonda":"Medium","Nirmal":"Medium",
    "Nizamabad":"Medium","Peddapalli":"Medium","Rangareddy":"Medium","Sangareddy":"Medium","Siddipet":"Medium",
    "Suryapet":"Medium","Vikarabad":"Medium","Wanaparthy":"Medium","Warangal Urban":"Medium","Warangal Rural":"Medium",
    "Yadadri Bhuvanagiri":"Medium",
    "Anantapur":"Low","Chittoor":"Medium","East Godavari":"High","Guntur":"Medium","Krishna":"Medium",
    "Kurnool":"Low","Prakasam":"Low","SPS Nellore":"Medium","Srikakulam":"High","Visakhapatnam":"High",
    "Vizianagaram":"High","West Godavari":"High","YSR Kadapa":"Low"
}

def get_rainfall_state(state):
    return rainfall_info_states.get(state, "Medium")

def get_rainfall_district(district):
    return rainfall_info_districts.get(district, "Medium")

# ================= MULTILINGUAL STATE & DISTRICT MAPPING =================
state_lang = {
    "Telangana": {"English":"Telangana","Telugu":"తెలంగాణ","Hindi":"तेलंगाना"},
    "Andhra Pradesh": {"English":"Andhra Pradesh","Telugu":"ఆంధ్ర ప్రదేశ్","Hindi":"आंध्र प्रदेश"},
}

district_lang = {
    "Telangana": {
        "Adilabad":{"English":"Adilabad","Telugu":"అదిలాబాద్","Hindi":"अदीलाबाद"},
        "Bhadradri Kothagudem":{"English":"Bhadradri Kothagudem","Telugu":"భద్రాద్రి కొత్తగూడెం","Hindi":"भद्राद्री कोठगुडेम"},
        "Hyderabad":{"English":"Hyderabad","Telugu":"హైదరాబాద్","Hindi":"हैदराबाद"},
        "Jagtial":{"English":"Jagtial","Telugu":"జగతియాల్","Hindi":"जगतियाल"},
        "Jangaon":{"English":"Jangaon","Telugu":"జంగాన్","Hindi":"जंगांव"},
        "Jayashankar Bhupalpally":{"English":"Jayashankar Bhupalpally","Telugu":"జయశంకర్ భూపాలపల్లి","Hindi":"जयशंकर भूपालपल्ली"},
        "Jogulamba Gadwal":{"English":"Jogulamba Gadwal","Telugu":"జోగులాంబ గడ్వాల్","Hindi":"जोगुलंबा गड़वाल"},
        "Kamareddy":{"English":"Kamareddy","Telugu":"కామారెడ్డి","Hindi":"कामारेड्डी"},
        "Karimnagar":{"English":"Karimnagar","Telugu":"కరీంనగర్","Hindi":"करीमनगर"},
        "Khammam":{"English":"Khammam","Telugu":"ఖమ్మం","Hindi":"खम्मम"},
        "Komaram Bheem Asifabad":{"English":"Komaram Bheem Asifabad","Telugu":"కొమరం భీం అసిఫాబాద్","Hindi":"कोमारम भीम आसिफाबाद"},
        "Mahabubabad":{"English":"Mahabubabad","Telugu":"మహబూబాబాద్","Hindi":"महबूबाबाद"},
        "Mahabubnagar":{"English":"Mahabubnagar","Telugu":"మహబూబ్ నగర్","Hindi":"महबूबनगर"},
        "Mancherial":{"English":"Mancherial","Telugu":"మంచిర్యాల","Hindi":"मंचेरियल"},
        "Medchal–Malkajgiri":{"English":"Medchal–Malkajgiri","Telugu":"మెడ్చల్–మల్కాజిగిరి","Hindi":"मेडचल–मलकाजिगिरी"},
        "Mulugu":{"English":"Mulugu","Telugu":"ములుగు","Hindi":"मुलुगु"},
        "Nagarkurnool":{"English":"Nagarkurnool","Telugu":"నగర్‌కర్నూల్","Hindi":"नगरकुर्नूल"},
        "Nalgonda":{"English":"Nalgonda","Telugu":"నల్గొండ","Hindi":"नलगोंडा"},
        "Nirmal":{"English":"Nirmal","Telugu":"నిర్మల్","Hindi":"निर्मल"},
        "Nizamabad":{"English":"Nizamabad","Telugu":"నిజామాబాద్","Hindi":"निज़ामाबाद"},
        "Peddapalli":{"English":"Peddapalli","Telugu":"పెద్దాపల్లి","Hindi":"पेड्डापल्ली"},
        "Rangareddy":{"English":"Rangareddy","Telugu":"రంగారెడ్డి","Hindi":"रंगारेड्डी"},
        "Sangareddy":{"English":"Sangareddy","Telugu":"సంగారెడ్డి","Hindi":"संगारेड्डी"},
        "Siddipet":{"English":"Siddipet","Telugu":"సిద్దిపేట్","Hindi":"सिद्धिपेट"},
        "Suryapet":{"English":"Suryapet","Telugu":"సూర్యపేట్","Hindi":"सूर्यापेट"},
        "Vikarabad":{"English":"Vikarabad","Telugu":"వికారాబాద్","Hindi":"विकाराबाद"},
        "Wanaparthy":{"English":"Wanaparthy","Telugu":"వనపర్తి","Hindi":"वानापर्थी"},
        "Warangal Urban":{"English":"Warangal Urban","Telugu":"వారంగల్ అర్బన్","Hindi":"वारंगल अर्बन"},
        "Warangal Rural":{"English":"Warangal Rural","Telugu":"వారంగల్ రూరల్","Hindi":"वारंगल रूरल"},
        "Yadadri Bhuvanagiri":{"English":"Yadadri Bhuvanagiri","Telugu":"యాదాద్రి భువనగిరి","Hindi":"यदाद्री भुवनगिरी"}
    },
    "Andhra Pradesh": {
        "Anantapur":{"English":"Anantapur","Telugu":"అనంతపుర్","Hindi":"अनंतपुर"},
        "Chittoor":{"English":"Chittoor","Telugu":"చిత్తూరు","Hindi":"चित्तूर"},
        "East Godavari":{"English":"East Godavari","Telugu":"ఈస్ట్ గోదావరి","Hindi":"ईस्ट गोदावरी"},
        "Guntur":{"English":"Guntur","Telugu":"గుంటూరు","Hindi":"गुंटूर"},
        "Krishna":{"English":"Krishna","Telugu":"కృష్ణ","Hindi":"कृष्णा"},
        "Kurnool":{"English":"Kurnool","Telugu":"కర్నూల్","Hindi":"कुरनूल"},
        "Prakasam":{"English":"Prakasam","Telugu":"ప్రకాశం","Hindi":"प्रकाशम"},
        "SPS Nellore":{"English":"SPS Nellore","Telugu":"ఎస్‌పీఎస్ నెల్లూరు","Hindi":"एसपीएस नेल्लोर"},
        "Srikakulam":{"English":"Srikakulam","Telugu":"శ్రీకాకుళం","Hindi":"श्रीकाकुलम"},
        "Visakhapatnam":{"English":"Visakhapatnam","Telugu":"విశాఖపట్నం","Hindi":"विशाखापत्तनम"},
        "Vizianagaram":{"English":"Vizianagaram","Telugu":"విజయనగరం","Hindi":"विजयनगरम"},
        "West Godavari":{"English":"West Godavari","Telugu":"వెస్ట్ గోదావరి","Hindi":"वेस्ट गोदावरी"},
        "YSR Kadapa":{"English":"YSR Kadapa","Telugu":"వైఎస్‌ఆర్ కడప","Hindi":"वाईएसआर कडपा"}
    }
}

# ================= SEASONS =================
season_lang = {
    "Rainy":{"English":"Rainy","Telugu":"ఖరీఫ్ (వర్షాకాలం)","Hindi":"मानसून"},
    "Winter":{"English":"Winter","Telugu":"రబీ (శీతాకాలం)","Hindi":"सर्दी"},
    "Summer":{"English":"Summer","Telugu":"జైద్ (వేసవికాలం)","Hindi":"गर्मियों"}
}

# ================= SOIL & CROP DATA =================
soil_classes = ["Black","Cinder","Laterite","Opeat","Yellow"]

soil_crop_mapping = {
    "Black": {
        "Rainy":{"English":["Cotton","Soybean"],"Telugu":["పత్తి","సోయాబీన్"],"Hindi":["कपास","सोयाबीन"]},
        "Winter":{"English":["Wheat","Sunflower"],"Telugu":["గోధుమ","సూర్యకాంతి"],"Hindi":["गेहूँ","सूरजमुखी"]},
        "Summer":{"English":["Sorghum","Maize"],"Telugu":["జొన్న","మక్కజొన్న"],"Hindi":["ज्वार","मक्का"]}},
    "Cinder": {
        "Rainy":{"English":["Maize","Groundnut"],"Telugu":["మక్కజొన్న","వేరుశనగ"],"Hindi":["मक्का","मूँगफली"]},
        "Winter":{"English":["Pulses"],"Telugu":["పప్పులు"],"Hindi":["दालें"]},
        "Summer":{"English":["Millets","Maize"],"Telugu":["జొన్న","మక్కజొన్న"],"Hindi":["मिलेट्स","मक्का"]}},
    "Laterite": {
        "Rainy":{"English":["Rice","Cashew"],"Telugu":["బియ్యం","కాజూ"],"Hindi":["चावल","काजू"]},
        "Winter":{"English":["Wheat"],"Telugu":["గోధుమ"],"Hindi":["गेहूँ"]},
        "Summer":{"English":["Coconut"],"Telugu":["కొబ్బరి"],"Hindi":["नारियल"]}},
    "Opeat": {
        "Rainy":{"English":["Rice","Vegetables"],"Telugu":["బియ్యం","కూరగాయలు"],"Hindi":["चावल","सब्ज़ियाँ"]},
        "Winter":{"English":["Sugarcane"],"Telugu":["చెక్క"],"Hindi":["गन्ना"]},
        "Summer":{"English":["Vegetables"],"Telugu":["కూరగాయలు"],"Hindi":["सब्ज़ियाँ"]}},
    "Yellow": {
        "Rainy":{"English":["Wheat","Barley"],"Telugu":["గోధుమ","జొన్న"],"Hindi":["गेहूँ","जौ"]},
        "Winter":{"English":["Pulses"],"Telugu":["పప్పులు"],"Hindi":["दालें"]},
        "Summer":{"English":["Millets","Maize"],"Telugu":["జొన్న","మిల్లెట్స్"],"Hindi":["मिलेट्स","मक्का"]}}
}

# ================= SESSION STATE =================
if "page" not in st.session_state: st.session_state.page = "login"
if "language" not in st.session_state: st.session_state.language = None

# ================= LOGIN PAGE =================
if st.session_state.page == "login":
    set_background("images/login_bg.jpg")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("<h2 style='color:white;text-align:center;'>Farmer Login / రైతు లాగిన్ / किसान लॉगिन</h2>", unsafe_allow_html=True)
        username = st.text_input("Username / వినియోగదారు పేరు / उपयोगकर्ता नाम")
        password = st.text_input("Password / పాస్‌వర్డ్ / पासवर्ड", type="password")
        if st.button("Login / లాగిన్ / लॉगिन"):
            if username and password:
                st.session_state.page = "language"
            else:
                st.error("Please enter username and password / దయచేసి వినియోగదారు పేరు మరియు పాస్‌వర్డ్ ఎంటర్ చేయండి / कृपया उपयोगकर्ता नाम और पासवर्ड दर्ज करें")

# ================= LANGUAGE SELECTION =================
elif st.session_state.page == "language":
    set_background("images/language_bg.jpg")
    st.markdown("<h2 style='color:white;text-align:center;'>Select Language / భాషను ఎంచుకోండి / भाषा चुनें</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("English"):
            st.session_state.language = "English"
            st.session_state.page = "home"
    with col2:
        if st.button("తెలుగు"):
            st.session_state.language = "Telugu"
            st.session_state.page = "home"
    with col3:
        if st.button("हिन्दी"):
            st.session_state.language = "Hindi"
            st.session_state.page = "home"

# ================= HOME PAGE WITH RIBBON =================
elif st.session_state.page == "home":
    set_background("images/home_bg.jpg")
    lang = st.session_state.language

    st.markdown(f"<h2 style='color:white;text-align:center;'>Raitu Seva Portal / రైతు సేవా పోర్టల్ / किसान सेवा पोर्टल</h2>", unsafe_allow_html=True)

    # Ribbon menu
    menu_options = ["Home", "Crop Ideas", "Crop Diseases", "Contact", "Help"]
    menu_labels = {
        "English": menu_options,
        "Telugu": ["హోమ్","పంట ఐడియాస్","పంట రోగాలు","సంప్రదించండి","సహాయం"],
        "Hindi": ["होम","फसल विचार","फसल रोग","संपर्क","मदद"]
    }

    st.markdown("""
        <style>
        div[data-baseweb="radio"] > div { flex-direction: row; justify-content: space-around; }
        div[data-baseweb="radio"] label {
            background-color: #4CAF50; color: white; padding: 10px 20px; margin: 0 5px; border-radius: 8px; cursor:pointer;
        }
        div[data-baseweb="radio"] label:hover { background-color:#45a049; }
        div[data-baseweb="radio"] input:checked + label { background-color:#FF9800; color:white; }
        </style>
    """, unsafe_allow_html=True)

    selected_tab = st.radio("", menu_labels[lang], index=0, horizontal=True)

    # ---------------- HOME TAB ----------------
    if selected_tab == menu_labels[lang][0]:
        st.markdown(f"<h3 style='color:white;'>{'Welcome to the Portal' if lang=='English' else 'పోర్టల్‌కు స్వాగతం' if lang=='Telugu' else 'पोर्टल में आपका स्वागत है'}</h3>", unsafe_allow_html=True)

    # ---------------- CROP IDEAS TAB ----------------
    elif selected_tab == menu_labels[lang][1]:
        # --- State Selection ---
        state_label = {"English":"Select State","Telugu":"రాష్ట్రం ఎంచుకోండి","Hindi":"राज्य चुनें"}[lang]
        selected_state_en = st.selectbox(
            state_label,
            list(INDIA.keys()),
            format_func=lambda x: state_lang[x][lang]
        )

        # --- District Selection ---
        district_label = {"English":"Select District","Telugu":"జిల్లా ఎంచుకోండి","Hindi":"जिला चुनें"}[lang]
        selected_district_en = st.selectbox(
            district_label,
            INDIA[selected_state_en],
            format_func=lambda x: district_lang[selected_state_en][x][lang]
        )

        # --- Show Rainfall Info ---
        rainfall_state = get_rainfall_state(selected_state_en)
        rainfall_district = get_rainfall_district(selected_district_en)
        color_map = {"Low":"blue", "Medium":"orange", "High":"red"}

        st.info(f"{state_lang[selected_state_en][lang]} - Rainfall: {rainfall_state}")
        st.markdown(f"<h3 style='color:{color_map[rainfall_district]};'>{district_lang[selected_state_en][selected_district_en][lang]} - Rainfall: {rainfall_district}</h3>", unsafe_allow_html=True)

        # --- Season Selection ---
        season_label = {"English":"Select Season","Telugu":"రుతు ఎంచుకోండి","Hindi":"मौसम चुनें"}[lang]
        season_options = ["Rainy","Winter","Summer"]
        selected_season = st.selectbox(season_label, season_options, format_func=lambda x: season_lang[x][lang])

        # --- Soil Upload ---
        soil_label = {"English":"Upload Soil Image","Telugu":"మట్టి చిత్రం అప్లోడ్ చేయండి","Hindi":"मिट्टी की तस्वीर अपलोड करें"}[lang]
        soil_file = st.file_uploader(soil_label, type=["jpg","jpeg","png"])
        
        if soil_file:
            st.image(soil_file, use_column_width=True)
            soil_type = random.choice(soil_classes)
            st.success(f"{'Soil Type' if lang=='English' else 'మట్టి రకం' if lang=='Telugu' else 'मिट्टी प्रकार'}: {soil_type}")

            crops = soil_crop_mapping[soil_type][selected_season][lang]
            crop_label = {"English":"Recommended Crops:","Telugu":"సిఫార్సు చేసిన పంటలు:","Hindi":"अनुशंसित फसलें:"}[lang]
            st.markdown(f"### {crop_label}")
            st.write(", ".join(crops))

    # ---------------- CROP DISEASES TAB ----------------
    elif selected_tab == menu_labels[lang][2]:
        st.info("Crop Diseases tab coming soon...")

    # ---------------- CONTACT TAB ----------------
    elif selected_tab == menu_labels[lang][3]:
        st.info("Contact info coming soon...")

    # ---------------- HELP TAB ----------------
    elif selected_tab == menu_labels[lang][4]:
        st.info("Help content coming soon...")
