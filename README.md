# Luau Discord Bot

This bot downloads the latest Luau VM and allows users to upload an obfuscated Luau script. It detects the pattern ~= #{} and adds warn() at specific points.

## Setup

1. Clone this repo.
2. Install requirements: `pip install -r requirements.txt`
3. Edit `config.py` with your Discord bot token.
4. Run: `python bot.py`

## Features

- Automatically downloads Luau VM from GitHub
- Accepts uploads of Luau scripts
- Injects warn() calls after certain obfuscated expressions
