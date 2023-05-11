from source.game import GameInstance
# Entry Point file for the main game loop.
import sys

if __name__ == '__main__':
    # Create a game instance object
    game = GameInstance()
    # Run the game loop.
    game.game_loop()
