from pathlib import Path

class GameStats:
    """track statistics for aliens"""
    def __init__(self,ai_game):
        """initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        # High score should never reset
        contents = Path("high_score.txt")
        self.high_score = int(contents.read_text())
    def reset_stats(self):
        """initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

