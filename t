ests/test_handlers.pyimport asyncio
import pytest
from handlers import CommandHandler


@pytest.fixture
def handler():
    return CommandHandler(prefix="!")


@pytest.mark.asyncio
async def test_help(handler):
    result = await handler.execute("help", "u1", "test")
    assert "help" in result.lower()


@pytest.mark.asyncio
async def test_ping(handler):
    result = await handler.execute("ping", "u1", "test")
    assert "pong" in result.lower()


@pytest.mark.asyncio
async def test_unknown_cmd(handler):
    result = await handler.execute("nonexistent", "u1", "test")
    assert "unknown" in result.lower()
