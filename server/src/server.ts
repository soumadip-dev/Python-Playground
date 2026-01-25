import http from 'node:http';
import { createApp } from './app.js';
import { env } from './config/env.config.js';
import { assertDatabaseConnection } from './db/db.js';
import logger from './lib/logger.lib.js';

async function bootstrap() {
  try {
    await assertDatabaseConnection();
    const app = createApp();
    const server = http.createServer(app);
    const PORT = Number(env.PORT) || 8080;
    server.listen(PORT, () => {
      logger.info(`Server is running on: http://localhost:${PORT} 🌐`);
    });
  } catch (error) {
    logger.error('Failed to start server', (error as Error).message);
    process.exit(1);
  }
}

bootstrap();
