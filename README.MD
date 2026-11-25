# Olist ETL Pipeline

## Overview
A Python-based ETL pipeline built using the Brazilian Olist E-Commerce dataset. The pipeline reads CSV files, performs data validation, transforms data, handles errors, and generates structured outputs.

## Project Structure

```text
Olist-ETL/
│
├── olist/                  # Raw Olist CSV datasets
├── output/                 # Processed output files
├── logs/                   # Pipeline execution logs
├── bad_records.csv         # Invalid records
│
├── reader.py               # CSV reading logic
├── validator.py            # Data validation
├── transformer.py          # Data transformation
├── test_functions.py       # Unit tests
│
├── config.yaml             # Pipeline configuration
├── config.json             # Column mappings
│
├── day11.ipynb
├── day12.ipynb
├── day13.ipynb
├── day14.ipynb
├── day15.ipynb
│
└── README.md
```

## Requirements

- Python 3.10+
- Pandas
- PyYAML
- Jupyter Notebook
- Pytest
- Ruff

## Environment Setup

Clone the repository:

```bash
git clone <your-repository-url>
cd <repository-folder>
```

Install dependencies:

```bash
pip install pandas pyyaml jupyter pytest ruff
```

## Running the Notebooks

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open the required notebook and execute its cells sequentially.

## Running Unit Tests

Execute:

```bash
pytest -v
```

## Code Quality

Check Python modules using Ruff:

```bash
ruff check *.py
```

Automatically fix supported issues:

```bash
ruff check *.py --fix
```

## Configuration

Pipeline paths, thresholds and column mappings are maintained through configuration files.

Update the configuration when input dataset structures change.

## Output

The pipeline generates:

- Processed CSV files
- JSON outputs and run summaries
- Bad records for validation failures
- Execution logs
- Processing manifest for idempotency

## Technologies

Python | Pandas | YAML | JSON | CSV | Pytest | Ruff | Jupyter Notebook
