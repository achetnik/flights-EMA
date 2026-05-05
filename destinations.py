"""East Midlands Airport (EMA) destinations — May 2026."""

DESTINATIONS = {
    "EMA": {
        "name": "East Midlands",
        "routes": {
            "ACE": "Lanzarote",
            "ADB": "Izmir",
            "AGP": "Malaga",
            "ALC": "Alicante",
            "AYT": "Antalya",
            "BCN": "Barcelona",
            "BER": "Berlin",
            "BFS": "Belfast Intl",
            "BJV": "Bodrum",
            "BOJ": "Bourgas",
            "BUD": "Budapest",
            "CCF": "Carcassonne",
            "CFU": "Corfu",
            "CHQ": "Chania",
            "CMF": "Chambery",
            "DBV": "Dubrovnik",
            "DLM": "Dalaman",
            "DUB": "Dublin",
            "EFL": "Kefalonia",
            "FAO": "Faro",
            "FCO": "Rome",
            "FNC": "Funchal",
            "FUE": "Fuerteventura",
            "GRO": "Girona",
            "GVA": "Geneva",
            "HER": "Heraklion",
            "IBZ": "Ibiza",
            "JER": "Jersey",
            "JSI": "Skiathos",
            "KEF": "Reykjavik",
            "KGS": "Kos",
            "KRK": "Krakow",
            "LCA": "Larnaca",
            "LIG": "Limoges",
            "LPA": "Gran Canaria",
            "MAH": "Menorca",
            "MLA": "Malta",
            "NAP": "Naples",
            "NBE": "Enfidha",
            "NOC": "Knock",
            "PFO": "Paphos",
            "PMI": "Palma",
            "PRG": "Prague",
            "PUY": "Pula",
            "PVK": "Preveza",
            "REU": "Reus",
            "RHO": "Rhodes",
            "RIX": "Riga",
            "SKG": "Thessaloniki",
            "SZG": "Salzburg",
            "TFS": "Tenerife South",
            "TRN": "Turin",
            "TSF": "Venice Treviso",
            "VIE": "Vienna",
            "VLC": "Valencia",
            "VRN": "Verona",
            "WRO": "Wroclaw",
            "ZTH": "Zakynthos",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
