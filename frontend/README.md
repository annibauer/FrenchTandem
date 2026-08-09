# Frontend

## Local development

```bash
cd frontend
npm install
npm start
```

This app runs on http://localhost:3000 and uses the frontend proxy configured in package.json to send API calls to the Django backend at http://localhost:8000.

## Useful scripts

- `npm start` — starts the dev server
- `npm run build` — creates the production build
- `npm test` — runs the React test suite

## Important note

This project does not use a real Django WebSocket for chat. The app communicates with Django over HTTP endpoints, while the React dev server still uses its own local websocket for hot reloading.
