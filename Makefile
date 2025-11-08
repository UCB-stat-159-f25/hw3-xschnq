ENV_NAME = myst-env

env:
	@echo "🔧 Creating or updating conda environment: $(ENV_NAME)"
	conda env update --file environment.yml --name $(ENV_NAME) --prune || conda env create -f environment.yml -n $(ENV_NAME)
	@echo "✅ Environment setup complete (not activated)."

html:
	@echo "🧱 Building MyST site as HTML..."
	myst build --html
	@echo "✅ HTML build complete. Check the _build/site folder."

clean:
	@echo "🧹 Cleaning figures, audio, and _build folders..."
	rm -rf figures/ audio/ _build/
	@echo "✅ Cleanup complete."
