# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Flask web application for practicing Flask and JavaScript by creating a fireworks website. The fireworks animation is implemented using pure CSS (no canvas/JavaScript) based on a tutorial from Zenn.

## Running the Application

```bash
# Run the Flask development server
python application.py &

# Or run in foreground (use Ctrl+C to stop)
python application.py
```

The application will be available at `http://127.0.0.1:5000`

Note: The application.py includes `if __name__ == '__main__':` block with `app.run(debug=True, host='127.0.0.1', port=5000)` for proper server startup.

## Application Structure

- **Flask Backend**: Single file `application.py` with three routes:
  - `/` - Simple "Hello, World!" page
  - `/hello/` and `/hello/<name>` - Personalized greeting using Jinja2 templates
  - `/fireworks` - Fireworks animation display page

- **Templates**: Jinja2 templates in `templates/` directory
  - `hello.html` - Template for personalized greetings with static asset integration
  - `fireworks.html` - Minimal template that loads the CSS-based fireworks animation

- **Static Assets**: 
  - `fireworks.css` - Complex CSS keyframe animation creating fireworks effect using radial gradients and transforms
  - `actions.js` - Minimal JavaScript file (currently only logs "file loaded")
  - `style.css` - General styling
  - `images/fireworks.png` - Fireworks image asset

## CSS Animation Architecture

The fireworks effect uses a sophisticated CSS-only approach:
- Base element `.c-firework` with `::before` and `::after` pseudo-elements
- Multiple radial gradients positioned to create particle effect
- Keyframe animation transforms from bottom viewport to expanded state
- Rotation transforms on pseudo-elements for layered animation effect

## Development Notes

- No package.json, requirements.txt, or dependency management files found
- No testing framework or linting configuration detected
- Static assets are served via Flask's built-in static file serving
- Templates use Jinja2 syntax with `url_for()` for asset linking