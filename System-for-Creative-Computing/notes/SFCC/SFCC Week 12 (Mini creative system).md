## Song Lyrics Generator (Python)



---
## Introduction

This project is a mini creative system made using Python.  
It explores how song lyrics can be generated with code instead of being written by hand.

The system uses simple rules, randomness, and a fixed song structure to create new lyrics each time it runs. The goal of the project is to show how creative ideas can be supported by algorithms.

---
## Project Aims

The aims of this project are:

- To create a small system that generates song lyrics  
- To use simple rules and randomness to support creativity  
- To generate different results on each run  
- To include basic user input  
- To demonstrate creative computing in a simple way  

---
## Concept

The idea of this project is based on how songs usually follow a clear structure, such as verses, choruses, and a bridge. Instead of writing lyrics manually, this system follows the same structure automatically using code.

The system selects lines of text from prepared lists and combines them into a song. Randomness is used so that the lyrics change every time, while the structure stays the same.

---
## Tools Used

- Python  
- Command line (PowerShell)  

---
## Practical Implementation

The project was implemented as a Python script.  
When the script is run, the user is asked to choose a music genre and enter a mood or theme.

Based on the selected genre, the system generates a song using a fixed structure:
- Verse  
- Chorus  
- Verse  
- Bridge  
- Chorus  

Each section is created by randomly selecting lines from predefined lists.

---
## User Input

The user provides:
- A genre (pop, rock, or electronic)  
- A short description of the mood or theme  

The genre affects which lyrics are used, while the mood adds context to the output. The user influences the result, but the system still makes its own decisions.

---
## How the System Works (Step by Step)

1. The program starts and asks the user for input  
2. Lyric lines are stored in lists grouped by genre  
3. The system randomly selects lines for each song section  
4. A fixed song structure is applied  
5. The final lyrics are printed in the terminal  

Each time the program runs, a new version of the song is created.

---
## Use of Randomness

Randomness is an important part of this system.  
It is used to:
- create variation  
- avoid repeating the same lyrics  
- make each output feel different  

Even though the lyrics change, the structure keeps the song understandable.

---
## Code Explanation (Simple Overview)

This section explains the main parts of the Python code used in this project in a simple way.

### Importing Libraries

``` python
import random
```

The `random` library is used to generate different results each time the program runs.
It allows the system to randomly select lyric lines, which is important for creating variation in the generated songs.

### Storing Lyrics Data

```python
lyrics = {
    "pop": { ... },
    "rock": { ... },
    "electronic": { ... }
}
```

The lyrics are stored in a dictionary.
Each key represents a music genre, and inside each genre there are lists for verses, choruses, and bridges.

This structure makes the code:
- easy to read
- easy to expand with new genres
- organised and clear

### User Input

```python
genre = input("Choose a genre: ").lower()
emotion = input("Describe the mood or theme: ")
```

These lines allow the user to interact with the system.
The user chooses a genre and writes a short description of the song’s mood or theme.

The genre affects the generated lyrics, while the theme adds context to the output.

### Input Check

```python
if genre not in lyrics:
    genre = "pop"
```

This condition checks if the user entered a valid genre.
If not, the system automatically selects a default genre so the program can still run without errors.

### Generating Song Sections

```python
def generate_section(section, count=2):
    return random.sample(lyrics[genre][section], count)
```

This function selects a random set of lyric lines from a specific song section.
Using a function helps avoid repeating code and keeps the program organised.

Random selection ensures that the lyrics change each time.

### Song Structure

```python
print("[Verse]")
print("[Chorus]")
print("[Bridge]")
```

These lines define the structure of the song.
The structure stays the same every time, which helps the generated lyrics feel like a real song.

Only the content inside each section changes.

### Output

```python
print(line)
```

The generated lyrics are printed in the terminal.
This makes the system simple and easy to test without using additional libraries or files.
Each run of the program creates a new version of the song.

### Final Code
``` python
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

```

---
## Reflection

This project helped me understand how creative systems can be built using simple rules and algorithms. I learned that creativity does not always require complex code, and that even basic randomness and structure can produce interesting results.

Using Python made it easy to experiment and quickly test ideas. I also learned how user input can be included without fully controlling the system.

---
## Conclusion

This mini creative system shows how songwriting ideas can be explored using code. By combining structure, randomness, and user input, the system is able to generate different song lyrics while staying easy to understand and use.
