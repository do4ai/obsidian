---
tags:
  - space-style
description: Notion-like reading and editing surface for the do4ai workspace.
priority: 50
---
```space-style
/* priority: 50 */
/* Force a coherent warm light palette even when SilverBullet auto-selects dark mode. */
html,
html[data-theme="light"],
html[data-theme="dark"] {
  color-scheme: light;
  --editor-width: 1120px !important;
  --editor-font: "Pretendard Variable", "Pretendard", "Inter", sans-serif !important;
  --ui-font: "Pretendard Variable", "Pretendard", "Inter", sans-serif !important;
  --ui-accent-color: #b45309;
  --ui-accent-text-color: #92400e;
  --ui-accent-contrast-color: #fffaf2;
  --highlight-color: rgba(245, 158, 11, 0.22);
  --link-color: #92400e;
  --link-missing-color: #c2410c;
  --link-invalid-color: #b91c1c;
  --meta-color: #c2410c;
  --meta-subtle-color: #8b7355;
  --subtle-color: #6b5b45;
  --subtle-background-color: rgba(180, 83, 9, 0.08);
  --root-background-color: #f6efe3;
  --root-color: #21180f;
  --top-color: #3f3220;
  --top-background-color: #efe6d7;
  --top-border-color: #d6c3a5;
  --top-sync-error-color: #7c2d12;
  --top-sync-error-background-color: #fef3c7;
  --top-saved-color: #3f3220;
  --top-unsaved-color: #7c6a52;
  --top-loading-color: #8f7a61;
  --panel-background-color: #fffaf2;
  --panel-border-color: #e7cfaa;
  --bhs-background-color: #fffaf2;
  --bhs-border-color: #d6c3a5;
  --modal-color: #2b2116;
  --modal-background-color: #fffaf2;
  --modal-border-color: #cbb38e;
  --modal-header-label-color: #92400e;
  --modal-help-background-color: #f8efe0;
  --modal-help-color: #6b5b45;
  --modal-selected-option-background-color: #b45309;
  --modal-selected-option-color: #fffaf2;
  --modal-hint-background-color: #92400e;
  --modal-hint-color: #fffaf2;
  --modal-hint-inactive-background-color: #efe6d7;
  --modal-hint-inactive-color: #3f3220;
  --modal-description-color: #7c6a52;
  --modal-selected-option-description-color: #fef3c7;
  --notifications-background-color: #fffaf2;
  --notifications-border-color: #cbb38e;
  --notification-info-background-color: #dbeafe;
  --notification-error-background-color: #fecaca;
  --button-background-color: #f8efe0;
  --button-hover-background-color: #efe0c7;
  --button-color: #2b2116;
  --button-border-color: #d6c3a5;
  --primary-button-background-color: #b45309;
  --primary-button-hover-background-color: #92400e;
  --primary-button-color: #fffaf2;
  --primary-button-border-color: transparent;
  --text-field-background-color: #fffdf8;
  --progress-background-color: #f1e3cd;
  --progress-sync-color: #92400e;
  --progress-index-color: #0f766e;
  --action-button-background-color: transparent;
  --action-button-color: #6b5b45;
  --action-button-hover-color: #92400e;
  --action-button-active-color: #92400e;
  --editor-caret-color: #1f2937;
  --editor-selection-background-color: #eadcc5;
  --editor-panels-bottom-color: #2b2116;
  --editor-panels-bottom-background-color: #f3e7d5;
  --editor-panels-bottom-border-color: #d6c3a5;
  --editor-completion-detail-color: #7c6a52;
  --editor-completion-detail-selected-color: #fef3c7;
  --editor-list-bullet-color: #9f8b6b;
  --editor-heading-color: #111827;
  --editor-heading-meta-color: #9f8b6b;
  --editor-hashtag-background-color: rgba(146, 64, 14, 0.12);
  --editor-hashtag-color: #92400e;
  --editor-hashtag-border-color: rgba(146, 64, 14, 0.18);
  --editor-ruler-color: #d6c3a5;
  --editor-naked-url-color: #92400e;
  --editor-code-color: #334155;
  --editor-link-color: #92400e;
  --editor-link-url-color: #92400e;
  --editor-link-meta-color: #8b7355;
  --editor-wiki-link-page-background-color: rgba(180, 83, 9, 0.08);
  --editor-wiki-link-page-color: #92400e;
  --editor-wiki-link-page-missing-color: #c2410c;
  --editor-wiki-link-page-invalid-color: #b91c1c;
  --editor-wiki-link-color: #92400e;
  --editor-command-button-color: #2b2116;
  --editor-command-button-background-color: #f3e7d5;
  --editor-command-button-hover-background-color: #ead8bd;
  --editor-command-button-meta-color: #8b7355;
  --editor-command-button-border-color: #d6c3a5;
  --editor-line-meta-color: #8b7355;
  --editor-meta-color: #c2410c;
  --editor-table-head-background-color: #e9d8bc;
  --editor-table-head-color: #3f3220;
  --editor-table-even-background-color: #fcf6eb;
  --editor-blockquote-background-color: rgba(146, 64, 14, 0.06);
  --editor-blockquote-color: #6b5b45;
  --editor-blockquote-border-color: #d6c3a5;
  --editor-code-background-color: rgba(120, 53, 15, 0.08);
  --editor-struct-color: #b91c1c;
  --editor-highlight-background-color: rgba(245, 158, 11, 0.22);
  --editor-code-comment-color: #8b7355;
  --editor-code-variable-color: #0f4c5c;
  --editor-code-typename-color: #166534;
  --editor-code-string-color: #7c2d12;
  --editor-code-number-color: #166534;
  --editor-code-operator-color: #78716c;
  --editor-code-info-color: #6b5b45;
  --editor-code-atom-color: #9a3412;
  --editor-frontmatter-background-color: #f3e7d5;
  --editor-frontmatter-color: #3f3220;
  --editor-frontmatter-marker-color: #8b735580;
  --editor-widget-background-color: #f3e7d5;
  --editor-task-marker-color: #6b5b45;
  --editor-task-state-color: #6b5b45;
  --editor-directive-mark-color: #9a3412;
  --editor-directive-color: #6b5b45;
  --editor-directive-background-color: rgba(180, 83, 9, 0.08);
}

html,
body {
  background: var(--root-background-color);
  color: var(--root-color);
}

#sb-root {
  background: var(--root-background-color);
  color: var(--root-color);
}

#sb-top {
  color: var(--top-color) !important;
  background: rgba(239, 230, 215, 0.94) !important;
  border-bottom: 1px solid #d6c3a5;
  backdrop-filter: blur(14px);
}

#sb-top button,
#sb-top a,
#sb-top .sb-link,
#sb-top .cm-content,
#sb-top .cm-line {
  color: inherit;
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

.cm-content,
.cm-content .cm-line,
.sb-frontmatter,
.sb-inline-content,
.sb-markdown-widget .content {
  color: var(--root-color);
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
.ProseMirror a,
.sb-link:not(.sb-meta, .sb-url),
.sb-url,
.sb-wiki-link {
  color: #92400e;
  text-decoration-thickness: 0.08em;
  text-underline-offset: 0.16em;
}

.sb-frontmatter {
  border-radius: 18px;
}

.sb-line-blockquote {
  border-radius: 12px;
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
