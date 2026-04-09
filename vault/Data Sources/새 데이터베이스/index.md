---
title: "새 데이터베이스"
source_kind: data_source
source_path: ssot/data-sources/31fe313f58b9804bb453000bac312cc0__새 데이터베이스
notion_id: 31fe313f58b9804bb453000bac312cc0
notion_url: https://www.notion.so/31fe313f58b98068b205f8c91f4a2b45
parent_notion_id: 31fe313f58b98053b5fefc9ccfc0be18
---

## Schema

```sql
CREATE TABLE IF NOT EXISTS "collection://31fe313f-58b9-804b-b453-000bac312cc0" (
	url TEXT UNIQUE,
	createdTime TEXT, -- ISO-8601 datetime string, automatically set. This is the canonical time for when the page was created.
	"직급" TEXT,
	"과정" TEXT,
	"직무" TEXT,
	"이름" TEXT
)
```

## Views

```json
{
  "views": [
    {
      "url": "view://31fe313f-58b9-8057-b135-000c4b83e65f",
      "dataSourceUrl": "collection://31fe313f-58b9-804b-b453-000bac312cc0",
      "displayProperties": [
        "이름",
        "직무",
        "직급",
        "과정"
      ],
      "name": "",
      "type": "table"
    }
  ]
}
```

## Rows

- [김현우](Rows/김현우.md)
