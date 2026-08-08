
import random
import string


class WordBank:
    """Stores and provides words that can be used in the game."""

    def __init__(self):
        # Keep the available words inside the class instead of using
        # a global list. This demonstrates encapsulation.
        self.words = [
            "python", "variable", "function", "iterator", "notebook",
            "pipeline", "dataset", "computer", "research", "analytics"
        ]

    def get_random_word(self):
        """Return a randomly selected word."""
        return random.choice(self.words)


class WordGuessingGame:
    """Controls the state and behaviour of a word guessing game."""

    def __init__(self, max_lives=6):
        # Store the game settings and state inside the object.
        self.max_lives = max_lives
        self.lives = max_lives
        self.word_bank = WordBank()

        # Select the secret word when a new game is created.
        self.secret_word = self.word_bank.get_random_word()

        # Create one blank for every character in the secret word.
        self.blanks = ["_" for _ in self.secret_word]

        # A set is used because each guessed letter should only appear once.
        self.used_letters = set()

    def display_word(self):
        """Display the currently revealed letters."""
        print(" ".join(self.blanks))

    def prompt_for_letter(self):
        """Ask the player for a valid letter that has not been used."""

        while True:
            guess = input("Guess a letter: ").strip().lower()

            # Check that the player entered exactly one alphabetic character.
            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print(" → Please enter a single A-Z letter.")
                continue

            # Prevent the player from guessing the same letter twice.
            if guess in self.used_letters:
                print(" → You already tried that letter.")
                continue

            return guess

    def reveal_letters(self, letter):
        """Reveal all occurrences of a correctly guessed letter."""

        found_any = False

        # Check every character in the secret word.
        for index, character in enumerate(self.secret_word):
            if character == letter and self.blanks[index] == "_":
                self.blanks[index] = letter
                found_any = True

        return found_any

    def is_word_complete(self):
        """Return True when all letters in the word have been revealed."""
        return "_" not in self.blanks

    def play(self):
        """Run the main game loop."""

        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(self.secret_word)} letters.")
        self.display_word()

        while True:
            # Ask the player to enter a valid, unused letter.
            guess = self.prompt_for_letter()
            self.used_letters.add(guess)

            # Check whether the guessed letter exists in the secret word.
            if self.reveal_letters(guess):
                print("\nWell done, nice job! You found a letter.")
                self.display_word()

                # Check whether the player has revealed the complete word.
                if self.is_word_complete():
                    print("\nCongratulations! You guessed the word!")
                    print(f"Word: {self.secret_word}")
                    print("GAME OVER")
                    break

            else:
                # A wrong guess reduces the player's remaining lives.
                self.lives -= 1

                print(f"\nNope. You lose a life. Lives left: {self.lives}")
                self.display_word()

                # End the game when the player has no lives remaining.
                if self.lives <= 0:
                    print("\nOut of lives! Better luck next time!")
                    print(f"The word was: {self.secret_word}")
                    print("GAME OVER")
                    break


def main():
    """Create a game object and start the game."""

    # Creating an object from the WordGuessingGame class
    # allows the game state and behaviour to be managed together.
    game = WordGuessingGame(max_lives=6)
    game.play()


# This ensures the game starts only when this file is executed directly.
if __name__ == "__main__":
    main()
