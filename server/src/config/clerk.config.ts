import type { Response, Request, NextFunction } from 'express';
import { clerkMiddleware, getAuth, clerkClient } from '@clerk/express';
import { UnauthorizedError } from '../lib/errors.lib.js';
import logger from '../lib/logger.lib.js';

export { clerkMiddleware, clerkClient, getAuth };

export function requireAuthApi(req: Request, _res: Response, next: NextFunction) {
  const { userId } = getAuth(req);

  if (!userId) {
    logger.warn('Unauthorized access attempt 💀');
    return next(new UnauthorizedError('You must be signed in to access this resource!!!'));
  }
  next();
}
