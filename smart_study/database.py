# ─────────────────────────────────────────────
# database.py  –  Smart Study Pro-Notes
# All static content lives here. Add new notes
# by appending dicts to the lists below.
# Key format:  "{level}__{classId}__{subjectId}"
# ─────────────────────────────────────────────

LEVEL_LABELS = {
    "primary":  "Primary",
    "ordinary": "O-Level",
    "advanced": "A-Level",
}

LEVEL_COLORS = {
    "primary":  "#1565c0",
    "ordinary": "#2e7d32",
    "advanced": "#6a1b9a",
}

CLASSES = {
    "primary": [
        {"id": "std1",   "label": "Darasa la 1",        "icon": "1️⃣"},
        {"id": "std2",   "label": "Darasa la 2",        "icon": "2️⃣"},
        {"id": "std34",  "label": "Darasa la 3 & 4",    "icon": "3️⃣"},
        {"id": "std567", "label": "Darasa la 5, 6 & 7", "icon": "🎯"},
    ],
    "ordinary": [
        {"id": "form1", "label": "Form One",   "icon": "📗"},
        {"id": "form2", "label": "Form Two",   "icon": "📘"},
        {"id": "form3", "label": "Form Three", "icon": "📙"},
        {"id": "form4", "label": "Form Four",  "icon": "🏅"},
    ],
    "advanced": [
        {"id": "form5", "label": "Form Five", "icon": "🔭"},
        {"id": "form6", "label": "Form Six",  "icon": "🎓"},
    ],
}

SUBJECTS = {
    "primary": [
        {"id": "math",    "label": "Hesabu",    "icon": "➕"},
        {"id": "swahili", "label": "Kiswahili", "icon": "📝"},
        {"id": "science", "label": "Sayansi",   "icon": "🔬"},
    ],
    "ordinary": [
        {"id": "math",    "label": "Basic Mathematics", "icon": "📐"},
        {"id": "physics", "label": "Physics",           "icon": "⚡"},
        {"id": "chem",    "label": "Chemistry",         "icon": "🧪"},
        {"id": "bio",     "label": "Biology",           "icon": "🧬"},
    ],
    "advanced": [
        {"id": "admath",  "label": "Advanced Mathematics", "icon": "📐"},
        {"id": "physics", "label": "Physics",              "icon": "⚡"},
        {"id": "chem",    "label": "Chemistry",            "icon": "🧪"},
    ],
}

# ── NOTES DATABASE ──────────────────────────────────────────────────────────
# Each entry:  {"title": str, "body": str}
# Optional:    {"type": "interactive"} | {"body_html": str}
#
# To ADD a new note, just append a dict to the right list.
# To ADD a new subject/class, create a new key below.
# ────────────────────────────────────────────────────────────────────────────

