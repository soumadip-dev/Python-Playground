import express, { Express, NextFunction, Request, Response } from 'express';
import helmet from 'helmet';
import configureCors from './config/cors.config.js';
import logger from './lib/logger.lib.js';
import { notFoundHandler } from './middleware/notFoundHandler.middleware.js';
import { errorHandler } from './middleware/errorHandler.middleware.js';

export function createApp() {
  const app: Express = express();
  app.use(helmet());
  app.use(configureCors());
  app.use(express.json()); // parse json request to body
  app.use(express.urlencoded({ extended: true })); // parse form data (like html form)

  app.use((req: Request, _res: Response, next: NextFunction) => {
    logger.info(`Received ${req.method} request to ${req.url} 📨`);
    logger.info(`Request body: ${JSON.stringify(req.body)}`);
    next();
  });

  app.use(notFoundHandler);

  app.use(errorHandler);
  return app;
}
