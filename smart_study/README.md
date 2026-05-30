# Smart Study Pro-Notes — FastAPI

A Tanzanian school notes web app converted from a single HTML file into a
proper FastAPI backend + Jinja2 frontend.

---

## 📁 Project Structure

```
smart_study/
├── main.py            ← FastAPI app entry point
├── database.py        ← ALL notes and metadata live here
├── requirements.txt
├── routers/
│   ├── levels.py      ← GET /api/levels
│   ├── classes.py     ← GET /api/levels/{level}/classes
│   ├── subjects.py    ← GET /api/levels/{level}/subjects
│   └── notes.py       ← CRUD /api/levels/{level}/classes/{class}/subjects/{sub}/notes
└── templates/
    └── index.html     ← Full frontend (fetches from the API)
```

---

## 🚀 Setup & Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start the server
uvicorn main:app --reload

# 3. Open in browser
# http://localhost:8000
```

The interactive API docs are at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**:      http://localhost:8000/redoc

---

## ✏️ How to Add New Notes / Books

### Method 1 — From the website (runtime, temporary)
1. Navigate to any subject in the app.
2. Scroll down to the **"Andika Note Mpya"** panel.
3. Fill in the title and body, then click **"Hifadhi Note"**.
4. The note appears in the sidebar immediately.
   *(These notes are lost when the server restarts — use Method 2 to make them permanent.)*

### Method 2 — Edit `database.py` (permanent)
Open `database.py` and find the right key, e.g.:
```python
"ordinary__form1__physics": [
    { "title": "Chapter 2: Measurement", "body": "…your content here…" },
    # ↑ add more chapters here
],
```

**Key format:** `"{level}__{classId}__{subjectId}"`

| Part      | Options |
|-----------|---------|
| level     | `primary`, `ordinary`, `advanced` |
| classId   | `std1`, `std2`, `std34`, `std567`, `form1`…`form6` |
| subjectId | `math`, `swahili`, `science`, `physics`, `chem`, `bio`, `admath` |

### Method 3 — POST request (via Swagger or script)
```bash
curl -X POST "http://localhost:8000/api/levels/ordinary/classes/form1/subjects/physics/notes" \
  -H "Content-Type: application/json" \
  -d '{"title":"Chapter 2: Measurement","body":"SI units are…"}'
```

---

## 📝 Note Types

| Field      | Description |
|------------|-------------|
| `title`    | Chapter/section title |
| `body`     | Plain text content (supports emoji, `\n` for newlines) |
| `body_html`| HTML content (for formatted chapters with headings, lists, etc.) |
| `note_type`| Set to `"interactive"` for the counting widget |

---

## ➕ Adding a New Subject or Class

1. Add the subject to the `SUBJECTS` dict in `database.py`.
2. Add a new key in `MY_DATABASE` with the matching format.
3. Restart the server — the new subject appears automatically.
