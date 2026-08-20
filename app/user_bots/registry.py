from typing import Dict


class BotRegistry:

    def __init__(self):
        self._bots: Dict[int, object] = {}

    def register(
        self,
        bot_id: int,
        runner
    ):
        self._bots[bot_id] = runner

    def unregister(
        self,
        bot_id: int
    ):
        if bot_id in self._bots:
            del self._bots[bot_id]

    def get(
        self,
        bot_id: int
    ):
        return self._bots.get(bot_id)

    def is_running(
        self,
        bot_id: int
    ):
        return bot_id in self._bots

    def count(self):
        return len(self._bots)

    def all_bots(self):
        return self._bots
        

registry = BotRegistry()