import pandas as pd
import pathlib

class Filemanager:
    root_path = pathlib.Path(__file__).parent.parent.absolute()
    products_excel_file = f"{root_path}/scraper/products.csv"


