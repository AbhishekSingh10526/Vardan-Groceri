# Groceri - Online Grocery Store

## Overview
Groceri is a web-based grocery store application built with Python Flask.

## Recent Changes (2026-02-07)
- **Circular Import Fix**: Refactored the application to use a factory pattern. Introduced `extensions.py` to hold the `db` instance and app creation logic, breaking the circular dependency between `app.py`, `models.py`, and `routes.py`.
- **Modernized Dependencies**: Updated the project to use Python 3.11 and 2024-compatible package versions (Flask 3.x, SQLAlchemy 2.x).
- **Deployment Readiness**: Configured Replit autoscale deployment settings.

## System Architecture
- **Entry Point**: `groceri-master/app.py`
- **Logic**: `groceri-master/extensions.py` (App Factory), `groceri-master/models.py` (Database Models), `groceri-master/routes.py` (Route Handlers)
- **Database**: SQLite (`groceri-master/database.sqlite3`)
