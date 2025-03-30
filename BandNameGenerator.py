import random

def generate_band_name():
    print("🎸 Welcome to the Band Name Generator! Let's create a unique name for your band. 🎶\n")

    # User inputs with validation
    user_city = input("What city did you grow up in?\n").strip()
    while not user_city:
        user_city = input("Please enter a valid city name:\n").strip()

    user_pet = input("What is the name of your pet?\n").strip()
    while not user_pet:
        user_pet = input("Please enter a valid pet name:\n").strip()

    favorite_color = input("What's your favorite color?\n").strip()
    while not favorite_color:
        favorite_color = input("Please enter a valid color:\n").strip()

    random_word = input("Enter a random word you like:\n").strip()
    while not random_word:
        random_word = input("Please enter a valid word:\n").strip()

    # Music genre selection
    genres = {
        "Rock": ["The", "Electric", "Rebel", "Sonic", "Wild"],
        "Pop": ["Glowing", "Neon", "Starry", "Echo", "Velvet"],
        "Jazz": ["Smooth", "Blue", "Soulful", "Groovy", "Cool"],
        "Hip-Hop": ["Lil", "MC", "Big", "Rhythmic", "Dope"],
        "Metal": ["Dark", "Thunder", "Inferno", "Shadow", "Venom"],
        "Indie": ["Wandering", "Dreamy", "Cosmic", "Rustic", "Ethereal"]
    }

    print("\nChoose your music genre:")
    for genre in genres.keys():
        print(f"- {genre}")

    user_genre = input("\nEnter your preferred genre:\n").strip().title()
    while user_genre not in genres:
        user_genre = input("Please choose from the genres listed above:\n").strip().title()

    # A band name based on genre
    genre_word = random.choice(genres[user_genre])
    band_names = [
        f"{genre_word} {user_city}",
        f"{user_pet} and the {random_word}s",
        f"The {favorite_color} {random_word}",
        f"{genre_word} {random_word}",
        f"{user_city} {genre_word} Collective",
        f"{genre_word} {user_pet}"
    ]

    band_name = random.choice(band_names)
    print(f"\n🔥 Your {user_genre} band name could be: {band_name}! 🔥")

# Run the generator
generate_band_name()
