# BCBS Parser

The Blue Cross-Blue Shield (BCBS) websites for various states in the U.S. provide PDF documents for reimbursement rates

ex - https://www.bcbstx.com/provider/standards/standards-requirements/gri

BCBS doesn't provide this information in any other format than a PDF, which is quite difficult to incorporate into 
MS Excel or other data manipulation tooling.

This Python module provides scripts that can parse the files and generate TSV files

### Requirements
python 3.7+

### Installation

Create a python virtual environment and install the requirements via `pip`.

#### macOS / *nix
```bash
python3 -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
```

#### Windows
```shell
python3 -m venv venv/
.\venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Usage

Execute python scripts via `python {script_name.py}` -- see each script's `__main__` section for more information.

### Why TSV?

Using comma-separated value files (CSV) proves difficult to work with because of commas included in the dollar amount 
fields. Using tab-separated value files (TSV) bypasses this, and TSV are easily interoperable in Excel

