# Pub Selector Pro 🍺

A PyQt6-based desktop tool for randomly selecting pubs from a database, 
with slot-machine style animation, tagging, and page creation for writing.

## Features
- 🎰 Slot machine vertical scroll animation for pub selection
- 📂 Three lists: To Work On, Working On, Finished
- 🏷 Tag support for filtering pubs by type (e.g., Irish, Pub Garden, Dancefloor)
- 📄 Opens `.odt` pages in LibreOffice Writer
- 💾 SQLite database backend

## Demo
*(Insert GIF or screenshot here once ready)*

## Tech Stack
- Python 3
- PyQt6
- SQLite
- LibreOffice Writer

## Installation
```bash
git clone https://github.com/<your-username>/pub-selector.git
cd pub-selector
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
