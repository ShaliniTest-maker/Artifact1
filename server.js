/**
 * server.js - Express application entry point for the "Artifact1" server.
 *
 * Serves two plain-text GET endpoints through a single Express application:
 *   - GET /              -> "Hello world"   (original greeting, preserved)
 *   - GET /good-evening  -> "Good evening"  (new greeting)
 *
 * Express is the sole HTTP layer. The listening port is configurable via the
 * PORT environment variable and defaults to 3000.
 */

const express = require('express');

// Single Express application instance - the only HTTP surface for this server.
const app = express();

// Configurable TCP port: honor process.env.PORT, otherwise default to 3000.
const PORT = process.env.PORT || 3000;

// FR-2: Preserve the original greeting endpoint.
app.get('/', (req, res) => res.type('text/plain').send('Hello world'));

// FR-3: New greeting endpoint.
app.get('/good-evening', (req, res) => res.type('text/plain').send('Good evening'));

// FR-4: Single application surface bound to a configurable port.
app.listen(PORT, () => console.log(`Listening on http://localhost:${PORT}`));
