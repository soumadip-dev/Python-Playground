CREATE TABLE IF NOT EXISTS users (
  id BIGSERIAL PRIMARY KEY,
  clerk_user_id TEXT NOT NULL UNIQUE,
  display_name TEXT,
  handle TEXT UNIQUE,
  avatar_url TEXT,
  bio TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
