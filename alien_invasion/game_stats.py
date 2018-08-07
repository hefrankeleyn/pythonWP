class GameStats():
    """information track game"""
    def __init__(self,ai_settings):
        self.ai_settings=ai_settings
        self.reset_stats()
        #Game is active,begin the game is not active.
        self.game_active=False
    
    def reset_stats(self):
        self.ships_left=self.ai_settings.ship_limit
        self.score = 0
