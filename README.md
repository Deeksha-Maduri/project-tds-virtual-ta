# project-tds-virtual-ta


This project implements an API that answers student queries and provides reference links.

## API Endpoint

`POST /api/`

### Request

```json
{
  "question": "string",
  "image": "optional base64 string"
}
