# hangman_stages.py

stages = [
    # Stage 0: Empty gallows (shown when lives = 6)
    """
    +---+
    |   |
        |
        |
        |
        |
    ====
    """,
    # Stage 1: Head (shown when lives = 5)
    """
    +---+
    |   |
    O   |
        |
        |
        |
    ====
    """,
    # Stage 2: Head + Body (shown when lives = 4)
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    ====
    """,
    # Stage 3: Head + Body + One Arm (shown when lives = 3)
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    ====
    """,
    # Stage 4: Head + Body + Both Arms (shown when lives = 2)
    """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    ====
    """,
    # Stage 5: Head + Body + Both Arms + One Leg (shown when lives = 1)
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    ====
    """,
    # Stage 6: Full hangman (shown when lives = 0, Game Over)
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    ====
    """
]