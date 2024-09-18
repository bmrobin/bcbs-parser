from pypdf import PdfReader

# exact text-matching values
header_value = "Procedure NDC Maximum \nAllowableEffective \nDateEnd Date Procedure NDC Maximum \nAllowableEffective \nDateEnd Date\n"
footer_value = "\nA Division of Health Care Service Corporation"


def run(date_pattern: str):
    # !! replace this filename with the INPUT PDF file in the current directory you wish to parse !!
    reader = PdfReader("ndc-example.pdf")
    data = list()
    for page_num in range(0, reader.get_num_pages()):
        page = reader.get_page(page_num)
        value = page.extract_text()

        # remove the headers and footers based on exact text matching
        value = value[value.index(header_value) : value.index(footer_value)]
        value = value.removeprefix(header_value)

        # should now be the contents of the entire table from left to right as one single string.
        # split on the month-end date, e.g. '5/31/24'
        rows = [r.strip() for r in value.split(date_pattern)]

        # the first page has a disclaimer paragraph that we need to remove; should be last element in list
        if page_num == 0:
            rows.pop()

        data.append(rows)

    # !! replace this filename with the OUTPUT TSV filename to write to in the current directory !!
    with open("ndc-output.tsv", "wt") as outfile:
        for chunk in data:
            for line in chunk:
                # there are some empty strings, ignore those
                if line:
                    # append the input date pattern at the end of each line since it was removed
                    out_value = line.replace(" ", "\t") + f"\t{date_pattern}\n"
                    outfile.write(out_value)
                    print(out_value)


if __name__ == "__main__":
    date_pattern = input("Month-ending date pattern in the file, i.e. 5/31/24:  ")
    should_continue = input(f"Using date pattern {date_pattern}. OK?  (y/n):  ")
    if should_continue.strip().lower() == "y":
        run(date_pattern)
    else:
        raise RuntimeError("Aborting!")
