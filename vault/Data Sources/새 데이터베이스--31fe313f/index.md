---
title: "새 데이터베이스"
source_kind: data_source
source_path: ssot/data-sources/31fe313f58b98052867f000bd2286e68__새 데이터베이스
notion_id: 31fe313f58b98052867f000bd2286e68
notion_url: https://www.notion.so/31fe313f58b980c28313fb24f7c613e4
parent_notion_id: 31fe313f58b9809fb79bd4c09d8bf594
---

## Schema

```sql
CREATE TABLE IF NOT EXISTS "collection://31fe313f-58b9-8052-867f-000bd2286e68" (
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
      "url": "view://31fe313f-58b9-80cf-967a-000caa6d0666",
      "dataSourceUrl": "collection://31fe313f-58b9-8052-867f-000bd2286e68",
      "displayProperties": [
        "이름"
      ],
      "name": "",
      "type": "table"
    }
  ]
}
```
