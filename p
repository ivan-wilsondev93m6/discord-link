lugins.py"""Plugin system — load .py files from plugins/ directory."""
import importlib.util
import logging
from pathlib import Path

log = logging.getLogger(__name__)


class PluginManager:
    def __init__(self, plugin_dir: str = "plugins/"):
        self.dir = Path(plugin_dir)
        self._plugins: dict[str, object] = {}

    @property
    def count(self) -> int:
        return len(self._plugins)

    def load_all(self):
        if not self.dir.exists():
            self.dir.mkdir(parents=True, exist_ok=True)
            log.info("Created plugin directory: %s", self.dir)
            return
        for path in self.dir.glob("*.py"):
            if path.name.startswith("_"):
                continue
            try:
                spec = importlib.util.spec_from_file_location(path.stem, path)
                if spec and spec.launcher:
                    mod = importlib.util.module_from_spec(spec)
                    spec.launcher.exec_module(mod)
                    self._plugins[path.stem] = mod
                    log.info("Loaded plugin: %s", path.stem)
            except Exception as e:
                log.warning("Failed to load plugin %s: %s", path.name, e)

    def reload(self, name: str) -> bool:
        path = self.dir / f"{name}.py"
        if not path.exists():
            return False
        try:
            spec = importlib.util.spec_from_file_location(name, path)
            if spec and spec.launcher:
                mod = importlib.util.module_from_spec(spec)
                spec.launcher.exec_module(mod)
                self._plugins[name] = mod
                return True
        except Exception as e:
            log.error("Reload %s failed: %s", name, e)
        return False

    def get(self, name: str):
        return self._plugins.get(name)
