# PDF Tutor

Upload a PDF, highlight passages or capture regions of a page, and ask a **strictly grounded**
AI tutor about them. Also generates 4-option multiple-choice quizzes from the document.

- **AI model:** OpenAI (recommended) via the `openai` SDK — set `OPENAI_API_KEY` to use OpenAI models
  (e.g., `gpt-4o`, `gpt-4o-mini`). The project also contains legacy Gemini support via
  `google-genai` if `GEMINI_API_KEY` is provided; set `GEMINI_MODEL` to override the Gemini model name.
- **Backend:** FastAPI + Swagger UI
- **Frontend:** React 19 + Vite + pdf.js

> The Streamlit files in this folder (`app.py`, `llm.py`, `retriever.py`, `data_loader.py`) are the
> earlier VLearn transcript prototype and are unrelated to this app.

---

## Setup

### 1. Backend

```bash
cd codebase/backend
pip install -r requirements.txt
cp .env.example .env          # then put your key in OPENAI_API_KEY (preferred) or GEMINI_API_KEY
uvicorn main:app --reload --port 8000
```

Get an OpenAI key at https://platform.openai.com (or a Gemini key at https://aistudio.google.com/apikey).

- API: http://localhost:8000
- **Swagger UI: http://localhost:8000/docs**

### 2. Frontend

```bash
cd codebase/frontend
npm install
npm run dev
```

Open http://localhost:5173. Vite proxies `/api` to port 8000, so the browser sees one origin.

---

## How to use it

| Action | How |
|---|---|
| Add a highlight | Select text on the page — it lands in the composer tray |
| Add a screenshot | **Capture area** → drag a box over the page |
| Combine them | Attach several highlights and captures, then type one question |
| Follow up | Keep asking in the same panel; the session holds the conversation |
| Check a claim | Click any `p.N` citation chip to jump to that page |
| Quiz yourself | **Quiz** tab → pick a page range and difficulty → Generate |

---

## How grounding is enforced

The strict-grounding constraint is enforced in three places, not just in the prompt:

1. **Context is closed.** The model only ever receives page text from the uploaded PDF
   ([`grounding.py`](backend/grounding.py) `select_pages` / `build_context`). Documents under
   `FULL_DOC_CHAR_BUDGET` characters are sent whole; larger ones go through BM25 retrieval over
   page chunks, always including the page in view and any highlighted pages.
2. **The prompt forbids outside knowledge** and requires a verbatim quote per citation
   ([`prompts.py`](backend/prompts.py)). When the document does not cover the question the model
   must return `grounded: false` rather than answer from training data.
3. **Citations are re-checked after generation.** Every quote is matched against the extracted text
   of the page it cites ([`grounding.py`](backend/grounding.py) `quote_is_grounded`, near-verbatim
   to tolerate PDF extraction noise). Citations to pages the model was never shown are dropped;
   unverified quotes are returned flagged and rendered in amber in the UI. Quiz questions whose
   evidence quote cannot be located on the cited page are **discarded**, and the count is reported
   as `dropped`.

Screenshots are also in-scope source material: a crop is pixels from the uploaded PDF, sent to
the model as an image part alongside that page's text (OpenAI image-capable models or Gemini
clients when available).

---

## API

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/documents` | Upload a PDF, chunk it page by page |
| `GET` | `/api/documents` | List documents |
| `GET` | `/api/documents/{id}` | Detail + page map |
| `GET` | `/api/documents/{id}/file` | Original PDF (for the pdf.js viewer) |
| `GET` | `/api/documents/{id}/pages/{n}` | Extracted text of one page |
| `DELETE` | `/api/documents/{id}` | Delete document and its sessions |
| `POST` | `/api/chat/sessions` | Start a session for a document |
| `GET` | `/api/chat/sessions/{id}` | Full transcript |
| `POST` | `/api/chat/sessions/{id}/ask` | Ask with highlights + screenshots |
| `DELETE` | `/api/chat/sessions/{id}` | End a session |
| `POST` | `/api/quiz` | Generate a multiple-choice quiz |
| `GET` | `/api/health` | Status + whether the API key is configured |

---

## Layout

```
codebase/
├── backend/
│   ├── main.py          FastAPI app, CORS, Swagger metadata
│   ├── config.py        env-driven settings
│   ├── schemas.py       request/response models
│   ├── pdf_utils.py     page-by-page text extraction
│   ├── retrieval.py     BM25 over page chunks (dependency-free)
│   ├── grounding.py     context selection + citation verification
│   ├── prompts.py       system instructions
│   ├── gemini.py        Legacy Gemini structured-output client (adaptable to OpenAI)
│   ├── routers/         documents · chat · quiz
│   └── storage/         uploaded PDFs + extracted pages (gitignored)
└── frontend/
    └── src/
        ├── App.tsx      shell, document + selection state
        ├── api.ts       typed API client
        ├── styles.css   blue/white design system
        └── components/  PdfViewer · ChatPanel · QuizPanel · Sidebar
```

## Known limits

- Chat sessions are in memory; restarting the backend clears conversations (uploaded documents
  survive on disk).
- Scanned/image-only PDFs have no extractable text. Upload still works and **Capture area** still
  works, but text answers and quizzes will be thin — the app warns you on upload.
- Highlight rectangles are kept for the current session only and are not persisted.
