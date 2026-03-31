#!/usr/bin/env python3
"""Discord bot with commands and plugin system."""
import argparse
import asyncio
import logging
import os
import sys
from config import load_config
from handlers import CommandHandler
from plugins import PluginManager
from middleware import RateLimiter

log = logging.getLogger(__name__)


class Discordlink:
    def __init__(self, config_path: str = "config.yaml"):
        self.cfg = load_config(config_path)
        self.token = os.environ.get("BOT_TOKEN", self.cfg.get("token", ""))
        self.prefix = self.cfg.get("prefix", "!")
        self.handler = CommandHandler(self.prefix)
        self.plugins = PluginManager("plugins/")
        self.rate_limiter = RateLimiter(
            max_per_minute=self.cfg.get("rate_limit", 30)
        )
        self._running = True

    async def start(self):
        if not self.token:
            log.error("No bot token. Set BOT_TOKEN env or token in config.yaml")
            sys.exit(1)
        self.plugins.load_all()
        log.info("discord-link starting (prefix=%s, plugins=%d)",
                 self.prefix, self.plugins.count)
        await self._main_loop()

    async def _main_loop(self):
        """Main event loop — override for specific platform."""
        log.info("Bot ready. Listening for commands...")
        while self._running:
            await asyncio.sleep(1)

    async def handle_message(self, user_id: str, username: str,
                              message: str) -> str | None:
        if not self.rate_limiter.allow(user_id):
            return "Rate limited. Slow down."
        if not message.startswith(self.prefix):
            return None
        cmd_text = message[len(self.prefix):].strip()
        response = await self.handler.execute(cmd_text, user_id, username)
        return response

    def stop(self):
        self._running = False
        log.info("discord-link stopped")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-c", "--config", default="config.yaml")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    bot = Discordlink(args.config)
    try:
        asyncio.run(bot.start())
    except KeyboardInterrupt:
        bot.stop()


if __name__ == "__main__":
    main()
