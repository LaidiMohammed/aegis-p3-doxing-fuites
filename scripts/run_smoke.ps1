$py = if (Test-Path .venv/bin/python) { '.venv/bin/python' } else { 'python' }
& $py "src\doxing-fuites_main.py"
