import datetime

import pdfplumber
import pandas as pd
from pdfplumber import page

with pdfplumber.open("reports.pdf") as pdf:
    x = 0

    for i in range(29, 48):
        bold_title_text = pdf.pages[i]
        ff = bold_title_text.extract_table(table_settings=
                                           {"vertical_strategy": "text",
                                            "keep_blank_chars": "False",
                                            "snap_tolerance": 4,

                                            })
        for row in ff[1:-1]:
            if row[1] =="Y":
                print(row[0].replace("\n"," "),x)
            x+=1

