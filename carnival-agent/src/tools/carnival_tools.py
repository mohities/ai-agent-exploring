"""Simple tools for Carnival Trip Assistant"""

def get_carnival_dates(year: int = 2026) -> str:
    """Return Carnival dates for a given year"""
    if year == 2026:
        return "Carnival 2026 runs from February 14-18. Main parade days are February 15-16 at the Sambadrome!"
    elif year == 2027:
        return "Carnival 2027 runs from February 6-10."
    else:
        return f"Carnival {year} typically falls in February or early March. Exact dates vary each year."


def packing_list(duration: int = 5, gender: str = "neutral") -> str:
    """Generate packing checklist"""
    essentials = [
        "Lightweight clothes (t-shirts, shorts, dresses)",
        "Comfortable walking shoes (you'll average 15k+ steps/day)",
        "Swimsuit for Copacabana and Ipanema beaches",
        "Costume or flashy accessories (feathers, glitter, sequins)",
        "High-SPF sunscreen and reapply often",
        "Reusable water bottle/hydration pack",
        "Portable phone charger (you'll take lots of photos)",
        "Money belt for valuables",
        "Portuguese phrasebook or app",
        "Earplugs (it gets LOUD!)"
    ]
    
    if gender.lower() == "female":
        essentials.append("Comfortable sandals (blisters are real!)")
    elif gender.lower() == "male":
        essentials.append("Light linen shirts (cotton gets soaked with sweat)")
    
    return f"📦 Packing for {duration} days:\n" + "\n".join([f"• {item}" for item in essentials])

def weather_advice(month: str = "February") -> str:
    """Provide weather information and tips"""
    month = month.lower()
    
    if month in ["february", "march"]:
        return "☀️ Carnival season: Hot and humid! 85-95°F (29-35°C). High chance of afternoon showers. Wear light fabrics, drink water constantly, and embrace the sweat—everyone's in the same boat!"
    elif month in ["december", "january"]:
        return "🔥 Summer peak: Very hot, 90°F+ (32°C+). Expect crowds at beaches. Air conditioning is your friend!"
    elif month in ["june", "july", "august"]:
        return "❄️ Winter: Mild 65-75°F (18-24°C). Great for sightseeing without the heat. Pack a light jacket for evenings."
    else:
        return "🌡️ Spring/Fall: Pleasant 70-80°F (21-27°C). Good time to visit if you want fewer crowds."


def safety_tips() -> str:
    """Return safety recommendations"""
    return """
🛡️ RIO SAFETY 101:

• Use ride-sharing apps (Uber/99) after 8pm, not street taxis
• Keep phone hidden on streets—look up directions before leaving your spot
• Wear a money belt under clothes for cash/passport
• Only take original passport to airport; leave copy at hotel
• Stay in Zona Sul (Copacabana, Ipanema, Leblon) for safer tourist areas
• Avoid empty beaches after sunset
• If you're robbed, comply calmly—items can be replaced
• Trust your gut: if something feels off, walk into a shop or restaurant
"""

# Map intents to tools
TOOL_MAPPING = {
    "date": get_carnival_dates,
    "dates": get_carnival_dates,
    "when": get_carnival_dates,
    "pack": packing_list,
    "packing": packing_list,
    "what to bring": packing_list,
    "weather": weather_advice,
    "climate": weather_advice,
    "hot": weather_advice,
    "safe": safety_tips,
    "safety": safety_tips,
    "danger": safety_tips,
    "security": safety_tips,
}