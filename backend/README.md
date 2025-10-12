# Backend (Express)

## Setup
1. Copy `.env.example` to `.env` and fill values.
2. `npm install`
3. `npm run dev` (requires nodemon) or `npm start`

Routes:
- POST /api/users/register
- POST /api/users/login
- GET /api/users/profile (protected: Authorization: Bearer <token>)
