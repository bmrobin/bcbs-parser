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

Execute python scripts via `python {script_name.py}` or use the included `launch.json` 
file to execute in VS Code.

* `ndc.py` -- "NDC" code sheet parser 

    This reads files like [ndc-example.pdf](https://github.com/bmrobin/bcbs-parser/blob/main/ndc-example.pdf) and 
    outputs a TSV file of the table contents from each page in the file.  The file's "header row" in the table is not 
    included in the TSV file output.

    1. Edit the script's input & output file where the comments denote with `# !!`

    2. When you execute the script, the terminal will first prompt you for the date. This should correspond to the 
    date value in the "End Date" column of the NDC PDF file. The second prompt is to ensure you typed it correctly;
    enter 'y' to continue or 'n' to abort (will also abort on anything not 'y'). **NOTE** - the program matches the text
    **exactly**, so be sure the numbers and slash separators are correct.

    ```plain
    $ Month-ending date pattern in the file, i.e. 5/31/24:  11/30/24
    $ Using date pattern 11/30/24. OK?  (y/n):  y
    ```

    3. When the script finishes, the output will dump to the terminal as well as the TSV file to indicate completion

* `no_ndc.py` -- "No NDC" code sheet parser
    This reads files like [no-ndc-example.pdf](https://github.com/bmrobin/bcbs-parser/blob/main/no-ndc-example.pdf) and
    outputs a TSV file of the table contents from each page in the file.

    1. Edit the script's input & output file where the comments denote with `# !!`

    2. Unlike the previous script, no input is required for execution. The script will dump the output to the terminal
    and the TSV file to indicate completion.

### Why TSV?

Using comma-separated value files (CSV) proves difficult to work with because of commas included in the dollar amount 
fields. Using tab-separated value files (TSV) bypasses this, and TSV are easily interoperable in Excel


### Maintenance?
This script is **100% dependent** on the exact text-matching of the paragraphs of text in the PDF files provided by 
Blue Cross/Blue Shield. See the `header_value` and `footer_value` variables in each python file for the exact
text-matching being used to distinguish the table data. Should the text provided by BC/BS change, these values will 
need to be updated!
