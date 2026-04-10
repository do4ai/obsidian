---
tags:
  - space-style
description: Notion-like reading and editing surface for the do4ai workspace.
priority: 50
---
```space-style
/* priority: 50 */
html {
  --editor-width: 1120px !important;
  --editor-font: "Pretendard Variable", "Pretendard", "Inter", sans-serif !important;
  --ui-font: "Pretendard Variable", "Pretendard", "Inter", sans-serif !important;
  --ui-accent-color: #b45309;
  --top-background-color: #efe6d7;
}

html,
body {
  background: #efe6d7;
  color: #171717;
}

#sb-top {
  background: rgba(239, 230, 215, 0.94) !important;
  border-bottom: 1px solid #d6c3a5;
  backdrop-filter: blur(14px);
}

#sb-main {
  background:
    radial-gradient(circle at top left, rgba(180, 83, 9, 0.12), transparent 24rem),
    radial-gradient(circle at top right, rgba(14, 116, 144, 0.1), transparent 20rem),
    linear-gradient(180deg, #efe6d7 0%, #f6efe3 100%);
}

#sb-editor {
  padding: 2.25rem 0 4.5rem;
}

.cm-editor {
  background: #fffdf8;
  border: 1px solid #dcc7a6;
  border-radius: 22px;
  box-shadow: 0 24px 60px rgba(83, 52, 15, 0.08);
  padding: 1.25rem 0;
}

.cm-scroller {
  padding: 0 1.75rem 2.5rem;
}

.cm-content .HyperMD-header-1,
.cm-content .sb-line-h1 {
  font-size: 2.2rem;
  font-weight: 700;
  letter-spacing: -0.03em;
  color: #111827;
}

.cm-content .HyperMD-header-2,
.cm-content .sb-line-h2 {
  margin-top: 1.8rem;
  font-size: 1.45rem;
  font-weight: 650;
  color: #1f2937;
}

.cm-content a,
.ProseMirror a {
  color: #92400e;
  text-decoration-thickness: 0.08em;
  text-underline-offset: 0.16em;
}

.cm-content ul,
.cm-content ol {
  line-height: 1.7;
}

.cm-content table,
.ProseMirror table {
  width: 100%;
  margin: 1rem 0 1.6rem;
  border-collapse: separate;
  border-spacing: 0;
  background: linear-gradient(180deg, #fffdf8 0%, #f9f1e3 100%);
  border: 1px solid #e7cfaa;
  border-radius: 18px;
  box-shadow: 0 12px 24px rgba(120, 53, 15, 0.07);
  overflow: hidden;
}

.cm-content table th,
.ProseMirror table th {
  background: rgba(231, 207, 170, 0.42);
  color: #111827;
  font-size: 0.98rem;
  font-weight: 700;
  letter-spacing: -0.01em;
  padding: 0.9rem 1rem;
  border: 0;
  text-align: left;
}

.cm-content table td,
.ProseMirror table td {
  min-width: 18rem;
  padding: 1rem;
  border: 0;
  border-top: 1px solid #ecd8b9;
  color: #4b5563;
  line-height: 1.7;
  vertical-align: top;
}

@media (max-width: 900px) {
  .cm-content table,
  .ProseMirror table {
    display: block;
    overflow-x: auto;
  }
}

button {
  border-radius: 10px;
}

.sb-panel,
.sb-modal,
.sb-sidebar {
  background: #f8f2e8;
}
```
