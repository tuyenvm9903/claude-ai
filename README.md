# Anthropic Academy — Bilingual quizzes (EN / VI)

Interactive multiple‑choice quizzes for Anthropic Academy courses on Skilljar.
Each quiz is **song ngữ Anh–Việt**, tracks score, and explains every answer.

## Live site / Trang trực tiếp

**Hub (chọn khóa học):** [https://tuyenvm9903.github.io/claude-ai/](https://tuyenvm9903.github.io/claude-ai/)

| Course | Quiz URL |
| --- | --- |
| **Claude 101** | […/courses/claude-101/](https://tuyenvm9903.github.io/claude-ai/courses/claude-101/) |
| **Building with the Claude API** | […/courses/claude-api/](https://tuyenvm9903.github.io/claude-ai/courses/claude-api/) |

## Repository layout

```
claude-ai/
├── index.html                 # Hub: tabs + cards linking to each course
├── courses/
│   ├── claude-101/index.html  # Claude 101 quiz (~29 questions)
│   └── claude-api/index.html  # Claude API course quiz (~80 questions)
├── scripts/
│   └── inject_api_quiz.py    # Dev helper to regenerate API quiz block (optional)
└── README.md
```

## Features

- **Hub:** hai tab / hai thẻ — **Claude 101** và **Building with the Claude API** — trỏ tới đúng thư mục khóa học.
- **Claude 101:** các module Meet Claude → Projects / Artifacts / Skills → mở rộng (Connector, Enterprise Search, Research) → tổng hợp use case → chứng chỉ + FAQ Skilljar.
- **Claude API:** API & Messages, system prompt / temperature / streaming / structured output, prompt eval, engineering, tool use, RAG, tính năng (thinking, đa phương thức, caching), MCP, Claude Code / Computer Use, agent workflows + FAQ Skilljar.
- Dark UI, responsive, **single HTML file per course** — không cần build.

## Local usage / Chạy trên máy

```bash
git clone https://github.com/tuyenvm9903/claude-ai.git
cd claude-ai
xdg-open index.html   # macOS: open index.html
```

## Sources

- [Claude 101 — Skilljar](https://anthropic.skilljar.com/claude-101)
- [Building with the Claude API — Skilljar](https://anthropic.skilljar.com/claude-with-the-anthropic-api)

This repository is a community study aid and is not affiliated with Anthropic.
© Anthropic PBC for the underlying course content.
