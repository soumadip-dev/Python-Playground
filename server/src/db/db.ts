import { Pool, type QueryResult, type QueryResultRow } from 'pg';
import { env } from '../config/env.config.js';
import logger from '../lib/logger.lib.js';

export const pool = new Pool({
  host: env.DB_HOST,
  port: Number(env.DB_PORT),
  database: env.DB_NAME,
  user: env.DB_USER,
  password: env.DB_PASSWORD,
});

export async function query<T extends QueryResultRow = QueryResultRow>(
  text: string,
  params?: unknown[]
): Promise<QueryResult<T>> {
  const result = await pool.query<T>(text, params as any[]);
  return result;
}

export async function assetDatabaseConnection() {
  try {
    await pool.query('SELECT 1');
    logger.info('Database connection successful ✅');
  } catch (error) {
    logger.error('Database connection failed ❌', error);
    throw error;
  }
}
