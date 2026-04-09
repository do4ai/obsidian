---
title: "[UL]"
source_kind: data_source
source_path: ssot/data-sources/31fe313f58b980bf9223000bf23154e7__[UL]
notion_title: "[UL] "
notion_id: 31fe313f58b980bf9223000bf23154e7
notion_url: https://www.notion.so/31fe313f58b980c6a6d0ec51905c4834
parent_notion_id: 31fe313f58b9809fb79bd4c09d8bf594
---

## Schema

```sql
CREATE TABLE IF NOT EXISTS "collection://31fe313f-58b9-80bf-9223-000bf23154e7" (
	url TEXT UNIQUE,
	createdTime TEXT,
	"이름" TEXT
);
```

## Views

```json
{
  "views": [
    {
      "url": "view://31fe313f-58b9-80c2-8052-000c93209821",
      "dataSourceUrl": "collection://31fe313f-58b9-80bf-9223-000bf23154e7",
      "displayProperties": [
        "이름"
      ],
      "name": "",
      "type": "table"
    }
  ]
}
```

## Rows

- [상품이란](Rows/상품이란.md)
