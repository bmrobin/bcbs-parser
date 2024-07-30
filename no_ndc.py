import re

from pypdf import PdfReader

header_value = "Procedure Maximum \nAllowableEffective \nDateEnd Date Procedure Maximum \nAllowableEffective \nDateEnd Date\n"
first_page_footer_value = (
    "2024 CPT/HCPCS Drug Fee Schedule\nThis schedule is not a guaranty of payment"
)
other_pages_footer_value = "\nA Division of Health Care Service Corporation"


def run():
    reader = PdfReader("no-ndc-example.pdf")
    data = list()
    for page_num in range(0, reader.get_num_pages()):
        page = reader.get_page(page_num)
        value = page.extract_text()

        # remove the headers and footers based on exact text matching
        # the first page has a different footer value than the other pages
        if page_num == 0:
            value = value[
                value.index(header_value) : value.index(first_page_footer_value)
            ]
        else:
            value = value[
                value.index(header_value) : value.index(other_pages_footer_value)
            ]
        value = value.removeprefix(header_value)

        result = re.split(r"([a-zA-Z0-9]{5})", value)
        # regex split() should put an empty string in the first position that we don't care about
        if result[0] == "":
            result.pop(0)
        for num in range(len(result)):
            # 0th item is an NDC code, 1st are the row values, 2nd is another NDC code, etc...
            if num % 2 == 0:
                row_value = (result[num], *result[num + 1].strip().split(" "))
                data.append(row_value)

    with open("no-ndc-output.tsv", "wt") as outfile:
        for chunk in ["\t".join(val) for val in data]:
            out = f"{chunk}\n"
            outfile.write(out)
            print(out)


if __name__ == "__main__":
    run()
