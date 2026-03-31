# 🤖 discord-link

![Version](https://img.shields.io/badge/version-1.0.0-green.svg) ![Platform](https://img.shields.io/badge/platform-Windows-blue.svg)

![tool](https://img.shields.io/badge/tool-MIT-green?style=flat-square) ![Version](https://img.shields.io/badge/Version-1.2.0-blue?style=flat-square) ![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=flat-square) ![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white) ![Stars](https://img.shields.io/github/stars/ivan-wilsondev93m6/discord-link?style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/ivan-wilsondev93m6/discord-link?style=flat-square)

Upload files of any size to Discord without Nitro and retrieve them using the app

## ✅ Features

- ✅ Rate limiting middleware per user
- ✅ Command handler with customizable prefix
- ✅ Role-based permission system
- ✅ Plugin system with hot-reload capability
- ✅ Configurable via YAML with .env secrets
- ✅ Auto-reconnect on connection loss

## ⚙️ Configuration

Copy and edit the example config:
```bash
cp config.example.yaml config.yaml
```

## ⚙️ Installation

[![Download](https://img.shields.io/badge/Download-Latest%20Release-blue?style=for-the-badge&logo=github)](../../releases/latest)

**Option 1:** Download from [Releases](../../releases/latest) and extract

**Option 2:** Clone and run
```bash
git clone https://github.com/ivan-wilsondev93m6/discord-link.git
cd discord-link
pip install -r requirements.txt
python main.py
```


## ❓ FAQ

<details><summary>How do I get a bot token?</summary>

See documentation for details.
</details>

<details><summary>Can I self-host this?</summary>

See documentation for details.
</details>

<details><summary>What permissions does it need?</summary>

See documentation for details.
</details>


## 📄 tool

MIT tool. See [tool](tool) for details.

___

If you find **discord-link** useful, give it a ⭐ — it helps others discover this project.

Found a bug? [Open an issue](../../issues/new).## 📋 Commands

| Command | Description |
|---------|-------------|
| `/help` | Show all commands |
| `/ping` | Check latency |
| `/config` | View settings |
| `/reload` | Reload plugins |



