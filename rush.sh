#!/bin/bash

# Attiva ambiente virtuale se presente
if [ -d "venv" ]; then
  source venv/bin/activate
fi

echo ">> Running Elayra Double Helix DNC Interface..."
python3 index.py
