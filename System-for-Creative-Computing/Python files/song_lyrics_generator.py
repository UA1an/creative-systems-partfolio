import random

lyrics = {
    "pop": {
        "verse": [
            "I see your face in every light",
            "Dancing through another night",
            "We are young and feeling free",
            "Every moment feels like destiny"
        ],
        "chorus": [
            "Hold me closer, don't let go",
            "This is all we've ever known",
            "We shine brighter when we stay",
            "Love will guide us all the way"
        ],
        "bridge": [
            "Maybe we are scared to fall",
            "But tonight we risk it all"
        ]
    },

    "rock": {
        "verse": [
            "Concrete streets and broken signs",
            "Running out of borrowed time",
            "Voices screaming in my head",
            "Dreams are hanging by a thread"
        ],
        "chorus": [
            "Turn it up and let it burn",
            "Feel the fire, never learn",
            "We won't fade into the night",
            "This is how we choose to fight"
        ],
        "bridge": [
            "Silence hits before the sound",
            "Everything comes crashing down"
        ]
    },

    "electronic": {
        "verse": [
            "Neon lights and data streams",
            "Losing sense of what it means",
            "Digital hearts start to race",
            "Fading in this endless space"
        ],
        "chorus": [
            "Static voices pull me in",
            "We dissolve beneath the skin",
            "Rhythms take control tonight",
            "Lost between the code and light"
        ],
        "bridge": [
            "Signals break and re-align",
            "Human touch becomes a sign"
        ]
    }
}

# ---- User Input ----
print("Available genres: pop, rock, electronic")
genre = input("Choose a genre: ").lower()

emotion = input("Describe the mood or theme (e.g. love, chaos, hope): ")

if genre not in lyrics:
    print("\nGenre not recognised. Defaulting to 'pop'.\n")
    genre = "pop"

def generate_section(section, count=2):
    return random.sample(lyrics[genre][section], count)

# ---- Output ----
print("\n--- Generated Song Lyrics ---\n")
print(f"Genre: {genre.capitalize()}")
print(f"Theme: {emotion}\n")

print("[Verse]")
for line in generate_section("verse"):
    print(line)

print("\n[Chorus]")
for line in generate_section("chorus"):
    print(line)

print("\n[Verse]")
for line in generate_section("verse"):
    print(line)

print("\n[Bridge]")
for line in generate_section("bridge", 1):
    print(line)

print("\n[Chorus]")
for line in generate_section("chorus"):
    print(line)