MY_DATABASE: dict[str, list[dict]] = {

    # ── PRIMARY › Std 1 › Hesabu ────────────────────────────────────────────
    "primary__std1__math": [
        {
            "title": "Sura ya 1: Kuhesabu Namba 0 – 10",
            "body": (
                "Tujifunze kuhesabu Namba 0 hadi 10:\n"
                "0   1   2   3   4   5   6   7   8   9   10\n"
                "3   5   7   9   2   0   1   10   4   8   6\n"
                "7   5   2   0   1   3   6   10   8   9   4\n"
                "5   8   7   2   4   3   0   9   10   1   6\n"
                "10   9   8   7   6   5   4   3   2   1   0\n"
                "6   7   8   9   0   5   4   10   3   2   1\n"
                "0   9   8   1   2   3   6   7   4   5   10"
            ),
        },
        {
            "title": "Sura ya 2: Kuhesabu Idadi ya Vitu",
            "body": (
                "☞Karibu tujifunze kuhusu kuhesabu idadi ya vitu.\n"
                "☞Namba ni alama tunayotumia kuwakilisha kiasi au nafasi.\n"
                "☞Hesabu ni mchakato wa kufanya mahesabu kwa kutumia namba.\n\n"
                "✦ Zoezi — Hesabu idadi ya vitu vifuatavyo:\n\n"
                "1. 🐝 🐝 🐝\n   🐝 🐝\n\n"
                "2. 🐓 🐓 🐓\n   🐓 🐓 🐓\n\n"
                "3. 🐆 🐆 🐆 🐆 🐆\n   🐆 🐆 🐆 🐆 🐆\n\n"
                "4. 🐇 🐇\n\n"
                "5. ⚽️ ⚽️ ⚽️ ⚽️\n   ⚽️ ⚽️ ⚽️ ⚽️\n\n"
                "6. 🚌 🚌 🚌\n\n"
                "7. 🛖 🛖 🛖 🛖\n   🛖 🛖 🛖\n\n"
                "8. 🎠 🎠 🎠\n   🎠 🎠 🎠\n   🎠 🎠 🎠\n\n"
                "9. 🛞 🛞\n   🛞\n\n"
                "10. 💻 💻"
            ),
        },
        {
            "title": "Sura ya 3: Kuhesabu Namba 0-10 kwa Maneno",
            "body": (
                "☞Tutajifunza kuhesabu namba kuanzia 0 hadi 10 kwa maneno.\n\n"
                "0 - Sifuri\n1 - Moja\n2 - Mbili\n3 - Tatu\n4 - Nne\n"
                "5 - Tano\n6 - Sita\n7 - Saba\n8 - Nane\n9 - Tisa\n10 - Kumi\n\n"
                "✦ Zoezi:\n➢ Hesabu vidole vya mkono wako wa kulia."
            ),
        },
        {
            "title": "Sura ya 4: Kujumlisha Namba",
            "body": (
                "☞ Kujumlisha ni kuweka vitu pamoja.\n\n"
                "➢ Mfano:\n"
                "1.  1 + 1 = 2\n"
                "2.  2 + 3 = 5\n"
                "3.  3 + 3 = 6\n"
                "4.  2 + 1 = 3\n"
                "5.  2 + 4 = 6\n"
                "6.  3 + 1 = 4\n"
                "7.  0 + 9 = 9\n"
                "8.  5 + 3 = 8\n"
                "9.  6 + 1 = 7\n"
                "10. 8 + 1 = 9\n"
                "11. 6 + 2 = 8\n"
                "12. 7 + 3 = 10\n"
                "13. 4 + 5 = 9\n"
                "14. 5 + 5 = 10"
            ),
        },
        {
            "title": "Sura ya 5: Kutoa Namba",
            "body": (
                "☞ Kutoa ni kutenganisha vitu vilivyo pamoja.\n"
                "➢ Namba kubwa ndiyo inaweza kutoa namba ndogo.\n\n"
                "➢ Mfano:\n"
                "1.  2 - 1 = 1\n"
                "2.  3 - 1 = 2\n"
                "3.  4 - 2 = 2\n"
                "4.  5 - 3 = 2\n"
                "5.  5 - 4 = 1\n"
                "6.  7 - 5 = 2\n"
                "7.  8 - 4 = 4\n"
                "8.  9 - 5 = 4\n"
                "9.  10 - 5 = 5\n"
                "10. 5 - 5 = 0\n\n"
                "Kumbuka: Namba ndogo kutoa namba kubwa haiwezekani.\n"
                "Mfano: 7 - 9 = Haiwezekani"
            ),
        },
        {
            "title": "Sura ya 6: Kuhesabu Namba kwa Kuangalia (Interactive)",
            "type": "interactive",
            "body": "",   # rendered by frontend widget
        },
    ],

    # ── PRIMARY › Std 1 › Kiswahili ─────────────────────────────────────────
    "primary__std1__swahili": [
        {
            "title": "Sura ya 1: Kusoma Irabu",
            "body": (
                "Kusoma Irabu za msingi:\n\n"
                "a   e   i   o   u\n\n"
                "Kuunganisha Irabu:\n"
                "a + u = au\n"
                "u + a = ua\n"
                "o + a = oa\n"
                "i + o = io\n\n"
                "Kusoma maneno kwa sauti:\n"
                "ua   au   io   oi\n"
                "ai   ae   aa   ao\n"
            ),
        },
        {
            "title": "Sura ya 2: Silabi za Herufi",
            "body": (
                "Kusoma silabi za msingi:\n\n"
                "ba be bi bo bu\n"
                "da de di do du\n"
                "fa fe fi fo fu\n"
                "ga ge gi go gu\n"
                "ha he hi ho hu\n"
                "ja je ji jo ju\n"
                "ka ke ki ko ku\n"
                "la le li lo lu\n"
                "ma me mi mo mu\n"
                "na ne ni no nu\n"
                "pa pe pi po pu\n"
                "ra re ri ro ru\n"
                "sa se si so su\n"
                "ta te ti to tu\n"
                "va ve vi vo vu\n"
                "wa we wi wo wu\n"
                "ya ye yi yo yu\n"
                "za ze zi zo zu"
            ),
        },
        {
            "title": "Sura ya 3: Herufi 'b'",
            "body": (
                "ba be bi bo bu\n"
                "be bi bo bu ba\n"
                "bi bo bu ba be\n\n"
                "Kuunganisha silabi (b):\n"
                "ba + ba = baba\n"
                "be + ba = beba\n"
                "bi + bi = bibi\n\n"
                "Kusoma kwa sauti:\n"
                "baba   beba   bibi   bubu   babu"
            ),
        },
        {
            "title": "Sura ya 4: Herufi 'd'",
            "body": (
                "da de di do du\n"
                "de di do du da\n\n"
                "Kuunganisha silabi (d):\n"
                "da + da = dada\n"
                "du + du = dudu\n\n"
                "Kusoma kwa sauti:\n"
                "dada   debe   dodo   dua   dudu"
            ),
        },
        {
            "title": "Sura ya 20: Zoezi — Soma silabi zifuatazo kwa usahihi",
            "body": (
                "ota   ugali   oza   oga   ana   ogopa\n"
                "bati   bata   bamia   bahati   bajaji   bakuli\n"
                "duara   dodoki   dodoma   deni   dunia\n"
                "fagia   fagio   fani   fanana\n"
                "giza   gota   gari   guta   gunia   gitaa\n"
                "haji   hewa   halima   huyo   hao\n"
                "jabali   junia   jeki   juta   joka\n"
                "karai   katani   kizibo   kata   kaburi\n"
                "lima   lete   lipa\n"
                "mama   mimi   mia   moja\n"
                "nanasi   nata   nenepa\n"
                "pera   pepeta   pesa\n"
                "saza   sawa   soya   sawia   tazama\n"
                "vazi   viazi\n"
                "wizi   waza   wazazi"
            ),
        },
    ],

    # ── ORDINARY › Form 1 › Physics ─────────────────────────────────────────
    "ordinary__form1__physics": [
        {
            "title": "Introduction to Physics",
            "body": (
                "What is Physics?\n"
                "Physics is the branch of science which deals with the study of matter in relation to energy.\n\n"
                "Branches of Physics:\n"
                "1. Mechanics\n"
                "2. Electricity\n"
                "3. Magnetism\n"
                "4. Thermodynamics"
            ),
        },
    ],

    # ── ORDINARY › Form 1 › Biology ─────────────────────────────────────────
    "ordinary__form1__bio": [
        {
            "title": "Chapter 1: Introduction to Biology",
            "body_html": (
                "<h3>What is Biology?</h3>"
                "<p>Biology is the branch of science which deals with the study of living things and their life.</p>"
                "<p>The term biology originates from two Greek words: <strong>bios</strong> (life) and <strong>logos</strong> (study).</p>"
                "<h3>Branches of Biology:</h3>"
                "<ol>"
                "<li>Botany — the study of plants</li>"
                "<li>Zoology — the study of animals</li>"
                "<li>Microbiology — the study of microorganisms</li>"
                "<li>Genetics — the study of heredity and variation in organisms</li>"
                "<li>Ecology — the study of interactions between organisms and their environment</li>"
                "</ol>"
            ),
        },
    ],

    # ── ADVANCED › Form 5 › Physics ─────────────────────────────────────────
    "advanced__form5__physics": [
        {
            "title": "Mechanics — Linear Motion",
            "body": (
                "Equations of uniformly accelerated motion:\n\n"
                "1. v = u + at\n"
                "2. s = ut + ½at²\n"
                "3. v² = u² + 2as\n\n"
                "Where:\n"
                "u = initial velocity (m/s)\n"
                "v = final velocity (m/s)\n"
                "a = acceleration (m/s²)\n"
                "s = displacement (m)\n"
                "t = time (s)"
            ),
        },
    ],
}
