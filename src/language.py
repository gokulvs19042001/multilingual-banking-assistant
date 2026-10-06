# Romanized Tamil (Tanglish) marker words. Add more as you collect real queries.
TANGLISH_WORDS = {
    "enna", "epdi", "eppadi", "paisa", "panam", "varala", "vanthuchu", "venum",
    "irukku", "illa", "enakku", "yen", "ean", "poyiduchu", "pochu", "kuduthuten",
    "sollitten", "maranthuten", "vaanguradhu", "kattanum", "pannanum", "panna",
    "eppo", "enga", "evlo", "evvalavu", "athu", "idhu", "naan", "enga",
    "kadan", "vatti", "kanakku", "podanum", "mudiyuma", "irukka",
}

LANG_NAMES = {
    "ta": "Tamil",
    "en": "English",
    "roman": "Tamil, written in Tamil script (the user typed Tamil using English letters)",
}

def detect_language(text: str) -> str:
    tamil_chars = sum(1 for ch in text if 0x0B80 <= ord(ch) <= 0x0BFF)
    if tamil_chars > 0:
        return "ta"
    words = text.lower().replace("?", " ").replace(",", " ").split()
    if any(w in TANGLISH_WORDS for w in words):
        return "roman"
    return "en"