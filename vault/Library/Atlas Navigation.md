---
description: Restore clickable page navigation for Wiki page links.
---
```space-lua
-- priority: 60
local function url_dir(url)
  return string.match(url, "^(.*/)[^/]+$") or ""
end

local function split_ref_suffix(ref)
  local path, suffix = string.match(ref, "^(.-)([@#].*)$")
  if path then
    return path, suffix
  end
  return ref, ""
end

local function normalize_path(path)
  local normalized = {}
  for segment in path:gmatch("[^/]+") do
    if segment ~= "" and segment ~= "." then
      if segment == ".." then
        if #normalized > 0 then
          table.remove(normalized)
        end
      else
        table.insert(normalized, segment)
      end
    end
  end
  return table.concat(normalized, "/")
end

local function is_external_url(url)
  return url:startsWith("//")
    or string.match(url, "^[a-zA-Z][a-zA-Z0-9+.-]*:")
end

local function resolve_internal_ref(current_page, ref)
  local path, suffix = split_ref_suffix(ref)
  if path == "" then
    return current_page .. suffix
  end
  if path:startsWith("/") then
    return normalize_path(path:sub(2)) .. suffix
  end
  return normalize_path(url_dir(current_page) .. path) .. suffix
end

local function find_markdown_link(text, pos)
  local search_from = 1
  while true do
    local start_pos, end_pos, _, url = text:find("%[([^%]]-)%]%(([^%)]+)%)", search_from)
    if not start_pos then
      return nil
    end
    local previous = start_pos > 1 and text:sub(start_pos - 1, start_pos - 1) or ""
    if previous ~= "!" and pos >= start_pos and pos <= end_pos then
      return url
    end
    search_from = end_pos + 1
  end
end

local function find_wiki_link(text, pos)
  local search_from = 1
  while true do
    local start_pos, end_pos, raw_ref = text:find("%[%[([^%]]-)%]%]", search_from)
    if not start_pos then
      return nil
    end
    if pos >= start_pos and pos <= end_pos then
      return string.match(raw_ref, "^([^|]+)")
    end
    search_from = end_pos + 1
  end
end

local function ensure_live_preview()
  if editor.getUiOption("markdownSyntaxRendering") then
    editor.setUiOption("markdownSyntaxRendering", false)
    editor.rebuildEditorState()
  end
end

local function navigate_from_ref(current_page, raw_ref, new_window)
  if not raw_ref or raw_ref == "" then
    return
  end

  if is_external_url(raw_ref) then
    editor.openUrl(raw_ref)
    return
  end

  editor.navigate(resolve_internal_ref(current_page, raw_ref), false, new_window)
end

event.listen {
  name = "editor:init",
  run = function()
    ensure_live_preview()
  end
}

event.listen {
  name = "page:click",
  run = function(e)
    if e.data.altKey then
      return
    end

    local text = editor.getText()
    local pos = e.data.pos + 1
    local current_page = editor.getCurrentPage()
    local new_window = e.data.metaKey or e.data.ctrlKey

    local wiki_ref = find_wiki_link(text, pos)
    if wiki_ref then
      navigate_from_ref(current_page, wiki_ref, new_window)
      return
    end

    local markdown_ref = find_markdown_link(text, pos)
    if markdown_ref then
      navigate_from_ref(current_page, markdown_ref, new_window)
    end
  end
}
```
