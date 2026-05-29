# Artifact1

A minimal Node.js HTTP server built with the [Express](https://expressjs.com/) web framework. It exposes two plain-text greeting endpoints.

## Prerequisites

- **Node.js v18 or newer** — this matches the `engines.node` (`>=18`) constraint declared in `package.json`.
- **npm** — bundled with Node.js.

## Installation

Install the project's dependencies. This downloads Express (declared in `package.json`) into `node_modules/`:

```bash
npm install
```

## Running the server

```bash
npm start
```

This runs `node server.js`. The server listens on the port defined by the `PORT` environment variable, defaulting to `3000` — i.e. `http://localhost:3000`. To use a different port, set `PORT` first (for example, `PORT=8080 npm start`).

## Endpoints

| Method | Path | Response |
|--------|------|----------|
| GET | `/` | `Hello world` |
| GET | `/good-evening` | `Good evening` |

## Example requests

With the server running, send requests with `curl`:

```bash
curl -s http://localhost:3000/            # -> Hello world
curl -s http://localhost:3000/good-evening # -> Good evening
```
