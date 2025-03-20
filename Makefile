.PHONY: build test

build:
	@echo "Building the application..."
	@python -m compileall .  # Kompiluje wszystkie moduły Pythona

test:
	@echo "Running tests..."
	@pytest --maxfail=1 --disable-warnings -q || { echo "Tests failed!"; exit 1; }
