onfig.pyimport yaml, os, logging
log = logging.getLogger(__name__)

DEFAULT = {
    "token": "",
    "prefix": "!",
    "rate_limit": 30,
    "admin_ids": [],
    "plugins_dir": "plugins/",
}

def load_config(path="config.yaml"):
    if not os.path.exists(path):
        with open(path, "w") as f:
            yaml.dump(DEFAULT, f, default_flow_style=False)
        return dict(DEFAULT)
    with open(path) as f:
        return {**DEFAULT, **(yaml.safe_load(f) or {})}
