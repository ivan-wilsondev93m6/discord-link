"""Command handlers."""
import logging
import time
from typing import Callable, Awaitable

log = logging.getLogger(__name__)

CommandFn = Callable[[str, str, list[str]], Awaitable[str]]


class CommandHandler:
    def __init__(self, prefix: str = "!"):
        self.prefix = prefix
        self._commands: dict[str, CommandFn] = {}
        self._register_builtins()

    def _register_builtins(self):
        self.register("help", self._cmd_help)
        self.register("ping", self._cmd_ping)
        self.register("info", self._cmd_info)
        self.register("uptime", self._cmd_uptime)
        self._start_time = time.time()

    def register(self, name: str, fn: CommandFn):
        self._commands[name.lower()] = fn

    async def execute(self, text: str, user_id: str, username: str) -> str:
        parts = text.split()
        if not parts:
            return "No command specified. Use {}help".format(self.prefix)
        cmd = parts[0].lower()
        args = parts[1:]
        fn = self._commands.get(cmd)
        if fn is None:
            return f"Unknown command: {cmd}. Use {self.prefix}help"
        try:
            return await fn(user_id, username, args)
        except Exception as e:
            log.error("Command %s error: %s", cmd, e)
            return f"Error: {e}"

    async def _cmd_help(self, uid, uname, args) -> str:
        cmds = ", ".join(sorted(self._commands.keys()))
        return f"Commands: {cmds}"

    async def _cmd_ping(self, uid, uname, args) -> str:
        return "Pong! Bot is alive."

    async def _cmd_info(self, uid, uname, args) -> str:
        return f"User: {uname} ({uid}) | Commands: {len(self._commands)}"

    async def _cmd_uptime(self, uid, uname, args) -> str:
        elapsed = int(time.time() - self._start_time)
        h, m = elapsed // 3600, (elapsed % 3600) // 60
        return f"Uptime: {h}h {m}m"
