append_log_schema = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "date",
    "tags",
    "text"
  ],
  "properties": {
    "date": {
      "$id": "#/properties/date",
      "type": "string",
      "title": "The Date Schema",
      "default": "",
      "examples": [
        "991231"
      ],
      "pattern": "^(.*)$"
    },
    "tags": {
      "$id": "#/properties/tags",
      "type": "array",
      "title": "The Tags Schema",
      "items": {
        "$id": "#/properties/tags/items",
        "type": "string",
        "title": "The Items Schema",
        "default": "",
        "examples": [
          "@test",
          "@sample"
        ],
        "pattern": "^(.*)$"
      }
    },
    "text": {
      "$id": "#/properties/text",
      "type": "string",
      "title": "The Text Schema",
      "default": "",
      "examples": [
        "サンプルだよ"
      ],
      "pattern": "^(.*)$"
    }
  }
}
