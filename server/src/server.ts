import { createApp } from "./app.js";
import { env } from "./config/env.js";
import { assertDatabaseConnection } from "./db/db.js";
import { logger } from "./lib/logger.js";
import http from "node:http";
import { initIo } from "./realtime/io.js";

async function boostrap() {
  try {
    await assertDatabaseConnection();

    const app = createApp();
    const server = http.createServer(app);

    const port = Number(env.PORT) || 5000;

    initIo(server);

    server.listen(port, () => {
      logger.info(`Server is now listening to port: http://localhost:${port}`);
    });
  } catch (err) {
    logger.error("Failed to start the server", `${(err as Error).message}`);
    process.exit(1);
  }
}

boostrap();
