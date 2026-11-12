import { defineConfig } from 'astro/config';

// Static output, same hosting setup as before (worker.js serves ./dist).
// compressHTML is disabled so the rendered markup stays byte-for-byte
// identical to the previous generator's output.
export default defineConfig({
  site: 'https://site-52f00d047e3a40c98ee7d33ad2f392dd.freebuff.page',
  compressHTML: false,
});
