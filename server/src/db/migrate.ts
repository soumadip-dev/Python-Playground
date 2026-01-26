import path from 'node:path';
import fs from 'node:fs';
import logger from '../lib/logger.lib.js';
import { query } from './db.js';

const migrationDir = path.resolve(process.cwd(), 'src', 'migrations');

/*
📌 NOTE:
🔴 process.cwd() → Returns the current working directory from where Node.js is executed.
🔴 'src', 'migrations' → Individual folder segments.
🔴 path.resolve(...) → Resolves all segments into a single absolute path.

➡️ Example output:
   /home/user/Forumix/src/migrations
*/
async function executeMigrations() {
  logger.info(`Looking for migrations in ${migrationDir} 📂`);

  const files = fs
    .readdirSync(migrationDir)
    .filter(file => file.endsWith('.sql'))
    .sort();

  /*
  📌 NOTE:
  🔴 fs.readdirSync(migrationDir)
     → Reads all file names inside the migrations directory.
     → Returns an array like:
       ['0001_users.sql', '0002_threads_core.sql', ...]

  🔴 .filter(file => file.endsWith('.sql'))
     → Keeps only SQL migration files.
     → Ignores non-SQL files.

  🔴 .sort()
     → Sorts files alphabetically to maintain execution order.
     → Ensures: 0001_ → 0002_ → 0003_
  */

  if (files.length === 0) {
    logger.info(`No migrations found in ${migrationDir} 🚫`);
    return;
  }

  /*
  📌 NOTE:
  🔴 for...of loop is used instead of forEach.
  🔴 This allows the use of await inside the loop.
  🔴 Ensures migrations run sequentially (not in parallel).
  */
  for (const file of files) {
    const filePath = path.join(migrationDir, file);
    const sql = fs.readFileSync(filePath, 'utf-8');

    /*
    📌 NOTE:
    🔴 path.join(migrationDir, file)
       → Combines directory path and filename into a full file path.
       → Example:
         /home/user/Forumix/src/migrations/0001_users.sql

    🔴 fs.readFileSync(filePath, 'utf-8')
       → Reads the SQL file content as a UTF-8 string.
    */

    logger.info(`Running migration ${file}... 🏃‍➡️`);

    await query(sql); // Executes the SQL statements inside the migration file.

    logger.info(`Migration completed successfully ✅`);
  }
}

executeMigrations()
  .then(() => {
    logger.info('All migrations executed successfully ✅');
    process.exit(0);
  })
  .catch(error => {
    logger.error('Migration execution failed ❌', error);
    process.exit(1);
  });
