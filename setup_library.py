# Activate virtual environment
source .venv/bin/activate

pip install --upgrade pip

# Install dependencies and dev tools
pip install yfinance pandas numpy pytest ruff mypy

# Check if everything is installed correctly
import yfinance, pandas, numpy, pytest, ruff
print('✓ All libraries installed successfully!')