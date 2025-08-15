# Postman — API Smoke

**Environment:** ReqRes (Demo) → `{{baseUrl}} = https://reqres.in/api`  

**Requests**
- `GET /users/2` — verify 200 + user id 2  
- `POST /users` — verify 201 + `id` + `createdAt`

**How to run**
1. Import the environment and collection into Postman.
2. Select **ReqRes (Demo)** environment.
3. Send both requests or use the Collection Runner.

## CLI (Newman)

Install once:
```bash
npm i -g newman newman-reporter-html

**HTML report:** [postman-smoke-report.html](../../test-summaries/postman-smoke-report.html)
