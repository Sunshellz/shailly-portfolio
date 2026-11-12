import { defineConfig } from 'astro/config';

import cloudflare from "@astrojs/cloudflare";

// Static output, same hosting setup as before (worker.js serves ./dist).
// compressHTML is disabled so the rendered markup stays byte-for-byte
// identical to the previous generator's output.
export default defineConfig({
  site: 'https://portfolio.shailly.workers.dev',
  compressHTML: false,
  adapter: cloudflare()
});