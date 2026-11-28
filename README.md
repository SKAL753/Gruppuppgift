# Minesweeper

Ett klassiskt Minesweeper-spel utvecklat i Python. Projektet började som ett terminalbaserat spel och utvecklas nu vidare med ett webbgränssnitt med hjälp av Flask, HTML, CSS och JavaScript.

## Funktioner

- Slumpmässig placering av minor på spelplanen.
- Beräkning av antal intilliggande minor.
- Möjlighet att avslöja rutor.
- Möjlighet att flagga misstänkta minor.
- Automatisk avslöjning av intilliggande tomma rutor.
- Kontroll av om spelaren har vunnit eller förlorat.

## Tekniker

- **Python** – Spelets logik och funktionalitet.
- **Flask** – Backend och kommunikation mellan Python och webbgränssnittet.
- **HTML** – Webbgränssnittets struktur.
- **CSS** – Webbgränssnittets utseende.
- **JavaScript** – Interaktivitet och kommunikation med backend.

## Projektstruktur

```text
minesweeper/
│
├── app.py
├── main.py
├── game.py
├── board.py
├── cell.py
├── ui.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

## Installation

1. Klona repot:

```bash
git clone <repository-url>
```

2. Gå till projektmappen:

```bash
cd minesweeper
```

3. Skapa en virtuell miljö:

```bash
python -m venv .venv
```

4. Aktivera den virtuella miljön:

**Windows PowerShell:**
```powershell
.\.venv\Scripts\Activate.ps1
```

5. Installera beroenden:

```bash
python -m pip install flask
```

## Starta projektet

Starta Flask-servern med:

```bash
python app.py
```

Öppna sedan följande adress i webbläsaren:

```text
http://127.0.0.1:5000
```

## Utvecklingsstatus

Projektets grundläggande spellogik är implementerad i Python. Arbetet med att utveckla ett webbgränssnitt och integrera det med spelets backend pågår fortfarande.