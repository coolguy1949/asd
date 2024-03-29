

class GameStats:
    """Represents the games the authenticated user has played"""
    def __init__(self, info: dict):
        self.won = info["gamesWon"]
        self.lost = info["gamesLost"]
        self.played = info["gamesPlayed"]


class Account:
    """Represents the authenticated user"""
    def __init__(self, info: dict) -> None:
        self.balance = info["wallet"]
        self.username = info["robloxUsername"]
        self.roblox_id = info["robloxId"]
        self.total_wagered = info["wager"]
        self.total_deposited = info["totalDeposited"]
        self.game = GameStats(info=info)
